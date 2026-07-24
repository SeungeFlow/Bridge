---
candidate_id: CAND-022
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-022 — 복수방법론 독립동시작동

**Canonical name:** `Parallel Independent Multi-Method Application`

## Purpose

여러 방법론이 동일 Data에 독립적으로 작동하고 Partial Result를 병합하지 않은 채 관계검산한다.

## Applicable Data

- 복합 Data
- 서로 다른 차원/출처/시간 검산이 동시에 필요

## Activation Signals

- 하나의 Method가 모든 문제를 떠맡음
- 여러 결과를 즉시 평균/합의로 병합

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- 각 Method Input Boundary 고정
- 독립 분석
- Partial Result Identity 보존
- Relation Validation
- Result Field 구성

## Output Contract

Method-attributed Partial Results와 관계결론

## Validators

- agreement is not proof
- disagreement is preserved

## Strengths

- 다각도 분석과 책임계보

## Limits

- Method 수 증가에 따른 비용

## Compatible Methods

- CAND-021
- CAND-023
- CAND-032

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 단일관측이면 한 Method만 활성

## Formation Lineage

- LIVE-E015
- LIVE-E027
