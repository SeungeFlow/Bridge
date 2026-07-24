---
candidate_id: CAND-029
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
current_lineup_role: NONE_UNTIL_DATA_PROFILE
round: R04/10
---

# CAND-029 — dot→접합·기둥·트러스 복원

**Canonical name:** `Dot–Joint–Column–Truss Reconstruction`

## Purpose

평면의 dot/교차점/대각배열을 입체의 Joint·Axis·Column·Truss 후보로 복원한다.

## Applicable Data

- 오감도 시제4호 dot 배열
- 교차점이 깊이축을 가질 가능성
- 건축적 Frame 해석

## Activation Signals

- 점이 이동/누적/교차하며 선형·경사연결을 만듦

## Required Conditions

- input identity is declared
- observer/reference/purpose are declared when relevant
- transformations are explicit
- output is reusable as Result.Data

## Process

- dot의 평면좌표 기록
- 교차되는 상태 Identity 확인
- Depth Axis 부여조건 확인
- Vertical/Diagonal Member 후보 연결
- Truss Closure 역투영

## Output Contract

Joint/Column/Truss Structural Candidate

## Validators

- architectural correspondence is not authorial proof
- joint does not merge members

## Strengths

- 점·선 배열에서 내부지지구조 발견

## Limits

- 역사적 작품설계 동일성은 OPEN

## Compatible Methods

- CAND-006
- CAND-010
- CAND-011
- CAND-028

## Conflicting Methods

- NONE DECLARED

## Substitution Triggers

- 숫자 단계가 핵심이면 CAND-012 병행

## Formation Lineage

- LIVE-E008
- LIVE-E021
