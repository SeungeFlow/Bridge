---
candidate_id: CAND-005
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-005 — 표면선형 우선기록

**Canonical name:** `Surface-First Linear Recording`

## Purpose

보이는 선형배열을 먼저 개작 없이 기록하고, 해석 실패 시 상위차원 복원으로 넘긴다.

## Applicable Data

- 수열·문장·화살표·선형 Trace
- 평면/입체 투영 가능성이 있는 선

## Activation Signals

- 선형으로 보이지만 의미가 닫히지 않음

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Visible Trace 기록
- 순서·방향·간격 기록
- 추가 의미를 붙이지 않음
- 불충분 시 CAND-006 활성

## Output Contract

변환 전 Linear Evidence Record

## Validators

- surface record precedes volumetric interpretation

## Strengths

- 성급한 입체화 방지
- 원표면 보존

## Limits

- 선형만으로는 원인구조를 설명하지 못함

## Compatible Methods

- CAND-006
- CAND-007
- CAND-012

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 표면이 이미 비선형이면 해당 표현차원에서 기록

## Formation Lineage

- LIVE-E002
- LIVE-E005
- LIVE-E006
