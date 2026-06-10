# Term card candidate — p

## status

term: p
card_status: CANDIDATE
final_definition: false
source_scope: selected README baseline + PASS33 AI DB reader smoke test
created_from: vocab.branch MVP / core-token recovery
created_in_pass: 48
base_commit_repo_9dot0: 0520090db64cad493ecd959bc3dfe177595ceed3

## 1. surface

```text
p
```

## 2. candidate role

p is a core token candidate inside the Ctp tuple surface.

In the current source-linked view, p appears as one element of:

```text
C = (m,t,p,?)
```

p also appears in:

```text
C = t × p
```

This card does not finalize p.

This card records p as a controlled candidate for the projection / place / field / observer-position that participates in forming or expressing C.

## 3. DB status

```text
status: core_token_candidate
score: 15
occurrence_count: 12
source_count: 4
```

## 4. README baseline presence

p appears in the selected README baseline sources through the AI DB reader smoke test as part of C=(m,t,p,?) and C=t×p surfaces.

Known source surfaces include:

```text
Repo.SeungeFlow / Y_Branch / README.md
Repo.SeungeFlow / first_flow / README.md
Repo.SeungeFlow / main / README.md
```

## 5. source identity rows

Current representative tuple rows from PASS33 / C-card basis:

```text
repo | branch | commit | path | line_no | context
SeungeFlow/SeungeFlow | Y_Branch | source-commit-in-DB | README.md | 100 | C = (m,t,p,?)
SeungeFlow/SeungeFlow | first_flow | source-commit-in-DB | README.md | 345 | C = t × p
SeungeFlow/SeungeFlow | main | source-commit-in-DB | README.md | 267 | C = (m, t, p, ?)
```

## 6. compact source context

### Y_Branch README

```text
C = (m,t,p,?)
```

Candidate reading:

```text
p appears as a projection/place/field position inside the tuple that forms or describes C.
```

### first_flow README

```text
C = t × p
```

Candidate reading:

```text
p appears as an operating field or place factor that relates with t to form or express C.
```

### main README

```text
C = (m, t, p, ?)
```

Candidate reading:

```text
p appears as the third internal member of the visible Ctp tuple expression.
```

## 7. structural role candidate

```text
core_token_candidate
projection_candidate
place_candidate
field_candidate
observer_position_candidate
Ctp_tuple_member
```

## 8. relation candidates

```text
p ↔ C
p ↔ m
p ↔ t
p ↔ ?
p ↔ Ctp
p ↔ C=(m,t,p,?)
p ↔ C=t×p
```

## 9. branch support candidates

### branch.market

Candidate only:

```text
p may later receive MT5 runtime, market field, order-execution field, backtesting field, and observer/execution place.
```

Guard:

```text
Price should be treated as C, not p.
p should point to the runtime/place/field where Price as C is observed or executed.
```

Possible later p-elements for branch.market:

```text
MT5 runtime
market field
order execution field
backtesting environment
broker/server context
chart/observer surface
capital deployment place
```

### branch.sohosa

Candidate only:

```text
p may later receive ritual-place, source-place, evidence field, observer-place, and return-preservation field.
```

Possible later p-elements for branch.sohosa:

```text
ritual-place
향사 place
source archive place
lineage evidence field
lost-place → ritual-place correction field
observer relation place
```

### branch.history

Candidate only:

```text
p may later receive historical field, source-place, origin-place, archive-place, and interpretation field.
```

Possible later p-elements for branch.history:

```text
source field
archive field
historical place
origin context
interpretation surface
evidence field
```

## 10. what this card does not claim

This card does not claim:

- final definition of p
- final relation of p to C
- final meaning of projection/place/field
- final market interpretation
- final sohosa interpretation
- final history interpretation
- whole-repo source coverage


## source anchors — PASS72 enrichment

## status

anchor_status: CANDIDATE_ENRICHED
anchor_source: PASS72 runtime anchor enrichment report
anchor_update_pass: 85
final_definition: false

## exact match basis

```text
PASS75 review status: p = exact matched
PASS72 section status: anchor_status: MATCHED
```

## anchor rows

```text
term | status | repo | branch | commit | path | line_no | raw_url | context
p | core_token_candidate | SeungeFlow/9Dot0 | main | 7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb | README.md | 17 | https://raw.githubusercontent.com/SeungeFlow/9Dot0/7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb/README.md | - p: place / position / field
p | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 100 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | C = (m,t,p,?)
p | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 108 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | p = 놓인 자리 + 현시점 position + field coordinate
p | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 247 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | dot = 현시점 + 정중심평형기준점 + p(t|?)로 고정되는 자리
p | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 397 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | 구조해석 = 관측기준 ?를 세우고, m, t, p 각각에 의미를 부여하여 특정 구조를 읽을 수 있는 상태로 만드는 작업
p | core_token_candidate | SeungeFlow/SeungeFlow | first_flow | 1fa5f28ca7647da445a5b2ef130f3852845ccb68 | README.md | 345 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/1fa5f28ca7647da445a5b2ef130f3852845ccb68/README.md | C = t × p
p | core_token_candidate | SeungeFlow/SeungeFlow | first_flow | 1fa5f28ca7647da445a5b2ef130f3852845ccb68 | README.md | 349 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/1fa5f28ca7647da445a5b2ef130f3852845ccb68/README.md | p : 위치
p | core_token_candidate | SeungeFlow/SeungeFlow | first_flow | 1fa5f28ca7647da445a5b2ef130f3852845ccb68 | README.md | 355 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/1fa5f28ca7647da445a5b2ef130f3852845ccb68/README.md | Δ → t → p → C → Δ
p | core_token_candidate | SeungeFlow/SeungeFlow | main | 85802d707160da1a1cfb2bfacfe9cea222a3c77c | README.md | 222 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/85802d707160da1a1cfb2bfacfe9cea222a3c77c/README.md | C = t p
p | core_token_candidate | SeungeFlow/SeungeFlow | main | 85802d707160da1a1cfb2bfacfe9cea222a3c77c | README.md | 242 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/85802d707160da1a1cfb2bfacfe9cea222a3c77c/README.md | 여기서 `p`는 단순 위치가 아니다.
p | core_token_candidate | SeungeFlow/SeungeFlow | main | 85802d707160da1a1cfb2bfacfe9cea222a3c77c | README.md | 245 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/85802d707160da1a1cfb2bfacfe9cea222a3c77c/README.md | p =
p | core_token_candidate | SeungeFlow/SeungeFlow | main | 85802d707160da1a1cfb2bfacfe9cea222a3c77c | README.md | 267 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/85802d707160da1a1cfb2bfacfe9cea222a3c77c/README.md | C = (m, t, p, ?)
```

## anchor guard

These anchors are DB-derived evidence.

These anchors do not finalize p.

Original source remains in md files and Raw URLs.

## 11. next action

Possible next actions:

```text
1. run read-only DB query for p with full raw_url output
2. add exact raw_url anchors to this card
3. create ? term-card candidate
4. create Ctp term-card candidate
5. compare p-position across branch.market / branch.sohosa / branch.history
```

## 12. guard

This card is a candidate.

This card is not a final definition.

DB output is derived evidence.

Original source remains in md files and Raw URLs.

gpt.direct performs final structure alignment.
