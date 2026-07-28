# Source-Bound Cases

| Case | 사례 | 입력 | Combination | 상태 |
|---|---|---|---|---|
| `CASE-SB-001` | 현대 철자 기계분해 | 가·나·사·아 / 간·난·산·안 | `RC-001` | `CR-PASS` |
| `CASE-SB-002` | 기계분해와 Lexical Closure | 16 mechanical / 9 complete·4 partial·3 not met | `RC-001→002` | `CR-PASS-SCOPED` |
| `CASE-SB-003` | 같은 음–복수 Hanja | 영: 英·永·榮·迎·映·營 | `RC-002` | `CR-PASS-SCOPED` |
| `CASE-SB-004` | Hanja Usage Correction | 영재·영구히·영광·환영사·방영·영양가 | `RC-002+SC-002` | `CR-PASS-SCOPED` |
| `CASE-SB-005` | 동일 Identity–환경 | 女·年·짓·목·옷 | `RC-003` | `CR-PASS-SCOPED` |
| `CASE-SB-006` | 무종성–유종성 | 20 relations | `RC-003→008` | `CR-PASS-SCOPED` |
| `CASE-SB-007` | ㅇ 계층 비병합 | ㆁ·중세 ㅇ·초성 ㅇ·Ø·종성 ㅇ | `RC-006` | `CR-PASS-SCOPED` |
| `CASE-SB-008` | 역사 Snapshot | 식브→십브→시브/시프→싶다 | `RC-004+008` | `CR-PASS-SCOPED` |
| `CASE-SB-009` | 분기·겹침 | 가리다·하다·짙다·날리다 | `RC-004+008` | `CR-PASS-SCOPED` |
| `CASE-SB-010` | Glyph Geometry Gap | 전사·PUA·Landing Page | `RC-007` | `CR-HOLD-SOURCE` |
