# Term card candidate — README baseline

## status

term: README baseline
filename_slug: README_baseline
card_status: CANDIDATE
final_definition: false
source_scope: vocab.branch MVP / README vocab source list / readme_source table / AI DB reader smoke test
created_from: vocab.branch MVP / README vocabulary law
created_in_pass: 60
base_commit_repo_9dot0: ee12b8cbc259a218500941e6e3217755ce2eecfb

## 1. surface

```text
README baseline
```

## 2. candidate role

README baseline is a vocabulary-law / source-scope gate candidate.

In vocab.branch, README baseline controls the first vocabulary surface before deeper source expansion.

Candidate reading:

```text
README.md is the first vocabulary law.
```

If a needed structural term is missing from the relevant README.md, the relevant README.md should be updated first.

This card does not finalize README baseline.

This card records README baseline as a controlled candidate for the first source-scope layer that decides which terms enter the vocab.branch DB and term-card workflow.

## 3. DB status

```text
status: README_baseline_operator_candidate
score: not_assigned_in_pass60
occurrence_count: not_queried_in_pass60
source_count: 8 readme_source rows already registered
```

Reason:

```text
PASS60 does not run query_vocab_reader.py.
This card is created from the committed vocab.branch MVP README baseline policy chain and readme_source population result.
Exact DB occurrence counts and raw_url anchors should be added after a later read-only DB query.
```

## 4. README baseline presence

README baseline is present through the committed vocab.branch MVP workflow:

```text
README vocab source list
README vocab scan protocol
readme_source table
AI DB reader smoke test
vocab.branch MVP milestone report
term-card candidate policy
```

Current readme_source baseline rows:

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

## 5. source identity rows

README baseline must preserve full source identity shape:

```text
repo | branch | commit | path | line_no | raw_url | context
```

The baseline itself is not just a list of files.

It is a controlled entry surface for terms.

Current baseline classes:

```text
repo_9dot0_branch_field
repo_seungeflow_primary_observer
```

## 6. compact source context

### Vocabulary law

```text
README.md remains the first vocabulary law.
```

Candidate reading:

```text
README baseline prevents uncontrolled term expansion.
```

### Missing term rule

```text
If a needed structural term is missing from the relevant README.md, update the README.md first.
```

Candidate reading:

```text
README baseline controls whether a term can enter the structured vocab layer.
```

### DB source scope

```text
The first DB build uses selected README sources only.
```

Candidate reading:

```text
README baseline is the first source-scope boundary before whole-repo expansion.
```

## 7. structural role candidate

```text
README_baseline_operator_candidate
vocabulary_law_candidate
source_scope_gate_candidate
term_entry_surface
DB_input_boundary
anti_uncontrolled_term_expansion_guard
```

## 8. relation candidates

```text
README baseline ↔ source identity
README baseline ↔ Raw URL
README baseline ↔ word
README baseline ↔ vocab scope
README baseline ↔ readme_source
README baseline ↔ source_file
README baseline ↔ DB build
README baseline ↔ term-card candidate
README baseline ↔ guard
README baseline ↔ branch-field
```

## 9. branch support candidates

### branch.market

Candidate only:

```text
README baseline may later decide which market terms enter branch.market vocab before Price is mapped as C.
```

Possible later use:

```text
confirm Price / MT5 / order flow / liquidity terms exist in branch.market README
update branch.market README before expanding market term cards
prevent uncontrolled market vocabulary expansion
```

### branch.sohosa

Candidate only:

```text
README baseline may later decide which sohosa/hyangsa terms enter branch.sohosa vocab before ritual-lineage interpretation.
```

Possible later use:

```text
confirm 소호사 / 향사 / 제례 / 계보 / 장소 terms exist in branch.sohosa README
update branch.sohosa README before expanding sohosa term cards
prevent unsupported historical vocabulary expansion
```

### branch.history

Candidate only:

```text
README baseline may later decide which history/origin/etymology terms enter branch.history vocab before meaning transformation is interpreted.
```

Possible later use:

```text
confirm origin / etymology / transformation / historical field terms exist in branch.history README
update branch.history README before expanding history term cards
prevent unsourced historical narrative expansion
```

## 10. what this card does not claim

This card does not claim:

- final definition of README baseline
- that current README baseline is complete
- that all needed terms already exist
- that whole-repo source coverage has been achieved
- that DB rows replace README source
- that frequency equals vocabulary priority
- final branch.market vocab scope
- final branch.sohosa vocab scope
- final branch.history vocab scope

## 11. next action

Possible next actions:

```text
1. run read-only DB query for README baseline / readme_sources
2. add exact Raw URL anchors to this card
3. create Seed.Base term-card candidate
4. create Y_Branch term-card candidate
5. create term-card index report for C / m / t / p / ? / Ctp / Ctp24 / Raw URL / source identity / README baseline
6. use README baseline card as guard before branch.market vocabulary expansion
7. use README baseline card as guard before branch.sohosa vocabulary expansion
8. use README baseline card as guard before branch.history vocabulary expansion
```

## 12. guard

This card is a candidate.

This card is not a final definition.

README baseline is the first vocab-scope gate, not the whole source body.

DB output is derived evidence.

Original source remains in md files and Raw URLs.

gpt.direct performs final structure alignment.
