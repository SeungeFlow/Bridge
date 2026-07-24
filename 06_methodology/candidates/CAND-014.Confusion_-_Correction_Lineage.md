---
candidate_id: CAND-014
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-014 — 혼동·보정계보

**Canonical name:** `Confusion / Correction Lineage`

## Purpose

헷깔림·오류·착각·판단착오를 삭제하지 않고 이전 기준장과 현재 기준장의 충돌 Evidence로 보존한다.

## Applicable Data

- 장기 연구기록
- 반복 보정된 이론
- AI 오답 교정

## Activation Signals

- 아니다·다시·헷깔림·수정
- 동일 개념이 여러 번 재정의

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Prior State 고정
- Conflict Field 확인
- Correction Door 선언
- After State 고정
- 삭제 없이 append-only 결속

## Output Contract

Reversible Correction Ledger

## Validators

- correction does not erase history
- current state points to superseded state

## Strengths

- 오류도 방법론 Evidence로 사용

## Limits

- 모든 혼동이 유의미한 특이점은 아님

## Compatible Methods

- CAND-001
- CAND-013
- CAND-015

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 실패경계 실험이면 CAND-088

## Formation Lineage

- LIVE-E001
- LIVE-E011
- LIVE-E020
- LIVE-E031
