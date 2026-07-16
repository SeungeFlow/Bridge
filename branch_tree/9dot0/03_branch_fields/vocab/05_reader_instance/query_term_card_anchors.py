#!/usr/bin/env python3
"""
Read-only batch anchor query for vocab.branch term-card candidates.

Designed in pass70.
Do not execute in pass70.

Purpose:
- Query local SQLite MVP DB for term-card candidate anchors.
- Produce a markdown report with source identity rows.
- Use read-only SQLite connection mode.
- Never modify DB.
"""

from __future__ import annotations

import argparse
import hashlib
import sqlite3
from dataclasses import dataclass
from pathlib import Path


DEFAULT_DB_PATH = Path.home() / "seungeflow_runtime" / "vocab_reader" / "vocab_reader.sqlite"
DEFAULT_REPORT_PATH = Path.home() / "seungeflow_runtime" / "vocab_reader" / "term_card_anchor_enrichment_report_pass72.md"


@dataclass(frozen=True)
class CardQuery:
    card_term: str
    card_file: str
    query_terms: tuple[str, ...]


CARD_QUERIES: tuple[CardQuery, ...] = (
    CardQuery("C", "03_branch_fields/vocab/02_term_cards/cards/C.term_card_candidate.md", ("C",)),
    CardQuery("m", "03_branch_fields/vocab/02_term_cards/cards/m.term_card_candidate.md", ("m",)),
    CardQuery("t", "03_branch_fields/vocab/02_term_cards/cards/t.term_card_candidate.md", ("t",)),
    CardQuery("p", "03_branch_fields/vocab/02_term_cards/cards/p.term_card_candidate.md", ("p",)),
    CardQuery("?", "03_branch_fields/vocab/02_term_cards/cards/question_mark.term_card_candidate.md", ("?",)),
    CardQuery("Ctp", "03_branch_fields/vocab/02_term_cards/cards/Ctp.term_card_candidate.md", ("Ctp",)),
    CardQuery("Ctp24", "03_branch_fields/vocab/02_term_cards/cards/Ctp24.term_card_candidate.md", ("Ctp24",)),
    CardQuery("Raw URL", "03_branch_fields/vocab/02_term_cards/cards/Raw_URL.term_card_candidate.md", ("Raw URL", "Raw", "URL", "raw_url")),
    CardQuery("source identity", "03_branch_fields/vocab/02_term_cards/cards/source_identity.term_card_candidate.md", ("source identity", "source", "identity")),
    CardQuery("README baseline", "03_branch_fields/vocab/02_term_cards/cards/README_baseline.term_card_candidate.md", ("README baseline", "README", "readme_source")),
    CardQuery("Seed.Base", "03_branch_fields/vocab/02_term_cards/cards/Seed_Base.term_card_candidate.md", ("Seed.Base",)),
    CardQuery("Y_Branch", "03_branch_fields/vocab/02_term_cards/cards/Y_Branch.term_card_candidate.md", ("Y_Branch",)),
    CardQuery("vocab.branch", "03_branch_fields/vocab/02_term_cards/cards/vocab_branch.term_card_candidate.md", ("vocab.branch",)),
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def connect_readonly(db_path: Path) -> sqlite3.Connection:
    if not db_path.exists():
        raise FileNotFoundError(f"SQLite DB not found: {db_path}")

    uri = f"file:{db_path}?mode=ro"
    conn = sqlite3.connect(uri, uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def query_summary(conn: sqlite3.Connection) -> list[str]:
    tables = [
        "scan_run",
        "source_file",
        "readme_source",
        "vocab_term",
        "term_status",
        "term_occurrence",
        "raw_url_index",
        "term_relation_candidate",
        "term_card_candidate",
        "reader_query_log",
    ]
    lines: list[str] = []
    for table in tables:
        count = conn.execute(f"SELECT COUNT(*) AS c FROM {table}").fetchone()["c"]
        lines.append(f"{table}={count}")
    return lines


def query_term_rows(conn: sqlite3.Connection, term: str, limit: int) -> list[sqlite3.Row]:
    return conn.execute(
        """
        SELECT
            vt.term AS term,
            o.occurrence_status AS status,
            sf.repo AS repo,
            sf.branch AS branch,
            sf.commit_hash AS commit_hash,
            sf.path AS path,
            o.line_no AS line_no,
            sf.raw_url AS raw_url,
            o.context AS context
        FROM term_occurrence o
        JOIN vocab_term vt ON vt.id = o.term_id
        JOIN source_file sf ON sf.id = o.source_file_id
        WHERE vt.term = ? OR vt.normalized_term = ?
        ORDER BY
            CASE o.occurrence_status
                WHEN 'core_token_candidate' THEN 1
                WHEN 'structural_trigger_candidate' THEN 2
                WHEN 'filtered_candidate' THEN 3
                WHEN 'demoted_common' THEN 4
                ELSE 5
            END,
            sf.repo,
            sf.branch,
            sf.path,
            o.line_no
        LIMIT ?
        """,
        (term, term, limit),
    ).fetchall()


def row_to_text(row: sqlite3.Row) -> str:
    return (
        f"{row['term']} | {row['status']} | {row['repo']} | {row['branch']} | "
        f"{row['commit_hash']} | {row['path']} | {row['line_no']} | "
        f"{row['raw_url']} | {row['context']}"
    )


def write_report(
    report_path: Path,
    db_path: Path,
    db_sha_before: str,
    db_sha_after: str,
    limit: int,
    conn: sqlite3.Connection,
) -> None:
    lines: list[str] = []
    lines.append("# term-card anchor enrichment runtime report")
    lines.append("")
    lines.append("## status")
    lines.append("")
    lines.append("role: read-only term-card anchor enrichment")
    lines.append("db_modification: false")
    lines.append("final_definition: false")
    lines.append("")
    lines.append("## DB path")
    lines.append("")
    lines.append(f"`{db_path}`")
    lines.append("")
    lines.append("## DB checksum")
    lines.append("")
    lines.append("```text")
    lines.append(f"db_sha_before={db_sha_before}")
    lines.append(f"db_sha_after={db_sha_after}")
    lines.append("read_only_checksum_check=OK" if db_sha_before == db_sha_after else "read_only_checksum_check=FAILED")
    lines.append("```")
    lines.append("")
    lines.append("## DB summary")
    lines.append("")
    lines.append("```text")
    lines.extend(query_summary(conn))
    lines.append("```")
    lines.append("")
    lines.append("## anchor rows")
    lines.append("")

    for card in CARD_QUERIES:
        lines.append(f"### {card.card_term}")
        lines.append("")
        lines.append(f"card_file: `{card.card_file}`")
        lines.append("")
        lines.append("query_terms:")
        lines.append("")
        lines.append("```text")
        for qt in card.query_terms:
            lines.append(qt)
        lines.append("```")
        lines.append("")

        matched_any = False
        for qt in card.query_terms:
            rows = query_term_rows(conn, qt, limit)
            lines.append(f"#### query term: {qt}")
            lines.append("")
            if not rows:
                lines.append("```text")
                lines.append("NO_EXACT_TERM_MATCH")
                lines.append("```")
                lines.append("")
                continue

            matched_any = True
            lines.append("```text")
            lines.append("term | status | repo | branch | commit | path | line_no | raw_url | context")
            for row in rows:
                lines.append(row_to_text(row))
            lines.append("```")
            lines.append("")

        if not matched_any:
            lines.append("anchor_status: NO_MATCH_FOR_CARD")
            lines.append("")
        else:
            lines.append("anchor_status: MATCHED")
            lines.append("")

    lines.append("## guard")
    lines.append("")
    lines.append("This report is DB-derived evidence.")
    lines.append("")
    lines.append("It does not finalize any term-card.")
    lines.append("")
    lines.append("Original source remains in md files and Raw URLs.")
    lines.append("")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only anchor enrichment query for vocab.branch term-card candidates.")
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH), help="Path to SQLite DB")
    parser.add_argument("--report", default=str(DEFAULT_REPORT_PATH), help="Output markdown report path")
    parser.add_argument("--limit", type=int, default=12, help="Maximum source rows per query term")
    parser.add_argument("--allow-overwrite", action="store_true", help="Allow overwriting existing report")
    args = parser.parse_args()

    db_path = Path(args.db).expanduser().resolve()
    report_path = Path(args.report).expanduser().resolve()

    if report_path.exists() and not args.allow_overwrite:
        raise FileExistsError(f"Report already exists, refusing overwrite: {report_path}")

    db_sha_before = sha256_file(db_path)
    with connect_readonly(db_path) as conn:
        db_sha_after = sha256_file(db_path)
        write_report(report_path, db_path, db_sha_before, db_sha_after, args.limit, conn)

    final_sha = sha256_file(db_path)
    if db_sha_before != final_sha:
        raise RuntimeError("DB checksum changed during read-only anchor enrichment query.")

    print(f"db_path={db_path}")
    print(f"report_path={report_path}")
    print(f"db_sha_before={db_sha_before}")
    print(f"db_sha_after={final_sha}")
    print("read_only_checksum_check=OK")
    print(f"card_query_count={len(CARD_QUERIES)}")
    print(f"row_limit_per_query={args.limit}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
