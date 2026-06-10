# Term card candidate — t

## status

term: t
card_status: CANDIDATE
final_definition: false
source_scope: selected README baseline + PASS33 AI DB reader smoke test
created_from: vocab.branch MVP / core-token recovery
created_in_pass: 46
base_commit_repo_9dot0: 5a3a6bd57786ccc81ab122d3143a0ea7a1a36a18

## 1. surface

```text
t
```

## 2. candidate role

t is a core token candidate inside the Ctp tuple surface.

In the current source-linked view, t appears as one element of:

```text
C = (m,t,p,?)
```

t also appears in:

```text
C = t × p
```

This card does not finalize t.

This card records t as a controlled candidate for the transition / time-flow / operation-flow position that participates in forming or expressing C.

## 3. DB status

```text
status: core_token_candidate
score: 15
occurrence_count: 12
source_count: 4
```

## 4. README baseline presence

t appears in the selected README baseline sources through the AI DB reader smoke test as part of C=(m,t,p,?) and C=t×p surfaces.

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
t appears as a transition/time-flow position inside the tuple that forms or describes C.
```

### first_flow README

```text
C = t × p
```

Candidate reading:

```text
t appears as an operating factor that relates with p to form or express C.
```

### main README

```text
C = (m, t, p, ?)
```

Candidate reading:

```text
t appears as the second internal member of the visible Ctp tuple expression.
```

## 7. structural role candidate

```text
core_token_candidate
transition_candidate
time_flow_candidate
operation_flow_candidate
Ctp_tuple_member
```

## 8. relation candidates

```text
t ↔ C
t ↔ m
t ↔ p
t ↔ ?
t ↔ Ctp
t ↔ C=(m,t,p,?)
t ↔ C=t×p
```

## 9. branch support candidates

### branch.market

Candidate only:

```text
t may later receive tick, candle, execution sequence, transition, and market time-flow conditions.
```

Possible later t-elements for branch.market:

```text
tick transition
candle transition
Close_n → Open_n+1
execution sequence
order timing
session flow
volatility phase shift
backtest time axis
```

### branch.sohosa

Candidate only:

```text
t may later receive historical transition, ritual succession, return sequence, and source-body preservation flow.
```

Possible later t-elements for branch.sohosa:

```text
lineage succession
ritual repetition
return sequence
lost-place → ritual-place correction
source preservation over time
```

### branch.history

Candidate only:

```text
t may later receive transformation over time, origin-to-meaning transition, and historical phase movement.
```

Possible later t-elements for branch.history:

```text
origin sequence
etymological transformation
time-layer shift
source transmission
meaning change
```

## 10. what this card does not claim

This card does not claim:

- final definition of t
- final relation of t to C
- final meaning of transition or time-flow
- final market interpretation
- final sohosa interpretation
- final history interpretation
- whole-repo source coverage


## source anchors — PASS72 enrichment

## status

anchor_status: CANDIDATE_ENRICHED
anchor_source: PASS72 runtime anchor enrichment report
anchor_update_pass: 83
final_definition: false

## exact match basis

```text
PASS75 review status: t = exact matched
PASS72 section status: anchor_status: MATCHED
```

## anchor rows

```text
term | status | repo | branch | commit | path | line_no | raw_url | context
t | core_token_candidate | SeungeFlow/9Dot0 | main | 7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb | README.md | 16 | https://raw.githubusercontent.com/SeungeFlow/9Dot0/7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb/README.md | - t: transition / difference / direction change / distance gap
t | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 100 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | C = (m,t,p,?)
t | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 106 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | t = 전이상태 + delta + rate + phase + recurrence
t | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 247 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | dot = 현시점 + 정중심평형기준점 + p(t|?)로 고정되는 자리
t | core_token_candidate | SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | 397 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/32f8b248dc7e9ec5c1856b78b4ee207b8861d315/README.md | 구조해석 = 관측기준 ?를 세우고, m, t, p 각각에 의미를 부여하여 특정 구조를 읽을 수 있는 상태로 만드는 작업
t | core_token_candidate | SeungeFlow/SeungeFlow | first_flow | 1fa5f28ca7647da445a5b2ef130f3852845ccb68 | README.md | 345 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/1fa5f28ca7647da445a5b2ef130f3852845ccb68/README.md | C = t × p
t | core_token_candidate | SeungeFlow/SeungeFlow | first_flow | 1fa5f28ca7647da445a5b2ef130f3852845ccb68 | README.md | 348 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/1fa5f28ca7647da445a5b2ef130f3852845ccb68/README.md | t : 전이
t | core_token_candidate | SeungeFlow/SeungeFlow | first_flow | 1fa5f28ca7647da445a5b2ef130f3852845ccb68 | README.md | 355 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/1fa5f28ca7647da445a5b2ef130f3852845ccb68/README.md | Δ → t → p → C → Δ
t | core_token_candidate | SeungeFlow/SeungeFlow | main | 85802d707160da1a1cfb2bfacfe9cea222a3c77c | README.md | 222 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/85802d707160da1a1cfb2bfacfe9cea222a3c77c/README.md | C = t p
t | core_token_candidate | SeungeFlow/SeungeFlow | main | 85802d707160da1a1cfb2bfacfe9cea222a3c77c | README.md | 225 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/85802d707160da1a1cfb2bfacfe9cea222a3c77c/README.md | 여기서 `t`는 단순 시간이 아니다.
t | core_token_candidate | SeungeFlow/SeungeFlow | main | 85802d707160da1a1cfb2bfacfe9cea222a3c77c | README.md | 228 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/85802d707160da1a1cfb2bfacfe9cea222a3c77c/README.md | t =
t | core_token_candidate | SeungeFlow/SeungeFlow | main | 85802d707160da1a1cfb2bfacfe9cea222a3c77c | README.md | 267 | https://raw.githubusercontent.com/SeungeFlow/SeungeFlow/85802d707160da1a1cfb2bfacfe9cea222a3c77c/README.md | C = (m, t, p, ?)
```

## anchor guard

These anchors are DB-derived evidence.

These anchors do not finalize t.

Original source remains in md files and Raw URLs.

## 11. next action

Possible next actions:

```text
1. run read-only DB query for t with full raw_url output
2. add exact raw_url anchors to this card
3. create p term-card candidate
4. create ? term-card candidate
5. compare t-position across branch.market / branch.sohosa / branch.history
```

## 12. guard

This card is a candidate.

This card is not a final definition.

DB output is derived evidence.

Original source remains in md files and Raw URLs.

gpt.direct performs final structure alignment.
