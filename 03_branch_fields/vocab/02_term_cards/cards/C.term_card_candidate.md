# Term card candidate — C

## status

term: C
card_status: CANDIDATE
final_definition: false
source_scope: selected README baseline + PASS33 AI DB reader smoke test
created_from: vocab.branch MVP / core-token recovery
created_in_pass: 42
base_commit_repo_9dot0: f7f94a02d4dfe6c8021f62f2d548e6d546f15dc3

## 1. surface

```text
C
```

## 2. candidate role

C is the first core token candidate for the vocab.branch term-card layer.

In the current source-linked view, C appears as a compact structural surface connected to:

```text
C = (m,t,p,?)
C = t × p
C : 구조
C축
```

This card does not finalize C.

This card only records C as a controlled source-linked candidate.

## 3. DB status

```text
status: core_token_candidate
score: 15
occurrence_count: 20
source_count: 3
```

## 4. README baseline presence

C appears in the selected README baseline sources through the AI DB reader smoke test.

Known source surfaces include:

```text
Repo.SeungeFlow / Y_Branch / README.md
Repo.SeungeFlow / first_flow / README.md
Repo.SeungeFlow / main / README.md
```

## 5. source identity rows

Current representative rows from PASS33 smoke test:

```text
repo | branch | commit | path | line_no | context
SeungeFlow/SeungeFlow | Y_Branch | source-commit-in-DB | README.md | 100 | C = (m,t,p,?)
SeungeFlow/SeungeFlow | Y_Branch | source-commit-in-DB | README.md | 156 | C축:
SeungeFlow/SeungeFlow | first_flow | source-commit-in-DB | README.md | 345 | C = t × p
SeungeFlow/SeungeFlow | first_flow | source-commit-in-DB | README.md | 347 | C : 구조
SeungeFlow/SeungeFlow | main | source-commit-in-DB | README.md | 267 | C = (m, t, p, ?)
```

## 6. compact source context

### Y_Branch README

```text
C = (m,t,p,?)
C축:
```

Candidate reading:

```text
C appears as a structured state/form surface in relation with m, t, p, and ?.
```

### first_flow README

```text
C = t × p
C : 구조
```

Candidate reading:

```text
C appears as structure formed through t and p relation.
```

### main README

```text
C = (m, t, p, ?)
```

Candidate reading:

```text
C appears as a visible entry-level expression of the Ctp tuple.
```

## 7. structural role candidate

```text
core_token_candidate
formed_state_candidate
structure_surface_candidate
Ctp_tuple_anchor
```

## 8. relation candidates

```text
C ↔ m
C ↔ t
C ↔ p
C ↔ ?
C ↔ Ctp
C ↔ Ctp24
C ↔ structure
C ↔ formed state
```

## 9. branch support candidates

### branch.market

Candidate only:

```text
C may later receive Price as formed state.
```

Guard:

```text
Price should be treated as C, not m.
```

### branch.sohosa

Candidate only:

```text
C may later receive a formed ritual-lineage / source-body state.
```

### branch.history

Candidate only:

```text
C may later receive formed historical meaning after origin/source/time transformation.
```

## 10. what this card does not claim

This card does not claim:

- final definition of C
- final proof of Ctp
- final relation of C to m/t/p/?
- final branch.market interpretation
- final branch.sohosa interpretation
- final branch.history interpretation
- whole-repo source coverage

## 11. next action

Possible next actions:

```text
1. run read-only DB query for C with full raw_url output
2. add exact raw_url anchors to this card
3. create m term-card candidate
4. create t term-card candidate
5. create p term-card candidate
6. create ? term-card candidate
7. later compare C across branch.market / branch.sohosa / branch.history
```

## 12. guard

This card is a candidate.

This card is not a final definition.

DB output is derived evidence.

Original source remains in md files and Raw URLs.

gpt.direct performs final structure alignment.
