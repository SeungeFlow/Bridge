---
candidate_id: CAND-037
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
---

# 닫힌 표면경로·열린 축경로 분리

## Purpose

곡면을 따라 되돌아오는 경로와 현재 경계에서 닫히지 않은 외향축을 분리한다.

## Applicable Data

- 지표면/원호/순환과 수직 외향 진행 비교
- Tree 경로와 폐합구조 비교

## Activation Signals

- 같은 선형이동으로 순환과 외향진행을 함께 설명

## Process

1. 표면/축 선언
2. 폐합조건 선언
3. 현재 경계에서 귀환 가능성 판정

## Output

closed-cycle candidate 또는 open-ended path

## Validators

- unknown closure is not proven infinity

## Strengths

- 폐합과 무한의 혼동 방지

## Limits

- 외부경계가 미확인일 수 있음

## Compatible

`CAND-006, CAND-007, CAND-018`

## Formation Lineage

- POST-R04-SPATIAL-PATHS
