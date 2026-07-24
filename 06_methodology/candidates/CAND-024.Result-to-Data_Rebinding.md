---
candidate_id: CAND-024
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-024 — Result→Next.Data 재결속

**Canonical name:** `Result-to-Data Rebinding`

## Purpose

한 Process의 Result를 동결·역할재지정하여 다음 Process의 Data로 전달한다.

## Applicable Data

- 회차 전달
- C Result→B Data
- AI 간 Handoff

## Activation Signals

- 결과가 다음 단계에서 재사용
- 같은 byte가 역할을 바꿈

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Result Boundary 검산
- Freeze State 기록
- New Purpose/ReferenceField 선언
- Data Role로 Rebind
- Lineage Pointer 생성

## Output Contract

Result.Data와 Next.Input Contract

## Validators

- same object role change is declared
- source lineage remains reachable

## Strengths

- 재귀적 Process 형성

## Limits

- 미검증 Result의 무조건 승격 금지

## Compatible Methods

- CAND-018
- CAND-025
- CAND-030

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- DB 승격이면 CAND-025 추가

## Formation Lineage

- LIVE-E015
- LIVE-E016
- LIVE-E022
- LIVE-E026
