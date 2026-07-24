---
candidate_id: CAND-019
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-019 — 영역우선 문서구성

**Canonical name:** `Region-First Document Composition`

## Purpose

서로 다른 내부문법의 결정화 영역을 공통장에 배치하고 관계를 사후 발생시킨다.

## Applicable Data

- 오감도식 문서
- README 내부 N개의 결정화 영역
- Book-type Active_Schema

## Activation Signals

- 모든 Section을 동일 Template에 강제로 맞춤
- 번호순 읽기 강제

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- 각 Region Local Boundary/Grammar 결정화
- Common Field에 배치
- Identity 유지
- 관계 잠재상태 보존

## Output Contract

Relation-connected Document Field

## Validators

- local completeness survives global placement
- placement does not merge regions

## Strengths

- 이질적 방법론을 한 문서에 보존

## Limits

- Region Identity가 약하면 긴 혼합문서가 됨

## Compatible Methods

- CAND-017
- CAND-020
- CAND-092

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 단일 선형논증이 실제 목적이면 일반 문서구성

## Formation Lineage

- LIVE-E013
- LIVE-E014
