---
candidate_id: CAND-040
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
---

# 현실·추상 분석모드 선발

## Purpose

입력 Data가 현실흔적·장비매개·추상표현·혼합형인지 판정해 적합한 Method Lineup을 구성한다.

## Applicable Data

- 모든 신규 Data profiling

## Activation Signals

- 직접 본 것과 표현된 것과 추론된 것이 혼재

## Process

1. 관측모드 분류
2. 변환계보 확인
3. 현실/추상/Bridge 후보군 선택

## Output

context-bound active method lineup seed

## Validators

- possession is not knowledge
- representation is not object

## Strengths

- 방법론 오선발 감소

## Limits

- 혼합 Data는 복수 후보 필요

## Compatible

`CAND-003, CAND-021, CAND-042, CAND-043`

## Formation Lineage

- POST-R04-REALITY-ABSTRACTION
