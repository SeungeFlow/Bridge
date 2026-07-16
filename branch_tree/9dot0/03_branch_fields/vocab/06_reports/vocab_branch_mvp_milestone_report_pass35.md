# vocab.branch MVP milestone report — pass35

## status

pass: 35
recorded_in_pass: 36
role: vocab.branch MVP milestone summary
repo_9dot0_commit_at_milestone: 98a3dc037416813361c6c3c7c38d25bb26554a14
recording_commit_base: 98a3dc037416813361c6c3c7c38d25bb26554a14

## milestone judgment

vocab.branch MVP first loop is complete.

The branch-field moved from skeleton design to an operational local AI DB reader MVP.

## core sentence

```text
vocab.branch는 단어장이 아니라, 생각의 표면을 구조적으로 해체하는 첫 branch.
```

## completed chain

```text
vocab.branch skeleton
→ README vocab source list
→ README vocab scan protocol
→ v1 raw preview
→ v2 structural filter
→ v3 core-token recovery
→ SQLite MVP schema
→ local runtime SQLite DB build
→ readme_source metadata correction
→ AI DB reader read-only query script
→ read-only smoke test
→ GitHub summary reports
```

## source principle

The DB is not original source.

The DB is a derived Seed.Base-like reader field.

Original source remains in md files and Raw URLs.

## minimal connector rule

Repo, Branch, Directory, and md files are connected by:

1. word
2. Raw URL

A word connects meaning.

A Raw URL fixes source identity.

## README baseline

The MVP uses selected README sources as the first vocabulary baseline.

Current readme_source rows:

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

## DB runtime state

Local runtime DB:

```text
/home/gogiseung/seungeflow_runtime/vocab_reader/vocab_reader.sqlite
```

DB counts after readme_source population:

```text
scan_run=1
source_file=8
readme_source=8
vocab_term=1710
term_status=1710
term_occurrence=3855
raw_url_index=3855
term_relation_candidate=0
term_card_candidate=0
reader_query_log=0
```

Status counts:

```text
filtered_candidate=2305
demoted_common=985
structural_trigger_candidate=403
core_token_candidate=162
```

## core-token recovery

v3 restored short structural tokens as core candidates.

Confirmed core candidates include:

```text
C
?
m
p
t
Ctp24
A
Core
S₄
Path
C=(m,t,p,?)
S₁
S₂
S₃
Ctp
C=tp
S4
```

## AI DB reader smoke test

The AI DB reader was tested in read-only mode.

Query modes tested:

```text
summary
readme_sources
core
status structural_trigger_candidate
term C
term Ctp24
term Y_Branch
context C
```

Read-only verification:

```text
db_sha_before=419d90b3779f83dba45ffc88126ede38aad16842d84c051ff702642ab01eb0af
db_sha_after=419d90b3779f83dba45ffc88126ede38aad16842d84c051ff702642ab01eb0af
read_only_checksum_check=OK
smoke_output_check=OK
```

## what has been achieved

The repo now contains:

- vocab.branch structure
- README vocab extraction protocol
- v1/v2/v3 scan scripts and reports
- SQLite MVP schema
- local runtime build script
- readme_source correction tooling
- AI DB reader read-only query script
- runtime-result summary reports

The local runtime now contains:

- SQLite reader DB
- DB build report
- readme_source population report
- AI DB reader smoke test report
- pre-pass28 DB backup

## what has not been claimed

This milestone does not claim:

- final interpretation
- full source coverage
- whole-repository scan completion
- term card completion
- relation finalization
- history/etymology decomposition
- Hanja/vector decomposition
- renderer integration
- music_language integration
- market/sohosa/history branch completion

## next work candidates

### next technical pass

Create a tracked GitHub summary report for this milestone, then commit it.

### next reader pass

Create a first AI DB reader handoff prompt so another AI instance can query DB outputs safely.

### next DB pass

Add reader_query_log only if logging is explicitly needed.

For now, keep reader mode read-only.

### next vocab pass

Generate first term-card candidates from core_token_candidate terms.

Suggested first term cards:

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

### next branch pass

Use vocab.branch as shared trigger layer for:

```text
branch.market
branch.sohosa
branch.history
```

## guard

The DB output is derived evidence.

The DB is not the original source.

High frequency is not final meaning priority.

README.md remains the first vocabulary law.

If a needed structural term is missing from the relevant README.md, update the README.md first.

Original source remains in md files and Raw URLs.
