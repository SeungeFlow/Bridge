---
candidate_id: CAND-035
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-035 — 관측자·기준장·대상 분리

**Canonical name:** `Observer–Reference–Target Separation`

## Purpose

관측자와 기준장과 관측대상을 병합하지 않고 각각의 자리와 역할을 고정한다.

## Applicable Data

- AI 구조검산
- Raw 기준장과 이론후보 비교
- 현재/과거 관측

## Activation Signals

- 기준장 내용이 관측자 생각으로 덮임
- 대상을 기준장과 동일시

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Observer 고정
- Criterion/Reference Field 고정
- Target 고정
- Relation Type 선언
- 병합금지

## Output Contract

Three-position Observation Field

## Validators

- observer_target_merge=false
- criterion_target_merge=false

## Strengths

- 분석자리 혼동 방지

## Limits

- 목적·표면이 중요하면 CAND-002로 확장

## Compatible Methods

- CAND-001
- CAND-002
- CAND-089

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 상세 ObservationContract 필요 시 CAND-002

## Formation Lineage

- LIVE-E001
- LIVE-E002
