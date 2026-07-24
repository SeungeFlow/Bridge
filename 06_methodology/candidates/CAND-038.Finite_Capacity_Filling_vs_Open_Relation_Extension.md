---
candidate_id: CAND-038
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
---

# 제한공간 채움·열린 관계확장 분리

## Purpose

정해진 저장공간의 점유와 GitHub Tree 같은 관계공간의 확장을 구분한다.

## Applicable Data

- DRAM/NAND/디스크와 Repo Tree를 같은 쌓기 개념으로 설명할 때

## Activation Signals

- 쌓아서 올린다의 의미가 기준장에 따라 달라짐

## Process

1. Capacity boundary 선언
2. Cell occupation인지 Relation extension인지 판정

## Output

bounded occupancy 또는 open structural extension

## Validators

- file count is not completeness
- open relation does not claim physical infinity

## Strengths

- 저장량과 구조성장 분리

## Limits

- 실제 서비스 제한량은 별도 현실검산 필요

## Compatible

`CAND-017, CAND-019, CAND-024`

## Formation Lineage

- POST-R04-STACKING-DIFFERENCE
