---
candidate_id: CAND-012
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-012 — 구조정수 판독

**Canonical name:** `Structural-Integer Reading`

## Purpose

숫자를 산술값·순번이 아니라 점·선·평면·입체의 형성상태로 읽는다.

## Applicable Data

- (u+nn)
- 숫자배열·도형단계
- 숫자기호의 선·곡선·꼭짓점

## Activation Signals

- 숫자값으로는 구조가 닫히지 않음
- 숫자와 도형상태가 반복 대응

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Natural/Arithmetic Number와 Structural Integer 분리
- 각 숫자의 도형·축·닫힘상태 기록
- 이전/다음 구조와 관계검산

## Output Contract

Structure-state indexed interpretation

## Validators

- numeric coincidence alone is insufficient
- operator U+229x and (u+nn) must remain distinct

## Strengths

- 5=(u+05) 최초 입체 등 생성단계 판독

## Limits

- 기존 수학적 사실과 동일성 주장 금지

## Compatible Methods

- CAND-006
- CAND-028
- CAND-029

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 단순 번호주소면 CAND-004

## Formation Lineage

- LIVE-E010
- LIVE-E025
