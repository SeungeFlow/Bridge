---
candidate_id: CAND-016
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-016 — 평바닥 우선설정

**Canonical name:** `Support-Plane First`

## Purpose

규칙·Schema·System을 수평 기준바닥으로 놓고 그 위에서 Data와 Plan이 형성되게 한다.

## Applicable Data

- AI 자율계획
- Repo Tree 배치
- Schema 기반 구현

## Activation Signals

- 위/아래·우선순위·배치방향이 혼란
- Data가 놓일 자리가 없음

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Support Plane 선택
- 고정 규칙/경계 선언
- Data 배치
- 관계·누락 확인
- Plan 생성

## Output Contract

Stable Planning Field

## Validators

- floor is relative reference not absolute rank

## Strengths

- AI가 규칙 안에서 자율계획 가능

## Limits

- 바닥이 너무 상세하면 자율성 억제

## Compatible Methods

- CAND-017
- CAND-090
- CAND-030

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 단순 Identity 정렬이면 CAND-090

## Formation Lineage

- LIVE-E012
- LIVE-E024
