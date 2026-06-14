#!/usr/bin/env python3
"""
branch.market source surface inventory candidate — pass135

Status:
- script_candidate: true
- read_only_intent: true
- path_scoped_root: 03_branch_fields/market
- repo_wide_find: false
- db_read: false
- db_write: false
- file_modification: false
- source_inventory_report_creation: false
- branch_market_analysis: false
- market_prediction: false
- trading_recommendation: false
- mt5_backtest_execution: false

Purpose:
Prepare a read-only, path-scoped inventory helper for later branch.market source surface inventory.

This script is a candidate only.
Do not execute in PASS135.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Dict, Iterable, List


REPO_REL_SCOPE = Path("03_branch_fields/market")

ALLOWED_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".csv",
    ".py",
    ".sh",
}

FORBIDDEN_SUFFIXES = {
    ".sqlite",
    ".sqlite-wal",
    ".sqlite-shm",
    ".db",
    ".bak",
}

EXCLUDED_DIR_NAMES = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}


def sha256_file(path: Path) -> str:
    """Read-only file hash."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def classify_source(path: Path) -> str:
    """Classify source role by path only; this is not market analysis."""
    parts = set(path.parts)
    name = path.name.lower()

    if "06_reports" in parts:
        return "report_or_plan_surface"
    if "05_scripts" in parts:
        return "script_surface"
    if name == "readme.md":
        return "readme_surface"
    if path.suffix == ".md":
        return "markdown_source_candidate"
    if path.suffix == ".py":
        return "script_candidate"
    if path.suffix == ".sh":
        return "shell_script_candidate"

    return "source_candidate"


def iter_scoped_files(scope_root: Path) -> Iterable[Path]:
    """
    Path-scoped traversal only.
    This intentionally avoids repo-wide find.
    """
    for path in scope_root.rglob("*"):
        if any(part in EXCLUDED_DIR_NAMES for part in path.parts):
            continue
        if not path.is_file():
            continue
        if path.suffix in FORBIDDEN_SUFFIXES:
            continue
        if path.suffix not in ALLOWED_SUFFIXES:
            continue
        yield path


def build_inventory(repo_root: Path) -> List[Dict[str, object]]:
    """
    Build a read-only inventory list.
    Does not write a report.
    Does not evaluate observers.
    Does not analyze branch.market.
    """
    scope_root = repo_root / REPO_REL_SCOPE

    if not scope_root.exists():
        raise FileNotFoundError(f"scope root missing: {scope_root}")

    rows: List[Dict[str, object]] = []

    for path in sorted(iter_scoped_files(scope_root)):
        rel_path = path.relative_to(repo_root)
        stat = path.stat()

        rows.append(
            {
                "source_path": str(rel_path),
                "source_type": path.suffix.lstrip(".") or "no_suffix",
                "source_role": classify_source(rel_path),
                "source_status": "source_surface_candidate",
                "scope": str(REPO_REL_SCOPE),
                "read_only_hash_sha256": sha256_file(path),
                "size_bytes": stat.st_size,
                "relation_to_C_m_t_p": "not_evaluated",
                "relation_to_MT5_runtime_readiness": "not_evaluated",
                "relation_to_observer_layer": "not_evaluated",
                "safe_for_later_alignment_use": "requires_review",
            }
        )

    return rows


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Read-only branch.market source surface inventory candidate. "
            "Path-scoped to 03_branch_fields/market. "
            "Does not write output files unless stdout is redirected by the operator."
        )
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root. Default: current directory.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print JSON inventory to stdout. Does not create a file.",
    )

    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    inventory = build_inventory(repo_root)

    if args.json:
        print(json.dumps(inventory, ensure_ascii=False, indent=2))
    else:
        print("branch.market source surface inventory candidate")
        print(f"scope={REPO_REL_SCOPE}")
        print("repo_wide_find=false")
        print("db_read=false")
        print("db_write=false")
        print("file_modification=false")
        print("branch_market_analysis=false")
        print(f"source_count={len(inventory)}")
        for row in inventory:
            print(f"- {row['source_path']} | {row['source_role']} | {row['source_status']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
