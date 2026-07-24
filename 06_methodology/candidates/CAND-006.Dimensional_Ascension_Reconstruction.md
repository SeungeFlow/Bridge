---
candidate_id: CAND-006
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-006 — 차원상향 복원

**Canonical name:** `Dimensional Ascension Reconstruction`

## Purpose

선형에서 풀리지 않는 구조를 평면·면체·입체의 최소 닫힘조건으로 확장한다.

## Applicable Data

- 선형표현이 난해한 Data
- 면·옆면·깊이·관측경로가 숨어 있는 표현

## Activation Signals

- 한 방향 해석으로 모순
- 선이 경계·모서리·관측축일 가능성

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Linear Trace 확인
- Plane Arrangement 복원
- Face Adjacency 복원
- Volume/Observer Path 복원

## Output Contract

상위차원의 구조후보와 필요한 추가 Evidence

## Validators

- each ascension explains a prior anomaly
- higher dimension is not added without structural need

## Strengths

- 난해함을 관측차원 불일치로 재검산

## Limits

- 무제한 차원상향 금지

## Compatible Methods

- CAND-005
- CAND-007
- CAND-008
- CAND-028
- CAND-029

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- Source 변환 문제면 CAND-003 우선

## Formation Lineage

- LIVE-E006
- LIVE-E007
- LIVE-E008
- LIVE-E025
