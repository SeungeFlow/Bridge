# Term card candidate — Ctp

## status

term: Ctp
card_status: CANDIDATE
final_definition: false
source_scope: selected README baseline + PASS33 AI DB reader smoke test
created_from: vocab.branch MVP / core-token recovery
created_in_pass: 52
base_commit_repo_9dot0: 7329fefbe53334f3f90ad478f43cefcaf810a9e2

## 1. surface

```text
Ctp
```

## 2. candidate role

Ctp is a core token candidate for the structural operation surface that connects C with m, t, p, and ?.

In the current source-linked view, Ctp is treated as the candidate operation surface behind:

```text
C = (m,t,p,?)
C = (m, t, p, ?)
C = t × p
C=tp
Ctp24
```

This card does not finalize Ctp.

This card records Ctp as a controlled candidate for the structural operation formula surface that later supports branch.market, branch.sohosa, and branch.history.

## 3. DB status

```text
status: core_token_candidate
score: 15
occurrence_count: 4
source_count: 2
```

## 4. README baseline presence

Ctp appears in the selected README baseline through the AI DB reader smoke test as a core token candidate.

Known related surfaces include:

```text
Repo.SeungeFlow / Y_Branch / README.md
Repo.SeungeFlow / main / README.md
```

Related tokens confirmed in the MVP reader layer:

```text
C
m
t
p
?
C=(m,t,p,?)
C=tp
Ctp24
```

## 5. source identity rows

Current representative rows are not yet fully expanded for Ctp in this card.

Known source-linked basis from PASS33:

```text
term | status | score | occurrence_count | source_count
Ctp | core_token_candidate | 15 | 4 | 2
```

Related representative rows already recorded in the C / m / t / p / ? cards:

```text
repo | branch | commit | path | line_no | context
SeungeFlow/SeungeFlow | Y_Branch | source-commit-in-DB | README.md | 100 | C = (m,t,p,?)
SeungeFlow/SeungeFlow | first_flow | source-commit-in-DB | README.md | 345 | C = t × p
SeungeFlow/SeungeFlow | main | source-commit-in-DB | README.md | 267 | C = (m, t, p, ?)
```

Exact Raw URL / line anchors for Ctp should be added after a later read-only DB query.

## 6. compact source context

### Tuple surface

```text
C = (m,t,p,?)
```

Candidate reading:

```text
Ctp is the candidate operation surface in which C is read through m, t, p, and ?.
```

### Operation surface

```text
C = t × p
```

Candidate reading:

```text
Ctp may preserve the relation where C is formed or expressed through t and p relation.
```

### Matrix/filter surface

```text
Ctp24
```

Candidate reading:

```text
Ctp24 may be treated as a later matrix/filter expansion of the Ctp operation surface.
```

## 7. structural role candidate

```text
core_token_candidate
structure_operation_surface_candidate
Ctp_tuple_operator
C_m_t_p_question_connector
Ctp24_base_candidate
```

## 8. relation candidates

```text
Ctp ↔ C
Ctp ↔ m
Ctp ↔ t
Ctp ↔ p
Ctp ↔ ?
Ctp ↔ C=(m,t,p,?)
Ctp ↔ C=tp
Ctp ↔ Ctp24
Ctp ↔ structure operation
```

## 9. branch support candidates

### branch.market

Candidate only:

```text
Ctp may later support the operation that reads Price as C through m-elements, t-transition, p-runtime, and unresolved execution question.
```

Possible later mapping:

```text
C = Price
m = components/forces forming Price
t = tick/candle/execution transition
p = MT5/runtime/market field
? = executable/open question
```

### branch.sohosa

Candidate only:

```text
Ctp may later support the operation that reads ritual-lineage source body as C through source materials, historical transition, ritual/source place, and unresolved evidence question.
```

Possible later mapping:

```text
C = formed ritual-lineage source body
m = source materials / lineage fragments / ritual components
t = historical transition / ritual succession
p = ritual-place / source-place / evidence field
? = unresolved source/evidence question
```

### branch.history

Candidate only:

```text
Ctp may later support the operation that reads historical meaning as C through origin fragments, transformation over time, historical field, and unresolved source question.
```

Possible later mapping:

```text
C = formed historical meaning
m = origin/source fragments
t = transformation over time
p = historical field / source-place
? = unresolved origin/evidence question
```

## 10. what this card does not claim

This card does not claim:

- final definition of Ctp
- final formula proof
- final relation of Ctp to C / m / t / p / ?
- final Ctp24 interpretation
- final branch.market interpretation
- final branch.sohosa interpretation
- final branch.history interpretation
- whole-repo source coverage


## source anchors — PASS72 enrichment

## status

anchor_status: CANDIDATE_ENRICHED
anchor_source: PASS72 runtime anchor enrichment report
anchor_update_pass: 93
final_definition: false

## exact match basis

```text
PASS75 review status: Ctp = exact matched
PASS72 section status: anchor_status: MATCHED
```

## anchor rows

```text
term | status | repo | branch | commit | path | line_no | raw_url | context
Ctp | core_token_candidate | SeungeFlow/9Dot0 | main | 7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb | 03_branch_fields/vocab/README.md | 24 | https://raw.githubusercontent.com/SeungeFlow/9Dot0/7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb/03_branch_fields/vocab/README.md | - Ctp structure-operation reading
Ctp | core_token_candidate | SeungeFlow/SeungeFlow | main | 85802d707160da1a1cfb2bfacfe9cea222a3c77c | README.md | 217 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/85802d707160da1a1cfb2bfacfe9cea222a3c77c/README.md | ## 6. Ctp
Ctp | core_token_candidate | SeungeFlow/SeungeFlow | main | 85802d707160da1a1cfb2bfacfe9cea222a3c77c | README.md | 219 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/85802d707160da1a1cfb2bfacfe9cea222a3c77c/README.md | Ctp는 SeungeFlow의 중심 구조연산식 중 하나다.
Ctp | core_token_candidate | SeungeFlow/SeungeFlow | main | 85802d707160da1a1cfb2bfacfe9cea222a3c77c | README.md | 525 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/85802d707160da1a1cfb2bfacfe9cea222a3c77c/README.md | 관계, 존재, 장에서 시작하고, Ctp, Core, Path, 9dot0, 역발상, Seed.Base, Active.Schema, runtime output을 통해 작동한다.
```

## anchor guard

These anchors are DB-derived evidence.

These anchors do not finalize Ctp.

Original source remains in md files and Raw URLs.

## 11. next action

Possible next actions:

```text
1. run read-only DB query for Ctp with full raw_url output
2. add exact raw_url anchors to this card
3. create Ctp24 term-card candidate
4. compare Ctp with C=(m,t,p,?) and C=tp
5. prepare first branch.market Ctp alignment prompt
6. prepare first branch.sohosa Ctp alignment prompt
7. prepare first branch.history Ctp alignment prompt
```

## 12. guard

This card is a candidate.

This card is not a final definition.

Ctp is treated as a structure-operation surface candidate, not as a completed theory statement.

DB output is derived evidence.

Original source remains in md files and Raw URLs.

gpt.direct performs final structure alignment.
