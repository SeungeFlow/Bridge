# Term card candidate — source identity

## status

term: source identity
filename_slug: source_identity
card_status: CANDIDATE
final_definition: false
source_scope: vocab.branch MVP policy / AI DB reader rule / Raw URL card / README baseline rule
created_from: vocab.branch MVP / source identity connector rule
created_in_pass: 58
base_commit_repo_9dot0: 1581b5429095fe5565b514685a2d33e14d5b7e05

## 1. surface

```text
source identity
```

## 2. candidate role

source identity is a source-boundary operator candidate.

In vocab.branch, source identity prevents a DB row, summary, report, or AI interpretation from replacing original md source.

Raw URL is one part of source identity.

The broader source identity coordinate includes:

```text
repo
branch
commit
path
line_no
raw_url
source_status
context
```

Candidate reading:

```text
source identity fixes where a statement comes from before any interpretation is allowed.
```

This card does not finalize source identity.

This card records source identity as a controlled candidate for the boundary that binds word, source, DB row, Raw URL, and interpretation guard.

## 3. DB status

```text
status: source_identity_operator_candidate
score: not_assigned_in_pass58
occurrence_count: not_queried_in_pass58
source_count: not_queried_in_pass58
```

Reason:

```text
PASS58 does not run query_vocab_reader.py.
This card is created from the committed vocab.branch MVP source identity policy chain.
Exact DB occurrence counts and raw_url anchors should be added after a later read-only DB query.
```

## 4. README baseline presence

source identity is part of the vocab.branch source boundary rule.

Known committed surfaces include:

```text
vocab.branch source policy
README vocab source list
SQLite MVP schema policy
AI DB reader query policy
AI DB reader output rule
AI DB reader guard prompt
Raw URL term-card candidate
term-card candidate policy
vocab.branch MVP milestone report
```

## 5. source identity rows

The source identity row shape is:

```text
repo | branch | commit | path | line_no | raw_url | context
```

For README baseline sources, source identity currently anchors:

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

## 6. compact source context

### AI DB reader source identity rule

```text
Every source/context result must preserve:
repo | branch | commit | path | line_no | raw_url | context
```

Candidate reading:

```text
source identity is the minimum coordinate required before a DB-derived row can be used as evidence.
```

### Raw URL relation

```text
Raw URL fixes source identity.
```

Candidate reading:

```text
Raw URL is not the whole identity, but it is the source coordinate anchor inside source identity.
```

### DB guard

```text
The DB is not original source.
Original source remains in md files and Raw URLs.
```

Candidate reading:

```text
source identity prevents the DB from becoming a false source body.
```

## 7. structural role candidate

```text
source_identity_operator_candidate
source_boundary_candidate
evidence_coordinate_candidate
DB_to_source_guard
Raw_URL_container
README_baseline_anchor
anti_hallucination_guard
```

## 8. relation candidates

```text
source identity ↔ Raw URL
source identity ↔ repo
source identity ↔ branch
source identity ↔ commit
source identity ↔ path
source identity ↔ line_no
source identity ↔ context
source identity ↔ source_status
source identity ↔ DB row
source identity ↔ README baseline
source identity ↔ guard
source identity ↔ word
```

## 9. branch support candidates

### branch.market

Candidate only:

```text
source identity may later anchor every branch.market claim before Price is mapped as C.
```

Possible later use:

```text
anchor MT5 hints
anchor Price-as-C rule
anchor m/t/p/? mapping
prevent unsourced trading interpretation
```

### branch.sohosa

Candidate only:

```text
source identity may later anchor every sohosa/hyangsa lineage, ritual, place, and evidence claim before interpretation.
```

Possible later use:

```text
anchor sohosa/hyangsa source files
anchor ritual-place claims
anchor lineage evidence
prevent historical overclaim
```

### branch.history

Candidate only:

```text
source identity may later anchor every historical, etymological, and origin claim before meaning transformation is interpreted.
```

Possible later use:

```text
anchor origin claims
anchor etymology claims
anchor source transmission
anchor time-layer evidence
prevent unsourced narrative
```

## 10. what this card does not claim

This card does not claim:

- final definition of source identity
- that source identity alone proves truth
- that Raw URL alone is enough
- that DB rows are original source
- that every source identity row is complete
- that all repo sources have been scanned
- final branch.market source mapping
- final branch.sohosa source mapping
- final branch.history source mapping

## 11. next action

Possible next actions:

```text
1. run read-only DB query for source/source_file rows
2. add exact source identity rows with Raw URL anchors
3. create README baseline term-card candidate
4. create Seed.Base term-card candidate
5. create Y_Branch term-card candidate
6. link source identity card to Raw URL card
7. use source identity card as guard layer for branch.market / branch.sohosa / branch.history
```

## 12. guard

This card is a candidate.

This card is not a final definition.

source identity fixes source boundary before interpretation.

DB output is derived evidence.

Original source remains in md files and Raw URLs.

gpt.direct performs final structure alignment.
