#!/usr/bin/env python3
"""
Populate readme_source table for vocab.branch SQLite MVP DB.

Designed in pass25.
Do not execute in pass25.

Purpose:
- Fix MVP gap where source_file rows exist but readme_source rows are 0.
- Populate readme_source from existing source_file rows.
- Do not rescan repositories.
- Do not rebuild DB.
"""

from __future__ import annotations

import argparse
import sqlite3
from dataclasses import dataclass
from pathlib import Path


DEFAULT_DB_PATH = Path.home() / "seungeflow_runtime" / "vocab_reader" / "vocab_reader.sqlite"
DEFAULT_REPORT_PATH = Path.home() / "seungeflow_runtime" / "vocab_reader" / "readme_source_population_report.md"


@dataclass(frozen=True)
class BaselineRule:
    repo: str
    path: str
    baseline_class: str
    note: str


BASELINE_RULES: list[BaselineRule] = [
    BaselineRule(
        "SeungeFlow/9Dot0",
        "README.md",
        "repo_9dot0_branch_field",
        "Repo.9Dot0 entry surface",
    ),
    BaselineRule(
        "SeungeFlow/9Dot0",
        "03_branch_fields/market/README.md",
        "repo_9dot0_branch_field",
        "branch.market surface",
    ),
    BaselineRule(
        "SeungeFlow/9Dot0",
        "03_branch_fields/sohosa/README.md",
        "repo_9dot0_branch_field",
        "branch.sohosa surface",
    ),
    BaselineRule(
        "SeungeFlow/9Dot0",
        "03_branch_fields/history/README.md",
        "repo_9dot0_branch_field",
        "branch.history surface",
    ),
    BaselineRule(
        "SeungeFlow/9Dot0",
        "03_branch_fields/vocab/README.md",
        "repo_9dot0_branch_field",
        "branch.vocab surface",
    ),
    BaselineRule(
        "SeungeFlow/SeungeFlow",
        "README.md",
        "repo_seungeflow_primary_observer",
        "Repo.SeungeFlow README baseline / observer surface",
    ),
]


def table_count(conn: sqlite3.Connection, table: str) -> int:
    return int(conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0])


def ensure_db_exists(db_path: Path) -> None:
    if not db_path.exists():
        raise FileNotFoundError(f"SQLite DB not found: {db_path}")


def fetch_source_files(conn: sqlite3.Connection) -> list[dict[str, object]]:
    rows = conn.execute(
        """
        SELECT id, repo, branch, commit_hash, path, raw_url, file_role
        FROM source_file
        ORDER BY id
        """
    ).fetchall()

    return [
        {
            "id": row[0],
            "repo": row[1],
            "branch": row[2],
            "commit_hash": row[3],
            "path": row[4],
            "raw_url": row[5],
            "file_role": row[6],
        }
        for row in rows
    ]


def classify_source(repo: str, path: str, file_role: str) -> tuple[str, str]:
    for rule in BASELINE_RULES:
        if repo == rule.repo and path == rule.path:
            return rule.baseline_class, rule.note

    if path.endswith("README.md") or "README" in path:
        return "readme_baseline_candidate", file_role

    return "unknown_source_class", file_role


def already_registered(conn: sqlite3.Connection, source_file_id: int) -> bool:
    row = conn.execute(
        "SELECT id FROM readme_source WHERE source_file_id = ?",
        (source_file_id,),
    ).fetchone()
    return row is not None


def populate(conn: sqlite3.Connection) -> dict[str, int]:
    stats: dict[str, int] = {
        "source_file_before": table_count(conn, "source_file"),
        "readme_source_before": table_count(conn, "readme_source"),
        "inserted": 0,
        "skipped_existing": 0,
        "unknown_class": 0,
    }

    source_files = fetch_source_files(conn)

    for order, source in enumerate(source_files, start=1):
        source_file_id = int(source["id"])

        if already_registered(conn, source_file_id):
            stats["skipped_existing"] += 1
            continue

        baseline_class, note = classify_source(
            str(source["repo"]),
            str(source["path"]),
            str(source["file_role"]),
        )

        if baseline_class == "unknown_source_class":
            stats["unknown_class"] += 1

        conn.execute(
            """
            INSERT INTO readme_source
            (source_file_id, baseline_order, baseline_class, note)
            VALUES (?, ?, ?, ?)
            """,
            (
                source_file_id,
                order,
                baseline_class,
                note,
            ),
        )
        stats["inserted"] += 1

    stats["readme_source_after"] = table_count(conn, "readme_source")
    return stats


def write_report(report_path: Path, db_path: Path, stats: dict[str, int]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# readme_source population report",
        "",
        "## status",
        "",
        "This report records metadata correction for the vocab.branch SQLite MVP DB.",
        "",
        "No repository scan was performed.",
        "No DB rebuild was performed.",
        "",
        "## paths",
        "",
        f"- db_path: `{db_path}`",
        "",
        "## stats",
        "",
    ]

    for key, value in stats.items():
        lines.append(f"- {key}: {value}")

    lines.extend(
        [
            "",
            "## judgment",
            "",
            "readme_source rows were populated from existing source_file rows.",
            "",
            "This is metadata correction, not final interpretation.",
            "",
            "Raw URLs remain the source coordinates.",
            "",
        ]
    )

    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Populate readme_source table for vocab.branch SQLite MVP DB."
    )
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH), help="Path to existing SQLite DB")
    parser.add_argument("--report", default=str(DEFAULT_REPORT_PATH), help="Output markdown report path")
    parser.add_argument("--dry-run", action="store_true", help="Inspect without committing DB changes")
    args = parser.parse_args()

    db_path = Path(args.db).expanduser().resolve()
    report_path = Path(args.report).expanduser().resolve()

    ensure_db_exists(db_path)

    conn = sqlite3.connect(str(db_path))
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        stats = populate(conn)
        if args.dry_run:
            conn.rollback()
            stats["dry_run"] = 1
        else:
            conn.commit()
            stats["dry_run"] = 0
    finally:
        conn.close()

    write_report(report_path, db_path, stats)

    print(f"db_path={db_path}")
    print(f"report_path={report_path}")
    for key, value in stats.items():
        print(f"{key}={value}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
