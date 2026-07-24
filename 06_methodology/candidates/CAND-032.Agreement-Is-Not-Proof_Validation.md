---
candidate_id: CAND-032
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-032 — 합의≠검증 판정

**Canonical name:** `Agreement-Is-Not-Proof Validation`

## Purpose

여러 AI/Method가 같은 결론을 내린 사실과 Source·역검산을 통과한 사실을 분리한다.

## Applicable Data

- 복수 AI 분석
- Parallel Method 결과

## Activation Signals

- 다수가 동의하므로 참이라고 승격

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- 각 Result의 Source/Method 계보 확인
- 독립성 확인
- 동일 결론의 공통 의존성 탐색
- 실제 Validator 별도 실행

## Output Contract

Agreement Record와 Verification Record의 분리

## Validators

- consensus alone cannot promote result

## Strengths

- 집단오류 방지

## Limits

- 검증자료가 없으면 HOLD만 가능

## Compatible Methods

- CAND-015
- CAND-022
- CAND-026

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 단일 Method라도 동일 원칙 적용

## Formation Lineage

- LIVE-E001
- LIVE-E015
