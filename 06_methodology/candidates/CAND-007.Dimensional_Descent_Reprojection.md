---
candidate_id: CAND-007
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-007 — 차원하향 재투영

**Canonical name:** `Dimensional Descent Reprojection`

## Purpose

복원한 입체관계를 다시 평면·선형 구조표현으로 투영해 원표현과 역검산한다.

## Applicable Data

- 입체구조 후보가 형성된 후
- 설명을 최소 구조표현으로 내려야 할 때

## Activation Signals

- 입체 설명이 원문 표면과 실제로 맞는지 확인 필요

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- View/Projection Axis 선언
- Volume을 Face/Plane로 투영
- Plane을 Linear Trace로 투영
- 원표면과 비교

## Output Contract

원표현과 결속된 구조표현식

## Validators

- reprojection must recover observed anomalies
- projection overlap is classified

## Strengths

- 상상적 입체모형의 역검산

## Limits

- 하나의 투영 일치만으로 원구조 확정 불가

## Compatible Methods

- CAND-006
- CAND-011
- CAND-015

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 단순 설명축약이면 일반 요약과 구분

## Formation Lineage

- LIVE-E006
- LIVE-E008
- LIVE-E009
