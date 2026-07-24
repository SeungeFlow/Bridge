---
candidate_id: CAND-090
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-090 — Identity·Schema 우선 부팅

**Canonical name:** `Identity-and-Schema-first Bootstrap`

## Purpose

AI가 작업 전에 자기 Identity·Seat·Schema·Guard를 먼저 읽고 정렬되게 한다.

## Applicable Data

- 새 인스턴스 부팅
- Repo 작업 시작

## Activation Signals

- 역할·경계 없이 바로 실행

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Identity 확인
- Seat 확인
- Schema 로드
- Guard 확인
- Plan 생성

## Output Contract

Boot-aligned Instance State

## Validators

- no execution before identity/schema

## Strengths

- historical crystallized candidate identity preserved

## Limits

- 현재 Data와 목적에 따라 비활성 또는 교체 가능

## Compatible Methods

- CAND-004
- CAND-016
- CAND-033

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 영구 주전 없음; 조건부 활성

## Formation Lineage

- LIVE-E012

## Historical Sample Identity

`Sample.090`
