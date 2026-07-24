---
candidate_id: CAND-015
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-015 — 정방향·역방향 구조검산

**Canonical name:** `Forward / Reverse Structural Validation`

## Purpose

생성방향과 해체방향을 모두 통과시켜 같은 구조관계가 보존되는지 검산한다.

## Applicable Data

- 입체복원
- Data→Result 계보
- Repo/Hash 역추적

## Activation Signals

- 한 방향 설명만 존재
- Result에서 Source로 돌아갈 수 없음

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Forward generation 실행
- Result 고정
- Reverse decomposition 실행
- Source/Boundary/Relation 일치 판정

## Output Contract

Forward/Reverse Validation Result

## Validators

- same conclusion by multiple AIs is not reverse proof

## Strengths

- 상상모형·변환계보 검산

## Limits

- 비가역 Function은 손실을 명시해야 함

## Compatible Methods

- CAND-003
- CAND-007
- CAND-014
- CAND-032

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 국소 Door 검증이면 CAND-087

## Formation Lineage

- LIVE-E002
- LIVE-E007
- LIVE-E017
