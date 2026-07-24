---
candidate_id: CAND-041
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
---

# 장비매개 관측계보

## Purpose

직접 보지 못하는 현실이 신호·측정·표현으로 변환되는 Door를 보존한다.

## Applicable Data

- 소나·센서·로그·측정장비 Data

## Activation Signals

- 대상 자체가 아니라 반사·신호·측정값만 있음

## Process

1. Reality interaction
2. Trace capture
3. Measurement
4. Transformation
5. Representation

## Output

instrument-to-representation lineage

## Validators

- calibration/error boundary explicit
- signal is not object

## Strengths

- 보이지 않는 현실의 검산 가능한 재구성

## Limits

- 장비오차와 모델오차가 누적될 수 있음

## Compatible

`CAND-003, CAND-031, CAND-040, CAND-042`

## Formation Lineage

- POST-R04-INSTRUMENT-MEDIATED
