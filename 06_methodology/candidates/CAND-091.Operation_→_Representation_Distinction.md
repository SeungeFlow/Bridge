---
candidate_id: CAND-091
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-091 — Operation→Representation 구분

**Canonical name:** `Operation → Representation Distinction`

## Purpose

Source에서 실제로 일어난 Operation과 AI가 Evidence를 재구성한 Representation을 분리한다.

## Applicable Data

- 과거 작업문서 분석
- AI 해석문 생성

## Activation Signals

- 표현문을 실제 작동과 동일시

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Source operation evidence 확인
- Trace/Input Door 확인
- AI representation 과정 기록
- Structure expression 동결

## Output Contract

Operation/Representation Lineage

## Validators

- representation cannot be claimed as source operation

## Strengths

- historical crystallized candidate identity preserved

## Limits

- 현재 Data와 목적에 따라 비활성 또는 교체 가능

## Compatible Methods

- CAND-003
- CAND-031
- CAND-089

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 영구 주전 없음; 조건부 활성

## Formation Lineage

- LIVE-E003

## Historical Sample Identity

`Sample.091`
