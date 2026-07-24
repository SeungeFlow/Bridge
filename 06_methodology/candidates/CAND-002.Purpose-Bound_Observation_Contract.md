---
candidate_id: CAND-002
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-002 — 목적결속 관측계약

**Canonical name:** `Purpose-Bound Observation Contract`

## Purpose

관측자·기준장·대상·목적·원천상태·출력경계를 선언해 같은 대상을 다른 자리에서 본 결과를 분리한다.

## Applicable Data

- 관측자 위치·방향·표면에 따라 결과가 달라지는 Data
- AI와 인간의 관측결과 비교

## Activation Signals

- 같은 대상인데 해석이 다름
- 정면/뒷면/윗면/옆면이 문제

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Observer 선언
- ReferenceField 선언
- Target 선언
- Purpose 선언
- ObserverSeat/Face/ViewDirection 필요여부 선언
- OutputBoundary 선언

## Output Contract

재현 가능한 ObservationContract

## Validators

- same target does not imply same surface
- purpose change is recorded

## Strengths

- 관측자리 혼동 방지
- 해석경로 재현 가능

## Limits

- 실제 물리 배치가 불명확하면 논리모형으로만 유지

## Compatible Methods

- CAND-008
- CAND-009
- CAND-010
- CAND-035

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- Source 변환이 핵심이면 CAND-003 병행

## Formation Lineage

- LIVE-E004
- LIVE-E005
- LIVE-E006
- LIVE-E007
