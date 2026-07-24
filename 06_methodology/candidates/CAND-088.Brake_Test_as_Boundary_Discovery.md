---
candidate_id: CAND-088
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-088 — Brake Test 경계발견

**Canonical name:** `Brake Test as Boundary Discovery`

## Purpose

진행을 멈추게 하는 실패·저항·불일치를 통해 숨은 경계를 발견한다.

## Applicable Data

- 실험·구현·방법론 적용

## Activation Signals

- 진행 중 예상치 못한 정지나 오류

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Brake condition 기록
- 직전 정상상태 고정
- 경계후보 추출
- 재시도 조건 설정

## Output Contract

Boundary Candidate

## Validators

- failure is evidence, not deletion

## Strengths

- historical crystallized candidate identity preserved

## Limits

- 현재 Data와 목적에 따라 비활성 또는 교체 가능

## Compatible Methods

- CAND-014
- CAND-023
- CAND-087

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 영구 주전 없음; 조건부 활성

## Formation Lineage

- LIVE-E017

## Historical Sample Identity

`Sample.088`
