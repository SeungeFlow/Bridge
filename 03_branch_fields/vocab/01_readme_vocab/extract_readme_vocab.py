#!/usr/bin/env python3
"""
README vocab extractor for Repo.9Dot0 vocab.branch.

Purpose:
- Read only explicitly listed README.md source units.
- Extract baseline vocab candidates.
- Preserve source identity with raw URLs.
- Produce markdown and CSV reports.

Guard:
- This script does not scan the whole repository.
- This script does not create a DB.
- This script does not modify Repo.SeungeFlow.
"""

from __future__ import annotations

import csv
import os
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SourceUnit:
    repo_label: str
    local_repo_env: str
    branch: str
    commit: str
    path: str
    role: str


SOURCES: list[SourceUnit] = [
    SourceUnit("SeungeFlow/9Dot0", "REPO_9DOT0", "main", "41308271f8c45277d51d1f2af8052b7788d61d78", "README.md", "Repo.9Dot0 entry surface"),
    SourceUnit("SeungeFlow/9Dot0", "REPO_9DOT0", "main", "41308271f8c45277d51d1f2af8052b7788d61d78", "03_branch_fields/market/README.md", "branch.market surface"),
    SourceUnit("SeungeFlow/9Dot0", "REPO_9DOT0", "main", "41308271f8c45277d51d1f2af8052b7788d61d78", "03_branch_fields/sohosa/README.md", "branch.sohosa surface"),
    SourceUnit("SeungeFlow/9Dot0", "REPO_9DOT0", "main", "41308271f8c45277d51d1f2af8052b7788d61d78", "03_branch_fields/history/README.md", "branch.history surface"),
    SourceUnit("SeungeFlow/9Dot0", "REPO_9DOT0", "main", "41308271f8c45277d51d1f2af8052b7788d61d78", "03_branch_fields/vocab/README.md", "branch.vocab surface"),

    SourceUnit("SeungeFlow/SeungeFlow", "REPO_SEUNGEFLOW", "Y_Branch", "32f8b248dc7e9ec5c1856b78b4ee207b8861d315", "README.md", "Y_Branch operating surface"),
    SourceUnit("SeungeFlow/SeungeFlow", "REPO_SEUNGEFLOW", "main", "85802d707160da1a1cfb2bfacfe9cea222a3c77c", "README.md", "main representative surface"),
    SourceUnit("SeungeFlow/SeungeFlow", "REPO_SEUNGEFLOW", "first_flow", "1fa5f28ca7647da445a5b2ef130f3852845ccb68", "README.md", "structure-body protection surface"),
]


TOKEN_RE = re.compile(
    r"Ctp24|Ctp|9dot0|S[1-4]|[A-Za-z][A-Za-z0-9_./+-]*|[가-힣]{1,}|[\u4E00-\u9FFF]{1,}|[0-9]+(?:dot[0-9]+)?"
)

STOPWORDS = {
    "the", "and", "or", "of", "to", "a", "an", "in", "is", "as", "for", "with",
    "this", "that", "not", "it", "be", "by", "from", "on", "at", "are",
    "true", "false", "md", "README", "README.md"
}


def run_git_show(repo_dir: Path, commit: str, path: str) -> str:
    cmd = ["git", "-C", str(repo_dir), "show", f"{commit}:{path}"]
    result = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise RuntimeError(f"git show failed for {repo_dir} {commit}:{path}\n{result.stderr}")
    return result.stdout


def raw_url(source: SourceUnit) -> str:
    return f"https://raw.githubusercontent.com/{source.repo_label}/{source.commit}/{source.path}"


def tokenize(line: str) -> list[str]:
    tokens = TOKEN_RE.findall(line)
    cleaned: list[str] = []
    for token in tokens:
        t = token.strip()
        if not t:
            continue
        if t in STOPWORDS:
            continue
        if len(t) == 1 and re.fullmatch(r"[A-Za-z]", t):
            continue
        cleaned.append(t)
    return cleaned


def main() -> int:
    repo_9dot0 = Path(os.environ.get("REPO_9DOT0", str(Path.home() / "seungeflow" / "9Dot0")))
    repo_seungeflow = Path(os.environ.get("REPO_SEUNGEFLOW", str(Path.home() / "seungeflow")))

    repo_map = {
        "REPO_9DOT0": repo_9dot0,
        "REPO_SEUNGEFLOW": repo_seungeflow,
    }

    out_dir = repo_9dot0 / "03_branch_fields" / "vocab" / "06_reports"
    out_dir.mkdir(parents=True, exist_ok=True)

    md_report = out_dir / "readme_vocab_scan_preview_pass6.md"
    csv_report = out_dir / "readme_vocab_scan_preview_pass6.csv"

    term_counter: Counter[str] = Counter()
    term_sources: dict[str, set[str]] = defaultdict(set)
    rows: list[dict[str, str | int]] = []
    source_errors: list[str] = []

    for source in SOURCES:
        repo_dir = repo_map[source.local_repo_env]
        try:
            text = run_git_show(repo_dir, source.commit, source.path)
        except Exception as exc:
            source_errors.append(f"{source.repo_label} {source.commit}:{source.path} :: {exc}")
            continue

        for line_no, line in enumerate(text.splitlines(), start=1):
            for token in tokenize(line):
                term_counter[token] += 1
                source_key = f"{source.repo_label}@{source.commit}:{source.path}"
                term_sources[token].add(source_key)
                rows.append({
                    "term": token,
                    "repo": source.repo_label,
                    "branch": source.branch,
                    "commit": source.commit,
                    "path": source.path,
                    "line_no": line_no,
                    "role": source.role,
                    "raw_url": raw_url(source),
                    "context": line.strip()[:300],
                })

    with csv_report.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["term", "repo", "branch", "commit", "path", "line_no", "role", "raw_url", "context"],
        )
        writer.writeheader()
        writer.writerows(rows)

    with md_report.open("w", encoding="utf-8") as f:
        f.write("# README vocab scan preview pass6\n\n")
        f.write("## status\n\n")
        f.write("This is a preview report generated from explicitly listed README sources only.\n\n")
        f.write("This is not a whole-repository scan.\n")
        f.write("This is not a DB build.\n\n")

        f.write("## source units\n\n")
        for source in SOURCES:
            f.write(f"- `{source.repo_label}` `{source.branch}` `{source.commit}` `{source.path}` — {source.role}\n")
        f.write("\n")

        if source_errors:
            f.write("## source errors\n\n")
            for err in source_errors:
                f.write(f"- {err}\n")
            f.write("\n")

        f.write("## top vocab candidates\n\n")
        f.write("| term | count | source_count |\n")
        f.write("|---|---:|---:|\n")
        for term, count in term_counter.most_common(120):
            f.write(f"| `{term}` | {count} | {len(term_sources[term])} |\n")

        f.write("\n## output files\n\n")
        f.write(f"- `{md_report.relative_to(repo_9dot0)}`\n")
        f.write(f"- `{csv_report.relative_to(repo_9dot0)}`\n")

    print(f"md_report={md_report}")
    print(f"csv_report={csv_report}")
    print(f"terms={len(term_counter)}")
    print(f"occurrences={len(rows)}")
    print(f"errors={len(source_errors)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
