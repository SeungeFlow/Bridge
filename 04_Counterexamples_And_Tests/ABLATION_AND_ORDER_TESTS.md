# Ablation and Order Tests

| Test | 제거/변경 | 결과 | 판정 |
|---|---|---|---|
| `TEST-001` | Identity Lock 제거 | 복수 Hanja 병합 | `FAIL_MERGE` |
| `TEST-002` | Reality Lock 제거 | 전사→Geometry 승격 | `FAIL_PROJECTION` |
| `TEST-003` | Meaning Shielding 제거 | 익숙한 의미가 구조선점 | `ORDER_CONTAMINATION` |
| `TEST-004` | Character View 제거 | Hidden Identity 소실 | `TYPED_RESULT_CHANGED` |
| `TEST-005` | Historical View 제거 | 현대분리 유지 | `THIRD_VIEW_NOT_REQUIRED` |
| `TEST-006` | Formation View 제거 | Full audit 불완전 | `THIRD_VIEW_REQUIRED` |
| `TEST-007` | 독립잠금 전 순서교환 | View 오염 | `ORDER_UNSTABLE` |
| `TEST-008` | 독립잠금 후 순서교환 | Typed Result 유지 | `ORDER_STABLE` |
| `TEST-009` | Conflict 제거 | 허위 완전집합 | `FAIL_ERASURE` |
| `TEST-010` | Partial/Not Met 제거 | 16/16 왜곡 | `FAIL_AUTHORITY_INFLATION` |
| `TEST-011` | View 추가로 Geometry 복원 | Source 생성 안 됨 | `HOLD_SOURCE` |
| `TEST-012` | Next Start 제거 | Relay Closure 불가 | `CLOSURE_OPEN` |
| `TEST-013` | Opposite 규칙 제거 | Center 임의화 | `CENTER_METHOD_GAP` |
| `TEST-014` | Inverse 제거 | Unfold 역검산 불가 | `INVALID_UNFOLDING` |
| `TEST-015` | Local Identity 제거 | τA·τB 병합 | `FAIL_MERGE` |
| `TEST-016` | Translation Surface 대체 | 문화·어휘범위 손실 | `WRONG_LAYER` |
