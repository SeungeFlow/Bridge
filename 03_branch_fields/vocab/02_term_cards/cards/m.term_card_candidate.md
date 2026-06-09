# Term card candidate — m

## status

term: m
card_status: CANDIDATE
final_definition: false
source_scope: selected README baseline + PASS33 AI DB reader smoke test
created_from: vocab.branch MVP / core-token recovery
created_in_pass: 44
base_commit_repo_9dot0: 0ec5478b665e11b6455bd9d64040919ac12b3462

## 1. surface

```text
m
```

## 2. candidate role

m is a core token candidate inside the Ctp tuple surface.

In the current source-linked view, m appears as one element of:

```text
C = (m,t,p,?)
```

This card does not finalize m.

This card records m as a controlled candidate for the component / material / forming-factor position that participates in forming C.

## 3. DB status

```text
status: core_token_candidate
score: 15
occurrence_count: 14
source_count: 3
```

## 4. README baseline presence

m appears in the selected README baseline sources through the AI DB reader smoke test as part of C=(m,t,p,?) surfaces.

Known source surfaces include:

```text
Repo.SeungeFlow / Y_Branch / README.md
Repo.SeungeFlow / main / README.md
```

## 5. source identity rows

Current representative tuple rows from PASS33 / C-card basis:

```text
repo | branch | commit | path | line_no | context
SeungeFlow/SeungeFlow | Y_Branch | source-commit-in-DB | README.md | 100 | C = (m,t,p,?)
SeungeFlow/SeungeFlow | main | source-commit-in-DB | README.md | 267 | C = (m, t, p, ?)
```

## 6. compact source context

### Y_Branch README

```text
C = (m,t,p,?)
```

Candidate reading:

```text
m appears as a component position inside the tuple that forms or describes C.
```

### main README

```text
C = (m, t, p, ?)
```

Candidate reading:

```text
m appears as the first internal member of the visible Ctp tuple expression.
```

## 7. structural role candidate

```text
core_token_candidate
component_candidate
forming_factor_candidate
Ctp_tuple_member
```

## 8. relation candidates

```text
m ↔ C
m ↔ t
m ↔ p
m ↔ ?
m ↔ Ctp
m ↔ C=(m,t,p,?)
```

## 9. branch support candidates

### branch.market

Candidate only:

```text
m may later receive the components, forces, objects, or conditions that form Price as C.
```

Guard:

```text
Price should not be treated as m.
Price should be treated as C.
m should point to what forms Price.
```

Possible later m-elements for branch.market:

```text
bid/ask
order flow
liquidity
spread
volume
volatility
participants
capital mass
margin
risk
demand/supply
execution conditions
```

### branch.sohosa

Candidate only:

```text
m may later receive the source materials, lineage fragments, ritual components, place records, and evidence units that form a ritual-lineage source body as C.
```

### branch.history

Candidate only:

```text
m may later receive origin fragments, source traces, etymological elements, and historical evidence pieces that form historical meaning as C.
```

## 10. what this card does not claim

This card does not claim:

- final definition of m
- final relation of m to C
- final meaning of material/component
- final market interpretation
- final sohosa interpretation
- final history interpretation
- whole-repo source coverage

## 11. next action

Possible next actions:

```text
1. run read-only DB query for m with full raw_url output
2. add exact raw_url anchors to this card
3. create t term-card candidate
4. create p term-card candidate
5. create ? term-card candidate
6. compare m-position across branch.market / branch.sohosa / branch.history
```

## 12. guard

This card is a candidate.

This card is not a final definition.

DB output is derived evidence.

Original source remains in md files and Raw URLs.

gpt.direct performs final structure alignment.
