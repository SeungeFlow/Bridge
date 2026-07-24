---
candidate_id: CAND-018
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-018 — 공간상태 차이로서의 시간

**Canonical name:** `Space-State Difference Time`

## Purpose

시간을 공간상태 A와 B 사이의 위치·상태·관계차이 및 전이계보로 표현한다.

## Applicable Data

- Result→Next.Data
- Repo propagation delay
- 상태전이 기록

## Activation Signals

- 같은 객체가 다른 시점에 다르게 보임
- 두 공간 사이 이동/차이

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Before Space.State 고정
- Transition Door 기록
- After Space.State 고정
- Difference Dimension 분류

## Output Contract

Temporal Transition Record

## Validators

- one frozen state alone cannot prove time relation

## Strengths

- 역할전이와 시간차를 함께 기록

## Limits

- 표준 물리학 시간과의 동일성 주장이 아님

## Compatible Methods

- CAND-023
- CAND-024
- CAND-027

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 단순 순서기록이면 lineage record로 제한

## Formation Lineage

- LIVE-E023
- LIVE-E026
