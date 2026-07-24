---
candidate_id: CAND-021
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-021 — 후보방법론 선발

**Canonical name:** `Candidate Method Lineup Selection`

## Purpose

모든 Sample/Method Candidate 중 현재 Data와 목적에 적합한 임시 주전 Lineup을 선택한다.

## Applicable Data

- 새 Data 묶음 분석
- N개 방법론 후보군

## Activation Signals

- Permanent Starter를 고정
- 모든 Method를 매번 실행

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Data Profile 생성
- Activation Signal 비교
- Required Evidence 확인
- 초기 Active Lineup 구성
- 선발근거 기록

## Output Contract

Context-bound Temporary Method Lineup

## Validators

- inactive does not mean rejected
- selection reason is explicit

## Strengths

- 후보군 다양성과 실행효율 양립

## Limits

- 선발자 Function 자체의 편향 검산 필요

## Compatible Methods

- CAND-020
- CAND-022
- CAND-023

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- Method가 하나뿐이면 직접 적용

## Formation Lineage

- LIVE-E015
- LIVE-E027
