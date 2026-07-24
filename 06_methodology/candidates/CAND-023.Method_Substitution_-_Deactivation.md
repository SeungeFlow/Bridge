---
candidate_id: CAND-023
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-023 — 방법론 교체·비활성

**Canonical name:** `Method Substitution / Deactivation`

## Purpose

Process 중 특이점·부적합·Evidence 부족이 드러나면 Method를 추가·교체·비활성화한다.

## Applicable Data

- 초기 Lineup이 문제를 못 닫음
- 새 Data가 들어옴

## Activation Signals

- Method output mismatch
- validator failure
- new dimension appears

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Mismatch 기록
- Substitution Trigger 분류
- 후보군 재평가
- 교체/추가
- 이전 Method 적용계보 보존

## Output Contract

Lineup Transition Record

## Validators

- substitution does not rewrite prior output

## Strengths

- 실행중 적응성

## Limits

- 무제한 교체로 종료조건 상실 가능

## Compatible Methods

- CAND-013
- CAND-014
- CAND-021

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 경계실패 실험이면 CAND-088 병행

## Formation Lineage

- LIVE-E006
- LIVE-E008
- LIVE-E027
