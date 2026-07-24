---
candidate_id: CAND-028
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-028 — Scale별 구조분리

**Canonical name:** `Scale-Indexed Structural Separation`

## Purpose

같은 도형·필드가 서로 다른 Scale에서 다른 역할을 가질 때 경쟁이론이 아니라 중첩 Scale로 분리한다.

## Applicable Data

- 공간 전체의 육면체 반복과 한 육면체 내부구조
- ReferenceField가 상위 Scale에서 State가 되는 경우

## Activation Signals

- 두 모형이 계속 헷깔리지만 각각 다른 범위에서 설명력 있음

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- 각 모형 Boundary/Scale 선언
- 상위/하위 포함관계 확인
- 공통 Anchor 확인
- Scale 간 변환관계 기록

## Output Contract

Scale-indexed Parallel Models

## Validators

- same word at different scale is not automatic contradiction

## Strengths

- 반복 Cell Network와 내부 Frame 동시보존

## Limits

- Scale 경계가 임의적이면 과잉설명

## Compatible Methods

- CAND-006
- CAND-012
- CAND-017
- CAND-029

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 관측면 차이만 있으면 CAND-002

## Formation Lineage

- LIVE-E025
