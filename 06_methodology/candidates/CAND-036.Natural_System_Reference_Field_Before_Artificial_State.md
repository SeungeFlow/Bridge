---
candidate_id: CAND-036
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
---

# 인공상태 이전 선행 기준장 우선

## Purpose

인공구조가 놓일 수 있게 한 자연·System 기준장을 먼저 복원한다.

## Applicable Data

- 건축·저장·AI System·Repo Tree를 분석할 때 선행바닥이 필요한 경우

## Activation Signals

- 수직·수평·중심이 절대개념처럼 사용됨
- 인공대상만 보이고 선행조건이 빠짐

## Process

1. 선행 기준장 탐색
2. 존립조건 분리
3. 인공상태를 그 위에 재배치

## Output

선행기준장과 후행상태가 분리된 구조

## Validators

- artificial state does not rewrite natural/system field

## Strengths

- 바닥 없는 방향개념 방지

## Limits

- 선행 기준장이 복수이면 추가 Selection 필요

## Compatible

`CAND-016, CAND-035, CAND-039`

## Formation Lineage

- POST-R04-NATURAL-REFERENCE
