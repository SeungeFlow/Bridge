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


## source anchors — PASS72 enrichment

## status

anchor_status: CANDIDATE_ENRICHED
anchor_source: PASS72 runtime anchor enrichment report
anchor_update_pass: 81
final_definition: false

## exact match basis

```text
PASS75 review status: m = exact matched
PASS72 section status: anchor_status: MATCHED
```

## anchor rows

```text
term | status | repo | branch | commit | path | line_no | raw_url | context
m | core_token_candidate | SeungeFlow/9Dot0 | main | 7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb | README.md | 15 | https://raw.githubusercontent.com/SeungeFlow/9Dot0/7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb/README.md | - m: existent / object / relation-bearing unit
m | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 100 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | C = (m,t,p,?)
m | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 104 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | m = 숫자로 표시 가능한 모든 관측대상 + 데이터값을 가진 모든 상태
m | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 116 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | 무엇을 m으로 볼 것인가?
m | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 205 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | S₃(M, m | U, A, P_m)
m | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 208 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | FieldBoundaryᵢ(M, m, P_m),
m | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 209 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | Coord_A(m - ㆍ),
m | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 210 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | EscapeCondition(m, FieldBoundaryᵢ, P_m)
m | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 223 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | S₄(m1, m2, m | U)
m | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 226 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | COG = center(m1, m2, m),
m | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 231 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | next = repeat_9dot0(m2, m),
m | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 397 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | 구조해석 = 관측기준 ?를 세우고, m, t, p 각각에 의미를 부여하여 특정 구조를 읽을 수 있는 상태로 만드는 작업
```

## anchor guard

These anchors are DB-derived evidence.

These anchors do not finalize m.

Original source remains in md files and Raw URLs.

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
