---
candidate_id: CAND-047
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
---

# Before_Position·Start_Position 활성상태 선택

## Purpose

과거 Formed State 전체와 현재 Process 바닥으로 선택된 Form을 분리한다.

## Applicable Data

- Principle_C Branch 운영
- 현재 Boot Reference 선택

## Activation Signals

- 과거 Schema 전체를 현재 Context에 적재
- 현재 Start와 역사 Branch 혼동

## Process

1. Before_Position history 보존
2. Current Start 후보평가
3. Start_Position 선택이유 기록

## Output

current active form pointer plus preserved history relation

## Validators

- history is not loaded as active by default
- current start is revisable

## Strengths

- Context 과부하 방지
- 계보와 현재 분리

## Limits

- Before_Position 실제 수정은 별도 승인 필요

## Compatible

`CAND-045, CAND-046, CAND-090`

## Formation Lineage

- POST-R04-BEFORE-START-POSITION
