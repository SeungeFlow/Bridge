# core-token term-card candidates — pass40

## status

pass: 40
role: first term-card candidate batch
final_term_cards: false
base_commit_repo_9dot0: 92f5c4e62fa41f0b69e6760df850935ededa3c5e

## source basis

This candidate batch is based on the vocab.branch MVP milestone and AI DB reader smoke test summary.

No new DB query is executed in pass40.

## first candidate list

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

## candidate table

| order | term            | first status                 | candidate role                    | reason                                                                    |
| ----: | --------------- | ---------------------------- | --------------------------------- | ------------------------------------------------------------------------- |
|     1 | C               | core_token_candidate         | formed structure/state candidate  | C is central to C=(m,t,p,?) and appears as a core token.                  |
|     2 | m               | core_token_candidate         | material/component candidate      | m belongs to the Ctp tuple and should not be lost as a short token.       |
|     3 | t               | core_token_candidate         | transition/time-flow candidate    | t belongs to the Ctp tuple and supports transition reading.               |
|     4 | p               | core_token_candidate         | projection/place/field candidate  | p belongs to the Ctp tuple and supports field/observer placement.         |
|     5 | ?               | core_token_candidate         | unresolved question/open variable | ? preserves the non-final/open boundary of C=(m,t,p,?).                   |
|     6 | Ctp             | core_token_candidate         | structure-operation formula token | Ctp is a compact formula surface for structure operation.                 |
|     7 | Ctp24           | core_token_candidate         | matrix filter token               | Ctp24 is the first structure filter surfaced through Y_Branch README.     |
|     8 | Y_Branch        | structural_trigger_candidate | source/guard/operator surface     | Y_Branch anchors source identity, guard, relation, and validator loop.    |
|     9 | Seed.Base       | structural_trigger_candidate | source-memory field candidate     | Seed.Base names the md-to-source-memory/DB direction.                     |
|    10 | Raw URL         | source_identity_operator     | source coordinate connector       | Raw URL fixes source identity and prevents DB rows from replacing source. |
|    11 | source identity | source_identity_operator     | source boundary operator          | source identity binds repo, branch, commit, path, Raw URL, status.        |
|    12 | README baseline | README_baseline_operator     | vocabulary law surface            | README baseline controls the first vocab scope.                           |

## first promotion order

Suggested individual card promotion order:

```text
C
m
t
p
?
Ctp
Ctp24
Raw URL
source identity
README baseline
Y_Branch
Seed.Base
```

## candidate relation map

```text
C ↔ m
C ↔ t
C ↔ p
C ↔ ?
Ctp ↔ C=(m,t,p,?)
Ctp24 ↔ Ctp
Y_Branch ↔ Ctp24
Raw URL ↔ source identity
README baseline ↔ vocab scope
Seed.Base ↔ source memory
```

## branch support map

### branch.market

Potential later terms:

```text
C = Price
m = components/forces forming Price
t = tick/candle/execution transition
p = MT5/runtime/market field
```

### branch.sohosa

Potential later terms:

```text
C = formed ritual-lineage source body
m = source materials / lineage / place / ritual components
t = historical transition / return sequence
p = ritual-place / observer-place / evidence field
```

### branch.history

Potential later terms:

```text
C = formed historical meaning
m = origin/source fragments
t = transformation over time
p = historical field / source-place
```

## not finalized

These candidate cards do not finalize:

- the definition of C
- the meaning of Ctp
- the full role of Ctp24
- the relation between branch.market / branch.sohosa / branch.history
- the whole vocab.branch scope

## next pass candidates

After this candidate batch is committed, possible next passes are:

1. create individual term-card files for C, m, t, p, ?
2. run read-only DB query per term and record source rows
3. create source-identity card for Raw URL
4. create README baseline card
5. connect first term cards to branch.market / branch.sohosa / branch.history

## guard

This document is a candidate index.

It is not final interpretation.

Original source remains in md files and Raw URLs.

DB output is derived evidence.
