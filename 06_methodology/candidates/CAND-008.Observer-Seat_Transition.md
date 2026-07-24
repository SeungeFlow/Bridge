---
candidate_id: CAND-008
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-008 — 관측자리 이동

**Canonical name:** `Observer-Seat Transition`

## Purpose

대상을 바꾸지 않고 관측자가 입체공간의 다른 자리로 이동했을 때 결과가 어떻게 변하는지 검산한다.

## Applicable Data

- 정면·반대면·옆면 이동
- 한 관측자의 위치이동

## Activation Signals

- 대상변환 없이 정상화 가능한지 질문
- Seat.1에서 Seat.0을 보는 구조

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Initial Seat 고정
- 가능한 이동경로 복원
- Final Seat/View Axis 선언
- 관측결과 비교

## Output Contract

Same Observer / Different Seat 결과쌍

## Validators

- object transform remains zero unless declared

## Strengths

- 객체반전과 관측자이동 분리

## Limits

- 실제 이동가능성은 입체경계 조건 필요

## Compatible Methods

- CAND-002
- CAND-006
- CAND-009

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 관측자가 둘이면 CAND-009

## Formation Lineage

- LIVE-E006
