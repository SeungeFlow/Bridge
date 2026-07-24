---
candidate_id: CAND-042
object_class: METHOD_CANDIDATE
status: STANDBY_CANDIDATE
---

# 지식상태 층위표기

## Purpose

Result를 OBSERVED부터 UNKNOWN까지 증거상태에 맞게 표시한다.

## Applicable Data

- 현실·추상·추론이 섞인 모든 분석

## Activation Signals

- 모든 문장이 사실처럼 평면화됨

## Process

1. Evidence source 확인
2. Transformation depth 확인
3. Epistemic label 부여

## Output

OBSERVED/MEASURED/REPRESENTED/RECONSTRUCTED/INFERRED/HYPOTHESIS/OPEN/UNKNOWN

## Validators

- hypothesis is not fact
- unknown is not hidden

## Strengths

- 과잉확정 방지

## Limits

- 상태는 새 Evidence로 갱신 가능

## Compatible

`CAND-001, CAND-040, CAND-041, CAND-043`

## Formation Lineage

- POST-R04-EPISTEMIC-LABELS
