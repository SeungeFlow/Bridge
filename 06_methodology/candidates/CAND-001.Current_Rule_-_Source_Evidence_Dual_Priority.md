---
candidate_id: CAND-001
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-001 — 현재 규칙·원천 증거 이중우선순위

**Canonical name:** `Current Rule / Source Evidence Dual Priority`

## Purpose

현재 목적과 용어는 현재 기준장이 정하고, 과거 원천이 실제로 보존한 증거범위는 원천계보가 제한하도록 한다.

## Applicable Data

- 과거 문서·현재 대화·새 목적이 함께 입력된 분석
- 기존 이론을 현재 용어로 재구성하는 작업

## Activation Signals

- 현재 이해와 과거 문서의 용어가 충돌
- 과거 기록을 현재 정본처럼 읽을 위험

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- 현재 Rule Priority를 선언
- Source Evidence Priority를 선언
- 현재 규칙으로 질문을 구성
- 원천 Evidence 범위를 넘는 주장을 OPEN으로 둠

## Output Contract

현재 규칙과 원천 증거가 병합되지 않은 분석계약

## Validators

- current context does not rewrite source
- source lineage does not freeze current method

## Strengths

- 시대·회차 혼합 방지
- 원천 개작 방지

## Limits

- 원천 자체가 불완전하면 결론도 제한됨

## Compatible Methods

- CAND-002
- CAND-003
- CAND-014
- CAND-034

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 현재 규칙 또는 원천 Identity가 선언되지 않으면 CAND-090을 먼저 활성

## Formation Lineage

- LIVE-E001
- LIVE-E002
- LIVE-E003
