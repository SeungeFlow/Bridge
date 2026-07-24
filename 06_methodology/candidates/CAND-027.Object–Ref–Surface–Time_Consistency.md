---
candidate_id: CAND-027
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-027 — 객체·Ref·표면·시간 정합검산

**Canonical name:** `Object–Ref–Surface–Time Consistency`

## Purpose

Git Object, 움직이는 Branch Ref, blob/raw Web Surface, 관측시간을 분리해 동일성·전파지연·실제충돌을 판정한다.

## Applicable Data

- GitHub blob/raw 불일치
- Local/Remote 정본검산

## Activation Signals

- 같은 branch/path인데 내용이 잠시 다름

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- Local Exact Bytes 확인
- Commit/Tree/Blob Identity 확인
- Remote Ref 확인
- 각 Web Surface 관측시간 기록
- Delay/Conflict 분류

## Output Contract

SAME_OBJECT_PROPAGATION_DELAY / DIFFERENT_COMMIT_STATE / TRUE_CONTENT_CONFLICT

## Validators

- web surface is not canonical object
- moving ref is not pinned commit

## Strengths

- Web 착시와 실제 Git 충돌 분리

## Limits

- GitHub 내부 물리 서버흐름은 OPEN

## Compatible Methods

- CAND-003
- CAND-018
- CAND-033

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 정적 파일 Identity만 필요하면 CAND-033

## Formation Lineage

- LIVE-E023
