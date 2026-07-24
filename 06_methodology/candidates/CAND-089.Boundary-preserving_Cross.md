---
candidate_id: CAND-089
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-089 — 경계보존 Cross

**Canonical name:** `Boundary-preserving Cross`

## Purpose

서로 다른 객체가 Cross Relation을 맺어도 각 Identity와 Boundary를 유지하도록 한다.

## Applicable Data

- Track/Hash 관계
- Observer/Target 관계
- Grid/Matrix overlap

## Activation Signals

- 교차 후 병합으로 오인

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- 양쪽 Identity 고정
- Cross point 선언
- shared relation 기록
- 분리상태 역검산

## Output Contract

Boundary-preserving Cross Record

## Validators

- relation is not merge

## Strengths

- historical crystallized candidate identity preserved

## Limits

- 현재 Data와 목적에 따라 비활성 또는 교체 가능

## Compatible Methods

- CAND-011
- CAND-035
- CAND-091

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 영구 주전 없음; 조건부 활성

## Formation Lineage

- LIVE-E008

## Historical Sample Identity

`Sample.089`
