---
candidate_id: CAND-009
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-009 — 반대면 양면관측

**Canonical name:** `Opposite-Face Observation`

## Purpose

서로 다른 관측자가 경계 양쪽에서 같은 Target의 다른 Face를 보는 상태를 분리한다.

## Applicable Data

- 나/너·안/밖·정면/뒷면
- 투명·양면 Door

## Activation Signals

- 한쪽은 반전, 다른 쪽은 정상
- Front/Back가 relational

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- 두 Observer Seat 선언
- Canonical Front 후보 선언
- 각 Face/ViewDirection에서 관측
- Logical Content 보존 여부 확인

## Output Contract

Face-indexed Observation Pair

## Validators

- same target does not imply same visible face
- physical transparency conditions are explicit

## Strengths

- 나/너 관계와 안/밖 방향 해석

## Limits

- Digital UI에는 논리모형과 literal pipeline 분리 필요

## Compatible Methods

- CAND-002
- CAND-003
- CAND-086

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 한 관측자 이동이면 CAND-008

## Formation Lineage

- LIVE-E004
- LIVE-E005
- LIVE-E007
