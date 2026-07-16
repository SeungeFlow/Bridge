#!/usr/bin/env python3
"""
README vocab extractor v2 for Repo.9Dot0 vocab.branch.

Purpose:
- Read only explicitly listed README.md source units.
- Preserve raw occurrences.
- Filter common function words.
- Highlight structural trigger candidates.
- Do not build a DB.
- Do not scan whole repositories.
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
    SourceUnit("SeungeFlow/9Dot0", "REPO_9DOT0", "main", "00937b38ee3aa47030153649988ea17ce133e0a9", "README.md", "Repo.9Dot0 entry surface"),
    SourceUnit("SeungeFlow/9Dot0", "REPO_9DOT0", "main", "00937b38ee3aa47030153649988ea17ce133e0a9", "03_branch_fields/market/README.md", "branch.market surface"),
    SourceUnit("SeungeFlow/9Dot0", "REPO_9DOT0", "main", "00937b38ee3aa47030153649988ea17ce133e0a9", "03_branch_fields/sohosa/README.md", "branch.sohosa surface"),
    SourceUnit("SeungeFlow/9Dot0", "REPO_9DOT0", "main", "00937b38ee3aa47030153649988ea17ce133e0a9", "03_branch_fields/history/README.md", "branch.history surface"),
    SourceUnit("SeungeFlow/9Dot0", "REPO_9DOT0", "main", "00937b38ee3aa47030153649988ea17ce133e0a9", "03_branch_fields/vocab/README.md", "branch.vocab surface"),

    SourceUnit("SeungeFlow/SeungeFlow", "REPO_SEUNGEFLOW", "Y_Branch", "32f8b248dc7e9ec5c1856b78b4ee207b8861d315", "README.md", "Y_Branch operating surface"),
    SourceUnit("SeungeFlow/SeungeFlow", "REPO_SEUNGEFLOW", "main", "85802d707160da1a1cfb2bfacfe9cea222a3c77c", "README.md", "main representative surface"),
    SourceUnit("SeungeFlow/SeungeFlow", "REPO_SEUNGEFLOW", "first_flow", "1fa5f28ca7647da445a5b2ef130f3852845ccb68", "README.md", "structure-body protection surface"),
]


TOKEN_RE = re.compile(
    r"9dot0|Ctp24|Ctp|S[1-4]|Y_Branch|vocab\.branch|[A-Za-z][A-Za-z0-9_./+-]*|[가-힣]{1,}|[\u4E00-\u9FFF]{1,}|[0-9]+"
)

KOREAN_COMMON = {
    "은", "는", "이", "가", "을", "를", "의", "와", "과", "에", "로", "으로", "에서", "에게",
    "것", "수", "등", "및", "또", "또는", "그리고", "그러나", "하지만", "때문", "먼저",
    "있다", "없다", "아니다", "않는다", "이다", "한다", "된다", "되는", "하는", "하지",
    "위한", "통해", "대한", "같은", "여기", "현재", "차후", "아직", "즉",
}

ENGLISH_COMMON = {
    "the", "and", "or", "of", "to", "a", "an", "in", "is", "as", "for", "with", "this", "that",
    "not", "it", "be", "by", "from", "on", "at", "are", "was", "were", "true", "false", "text",
    "markdown", "file", "files", "readme", "md", "path", "role", "status", "first", "current",
    "later", "future", "under", "over", "only", "all", "whole", "new",
}

STRUCTURAL_ALLOWLIST = {
    "AI", "Ctp", "Ctp24", "S1", "S2", "S3", "S4", "Y_Branch", "SeungeFlow", "9dot0",
    "dot", "diff", "difference", "orbit", "COG", "boundary", "field", "source", "identity",
    "guard", "relation", "matrix", "swap", "branch", "vocab.branch", "vocab", "README.md",
    "Raw", "URL", "Raw_URL", "context", "window", "Seed", "Seed.Base", "DB", "reader",
    "directory", "repo", "runtime", "surface", "entry", "observer", "target", "criterion",
    "구조", "원리", "구조원리", "구조연산식", "존재", "자리", "경계", "차이", "전이",
    "관계", "관측자", "관측기준", "관측대상", "단어", "문자", "생각", "표면", "해체",
    "훈민정음", "벡터", "행렬", "스칼라", "집합", "수열", "구조수열", "소호사", "향사",
    "자본시장", "역사", "오감도", "김해경", "이상", "이 상", "Price", "MT5", "OHLC",
}

NUMERIC_KEEP = {"0", "9"}


def run_git_show(repo_dir: Path, commit: str, path: str) -> str:
    cmd = ["git", "-C", str(repo_dir), "show", f"{commit}:{path}"]
    result = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise RuntimeError(f"git show failed for {repo_dir} {commit}:{path}\n{result.stderr}")
    return result.stdout


def raw_url(source: SourceUnit) -> str:
    return f"https://raw.githubusercontent.com/{source.repo_label}/{source.commit}/{source.path}"


def tokenize(line: str) -> list[str]:
    return [t.strip() for t in TOKEN_RE.findall(line) if t.strip()]


def is_common(token: str) -> bool:
    lower = token.lower()
    if token in KOREAN_COMMON:
        return True
    if lower in ENGLISH_COMMON:
        return True
    if re.fullmatch(r"[0-9]+", token) and token not in NUMERIC_KEEP:
        return True
    if len(token) == 1 and re.fullmatch(r"[A-Za-z가-힣]", token) and token not in NUMERIC_KEEP:
        return True
    return False


def structural_score(token: str, count: int, source_count: int) -> int:
    score = 0
    if token in STRUCTURAL_ALLOWLIST:
        score += 10
    if "_" in token or "." in token or "/" in token:
        score += 3
    if re.search(r"[A-Za-z]", token) and re.search(r"[0-9]", token):
        score += 3
    if re.search(r"[가-힣]", token) and len(token) >= 2:
        score += 1
    if re.search(r"[\u4E00-\u9FFF]", token):
        score += 2
    if source_count >= 2:
        score += 2
    if count >= 5:
        score += 1
    return score


def main() -> int:
    repo_9dot0 = Path(os.environ.get("REPO_9DOT0", str(Path.home() / "seungeflow" / "9Dot0")))
    repo_seungeflow = Path(os.environ.get("REPO_SEUNGEFLOW", str(Path.home() / "seungeflow")))

    repo_map = {
        "REPO_9DOT0": repo_9dot0,
        "REPO_SEUNGEFLOW": repo_seungeflow,
    }

    out_dir = repo_9dot0 / "03_branch_fields" / "vocab" / "06_reports"
    out_dir.mkdir(parents=True, exist_ok=True)

    md_report = out_dir / "readme_vocab_scan_filtered_preview_pass10.md"
    csv_report = out_dir / "readme_vocab_scan_filtered_preview_pass10.csv"

    raw_counter: Counter[str] = Counter()
    filtered_counter: Counter[str] = Counter()
    demoted_counter: Counter[str] = Counter()
    term_sources: dict[str, set[str]] = defaultdict(set)
    rows: list[dict[str, str | int]] = []
    errors: list[str] = []

    for source in SOURCES:
        repo_dir = repo_map[source.local_repo_env]
        try:
            text = run_git_show(repo_dir, source.commit, source.path)
        except Exception as exc:
            errors.append(f"{source.repo_label} {source.commit}:{source.path} :: {exc}")
            continue

        for line_no, line in enumerate(text.splitlines(), start=1):
            for token in tokenize(line):
                raw_counter[token] += 1
                source_key = f"{source.repo_label}@{source.commit}:{source.path}"
                term_sources[token].add(source_key)
                common = is_common(token)
                if common:
                    demoted_counter[token] += 1
                    status = "demoted_common"
                else:
                    filtered_counter[token] += 1
                    status = "filtered_candidate"

                rows.append({
                    "term": token,
                    "status": status,
                    "repo": source.repo_label,
                    "branch": source.branch,
                    "commit": source.commit,
                    "path": source.path,
                    "line_no": line_no,
                    "role": source.role,
                    "raw_url": raw_url(source),
                    "context": line.strip()[:300],
                })

    structural_rank = []
    for token, count in filtered_counter.items():
        source_count = len(term_sources[token])
        score = structural_score(token, count, source_count)
        structural_rank.append((score, count, source_count, token))
    structural_rank.sort(key=lambda x: (-x[0], -x[1], x[3]))

    with csv_report.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["term", "status", "repo", "branch", "commit", "path", "line_no", "role", "raw_url", "context"],
        )
        writer.writeheader()
        writer.writerows(rows)

    with md_report.open("w", encoding="utf-8") as f:
        f.write("# README vocab filtered preview pass10\n\n")
        f.write("## status\n\n")
        f.write("This is a filtered preview generated from explicitly listed README sources only.\n\n")
        f.write("This is not a whole-repository scan.\n")
        f.write("This is not a DB build.\n\n")
        f.write("## counts\n\n")
        f.write(f"- raw_terms: {len(raw_counter)}\n")
        f.write(f"- filtered_terms: {len(filtered_counter)}\n")
        f.write(f"- demoted_terms: {len(demoted_counter)}\n")
        f.write(f"- occurrences: {len(rows)}\n")
        f.write(f"- errors: {len(errors)}\n\n")

        if errors:
            f.write("## source errors\n\n")
            for err in errors:
                f.write(f"- {err}\n")
            f.write("\n")

        f.write("## top structural candidates\n\n")
        f.write("| rank | term | score | count | source_count |\n")
        f.write("|---:|---|---:|---:|---:|\n")
        for idx, (score, count, source_count, token) in enumerate(structural_rank[:160], start=1):
            f.write(f"| {idx} | `{token}` | {score} | {count} | {source_count} |\n")

        f.write("\n## top demoted common tokens\n\n")
        f.write("| term | count |\n")
        f.write("|---|---:|\n")
        for token, count in demoted_counter.most_common(80):
            f.write(f"| `{token}` | {count} |\n")

        f.write("\n## output files\n\n")
        f.write(f"- `{md_report.relative_to(repo_9dot0)}`\n")
        f.write(f"- `{csv_report.relative_to(repo_9dot0)}`\n")

    print(f"md_report={md_report}")
    print(f"csv_report={csv_report}")
    print(f"raw_terms={len(raw_counter)}")
    print(f"filtered_terms={len(filtered_counter)}")
    print(f"demoted_terms={len(demoted_counter)}")
    print(f"occurrences={len(rows)}")
    print(f"errors={len(errors)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
