---
candidate_id: CAND-034
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-034 — 시대내재 원천읽기

**Canonical name:** `Epoch-Intrinsic Source Reading`

## Purpose

현대 표현·관습을 과거 원천에 역투사하지 않고 당시 표기·읽기·기술환경을 먼저 복원한다.

## Applicable Data

- 역사문서·옛 표기법·원본 이미지
- 오감도 날짜/읽기방향

## Activation Signals

- 현대 좌→우 표기로 원본을 개작
- 후대 의미로 과거기호 설명

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- 원천시대/매체 확인
- 당대 읽기규칙 후보 수집
- 현대 변환과 원본상태 분리
- 구조불변식 검산

## Output Contract

Epoch-indexed Source Interpretation

## Validators

- historical claim requires source
- structural analogy remains separate

## Strengths

- 현대 역투사 방지

## Limits

- 당대 관습 자료가 부족하면 OPEN

## Compatible Methods

- CAND-001
- CAND-003
- CAND-031

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 시대가 무관한 순수구조는 일반 Source Reading

## Formation Lineage

- LIVE-E004
- LIVE-E005
