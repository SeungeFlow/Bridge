# README vocab scan protocol

## status

pass: 6
role: scan protocol
commit_base_repo_9dot0: 41308271f8c45277d51d1f2af8052b7788d61d78

## purpose

This protocol defines how vocab.branch scans README.md baseline vocabulary.

This is not a whole-repository scan.

This is not a DB build.

This is a selected README.md vocab extraction protocol.

## source rule

README.md is the baseline vocab surface.

The scan target must be explicitly listed.

The scanner must not recursively scan all files.

## first scan target classes

### A. Repo.9Dot0 README surfaces

- Repo.9Dot0 / main / README.md
- Repo.9Dot0 / main / 03_branch_fields/market/README.md
- Repo.9Dot0 / main / 03_branch_fields/sohosa/README.md
- Repo.9Dot0 / main / 03_branch_fields/history/README.md
- Repo.9Dot0 / main / 03_branch_fields/vocab/README.md

### B. Repo.SeungeFlow primary observer README surfaces

- Repo.SeungeFlow / Y_Branch / README.md
- Repo.SeungeFlow / main / README.md
- Repo.SeungeFlow / first_flow / README.md

### C. Later function-layer README surfaces

- seed_base README / README_for_AI / README_of selected files
- music_language README.md
- rendering README.md
- epluone capital market / sohosa_hyangsa README files

## extraction rule

The scanner may extract:

- Korean/Hangul tokens
- Hanja tokens
- English tokens
- structural symbols such as Ctp, 9dot0, S1, S2, S3, S4
- path-like source words

The scanner must preserve source identity:

- repo
- branch
- commit
- path
- raw_url
- line number
- source role

## no semantic finalization

The scanner does not decide final meaning.

It only produces candidate vocab and occurrence contexts.

## output rule

The scanner may write reports under:

`03_branch_fields/vocab/06_reports/`

Reports are derived outputs.

They do not replace original README.md sources.

## future DB relation

A later pass may insert scan results into SQLite/PostgreSQL.

That later DB is a derived Seed.Base-like reader field.
