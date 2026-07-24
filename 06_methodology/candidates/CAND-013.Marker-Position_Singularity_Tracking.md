---
candidate_id: CAND-013
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-013 — Marker 위치 특이점 추적

**Canonical name:** `Marker-Position Singularity Tracking`

## Purpose

`**`, `***`, 특이점 등의 기호내용보다 앞뒤 상태차이를 추적한다.

## Applicable Data

- 장기 Idea Flow 문서
- 자기보정 기록
- Trigger/Anchor 문서

## Activation Signals

- Marker 직후 기준·용어·방향이 바뀜

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Marker 위치 Index
- Before State 추출
- After State 추출
- Difference 판정
- 실제 Formation Singularity 승격 여부 결정

## Output Contract

Before–Marker–After Singularity Record

## Validators

- marker occurrence is not automatic proof

## Strengths

- 결론보다 생성전환점 발견

## Limits

- 문맥이 짧으면 오판 가능

## Compatible Methods

- CAND-014
- CAND-085

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 명시 Marker가 없으면 Difference 기반 탐색

## Formation Lineage

- LIVE-E011
