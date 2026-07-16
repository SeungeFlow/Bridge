# AI DB reader operation guide

## status

pass: 38
role: AI DB reader operation guide
db_modification: false

## purpose

This guide defines how gpt.direct, gpt.github, or a reader instance should operate the vocab.branch SQLite MVP reader safely.

## operating chain

```text
gpt.direct asks a source/term question
→ gpt.github runs read-only query command
→ query_vocab_reader.py returns compact rows
→ gpt.direct interprets with guard
→ Raw URL is followed only when source inspection is needed
```

## current DB baseline

```text
source_file=8
readme_source=8
vocab_term=1710
term_status=1710
term_occurrence=3855
raw_url_index=3855
core_token_candidate=162
structural_trigger_candidate=403
```

## first readme_source rows

```text
1|repo_9dot0_branch_field|SeungeFlow/9Dot0|main|README.md
2|repo_9dot0_branch_field|SeungeFlow/9Dot0|main|03_branch_fields/market/README.md
3|repo_9dot0_branch_field|SeungeFlow/9Dot0|main|03_branch_fields/sohosa/README.md
4|repo_9dot0_branch_field|SeungeFlow/9Dot0|main|03_branch_fields/history/README.md
5|repo_9dot0_branch_field|SeungeFlow/9Dot0|main|03_branch_fields/vocab/README.md
6|repo_seungeflow_primary_observer|SeungeFlow/SeungeFlow|Y_Branch|README.md
7|repo_seungeflow_primary_observer|SeungeFlow/SeungeFlow|main|README.md
8|repo_seungeflow_primary_observer|SeungeFlow/SeungeFlow|first_flow|README.md
```

## core reader tasks

### 1. summary check

Purpose:

Confirm DB is available and counts are expected.

### 2. readme source check

Purpose:

Confirm the reader is anchored to README baseline surfaces.

### 3. term lookup

Purpose:

Find status, occurrence count, and top source/context rows for one term.

### 4. context lookup

Purpose:

Return compact source line contexts with Raw URL coordinates.

### 5. status lookup

Purpose:

List structural_trigger_candidate or core_token_candidate terms.

## preferred first terms

```text
C
m
t
p
?
Ctp
Ctp24
Y_Branch
Seed.Base
Raw URL
source identity
README baseline
```

## branch use

vocab.branch reader output may support:

```text
branch.market
branch.sohosa
branch.history
```

But it does not complete those branches by itself.

## stop conditions

Stop reader operation if:

- DB checksum changes during read-only query
- query output lacks Raw URL/source identity
- repo status changes after query
- query requires whole-repo scan
- term is missing from README baseline and user requests interpretation

## escalation

If a term is missing from the DB, do not invent.

Escalate to gpt.direct:

```text
TERM_MISSING_FROM_README_BASELINE
```

Then gpt.direct decides whether README.md must be updated first.
