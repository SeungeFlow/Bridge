#!/usr/bin/env python3
"""
Read-only query tool for vocab.branch SQLite MVP DB.

Designed in pass31.
Do not execute in pass31.

Purpose:
- Let an AI instance query the local SQLite reader DB safely.
- Use read-only SQLite connection mode.
- Return compact source/term/context results.
- Never modify the DB.
"""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path
from typing import Iterable


DEFAULT_DB_PATH = Path.home() / "seungeflow_runtime" / "vocab_reader" / "vocab_reader.sqlite"


def connect_readonly(db_path: Path) -> sqlite3.Connection:
    if not db_path.exists():
        raise FileNotFoundError(f"SQLite DB not found: {db_path}")

    uri = f"file:{db_path}?mode=ro"
    conn = sqlite3.connect(uri, uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def print_rows(rows: Iterable[sqlite3.Row], columns: list[str]) -> None:
    print("|".join(columns))
    print("|".join("---" for _ in columns))
    for row in rows:
        print("|".join(str(row[col]) if row[col] is not None else "" for col in columns))


def query_summary(conn: sqlite3.Connection) -> None:
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

    print("# summary")
    for table in tables:
        count = conn.execute(f"SELECT COUNT(*) AS c FROM {table}").fetchone()["c"]
        print(f"{table}={count}")

    print()
    print("# occurrence status counts")
    rows = conn.execute(
        """
        SELECT occurrence_status, COUNT(*) AS count
        FROM term_occurrence
        GROUP BY occurrence_status
        ORDER BY count DESC, occurrence_status
        """
    ).fetchall()
    print_rows(rows, ["occurrence_status", "count"])


def query_readme_sources(conn: sqlite3.Connection) -> None:
    rows = conn.execute(
        """
        SELECT
            rs.baseline_order,
            rs.baseline_class,
            sf.repo,
            sf.branch,
            sf.commit_hash,
            sf.path,
            sf.raw_url
        FROM readme_source rs
        JOIN source_file sf ON sf.id = rs.source_file_id
        ORDER BY rs.baseline_order
        """
    ).fetchall()

    print("# readme_sources")
    print_rows(
        rows,
        [
            "baseline_order",
            "baseline_class",
            "repo",
            "branch",
            "commit_hash",
            "path",
            "raw_url",
        ],
    )


def query_term(conn: sqlite3.Connection, term: str, limit: int) -> None:
    print(f"# term: {term}")

    rows = conn.execute(
        """
        SELECT
            vt.term,
            vt.normalized_term,
            ts.status,
            ts.score,
            COUNT(o.id) AS occurrence_count
        FROM vocab_term vt
        LEFT JOIN term_status ts ON ts.term_id = vt.id
        LEFT JOIN term_occurrence o ON o.term_id = vt.id
        WHERE vt.term = ? OR vt.normalized_term = ?
        GROUP BY vt.id, ts.id
        ORDER BY ts.score DESC, occurrence_count DESC
        """,
        (term, term),
    ).fetchall()

    if not rows:
        print("NO_TERM_MATCH")
        return

    print_rows(rows, ["term", "normalized_term", "status", "score", "occurrence_count"])

    print()
    print(f"# contexts limit={limit}")
    context_rows = conn.execute(
        """
        SELECT
            vt.term,
            o.occurrence_status,
            sf.repo,
            sf.branch,
            sf.commit_hash,
            sf.path,
            o.line_no,
            sf.raw_url,
            o.context
        FROM term_occurrence o
        JOIN vocab_term vt ON vt.id = o.term_id
        JOIN source_file sf ON sf.id = o.source_file_id
        WHERE vt.term = ? OR vt.normalized_term = ?
        ORDER BY
            CASE o.occurrence_status
                WHEN 'core_token_candidate' THEN 1
                WHEN 'structural_trigger_candidate' THEN 2
                WHEN 'filtered_candidate' THEN 3
                ELSE 4
            END,
            sf.repo,
            sf.branch,
            sf.path,
            o.line_no
        LIMIT ?
        """,
        (term, term, limit),
    ).fetchall()

    print_rows(
        context_rows,
        [
            "term",
            "occurrence_status",
            "repo",
            "branch",
            "commit_hash",
            "path",
            "line_no",
            "raw_url",
            "context",
        ],
    )


def query_status(conn: sqlite3.Connection, status: str, limit: int) -> None:
    rows = conn.execute(
        """
        SELECT
            vt.term,
            ts.status,
            ts.score,
            COUNT(o.id) AS occurrence_count,
            COUNT(DISTINCT o.source_file_id) AS source_count
        FROM term_status ts
        JOIN vocab_term vt ON vt.id = ts.term_id
        LEFT JOIN term_occurrence o ON o.term_id = vt.id
        WHERE ts.status = ?
        GROUP BY vt.id, ts.id
        ORDER BY ts.score DESC, occurrence_count DESC, source_count DESC, vt.term
        LIMIT ?
        """,
        (status, limit),
    ).fetchall()

    print(f"# status: {status}")
    print_rows(rows, ["term", "status", "score", "occurrence_count", "source_count"])


def query_core(conn: sqlite3.Connection, limit: int) -> None:
    query_status(conn, "core_token_candidate", limit)


def query_context(conn: sqlite3.Connection, term: str, limit: int) -> None:
    rows = conn.execute(
        """
        SELECT
            vt.term,
            o.occurrence_status,
            sf.repo,
            sf.branch,
            sf.path,
            o.line_no,
            sf.raw_url,
            o.context
        FROM term_occurrence o
        JOIN vocab_term vt ON vt.id = o.term_id
        JOIN source_file sf ON sf.id = o.source_file_id
        WHERE vt.term = ? OR vt.normalized_term = ?
        ORDER BY sf.repo, sf.branch, sf.path, o.line_no
        LIMIT ?
        """,
        (term, term, limit),
    ).fetchall()

    print(f"# context: {term}")
    print_rows(
        rows,
        ["term", "occurrence_status", "repo", "branch", "path", "line_no", "raw_url", "context"],
    )


def query_source(conn: sqlite3.Connection, limit: int) -> None:
    rows = conn.execute(
        """
        SELECT
            id,
            repo,
            branch,
            commit_hash,
            path,
            source_status,
            file_role,
            raw_url
        FROM source_file
        ORDER BY repo, branch, path
        LIMIT ?
        """,
        (limit,),
    ).fetchall()

    print("# source_file")
    print_rows(rows, ["id", "repo", "branch", "commit_hash", "path", "source_status", "file_role", "raw_url"])


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only query tool for vocab.branch SQLite MVP DB.")
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH), help="Path to SQLite DB")
    parser.add_argument(
        "--mode",
        required=True,
        choices=["summary", "readme_sources", "term", "status", "context", "source", "core"],
        help="Query mode",
    )
    parser.add_argument("--term", default="", help="Term for term/context mode")
    parser.add_argument("--status", default="structural_trigger_candidate", help="Status for status mode")
    parser.add_argument("--limit", type=int, default=40, help="Maximum row count")
    args = parser.parse_args()

    db_path = Path(args.db).expanduser().resolve()

    with connect_readonly(db_path) as conn:
        if args.mode == "summary":
            query_summary(conn)
        elif args.mode == "readme_sources":
            query_readme_sources(conn)
        elif args.mode == "term":
            if not args.term:
                raise SystemExit("--term is required for term mode")
            query_term(conn, args.term, args.limit)
        elif args.mode == "status":
            query_status(conn, args.status, args.limit)
        elif args.mode == "context":
            if not args.term:
                raise SystemExit("--term is required for context mode")
            query_context(conn, args.term, args.limit)
        elif args.mode == "source":
            query_source(conn, args.limit)
        elif args.mode == "core":
            query_core(conn, args.limit)
        else:
            raise SystemExit(f"Unsupported mode: {args.mode}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
