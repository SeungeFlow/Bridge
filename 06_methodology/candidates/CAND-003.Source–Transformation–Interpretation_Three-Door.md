---
candidate_id: CAND-003
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-003 — 원천–변환–해석 3-Door 계보

**Canonical name:** `Source–Transformation–Interpretation Three-Door`

## Purpose

원천 증거, 적용된 변환, 현재 해석후보를 세 Door로 분리해 숨은 변환을 금지한다.

## Applicable Data

- 이미지 반전·회전·전사·정규화
- 과거 문서의 현대식 재표현
- Web/Raw/Local 비교

## Activation Signals

- 원본과 현재 표시가 다름
- 어떤 변환이 있었는지 불명확

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Source Door에서 보존 Evidence 확인
- Transformation Door에서 모든 변환 선언
- Interpretation Door에서 현재 구조후보 판정

## Output Contract

Source.State₀부터 Current.Input.State까지의 변환계보

## Validators

- hidden transformation forbidden
- interpretation cannot modify source evidence

## Strengths

- 변환과 해석의 혼합 방지

## Limits

- 원천 byte가 없으면 일부 Door는 HOLD

## Compatible Methods

- CAND-001
- CAND-031
- CAND-033
- CAND-091

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 질문 통과조건만 필요하면 CAND-085 또는 CAND-087

## Formation Lineage

- LIVE-E003
- LIVE-E004
- LIVE-E005
- LIVE-E023
