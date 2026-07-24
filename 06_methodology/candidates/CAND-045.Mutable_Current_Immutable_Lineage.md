---
candidate_id: CAND-045
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
---

# 가변 현재·불변 계보

## Purpose

현재 해석과 Branch는 수정 가능하게 두고 과거 Commit·객체·형성계보는 보존한다.

## Applicable Data

- GitHub Schema 갱신
- Before_Position/Start_Position 운영
- 새 Version 생성

## Activation Signals

- GitHub 전체를 절대불변으로 고정
- 새 아이디어가 기존 정본과 충돌

## Process

1. Past formed state 보존
2. Current form 선택
3. New Data로 re-forming
4. 새 Form 결정화

## Output

append-only form lineage with mutable active pointer

## Validators

- supersedes does not delete
- current branch does not rewrite past commit

## Strengths

- 생각의 성장과 역사보존 동시달성

## Limits

- 현재 우선상태 선택이 필요

## Compatible

`CAND-024, CAND-027, CAND-044, CAND-046`

## Formation Lineage

- POST-R04-FORM-LINEAGE
