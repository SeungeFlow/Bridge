---
candidate_id: CAND-086
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-086 — 양면 Door 전이

**Canonical name:** `Two-sided Door Transition`

## Purpose

Door 양쪽의 Inside/Outside·Face·Direction을 분리하고 통과 전후 상태를 기록한다.

## Applicable Data

- 양면경계
- 나/너·정면/뒷면

## Activation Signals

- 같은 Door 양쪽에서 관측결과가 다름

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Face A/B 선언
- Direction 선언
- Pass condition 확인
- State transition 기록

## Output Contract

Two-sided Transition Record

## Validators

- front/back are relational
- passage is not merge

## Strengths

- historical crystallized candidate identity preserved

## Limits

- 현재 Data와 목적에 따라 비활성 또는 교체 가능

## Compatible Methods

- CAND-009
- CAND-011
- CAND-087

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 영구 주전 없음; 조건부 활성

## Formation Lineage

- LIVE-E007

## Historical Sample Identity

`Sample.086`
