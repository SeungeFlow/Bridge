---
candidate_id: CAND-043
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
---

# 현실–추상 왕복검산

## Purpose

현실 Data에서 추상구조를 만들고 다시 현실 Data에 재투영해 차이를 찾는다.

## Applicable Data

- 구조모형·좌표·도형으로 현실 Data를 해석할 때

## Activation Signals

- 추상구조가 현실 Data에서 분리될 위험

## Process

1. Reality Data
2. Abstract reconstruction
3. Reality reprojection
4. Difference detection
5. Correction

## Output

validated correspondence or bounded mismatch

## Validators

- reprojection difference is explicit
- model does not overwrite source

## Strengths

- 자유연상 억제
- 구조모형 개선

## Limits

- 현실 Data가 빈약하면 OPEN

## Compatible

`CAND-015, CAND-039, CAND-040, CAND-042`

## Formation Lineage

- POST-R04-ROUND-TRIP
