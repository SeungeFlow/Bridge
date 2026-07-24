---
candidate_id: CAND-010
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-010 — 윗면 깊이누적 관측

**Canonical name:** `Top-View Depth Accumulation`

## Purpose

정면에서 시간적 이동으로 보이는 상태들을 윗면에서 Z축 누적·가림으로 재해석한다.

## Applicable Data

- 행별 이동점
- 층·깊이·누적과정
- Occlusion

## Activation Signals

- 하나로 보이는 표식 아래 여러 상태가 있을 가능성

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- 각 행을 Layer로 재배치
- Top View Axis 선언
- 동일 XY 위치의 Z-depth 계산
- Visible Count와 Structural Multiplicity 분리

## Output Contract

Layered State Field와 Occlusion Record

## Validators

- occlusion is not deletion
- overlap is not merge

## Strengths

- Process를 Accumulated Result로 변환

## Limits

- 층 배치 근거가 없으면 후보 유지

## Compatible Methods

- CAND-006
- CAND-011
- CAND-029

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 단순 평면중첩이면 CAND-011

## Formation Lineage

- LIVE-E008
