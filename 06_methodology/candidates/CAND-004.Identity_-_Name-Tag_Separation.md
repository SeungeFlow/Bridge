---
candidate_id: CAND-004
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-004 — Identity·Name Tag 분리

**Canonical name:** `Identity / Name-Tag Separation`

## Purpose

파일명·번호·통칭을 객체 Identity 자체로 오인하지 않고 내용·계보·자리와 분리한다.

## Applicable Data

- 운송 suffix가 붙은 파일
- 동일 내용의 다른 파일명
- 번호가 읽기순서로 오인되는 문서

## Activation Signals

- (1),(13) 같은 자동번호
- 파일명이 다르지만 byte가 같음
- 번호에 의미가 과도하게 부여됨

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Transport Name 기록
- Logical Name 기록
- Content Identity 확인
- Seat/Role Identity 확인

## Output Contract

Transport Name과 Content/Object Identity가 분리된 Registry

## Validators

- filename alone cannot prove identity
- same bytes may have different role only if rebinding declared

## Strengths

- 중복·개작·운송 오류 방지

## Limits

- byte를 얻을 수 없으면 content identity는 제한

## Compatible Methods

- CAND-033
- CAND-090
- CAND-027

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 구조기호 자체를 해체해야 하면 CAND-012

## Formation Lineage

- LIVE-E009
- LIVE-E012
- LIVE-E030
