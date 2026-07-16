#!/usr/bin/env python3
"""
Build local SQLite MVP DB for Repo.9Dot0 vocab.branch.

This script is designed in pass20.
Do not execute it in pass20.

Default behavior:
- Reads committed v3 core-filtered preview CSV.
- Builds a local SQLite DB under ~/seungeflow_runtime/vocab_reader/.
- Does not scan whole repositories.
- Does not modify Repo.SeungeFlow.
- Does not commit the DB file.

Source remains the original md files at Raw URLs.
The SQLite DB is a derived reader index.
"""

from __future__ import annotations

import argparse
import csv
import os
import sqlite3
from pathlib import Path


DEFAULT_RUNTIME_DIR = Path.home() / "seungeflow_runtime" / "vocab_reader"
DEFAULT_DB_PATH = DEFAULT_RUNTIME_DIR / "vocab_reader.sqlite"

DEFAULT_INPUT_CSV = (
    "03_branch_fields/vocab/06_reports/"
    "readme_vocab_scan_core_filtered_preview_pass14.csv"
)

DEFAULT_SCHEMA_SQL = "03_branch_fields/vocab/04_db_schema/schema_v0_1.sql"


def read_sql(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def connect_db(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def get_or_create_source_file(conn: sqlite3.Connection, row: dict[str, str]) -> int:
    repo = row["repo"]
    branch = row["branch"]
    commit_hash = row["commit"]
    path = row["path"]
    raw_url = row["raw_url"]
    file_role = row.get("role", "readme_source")

    existing = conn.execute(
        """
        SELECT id FROM source_file
        WHERE repo = ? AND commit_hash = ? AND path = ?
        """,
        (repo, commit_hash, path),
    ).fetchone()

    if existing:
        return int(existing[0])

    cur = conn.execute(
        """
        INSERT INTO source_file
        (repo, branch, commit_hash, path, raw_url, source_status, file_role)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            repo,
            branch,
            commit_hash,
            path,
            raw_url,
            "source_identity_candidate",
            file_role,
        ),
    )
    return int(cur.lastrowid)


def get_or_create_term(conn: sqlite3.Connection, term: str) -> int:
    normalized = term.strip()
    existing = conn.execute(
        "SELECT id FROM vocab_term WHERE normalized_term = ?",
        (normalized,),
    ).fetchone()

    if existing:
        return int(existing[0])

    cur = conn.execute(
        """
        INSERT INTO vocab_term
        (term, normalized_term, surface_language, term_kind, is_readme_vocab, is_structural_trigger)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            term,
            normalized,
            "unknown",
            "readme_vocab_candidate",
            1,
            1 if term in {"Ctp", "Ctp24", "9dot0", "C", "m", "t", "p", "?", "Y_Branch"} else 0,
        ),
    )
    return int(cur.lastrowid)


def insert_term_status(conn: sqlite3.Connection, term_id: int, status: str) -> None:
    exists = conn.execute(
        """
        SELECT id FROM term_status
        WHERE term_id = ? AND status = ?
        """,
        (term_id, status),
    ).fetchone()

    if exists:
        return

    score = {
        "core_token_candidate": 15,
        "structural_trigger_candidate": 13,
        "filtered_candidate": 5,
        "demoted_common": 0,
    }.get(status, 0)

    conn.execute(
        """
        INSERT INTO term_status
        (term_id, status, score, status_source, note)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            term_id,
            status,
            score,
            "readme_vocab_scan_core_filtered_preview_pass14",
            "Imported from v3 core-filtered README preview CSV.",
        ),
    )


def import_csv(conn: sqlite3.Connection, csv_path: Path, scan_run_id: int) -> dict[str, int]:
    stats = {
        "rows": 0,
        "source_files": 0,
        "terms": 0,
        "occurrences": 0,
    }

    source_seen: set[int] = set()
    term_seen: set[int] = set()

    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        required = {
            "term", "status", "repo", "branch", "commit", "path",
            "line_no", "role", "raw_url", "context",
        }
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"CSV missing required fields: {sorted(missing)}")

        for row in reader:
            stats["rows"] += 1
            source_id = get_or_create_source_file(conn, row)
            term_id = get_or_create_term(conn, row["term"])
            insert_term_status(conn, term_id, row["status"])

            source_seen.add(source_id)
            term_seen.add(term_id)

            conn.execute(
                """
                INSERT INTO term_occurrence
                (scan_run_id, term_id, source_file_id, line_no, context, occurrence_status)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    scan_run_id,
                    term_id,
                    source_id,
                    int(row["line_no"]),
                    row.get("context", ""),
                    row["status"],
                ),
            )

            conn.execute(
                """
                INSERT OR IGNORE INTO raw_url_index
                (source_file_id, raw_url, raw_url_line_anchor, access_status)
                VALUES (?, ?, ?, ?)
                """,
                (
                    source_id,
                    row["raw_url"],
                    f"{row['raw_url']}#L{row['line_no']}",
                    "candidate",
                ),
            )

    stats["source_files"] = len(source_seen)
    stats["terms"] = len(term_seen)
    stats["occurrences"] = stats["rows"]
    return stats


def create_scan_run(conn: sqlite3.Connection, repo_9dot0_commit: str) -> int:
    cur = conn.execute(
        """
        INSERT INTO scan_run
        (run_name, scanner_version, repo_9dot0_commit, scope_note, is_whole_repo_scan, is_db_build)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            "readme_vocab_core_filtered_preview_pass14_import",
            "extract_readme_vocab_v3.py",
            repo_9dot0_commit,
            "Selected README source import only. No whole-repo scan.",
            0,
            1,
        ),
    )
    return int(cur.lastrowid)


def write_build_report(report_path: Path, db_path: Path, csv_path: Path, stats: dict[str, int]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# SQLite MVP build report",
        "",
        "## status",
        "",
        "This is a derived DB build report.",
        "",
        "The SQLite DB is not original source.",
        "Raw URLs remain the source coordinates.",
        "",
        "## paths",
        "",
        f"- db_path: `{db_path}`",
        f"- input_csv: `{csv_path}`",
        "",
        "## stats",
        "",
    ]
    for key, value in stats.items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build vocab.branch SQLite MVP DB.")
    parser.add_argument("--repo", default=os.getcwd(), help="Path to Repo.9Dot0")
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH), help="Output SQLite DB path")
    parser.add_argument("--input-csv", default=DEFAULT_INPUT_CSV, help="Input v3 preview CSV path")
    parser.add_argument("--schema", default=DEFAULT_SCHEMA_SQL, help="SQL schema path")
    parser.add_argument("--repo-commit", default="unknown", help="Repo.9Dot0 commit hash")
    parser.add_argument("--report", default="", help="Optional markdown build report path")
    parser.add_argument("--allow-repo-db", action="store_true", help="Allow DB output inside Git repo")
    args = parser.parse_args()

    repo_dir = Path(args.repo).resolve()
    db_path = Path(args.db).expanduser().resolve()
    csv_path = (repo_dir / args.input_csv).resolve()
    schema_path = (repo_dir / args.schema).resolve()

    if not csv_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {csv_path}")

    if not schema_path.exists():
        raise FileNotFoundError(f"Schema SQL not found: {schema_path}")

    if repo_dir in db_path.parents and not args.allow_repo_db:
        raise RuntimeError(
            "Refusing to create SQLite DB inside Git repo. "
            "Use runtime path outside repo or pass --allow-repo-db intentionally."
        )

    if db_path.exists():
        raise FileExistsError(f"DB already exists, refusing overwrite: {db_path}")

    conn = connect_db(db_path)
    try:
        conn.executescript(read_sql(schema_path))
        scan_run_id = create_scan_run(conn, args.repo_commit)
        stats = import_csv(conn, csv_path, scan_run_id)
        conn.commit()
    finally:
        conn.close()

    if args.report:
        report_path = Path(args.report).expanduser().resolve()
    else:
        report_path = DEFAULT_RUNTIME_DIR / "sqlite_mvp_build_report.md"

    write_build_report(report_path, db_path, csv_path, stats)

    print(f"db_path={db_path}")
    print(f"report_path={report_path}")
    for key, value in stats.items():
        print(f"{key}={value}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
