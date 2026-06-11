# Term card candidate — Raw URL

## status

term: Raw URL
filename_slug: Raw_URL
card_status: CANDIDATE
final_definition: false
source_scope: vocab.branch MVP policy / source identity layer / README baseline rule
created_from: vocab.branch MVP / source identity connector rule
created_in_pass: 56
base_commit_repo_9dot0: 3945a690b3564254713e0eff96c3f1ce6bd5c331

## 1. surface

```text
Raw URL
```

## 2. candidate role

Raw URL is a source-identity connector candidate.

In vocab.branch, Raw URL does not connect meaning by itself.

Raw URL fixes source location and source identity.

The paired minimal connector rule is:

```text
word + Raw URL
```

Candidate reading:

```text
word connects meaning
Raw URL fixes source identity
```

This card does not finalize Raw URL.

This card records Raw URL as a controlled candidate for the source coordinate operator that prevents DB rows, summaries, or AI interpretations from replacing original md source.

## 3. DB status

```text
status: source_identity_operator_candidate
score: not_assigned_in_pass56
occurrence_count: not_queried_in_pass56
source_count: not_queried_in_pass56
```

Reason:

```text
PASS56 does not run query_vocab_reader.py.
This card is created from the committed vocab.branch MVP source identity policy chain.
Exact DB occurrence counts and raw_url anchors should be added after a later read-only DB query.
```

## 4. README baseline presence

Raw URL is part of the vocab.branch source identity rule.

Known committed surfaces include:

```text
vocab.branch source policy
README vocab source list
SQLite MVP schema policy
AI DB reader output rule
AI DB reader guard prompt
term-card candidate policy
vocab.branch MVP milestone report
```

## 5. source identity rows

Raw URL belongs to the source identity row shape:

```text
repo | branch | commit | path | line_no | raw_url | context
```

Raw URL must not be separated from:

```text
repo
branch
commit
path
source status
line number / anchor
```

## 6. compact source context

### Minimal connector rule

```text
Repo, Branch, Directory, and md files are connected by:
1. word
2. Raw URL
```

Candidate reading:

```text
Raw URL is the source-location connector paired with word as the meaning trigger.
```

### DB source guard

```text
The DB is not original source.
Original source remains in md files and Raw URLs.
```

Candidate reading:

```text
Raw URL keeps the DB from becoming a false source body.
```

### Reader output rule

```text
repo | branch | commit | path | line_no | raw_url | context
```

Candidate reading:

```text
Raw URL is one field in the full source identity coordinate.
```

## 7. structural role candidate

```text
source_identity_operator_candidate
source_coordinate_candidate
raw_source_anchor_candidate
DB_to_source_bridge
anti_hallucination_guard
term_card_source_anchor
```

## 8. relation candidates

```text
Raw URL ↔ source identity
Raw URL ↔ repo
Raw URL ↔ branch
Raw URL ↔ commit
Raw URL ↔ path
Raw URL ↔ line_no
Raw URL ↔ md source
Raw URL ↔ DB row
Raw URL ↔ README baseline
Raw URL ↔ guard
Raw URL ↔ word
```

## 9. branch support candidates

### branch.market

Candidate only:

```text
Raw URL may later anchor market terms back to exact source rows before mapping Price as C.
```

Possible later use:

```text
prevent Price-as-C from becoming unsupported interpretation
anchor MT5/runtime hints to source identity
anchor branch.market README terms to exact source rows
```

### branch.sohosa

Candidate only:

```text
Raw URL may later anchor sohosa/hyangsa source claims to exact source rows before ritual-lineage interpretation.
```

Possible later use:

```text
prevent lineage / ritual / place claims from floating without source
anchor sohosa/hyangsa thinking_flow materials
anchor evidence relation before interpretation
```

### branch.history

Candidate only:

```text
Raw URL may later anchor historical and etymological claims to exact source rows before meaning transformation is interpreted.
```

Possible later use:

```text
anchor origin claims
anchor time-layer claims
anchor source transmission
prevent history branch from becoming unsourced narrative
```

## 10. what this card does not claim

This card does not claim:

- final definition of Raw URL
- that Raw URL alone proves source truth
- that DB rows are original source
- that frequency equals source priority
- that all source identity rows are complete
- whole-repo source coverage
- final branch.market source mapping
- final branch.sohosa source mapping
- final branch.history source mapping


## source anchors — PASS72 enrichment

## status

anchor_status: VARIANT_REVIEWED_CANDIDATE_ENRICHED
anchor_source: PASS109 variant-aware anchor review report
anchor_update_pass: 111
final_definition: false

## variant-aware match basis

PASS75 review status: Raw URL = variant matched
PASS109 review basis: accept_candidate rows only
variant status allowed here: VALID_COMPONENT

## reviewed anchor rows

| card | query_term | row_term | row_status | variant_status | accept_for_card_update | repo | branch | commit | path | line_no | raw_url | reason |
|---|---|---|---|---|---|---|---|---|---|---:|---|---|
| Raw URL | Raw | Raw | structural_trigger_candidate | VALID_COMPONENT | accept_candidate | SeungeFlow/9Dot0 | main | 7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb | 03_branch_fields/vocab/README.md | 22 | https://raw.githubusercontent.com/SeungeFlow/9Dot0/7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb/03_branch_fields/vocab/README.md | Raw/URL component row supports Raw URL anchor surface; keep as component evidence, not exact phrase. |
| Raw URL | Raw | Raw | structural_trigger_candidate | VALID_COMPONENT | accept_candidate | SeungeFlow/9Dot0 | main | 7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb | 03_branch_fields/vocab/README.md | 33 | https://raw.githubusercontent.com/SeungeFlow/9Dot0/7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb/03_branch_fields/vocab/README.md | Raw/URL component row supports Raw URL anchor surface; keep as component evidence, not exact phrase. |
| Raw URL | Raw | Raw | structural_trigger_candidate | VALID_COMPONENT | accept_candidate | SeungeFlow/9Dot0 | main | 7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb | 03_branch_fields/vocab/README.md | 36 | https://raw.githubusercontent.com/SeungeFlow/9Dot0/7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb/03_branch_fields/vocab/README.md | Raw/URL component row supports Raw URL anchor surface; keep as component evidence, not exact phrase. |
| Raw URL | Raw | Raw | structural_trigger_candidate | VALID_COMPONENT | accept_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 84 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | Raw/URL component row supports Raw URL anchor surface; keep as component evidence, not exact phrase. |
| Raw URL | URL | URL | structural_trigger_candidate | VALID_COMPONENT | accept_candidate | SeungeFlow/9Dot0 | main | 7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb | 03_branch_fields/vocab/README.md | 22 | https://raw.githubusercontent.com/SeungeFlow/9Dot0/7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb/03_branch_fields/vocab/README.md | Raw/URL component row supports Raw URL anchor surface; keep as component evidence, not exact phrase. |
| Raw URL | URL | URL | structural_trigger_candidate | VALID_COMPONENT | accept_candidate | SeungeFlow/9Dot0 | main | 7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb | 03_branch_fields/vocab/README.md | 33 | https://raw.githubusercontent.com/SeungeFlow/9Dot0/7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb/03_branch_fields/vocab/README.md | Raw/URL component row supports Raw URL anchor surface; keep as component evidence, not exact phrase. |
| Raw URL | URL | URL | structural_trigger_candidate | VALID_COMPONENT | accept_candidate | SeungeFlow/9Dot0 | main | 7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb | 03_branch_fields/vocab/README.md | 36 | https://raw.githubusercontent.com/SeungeFlow/9Dot0/7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb/03_branch_fields/vocab/README.md | Raw/URL component row supports Raw URL anchor surface; keep as component evidence, not exact phrase. |
| Raw URL | URL | URL | structural_trigger_candidate | VALID_COMPONENT | accept_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 84 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | Raw/URL component row supports Raw URL anchor surface; keep as component evidence, not exact phrase. |

## anchor guard

These anchors are DB-derived and review-filtered evidence.

These anchors do not finalize Raw URL.

Raw/URL component evidence does not equal final definition of Raw URL.

Original source remains in md files and Raw URLs.

## 11. next action

Possible next actions:

```text
1. run read-only DB query for Raw URL / raw_url-related rows
2. add exact source policy contexts with Raw URL anchors
3. create source identity term-card candidate
4. create README baseline term-card candidate
5. create Seed.Base term-card candidate
6. link Raw URL card to AI DB reader guard prompt
7. use Raw URL card as guard layer for branch.market / branch.sohosa / branch.history
```

## 12. guard

This card is a candidate.

This card is not a final definition.

Raw URL fixes source coordinate, but it does not replace source reading.

DB output is derived evidence.

Original source remains in md files and Raw URLs.

gpt.direct performs final structure alignment.
