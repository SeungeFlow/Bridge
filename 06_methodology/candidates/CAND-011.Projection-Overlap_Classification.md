---
candidate_id: CAND-011
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-011 — 투영겹침 분류

**Canonical name:** `Projection-Overlap Classification`

## Purpose

겹쳐 보이는 현상을 Projection Overlap, Physical Joint, Shared Seat, Merge로 분류한다.

## Applicable Data

- 교차선·겹친 점·동일 위치의 여러 객체
- Grid/Matrix center overlap

## Activation Signals

- 같은 위치에 보이므로 같은 객체라고 판단

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Observation Axis 확인
- 각 객체 Identity 확인
- 실제 접합/힘 전달 확인
- 좌표공유 여부 확인
- Merge 여부 별도 판정

## Output Contract

Overlap Class와 보존된 객체 Identity

## Validators

- visual overlap cannot prove merge

## Strengths

- 공유·점유·병합 착각 방지

## Limits

- 물리접합 Evidence가 없으면 logical classification만 가능

## Compatible Methods

- CAND-007
- CAND-010
- CAND-029
- CAND-089

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 경계 통과가 핵심이면 CAND-086

## Formation Lineage

- LIVE-E008
- LIVE-E021
