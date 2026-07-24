---
candidate_id: CAND-033
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-033 — 운송이름보다 내용 Identity

**Canonical name:** `Content Identity over Transport Name`

## Purpose

파일의 Exact Bytes와 Object Role을 filename suffix·Web display name보다 우선해 동일성을 판정한다.

## Applicable Data

- 중복 업로드 자동번호
- <hash.code.file.name>
- Repo 파일이동

## Activation Signals

- 이름만 달라서 다른 객체로 판단
- 이름만 같아서 같은 객체로 판단

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Exact Bytes hash 계산
- Logical Object Role 확인
- Transport Name 기록
- Identity verdict

## Output Contract

Content/Object Identity Record

## Validators

- hash is filename self-identity for publication zip
- standalone sidecar not required by current contract

## Strengths

- 정본·복제·운송상태 구분

## Limits

- 동일 byte의 역할재결속은 별도 선언 필요

## Compatible Methods

- CAND-004
- CAND-027
- CAND-090

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- Git Ref 시간문제면 CAND-027

## Formation Lineage

- LIVE-E020
- LIVE-E030
- LIVE-E031
