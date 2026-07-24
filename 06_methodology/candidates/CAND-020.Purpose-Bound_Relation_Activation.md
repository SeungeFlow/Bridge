---
candidate_id: CAND-020
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-020 — 목적결속 관계활성

**Canonical name:** `Purpose-Bound Relation Activation`

## Purpose

공통장에 잠재된 관계 중 질문·목적·역할에 맞는 경로만 활성화한다.

## Applicable Data

- AI가 README/DB를 비선형 탐색
- 동일 Region의 여러 관측면

## Activation Signals

- 모든 관계를 미리 열거하려는 조합폭발
- 번호순 읽기가 부적합

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Question/Profile 입력
- Start Region 선택
- Relation Type 선택
- Traversal Path 생성
- Output Boundary에서 종료

## Output Contract

Context-specific Reading/Execution Path

## Validators

- path must preserve source and declared transformations

## Strengths

- 문서를 실행환경으로 사용

## Limits

- 관계 metadata가 부족하면 탐색비용 증가

## Compatible Methods

- CAND-019
- CAND-021
- CAND-092

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 단일 Method 선택만 필요하면 CAND-021

## Formation Lineage

- LIVE-E014
- LIVE-E015
