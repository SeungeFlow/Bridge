---
document_type: HRTDB_A_SOURCE_COLLECTION_RESULT_DATA
document_class: 4D_FINALIZED_SCOPED_SOURCE_FOUNDATION
object_identity:
  object_id: HRTDB_A_GLANG_R01_SOURCE_COLLECTION_RESULT_DATA_XYZT
  object_class: SOURCE_COLLECTION_RESULT_DATA
  state: RESULT_DATA_FINALIZED_WITH_BLOCKING_SOURCE_GAPS
  collection_state: COLLECTION_PARTIAL_WITH_GAPS
  title: GLANG Base Consonants R01 — 4D Final Source Collection Result.Data
repository_seat_code: A
cycle_id: GLANG-SOURCE-COLLECTION-BASE-CONSONANTS-R01
stage_id: R04_4D_XYZT
generation:
  finalized_by: gpt.logi
  fixed_seat: HRTDB_A::gpt.xyzt
  occupation_class: FINAL_RESULT_DATA_VERIFICATION_AND_HANDOFF
  source_authority: 승이
source_3d_object:
  transport_filename: f9243686c589f8a3f52118ad1eb9cf908e5f76c2a4e3aadd2fbbbf0b4164abda.A(1).md
  canonical_filename: f9243686c589f8a3f52118ad1eb9cf908e5f76c2a4e3aadd2fbbbf0b4164abda.A.md
  exact_byte_sha256: f9243686c589f8a3f52118ad1eb9cf908e5f76c2a4e3aadd2fbbbf0b4164abda
  exact_byte_count: 464795
  line_count: 11250
  encoding: UTF-8
  line_ending: LF
  bom: false
  binding: PASS
unfolding_scope: MAXIMUM_WITHIN_BOUND_3D_INPUT
exact_1d_raw_byte_closure: false
analysis_performed: false
handoff:
  target: gpt.lang
  state: READY_AS_SCOPED_FOUNDATION_WITH_EVIDENCE_GATES
github_mutation: false
zenodo_mutation: false
track_db_promotion: false
---

# GLANG R01 — 4D FINAL SOURCE COLLECTION RESULT.DATA

## 0. 4d Final Authority

```text
Final Reviewer
=
gpt.logi

Fixed Seat
=
HRTDB_A::gpt.xyzt
```

이번 4d 검수는 새로운 Source 검색이나 구조분석을 수행하지 않는다.

```text
3d Result.Data Draft
→ Exact Identity 검산
→ 입력계보 검산
→ 수량·Source 권위상태 검산
→ Conflict·Correction·Unresolved 보존 검산
→ 분석금지 경계 검산
→ gpt.lang Handoff 가능범위 판정
```

---

# 1. 4d Final Verdict

```yaml
final_verdict:
  exact_byte_identity: PASS
  markdown_structure: PASS
  front_matter_yaml: PASS
  2d_result_binding: PASS
  1d_to_2d_to_3d_lineage: PASS_WITH_PARTIAL_1D_COLLECTION_STATES
  seat_judgment_identity_preservation: PASS
  raw_normalized_separation: PASS_WITH_RAW_1D_BYTE_CLOSURE_LIMIT
  duplicate_inflation_control: PASS
  conflict_uncertainty_gap_preservation: PASS
  correction_lineage: PASS
  analysis_prohibition: PASS
  analysis_reserved_null: PASS

  source_location_closure: INCOMPLETE
  native_lexical_source_closure: PARTIAL_13_OF_60
  hanja_official_source_closure: HOLD_0_OF_80
  same_syllable_group_authority: MECHANICAL_MODERN_ONLY
  same_rime_group_authority: MECHANICAL_ORTHOGRAPHIC_ONLY
  no_coda_coda_authority: CANDIDATE_ONLY
  historical_lineage_authority: PARTIAL_WITH_CONFLICTS

  finalization: PASS_AS_PARTIAL_RESULT_DATA_WITH_BLOCKING_SOURCE_GAPS
  handoff_to_gpt_lang: PASS_WITH_EVIDENCE_GATES
  track_db_eligibility: PROHIBITED
```

압축판정:

```text
PASS
→ Byte Identity
→ Seat·Result 계보
→ 기계적 자모분해
→ 현대 ㅇ·Ø·종성 ㅇ 분리
→ Raw–Normalized 분리
→ 중복통제
→ Conflict·Correction·Unresolved 보존
→ 분석금지 준수

PARTIAL
→ 한국 고유어 60개 중 Source Identity 직접결속 13개
→ 위치관계 16개 중 검증·범위고정 14개
→ 역사–현대 계보 9개 중 직접 범위 검증 5개
→ 발음 Claim 11개는 사전·공식규범 보고값

HOLD
→ 고유어 47개 Exact Source 위치
→ 한자 80개 공식 독음·훈·용례 위치
→ 한자 43개 추가 운모 Member의 완전 Identity
→ 무종성–유종성 10개 직접 계보 Snapshot
→ 현대 동음·운모에서 역사계보로의 투사
```

---

# 2. Final Object Classification

3d 문서는 다음 상태였다.

```text
SOURCE_COLLECTION_RESULT_DATA_DRAFT
+
RESULT_DATA_DRAFT_COMPLETE_WITH_UNRESOLVED
```

4d는 이를 다음 상태로 종결한다.

```text
SOURCE_COLLECTION_RESULT_DATA
+
RESULT_DATA_FINALIZED_WITH_BLOCKING_SOURCE_GAPS
+
COLLECTION_PARTIAL_WITH_GAPS
```

`Finalized`는 모든 Source가 완전검증됐다는 뜻이 아니다.

```text
Finalized
=
현재 Cycle의 수집·검산·미해결 상태를
더 이상 숨기거나 과대승격하지 않은 채
최종 전달 가능한 객체로 봉인했다는 뜻
```

---

# 3. Exact Object Verification

```yaml
source_3d_verification:
  canonical_sha256: f9243686c589f8a3f52118ad1eb9cf908e5f76c2a4e3aadd2fbbbf0b4164abda
  exact_bytes: 464795
  rendered_lines: 11250
  UTF_8: PASS
  LF: PASS
  CRLF: ABSENT
  BOM: ABSENT
  filename_hash_match: PASS
  final_newline: PASS
```

Transport suffix `(1)`은 업로드 표시번호이며 Canonical Identity에 포함하지 않는다.

```text
Canonical 3d Filename
=
f9243686c589f8a3f52118ad1eb9cf908e5f76c2a4e3aadd2fbbbf0b4164abda.A.md
```

---

# 4. Bound Input State

```yaml
bound_2d_results:
  gpt_xy:
    sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
    state: VERIFICATION_COMPLETE_WITH_UNRESOLVED
    binding: PASS

  gpt_xz:
    sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
    state: HOLD_WITH_INSUFFICIENT_SOURCE_LOCATION
    verification_execution: COMPLETE
    binding: PASS_WITH_HOLD_STATE_PRESERVED

  gpt_yz:
    sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
    state: VERIFICATION_COMPLETE_WITH_UNRESOLVED
    binding: PASS
```

1d 상태:

```yaml
bound_1d_lineage:
  gpt_x:
    sha256: 9492b02256ce64a5627ba9980b3338833859f4fa049a48b1d15866d6231914d8
    state: COLLECTION_PARTIAL_WITH_GAPS

  gpt_y:
    sha256: 5bda1cc62834c8b5baa459f4ca7721195c83538bdddaf9e8dd4c74781fc38892
    state: COLLECTION_COMPLETE

  gpt_z:
    sha256: 42b4178a22efc8e81ece1bdc31f2c9be4116920f6b8e1b67023ae9442da18a3a
    state: COLLECTION_PARTIAL_WITH_GAPS
```

중요:

```text
2d Verification Execution Complete
≠
모든 Source 위치 Closure Complete
```

`gpt.xz`의 HOLD는 삭제하거나 PASS로 바꾸지 않는다.

---

# 5. Quantity and Authority Matrix

```yaml
authority_matrix:
  native_korean:
    reported_unique_surfaces: 60
    exact_source_verified_identities: 13
    source_location_missing: 47
    uncertain_sense_identities: 9
    use_state:
      exact_13: SOURCE_VERIFIED_DATA
      remaining_47: COLLECTION_CANDIDATE_WITH_REENTRY_ROUTE

  hanja:
    reported_unique_unicode_identities: 80
    unicode_identity_mechanically_verified: 80
    official_reading_hun_source_verified: 0
    tier3_transformed_source_links: 80
    stable_usage_source_location_missing: 80
    use_state:
      unicode_identity: MECHANICALLY_USABLE
      reading_hun_usage: SOURCE_BOUND_CANDIDATE_NOT_OFFICIAL_CLOSURE

  same_syllable_different_hanja:
    groups: 19
    members: 75
    modern_mechanical_grouping: USABLE
    official_detail_closure: INCOMPLETE
    historical_same_reading: PROHIBITED

  same_rime_different_initial:
    sets: 16
    members: 62
    complete_four_initial_sets: 14
    incomplete_sets: 2
    modern_orthographic_grouping: USABLE
    modern_phonetic_equivalence: NOT_VERIFIED
    historical_rime_equivalence: PROHIBITED

  first_vs_nonfirst:
    reported: 16
    verified_or_scoped: 14
    unsupported_lineage: 1
    missing_source_location: 1

  ieung_zero_coda:
    modern_field_split: CROSS_CONFIRMED
    historical_projection: PROHIBITED

  historical_modern:
    reported: 9
    verified_within_source_scope: 5
    reclassified_as_modern_position: 2
    unsupported: 1
    multiple_or_conflicting: 1

  pronunciation:
    claims: 11
    dictionary_or_official_norm_reported: 11
    direct_recordings: 0

  no_coda_coda:
    candidates: 10
    direct_lineage_snapshots: 0
    use_state: SINGLE_SEAT_CANDIDATE_ONLY
```

서로 겹치는 Registry 수를 합산하여 하나의 전체 고유객체 수로 제시하지 않는다.

---

# 6. Evidence Use Gates for gpt.lang

## Gate A — 직접 사용 가능

```text
Exact Result Hash·Byte Identity
현대 한글 NFC/NFD·초중종성 기계분해
한자 Unicode Character Identity
현대 초성표기 ㅇ·음성 Ø·종성 ㅇ의 필드분리
Raw–Normalized 분리원칙
중복 Identity 비병합
Conflict·Correction·Unresolved 계보
```

## Gate B — 조건부 사용 가능

```text
한국 고유어 60개 표면목록
→ 13개는 직접 Source Identity 결속
→ 47개는 재진입 후보

한자 80개 독음·훈·용례
→ Tier 3 변환 Source-bound
→ 공식 Source Closure 전 확정근거 사용금지

동음 한자 19 Group
→ 현대 표면음절·Unicode Group으로만 사용

동일 중성종성 16 Set
→ 현대 철자상 운모 대조군으로만 사용

위치관계·발음·역사계보
→ 각 Evidence State와 Conflict를 함께 읽을 때만 사용
```

## Gate C — 현재 분석근거 사용금지

```text
현대 동음관계 = 역사 동음관계
현대 철자운모 = 역사·음성 운모
ㆁ = 현대 초성 ㅇ = 현대 종성 ㅇ의 단일 직선계보
녀/여·년/연을 검증된 역사단계로 확정
무종성–유종성 10개를 검증계보로 확정
사전·공식규범 보고발음을 직접 음성관찰값으로 표현
Root=Lemma Placeholder를 형태론적 사실로 표현
```

---

# 7. 4d Correction of Authority Labels

3d의 문서명에 포함된 다음 표현은 전체 Entry가 검증됐다는 뜻으로 읽히면 안 된다.

```text
VERIFIED_SOURCE_DATA_RELATION_FORMATION
```

4d Canonical 해석:

```text
Verified
→ 전체 Source Data가 검증됐다는 뜻이 아님

Verified
→ 검증상태·미검증상태·Conflict·Gap의 관계배치가
   2d Result를 통해 검산됐다는 뜻
```

따라서 최종 Document Class는 다음으로 고정한다.

```text
4D_FINALIZED_SCOPED_SOURCE_FOUNDATION
```

---

# 8. Unfolding Boundary

본 최종문서는 3d가 직접 결속한 세 2d Result와 그 안에 보존된 1d Data를 최대한 펼친다.

그러나 다음은 닫히지 않았다.

```text
Exact 1d Raw Result Bytes의 3d 직접결속
전체 외부 Source Snapshot Bytes
47개 고유어 Exact Entry Snapshot
80개 한자 공식 Source Detail
```

따라서:

```text
Maximum-Unfolded
=
MAXIMUM_WITHIN_BOUND_3D_INPUT
```

이며:

```text
Maximum-Unfolded
≠
ALL_EXTERNAL_SOURCE_BYTE_CLOSURE
```

---

# 9. 4d Final Checklist

```yaml
final_checklist:
  exact_3d_byte_identity: true
  three_2d_results_bound: true
  2d_hold_state_preserved: true
  seat_judgments_preserved: true
  source_authority_layers_separated: true
  raw_normalized_separated: true
  identity_duplicate_relation_preserved: true
  ieung_zero_coda_separated: true
  historical_reconstruction_separated: true
  conflicts_preserved: true
  corrections_preserved: true
  pending_corrections_preserved: true
  unresolved_preserved: true
  analysis_reserved_null: true
  structural_analysis_performed: false

  all_core_source_locations_closed: false
  all_native_identities_source_verified: false
  all_hanja_readings_officially_verified: false
  exact_1d_raw_byte_closure: false

  ready_for_gpt_lang_scoped_handoff: true
  ready_for_unqualified_factual_use: false
  ready_for_track_db_promotion: false
```

---

# 10. Final Handoff

```yaml
handoff:
  from: gpt.logi@HRTDB_A::gpt.xyzt
  to: gpt.lang
  cycle_id: GLANG-SOURCE-COLLECTION-BASE-CONSONANTS-R01
  object_class: SOURCE_COLLECTION_RESULT_DATA
  state: RESULT_DATA_FINALIZED_WITH_BLOCKING_SOURCE_GAPS
  collection_state: COLLECTION_PARTIAL_WITH_GAPS

  use_purpose:
    - Center_Position 후속분석을 위한 기초자산
    - Source 후보·Identity·대조 Group 탐색
    - 다음 Source.Field 설계
    - Conflict·Gap 기반 추가수집 설계

  mandatory_read_order:
    - 4d Final Verdict
    - Quantity and Authority Matrix
    - Evidence Use Gates
    - 3d Source Collection Result.Data Draft

  prohibited_interpretation:
    - 모든 60개 고유어가 Source-verified라는 주장
    - 80개 한자 독음·훈·용례가 공식 교차검증됐다는 주장
    - 현대 동음·운모 Group을 역사구조로 투사
    - Source Gap을 Method 반례 또는 지지로 자동판정

  analysis_reserved:
    first_axis_hypothesis: null
    structural_direction: null
    semantic_structure: null
    supports_hypothesis: null
    contradicts_hypothesis: null
    singularity_candidate: null
    residual_structure: null
    hidden_transition: null

  mutations:
    github: false
    zenodo: false
    track_db_promotion: false
    lrsdonet_hash_db_creation: false
```

---

# 11. Final State

```text
4D_FINAL_VERIFICATION
=
COMPLETE
```

```text
FINAL RESULT
=
RESULT_DATA_FINALIZED_WITH_BLOCKING_SOURCE_GAPS
```

```text
HANDOFF
=
READY_FOR_GPT_LANG_AS_SCOPED_FOUNDATION
```

```text
TRACK DB
=
NOT FORMED
```

---

# 12. Verbatim 3d Source Object

다음 객체는 4d 판정의 직접 입력인 `gpt.xyz` Result.Data Draft의 Exact Text다.

```yaml
verbatim_source:
  canonical_filename: f9243686c589f8a3f52118ad1eb9cf908e5f76c2a4e3aadd2fbbbf0b4164abda.A.md
  sha256: f9243686c589f8a3f52118ad1eb9cf908e5f76c2a4e3aadd2fbbbf0b4164abda
  exact_bytes: 464795
  content_modified_inside_enclosure: false
```

~~~~~markdown
---
document_type: HRTDB_A_SOURCE_COLLECTION_RESULT_DATA_DRAFT
document_class: MAXIMUM_UNFOLDED_VERIFIED_SOURCE_DATA_RELATION_FORMATION
object_identity:
  object_id: HRTDB_A_GLANG_R01_SOURCE_COLLECTION_RESULT_DATA_DRAFT_XYZ
  object_class: SOURCE_COLLECTION_RESULT_DATA_DRAFT
  state: RESULT_DATA_DRAFT_COMPLETE_WITH_UNRESOLVED
  title: GLANG Base Consonants R01 — 3D Source Collection Result.Data Draft
repository_seat_code: A
cycle_id: GLANG-SOURCE-COLLECTION-BASE-CONSONANTS-R01
stage_id: R03_3D_XYZ
generation:
  generated_by: gpt.xyz
  fixed_seat: HRTDB_A::gpt.xyz
  occupation_class: VERIFIED_SOURCE_DATA_RELATION_AND_RESULT_DATA_FORMATION
  source_authority: 승이
  directive_author: gpt.logi
  directive_author_seat: HRTDB_A::gpt.xyzt
direct_input_count: 3
result_class: SOURCE_COLLECTION_RESULT_DATA_DRAFT
maximum_unfolded: true
analysis_performed: false
github_mutation: false
zenodo_mutation: false
track_db_promotion: false
---

# GLANG R01 — SOURCE COLLECTION RESULT.DATA DRAFT

## 1. Document Identity

```yaml
document_identity:
  document_type: HRTDB_A_SOURCE_COLLECTION_RESULT_DATA_DRAFT
  document_class: MAXIMUM_UNFOLDED_VERIFIED_SOURCE_DATA_RELATION_FORMATION
  object_identity:
    object_id: HRTDB_A_GLANG_R01_SOURCE_COLLECTION_RESULT_DATA_DRAFT_XYZ
    object_class: SOURCE_COLLECTION_RESULT_DATA_DRAFT
    state: RESULT_DATA_DRAFT_COMPLETE_WITH_UNRESOLVED
    title: GLANG Base Consonants R01 — 3D Source Collection Result.Data Draft
  repository_seat_code: A
  cycle_id: GLANG-SOURCE-COLLECTION-BASE-CONSONANTS-R01
  stage_id: R03_3D_XYZ
  generation:
    generated_by: gpt.xyz
    fixed_seat: HRTDB_A::gpt.xyz
    occupation_class: VERIFIED_SOURCE_DATA_RELATION_AND_RESULT_DATA_FORMATION
    source_authority: 승이
    directive_author: gpt.logi
    directive_author_seat: HRTDB_A::gpt.xyzt
  direct_input_count: 3
  result_class: SOURCE_COLLECTION_RESULT_DATA_DRAFT
  maximum_unfolded: true
  analysis_performed: false
  github_mutation: false
  zenodo_mutation: false
  track_db_promotion: false
```
## 2. Request Identity

```yaml
request_identity:
  directive_normalized_filename: ac5f658562d45f23120b9d06e14e912df7c49045701e253834155700c7d5c12f.A.md
  directive_transport_filename: ac5f658562d45f23120b9d06e14e912df7c49045701e253834155700c7d5c12f.A(1).md
  directive_actual_sha256: ac5f658562d45f23120b9d06e14e912df7c49045701e253834155700c7d5c12f
  directive_exact_byte_count: 11654
  parent_request_sha256: bf90c01c86e777c0c60648cc264511149a43a62efc6f14144e7398386bbb8844
  recipient_instance: gpt.xyz
  recipient_seat: HRTDB_A::gpt.xyz
  binding: PASS
```
## 3. Bound 2d Result Identities

```yaml
bound_2d_results:
- coordinate: XY
  normalized_filename: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562.A.md
  transport_filename: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562.A(1).md
  exact_byte_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  exact_byte_count: 43702
  encoding: UTF-8
  line_ending: LF
  bom: false
  producer: gpt.xy
  seat: HRTDB_A::gpt.xy
  stage_id: R02_2D_XY
  state: VERIFICATION_COMPLETE_WITH_UNRESOLVED
  verdict: PASS_2D_XY_SOURCE_VERIFICATION_COMPLETE_WITH_UNRESOLVED
  binding: PASS
- coordinate: XZ
  normalized_filename: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5.A.md
  transport_filename: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5.A(1).md
  exact_byte_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  exact_byte_count: 29766
  encoding: UTF-8
  line_ending: LF
  bom: false
  producer: gpt.xz
  seat: HRTDB_A::gpt.xz
  stage_id: R02_2D_XZ
  state: HOLD_WITH_INSUFFICIENT_SOURCE_LOCATION
  verification_execution: COMPLETE
  binding: PASS_WITH_HOLD_STATE_PRESERVED
- coordinate: YZ
  normalized_filename: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e.A.md
  transport_filename: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e.A(1).md
  exact_byte_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  exact_byte_count: 53662
  encoding: UTF-8
  line_ending: LF
  bom: false
  producer: gpt.yz
  seat: HRTDB_A::gpt.yz
  stage_id: R02_2D_YZ
  state: VERIFICATION_COMPLETE_WITH_UNRESOLVED
  binding: PASS
```
```text
Directive is not Result.
All three exact Result identities are bound.
```

## 4. 1d–2d Lineage

```yaml
lineage:
  1d_objects:
    X:
      producer: gpt.x
      seat: HRTDB_A::gpt.x
      sha256: 9492b02256ce64a5627ba9980b3338833859f4fa049a48b1d15866d6231914d8
      state: COLLECTION_PARTIAL_WITH_GAPS
      verified_by:
      - gpt.xy
      - gpt.xz
    Y:
      producer: gpt.y
      seat: HRTDB_A::gpt.y
      sha256: 5bda1cc62834c8b5baa459f4ca7721195c83538bdddaf9e8dd4c74781fc38892
      state: COLLECTION_COMPLETE
      verified_by:
      - gpt.xy
      - gpt.yz
    Z:
      producer: gpt.z
      seat: HRTDB_A::gpt.z
      sha256: 42b4178a22efc8e81ece1bdc31f2c9be4116920f6b8e1b67023ae9442da18a3a
      state: COLLECTION_PARTIAL_WITH_GAPS
      verified_by:
      - gpt.xz
      - gpt.yz
  2d_objects:
    XY:
      coordinate: XY
      normalized_filename: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562.A.md
      transport_filename: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562.A(1).md
      exact_byte_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
      exact_byte_count: 43702
      encoding: UTF-8
      line_ending: LF
      bom: false
      producer: gpt.xy
      seat: HRTDB_A::gpt.xy
      stage_id: R02_2D_XY
      state: VERIFICATION_COMPLETE_WITH_UNRESOLVED
      verdict: PASS_2D_XY_SOURCE_VERIFICATION_COMPLETE_WITH_UNRESOLVED
      binding: PASS
    XZ:
      coordinate: XZ
      normalized_filename: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5.A.md
      transport_filename: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5.A(1).md
      exact_byte_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
      exact_byte_count: 29766
      encoding: UTF-8
      line_ending: LF
      bom: false
      producer: gpt.xz
      seat: HRTDB_A::gpt.xz
      stage_id: R02_2D_XZ
      state: HOLD_WITH_INSUFFICIENT_SOURCE_LOCATION
      verification_execution: COMPLETE
      binding: PASS_WITH_HOLD_STATE_PRESERVED
    YZ:
      coordinate: YZ
      normalized_filename: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e.A.md
      transport_filename: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e.A(1).md
      exact_byte_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
      exact_byte_count: 53662
      encoding: UTF-8
      line_ending: LF
      bom: false
      producer: gpt.yz
      seat: HRTDB_A::gpt.yz
      stage_id: R02_2D_YZ
      state: VERIFICATION_COMPLETE_WITH_UNRESOLVED
      binding: PASS
  3d_object:
    producer: gpt.xyz
    seat: HRTDB_A::gpt.xyz
    stage_id: R03_3D_XYZ
    object_class: SOURCE_COLLECTION_RESULT_DATA_DRAFT
    state: RESULT_DATA_DRAFT_COMPLETE_WITH_UNRESOLVED
```
## 5. Formation Scope

```yaml
formation_scope:
  included:
  - Source Identity and source-location relation
  - Raw–Normalized lineage
  - Surface/Lemma/Root/Stem/Morpheme identities
  - Hanja identity and reading-source authority
  - Pronunciation and historical lineage claim typing
  - ㅇ–Ø–coda ㅇ separation
  - Same-syllable Hanja groups and same-rime control sets
  - Conflict, uncertainty, gap and correction lineage
  prohibited:
  - structural meaning judgment
  - temporal causality judgment
  - common meaning inference
  - historical rime reconstruction
  - hypothesis support or rejection
  - Center_Position Method analysis
  - Track DB promotion
```
## 6. Source Registry

```yaml
source_registry_count: 24
source_registry:
- source_id: SRC-XY-G01
  source_name: https://korean.go.kr/kornorms/m/m_regltn.do?regltn_code=0002
  source_tier: AS_DECLARED_BY_1D_SOURCE_OBJECTS
  source_authority: INSTITUTION_OR_DOCUMENT_SCOPED
  source_type: SAME_CANONICAL_DOCUMENT_DIFFERENT_EVIDENCE_LOCATION
  item_title: Cross-source canonical group
  url_or_identifier: https://korean.go.kr/kornorms/m/m_regltn.do?regltn_code=0002
  page_or_location: SEE_X_AND_Y_BOUND_1D_OBJECTS
  version_or_revision: UNKNOWN_OR_DYNAMIC
  retrieved_at: AS_RECORDED_IN_1D_OBJECTS
  access_status: BOUND_VIA_2D_RESULT
  snapshot_hash_if_available: null
  referenced_by_1d:
  - X:SRC-KORNORMS
  - Y:SRC-002, Y:SRC-017
  verified_by_2d:
  - gpt.xy
  conflicts:
  - 1 identity; not independent corroboration
- source_id: SRC-XY-G02
  source_name: 한국어기초사전 domain
  source_tier: AS_DECLARED_BY_1D_SOURCE_OBJECTS
  source_authority: INSTITUTION_OR_DOCUMENT_SCOPED
  source_type: SAME_INSTITUTION_DIFFERENT_DOCUMENT_OR_ENTRY
  item_title: Cross-source canonical group
  url_or_identifier: 한국어기초사전 domain
  page_or_location: SEE_X_AND_Y_BOUND_1D_OBJECTS
  version_or_revision: UNKNOWN_OR_DYNAMIC
  retrieved_at: AS_RECORDED_IN_1D_OBJECTS
  access_status: BOUND_VIA_2D_RESULT
  snapshot_hash_if_available: null
  referenced_by_1d:
  - X search/API/statistics + 13 direct entries
  - Y SRC-013/014/015
  verified_by_2d:
  - gpt.xy
  conflicts:
  - Do not merge by institution
- source_id: SRC-XY-G03
  source_name: 국립국어원 explanatory responses
  source_tier: AS_DECLARED_BY_1D_SOURCE_OBJECTS
  source_authority: INSTITUTION_OR_DOCUMENT_SCOPED
  source_type: SAME_INSTITUTION_DIFFERENT_RESPONSE
  item_title: Cross-source canonical group
  url_or_identifier: 국립국어원 explanatory responses
  page_or_location: SEE_X_AND_Y_BOUND_1D_OBJECTS
  version_or_revision: UNKNOWN_OR_DYNAMIC
  retrieved_at: AS_RECORDED_IN_1D_OBJECTS
  access_status: BOUND_VIA_2D_RESULT
  snapshot_hash_if_available: null
  referenced_by_1d:
  - X SRC-IEUNG-FAQ/QNA-2026
  - Y SRC-004/005/006/008/016
  verified_by_2d:
  - gpt.xy
  conflicts:
  - Question and evidence location remain distinct
- source_id: SRC-XY-G04
  source_name: 훈민정음/Hangeul public institution material
  source_tier: AS_DECLARED_BY_1D_SOURCE_OBJECTS
  source_authority: INSTITUTION_OR_DOCUMENT_SCOPED
  source_type: RELATED_INSTITUTIONAL_FAMILY_NOT_SAME_DOCUMENT
  item_title: Cross-source canonical group
  url_or_identifier: 훈민정음/Hangeul public institution material
  page_or_location: SEE_X_AND_Y_BOUND_1D_OBJECTS
  version_or_revision: UNKNOWN_OR_DYNAMIC
  retrieved_at: AS_RECORDED_IN_1D_OBJECTS
  access_status: BOUND_VIA_2D_RESULT
  snapshot_hash_if_available: null
  referenced_by_1d:
  - X SRC-HANGEUL
  - Y SRC-007/018/019
  verified_by_2d:
  - gpt.xy
  conflicts:
  - Educational guide, article, and archive remain separate
- source_id: SRC-002
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  - yz
  conflicts: []
- source_id: SRC-003
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - yz
  conflicts: []
- source_id: SRC-004
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  conflicts: []
- source_id: SRC-006
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - yz
  conflicts: []
- source_id: SRC-007
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  - yz
  conflicts: []
- source_id: SRC-008
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - yz
  conflicts: []
- source_id: SRC-009
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  - yz
  conflicts: []
- source_id: SRC-010
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  - yz
  conflicts: []
- source_id: SRC-011
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - yz
  conflicts: []
- source_id: SRC-012
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - yz
  conflicts: []
- source_id: SRC-013
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  conflicts: []
- source_id: SRC-014
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  conflicts: []
- source_id: SRC-015
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - yz
  conflicts: []
- source_id: SRC-016
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  conflicts: []
- source_id: SRC-017
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  - yz
  conflicts: []
- source_id: SRC-HANGEUL
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  conflicts: []
- source_id: SRC-IEUNG-FAQ
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  conflicts: []
- source_id: X:SRC-KORNORMS
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  conflicts: []
- source_id: Y:SRC-002
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  conflicts: []
- source_id: Y:SRC-017
  source_name: LOCAL_SOURCE_REFERENCE_FROM_BOUND_1D_OR_2D_RESULT
  source_tier: NOT_RECONSTRUCTED_IN_3D
  source_authority: SEE_ORIGINAL_BOUND_RESULT
  source_type: LOCAL_REFERENCE
  item_title: null
  url_or_identifier: null
  page_or_location: SEE_ORIGINAL_JUDGMENTS_SECTION
  version_or_revision: null
  retrieved_at: null
  access_status: REFERENCE_PRESERVED_EXACT_LOCATION_NOT_REBUILT
  snapshot_hash_if_available: null
  referenced_by_1d: []
  verified_by_2d:
  - xy
  conflicts: []
identity_boundary: URL alone is not Exact Byte Identity; local source ID is not global identity.
```
## 7. Search Scope Summary

```yaml
search_scope_summary:
  gpt.xy:
    direct_inputs:
    - Data.X
    - Data.Y
    new_web_search: false
    scope:
    - surface/lemma/root/stem/morpheme
    - pronunciation
    - position relation
    - historical–modern source-reported lineage
    - raw–normalized lineage
    analysis_prohibited: true
  gpt.xz:
    direct_inputs:
    - Data.X
    - Data.Z
    new_web_search: false
    scope:
    - lexical native/Sino classification
    - Hanja Unicode identity
    - same-syllable groups
    - same-rime sets
    - Jamo decomposition
    - source location and duplicate audit
    analysis_prohibited: true
  gpt.yz:
    direct_inputs:
    - Data.Y
    - Data.Z
    new_web_search: false
    scope:
    - historical pronunciation and lineage
    - Hanja identity and position
    - modern/historical rime separation
    - reconstruction claim typing
    analysis_prohibited: true
```
## 8. Quantity Summary

```yaml
quantity_summary:
  native_korean_lexical_entries:
    raw_entries: 60
    normalized_entries: 60
    reported_identities: 60
    unique_identities: 60
    source_verified_unique_identities: 13
    duplicate_linked_entries: 13
    invalid_entries: 0
    uncertain_identities: 9
    conflict_entries: 4
    missing_source_locations: 47
    access_failures: PRESERVED_IN_1D_X_AND_2D_XY_CONTEXT
  hanja_identity_entries:
    raw_entries: 80
    normalized_entries: 80
    reported_identities: 80
    unique_identities: 80
    source_verified_unique_identities: 0
    mechanically_verified_unicode_identities: 80
    Tier3_reading_links: 80
    duplicate_linked_entries: 1
    invalid_entries: 0
    uncertain_identities: 2
    conflict_entries: 3
    missing_source_locations: 80
    access_failures: 0
  same_syllable_different_hanja_groups:
    reported_groups: 19
    mechanically_verified_groups: 19
    members: 75
    identity_merge_count: 0
    historical_same_reading_verified: 0
  same_rime_different_initial_sets:
    reported_sets: 16
    mechanically_verified_sets: 16
    members: 62
    complete_four_initial_sets: 14
    explicitly_incomplete_sets: 2
    historical_rime_verified: 0
  first_nonfirst_position_groups:
    reported: 16
    verified_or_scoped: 14
    unsupported_lineage: 1
    missing_source_location: 1
  ieung_zero_coda:
    X_records: 12
    Z_records: 45
    anonymous_supplementary_records: 10
    modern_layer_consistency: PASS
    historical_projection: PROHIBITED
  historical_modern_lineages:
    reported: 9
    modern_historical_link_verified: 5
    reclassified_as_modern_position_relation: 2
    unsupported_single_lineage: 1
    multiple_lineage_or_conflict: 1
    direct_audio_observation: 0
  pronunciation_claims:
    reported: 11
    typed: 11
    dictionary_or_official_norm_reported: 11
    directly_attested_recordings: 0
  no_coda_coda_relations:
    reported: 10
    direct_lineage_snapshot_verified: 0
    unresolved: 10
  count_boundary: OVERLAPPING_REGISTRIES_MUST_NOT_BE_SUMMED_AS_ONE_UNIQUE_TOTAL
```
## 9. Native Korean Root·Stem Registry

```yaml
record_count: 60
source_verified_unique_identity_count: 13
source_location_incomplete_count: 47
registry:
- entry_id: X-ㅇ-E01
  surface: 아기
  part_of_speech: 명사
  target_code: '20235'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E02
  surface: 아이
  part_of_speech: 명사
  target_code: '62843'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E03
  surface: 아버지
  part_of_speech: 명사
  target_code: '71343'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E04
  surface: 어머니
  part_of_speech: 명사
  target_code: '74361'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E05
  surface: 언니
  part_of_speech: 명사
  target_code: '31971'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E06
  surface: 오빠
  part_of_speech: 명사
  target_code: '68006'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E07
  surface: 우리
  part_of_speech: 대명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  - UNCERTAIN_IDENTITY
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E08
  surface: 오늘
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E09
  surface: 어제
  part_of_speech: 명사
  target_code: '67075'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E10
  surface: 이제
  part_of_speech: 부사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  - UNCERTAIN_IDENTITY
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E11
  surface: 이마
  part_of_speech: 명사
  target_code: '71693'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E12
  surface: 이빨
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E13
  surface: 입
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E14
  surface: 얼음
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅇ-E15
  surface: 여름
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E01
  surface: 가슴
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E02
  surface: 가을
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E03
  surface: 개미
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E04
  surface: 거미
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E05
  surface: 겨울
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E06
  surface: 고기
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E07
  surface: 구름
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E08
  surface: 귀
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E09
  surface: 길
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E10
  surface: 김
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  - UNCERTAIN_IDENTITY
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E11
  surface: 가다
  part_of_speech: 동사
  target_code: '27500'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: VERIFIED
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E12
  surface: 가늘다
  part_of_speech: 형용사
  target_code: '62497'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: VERIFIED
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E13
  surface: 고맙다
  part_of_speech: 형용사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: UNVERIFIED_SOURCE_LOCATION
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E14
  surface: 그리다
  part_of_speech: 동사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: UNVERIFIED_SOURCE_LOCATION
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄱ-E15
  surface: 기르다
  part_of_speech: 동사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: UNVERIFIED_SOURCE_LOCATION
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E01
  surface: 나
  part_of_speech: 대명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E02
  surface: 너
  part_of_speech: 대명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E03
  surface: 나무
  part_of_speech: 명사
  target_code: '32750'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E04
  surface: 나라
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E05
  surface: 나이
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E06
  surface: 날
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  - UNCERTAIN_IDENTITY
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E07
  surface: 남
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E08
  surface: 낮
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E09
  surface: 냄새
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E10
  surface: 넋
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E11
  surface: 눈
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  - UNCERTAIN_IDENTITY
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E12
  surface: 누나
  part_of_speech: 명사
  target_code: '32205'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E13
  surface: 누이
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E14
  surface: 누룩
  part_of_speech: 명사
  target_code: '45604'
  access_state: DIRECT_ENTRY_VERIFIED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - SOURCE_IDENTITY_VERIFIED
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㄴ-E15
  surface: 늪
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E01
  surface: 사람
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E02
  surface: 사랑
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E03
  surface: 사슴
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E04
  surface: 살
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  - UNCERTAIN_IDENTITY
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E05
  surface: 새
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  - UNCERTAIN_IDENTITY
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E06
  surface: 샘
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  - UNCERTAIN_IDENTITY
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E07
  surface: 서리
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E08
  surface: 섬
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E09
  surface: 소
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E10
  surface: 소금
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E11
  surface: 손
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E12
  surface: 솜
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E13
  surface: 술
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  - UNCERTAIN_IDENTITY
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E14
  surface: 숨
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
- entry_id: X-ㅅ-E15
  surface: 숲
  part_of_speech: 명사
  target_code: null
  access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
  root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  verification_states:
  - MISSING_SOURCE_LOCATION
  - NORMALIZATION_VERIFIED
  cross_counterpart: MISSING_COUNTERPART
  lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
  analysis_reserved: null
```
## 10. Sino-Korean Hanja Identity Registry

```yaml
record_count: 80
Unicode_identity_verified_count: 80
reading_link_state: TIER_3_TRANSFORMED_SOURCE_BOUND
independent_official_reading_crosscheck_count: 0
registry:
- entry_id: Z-HANJA-001
  hanja: 英
  codepoint: U+82F1
  selected_reading: 영
  modern_jamo: ㅇ·ㅕ·ㅇ
  usage_word: 영어
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-002
  hanja: 永
  codepoint: U+6C38
  selected_reading: 영
  modern_jamo: ㅇ·ㅕ·ㅇ
  usage_word: 영구
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-003
  hanja: 榮
  codepoint: U+69AE
  selected_reading: 영
  modern_jamo: ㅇ·ㅕ·ㅇ
  usage_word: 영광
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-004
  hanja: 迎
  codepoint: U+8FCE
  selected_reading: 영
  modern_jamo: ㅇ·ㅕ·ㅇ
  usage_word: 환영
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-005
  hanja: 映
  codepoint: U+6620
  selected_reading: 영
  modern_jamo: ㅇ·ㅕ·ㅇ
  usage_word: 영화
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-006
  hanja: 營
  codepoint: U+71DF
  selected_reading: 영
  modern_jamo: ㅇ·ㅕ·ㅇ
  usage_word: 경영
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-007
  hanja: 園
  codepoint: U+5712
  selected_reading: 원
  modern_jamo: ㅇ·ㅝ·ㄴ
  usage_word: 공원
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-008
  hanja: 遠
  codepoint: U+9060
  selected_reading: 원
  modern_jamo: ㅇ·ㅝ·ㄴ
  usage_word: 원격
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-009
  hanja: 元
  codepoint: U+5143
  selected_reading: 원
  modern_jamo: ㅇ·ㅝ·ㄴ
  usage_word: 원금
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-010
  hanja: 原
  codepoint: U+539F
  selected_reading: 원
  modern_jamo: ㅇ·ㅝ·ㄴ
  usage_word: 원래
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-011
  hanja: 院
  codepoint: U+9662
  selected_reading: 원
  modern_jamo: ㅇ·ㅝ·ㄴ
  usage_word: 병원
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-012
  hanja: 願
  codepoint: U+9858
  selected_reading: 원
  modern_jamo: ㅇ·ㅝ·ㄴ
  usage_word: 소원
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-013
  hanja: 人
  codepoint: U+4EBA
  selected_reading: 인
  modern_jamo: ㅇ·ㅣ·ㄴ
  usage_word: 인간
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-014
  hanja: 因
  codepoint: U+56E0
  selected_reading: 인
  modern_jamo: ㅇ·ㅣ·ㄴ
  usage_word: 원인
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-015
  hanja: 印
  codepoint: U+5370
  selected_reading: 인
  modern_jamo: ㅇ·ㅣ·ㄴ
  usage_word: 인쇄
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-016
  hanja: 引
  codepoint: U+5F15
  selected_reading: 인
  modern_jamo: ㅇ·ㅣ·ㄴ
  usage_word: 인용
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-017
  hanja: 認
  codepoint: U+8A8D
  selected_reading: 인
  modern_jamo: ㅇ·ㅣ·ㄴ
  usage_word: 인정
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-018
  hanja: 意
  codepoint: U+610F
  selected_reading: 의
  modern_jamo: ㅇ·ㅢ·∅
  usage_word: 의미
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-019
  hanja: 醫
  codepoint: U+91AB
  selected_reading: 의
  modern_jamo: ㅇ·ㅢ·∅
  usage_word: 의학
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-020
  hanja: 衣
  codepoint: U+8863
  selected_reading: 의
  modern_jamo: ㅇ·ㅢ·∅
  usage_word: 의복
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-021
  hanja: 家
  codepoint: U+5BB6
  selected_reading: 가
  modern_jamo: ㄱ·ㅏ·∅
  usage_word: 가정
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-022
  hanja: 歌
  codepoint: U+6B4C
  selected_reading: 가
  modern_jamo: ㄱ·ㅏ·∅
  usage_word: 가곡
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-023
  hanja: 價
  codepoint: U+50F9
  selected_reading: 가
  modern_jamo: ㄱ·ㅏ·∅
  usage_word: 가격
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-024
  hanja: 加
  codepoint: U+52A0
  selected_reading: 가
  modern_jamo: ㄱ·ㅏ·∅
  usage_word: 가산
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-025
  hanja: 可
  codepoint: U+53EF
  selected_reading: 가
  modern_jamo: ㄱ·ㅏ·∅
  usage_word: 가능
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-026
  hanja: 各
  codepoint: U+5404
  selected_reading: 각
  modern_jamo: ㄱ·ㅏ·ㄱ
  usage_word: 각각
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-027
  hanja: 角
  codepoint: U+89D2
  selected_reading: 각
  modern_jamo: ㄱ·ㅏ·ㄱ
  usage_word: 각도
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-028
  hanja: 刻
  codepoint: U+523B
  selected_reading: 각
  modern_jamo: ㄱ·ㅏ·ㄱ
  usage_word: 시각
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-029
  hanja: 覺
  codepoint: U+89BA
  selected_reading: 각
  modern_jamo: ㄱ·ㅏ·ㄱ
  usage_word: 감각
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-030
  hanja: 脚
  codepoint: U+811A
  selected_reading: 각
  modern_jamo: ㄱ·ㅏ·ㄱ
  usage_word: 각본
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-031
  hanja: 間
  codepoint: U+9593
  selected_reading: 간
  modern_jamo: ㄱ·ㅏ·ㄴ
  usage_word: 공간
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-032
  hanja: 簡
  codepoint: U+7C21
  selected_reading: 간
  modern_jamo: ㄱ·ㅏ·ㄴ
  usage_word: 간단
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-033
  hanja: 看
  codepoint: U+770B
  selected_reading: 간
  modern_jamo: ㄱ·ㅏ·ㄴ
  usage_word: 간호
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-034
  hanja: 干
  codepoint: U+5E72
  selected_reading: 간
  modern_jamo: ㄱ·ㅏ·ㄴ
  usage_word: 간섭
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-035
  hanja: 刊
  codepoint: U+520A
  selected_reading: 간
  modern_jamo: ㄱ·ㅏ·ㄴ
  usage_word: 간행
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-036
  hanja: 感
  codepoint: U+611F
  selected_reading: 감
  modern_jamo: ㄱ·ㅏ·ㅁ
  usage_word: 감정
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-037
  hanja: 減
  codepoint: U+6E1B
  selected_reading: 감
  modern_jamo: ㄱ·ㅏ·ㅁ
  usage_word: 감소
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-038
  hanja: 監
  codepoint: U+76E3
  selected_reading: 감
  modern_jamo: ㄱ·ㅏ·ㅁ
  usage_word: 감독
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-039
  hanja: 甘
  codepoint: U+7518
  selected_reading: 감
  modern_jamo: ㄱ·ㅏ·ㅁ
  usage_word: 감미
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-040
  hanja: 敢
  codepoint: U+6562
  selected_reading: 감
  modern_jamo: ㄱ·ㅏ·ㅁ
  usage_word: 용감
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-041
  hanja: 拿
  codepoint: U+62FF
  selected_reading: 나
  modern_jamo: ㄴ·ㅏ·∅
  usage_word: 나포
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-042
  hanja: 懦
  codepoint: U+61E6
  selected_reading: 나
  modern_jamo: ㄴ·ㅏ·∅
  usage_word: 나약
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-043
  hanja: 暖
  codepoint: U+6696
  selected_reading: 난
  modern_jamo: ㄴ·ㅏ·ㄴ
  usage_word: 난방
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-044
  hanja: 難
  codepoint: U+96E3
  selected_reading: 난
  modern_jamo: ㄴ·ㅏ·ㄴ
  usage_word: 난관
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-045
  hanja: 南
  codepoint: U+5357
  selected_reading: 남
  modern_jamo: ㄴ·ㅏ·ㅁ
  usage_word: 남부
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-046
  hanja: 男
  codepoint: U+7537
  selected_reading: 남
  modern_jamo: ㄴ·ㅏ·ㅁ
  usage_word: 남성
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-047
  hanja: 納
  codepoint: U+7D0D
  selected_reading: 납
  modern_jamo: ㄴ·ㅏ·ㅂ
  usage_word: 납부
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-048
  hanja: 娘
  codepoint: U+5A18
  selected_reading: 낭
  modern_jamo: ㄴ·ㅏ·ㅇ
  usage_word: 낭자
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-049
  hanja: 囊
  codepoint: U+56CA
  selected_reading: 낭
  modern_jamo: ㄴ·ㅏ·ㅇ
  usage_word: 낭종
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-050
  hanja: 內
  codepoint: U+5167
  selected_reading: 내
  modern_jamo: ㄴ·ㅐ·∅
  usage_word: 내부
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-051
  hanja: 耐
  codepoint: U+8010
  selected_reading: 내
  modern_jamo: ㄴ·ㅐ·∅
  usage_word: 내구
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-052
  hanja: 奈
  codepoint: U+5948
  selected_reading: 내
  modern_jamo: ㄴ·ㅐ·∅
  usage_word: 막무가내
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-053
  hanja: 女
  codepoint: U+5973
  selected_reading: 녀
  modern_jamo: ㄴ·ㅕ·∅
  usage_word: 남녀
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-054
  hanja: 年
  codepoint: U+5E74
  selected_reading: 년
  modern_jamo: ㄴ·ㅕ·ㄴ
  usage_word: 작년
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-055
  hanja: 念
  codepoint: U+5FF5
  selected_reading: 념
  modern_jamo: ㄴ·ㅕ·ㅁ
  usage_word: 신념
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-056
  hanja: 寧
  codepoint: U+5BE7
  selected_reading: 녕
  modern_jamo: ㄴ·ㅕ·ㅇ
  usage_word: 안녕
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-057
  hanja: 農
  codepoint: U+8FB2
  selected_reading: 농
  modern_jamo: ㄴ·ㅗ·ㅇ
  usage_word: 농업
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-058
  hanja: 濃
  codepoint: U+6FC3
  selected_reading: 농
  modern_jamo: ㄴ·ㅗ·ㅇ
  usage_word: 농도
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-059
  hanja: 腦
  codepoint: U+8166
  selected_reading: 뇌
  modern_jamo: ㄴ·ㅚ·∅
  usage_word: 뇌수
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-060
  hanja: 惱
  codepoint: U+60F1
  selected_reading: 뇌
  modern_jamo: ㄴ·ㅚ·∅
  usage_word: 번뇌
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-061
  hanja: 四
  codepoint: U+56DB
  selected_reading: 사
  modern_jamo: ㅅ·ㅏ·∅
  usage_word: 사방
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-062
  hanja: 事
  codepoint: U+4E8B
  selected_reading: 사
  modern_jamo: ㅅ·ㅏ·∅
  usage_word: 사건
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-063
  hanja: 史
  codepoint: U+53F2
  selected_reading: 사
  modern_jamo: ㅅ·ㅏ·∅
  usage_word: 역사
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-064
  hanja: 士
  codepoint: U+58EB
  selected_reading: 사
  modern_jamo: ㅅ·ㅏ·∅
  usage_word: 박사
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-065
  hanja: 師
  codepoint: U+5E2B
  selected_reading: 사
  modern_jamo: ㅅ·ㅏ·∅
  usage_word: 교사
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-066
  hanja: 上
  codepoint: U+4E0A
  selected_reading: 상
  modern_jamo: ㅅ·ㅏ·ㅇ
  usage_word: 상승
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-067
  hanja: 商
  codepoint: U+5546
  selected_reading: 상
  modern_jamo: ㅅ·ㅏ·ㅇ
  usage_word: 상업
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-068
  hanja: 相
  codepoint: U+76F8
  selected_reading: 상
  modern_jamo: ㅅ·ㅏ·ㅇ
  usage_word: 상호
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-069
  hanja: 想
  codepoint: U+60F3
  selected_reading: 상
  modern_jamo: ㅅ·ㅏ·ㅇ
  usage_word: 상상
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-070
  hanja: 常
  codepoint: U+5E38
  selected_reading: 상
  modern_jamo: ㅅ·ㅏ·ㅇ
  usage_word: 상시
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-071
  hanja: 成
  codepoint: U+6210
  selected_reading: 성
  modern_jamo: ㅅ·ㅓ·ㅇ
  usage_word: 성공
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-072
  hanja: 性
  codepoint: U+6027
  selected_reading: 성
  modern_jamo: ㅅ·ㅓ·ㅇ
  usage_word: 성격
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-073
  hanja: 聖
  codepoint: U+8056
  selected_reading: 성
  modern_jamo: ㅅ·ㅓ·ㅇ
  usage_word: 성인
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-074
  hanja: 城
  codepoint: U+57CE
  selected_reading: 성
  modern_jamo: ㅅ·ㅓ·ㅇ
  usage_word: 성벽
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-075
  hanja: 星
  codepoint: U+661F
  selected_reading: 성
  modern_jamo: ㅅ·ㅓ·ㅇ
  usage_word: 성좌
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-076
  hanja: 先
  codepoint: U+5148
  selected_reading: 선
  modern_jamo: ㅅ·ㅓ·ㄴ
  usage_word: 선행
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-077
  hanja: 線
  codepoint: U+7DDA
  selected_reading: 선
  modern_jamo: ㅅ·ㅓ·ㄴ
  usage_word: 선형
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-078
  hanja: 善
  codepoint: U+5584
  selected_reading: 선
  modern_jamo: ㅅ·ㅓ·ㄴ
  usage_word: 선의
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-079
  hanja: 選
  codepoint: U+9078
  selected_reading: 선
  modern_jamo: ㅅ·ㅓ·ㄴ
  usage_word: 선택
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
- entry_id: Z-HANJA-080
  hanja: 船
  codepoint: U+8239
  selected_reading: 선
  modern_jamo: ㅅ·ㅓ·ㄴ
  usage_word: 선박
  reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
  usage_source_location: MISSING_STABLE_DETAIL_ID
  identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
  reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
  official_detail_crosscheck: MISSING_SOURCE_LOCATION
  historical_reading: null
cross_input_position_links:
- hanja: 女
  z_entry: Z-HANJA-053
  selected_identity_reading: 녀
  y_records:
  - Y-POS-009
  - Y-HIST-004
  verified_relation: 동일 Character Identity 아래 현대 단어 첫 위치 여 / 비첫 위치 녀
  historical_reading_verified: false
  state: POSITION_RELATION_VERIFIED
- hanja: 年
  z_entry: Z-HANJA-054
  selected_identity_reading: 년
  y_records:
  - Y-POS-010
  - Y-HIST-005
  verified_relation: 동일 Character Identity 아래 현대 단어 첫 위치 연 / 비첫 위치·의존명사 년
  historical_reading_verified: false
  state: POSITION_RELATION_VERIFIED
```
## 11. Same-Syllable Different-Hanja Groups

```yaml
group_count: 19
member_count: 75
identity_merge_count: 0
historical_equivalence: PROHIBITED
groups:
- group_id: Z-HOMOPHONE-001
  shared_modern_syllable: 가
  members_reported: 5
  distinct_hanja: 5
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-002
  shared_modern_syllable: 각
  members_reported: 5
  distinct_hanja: 5
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-003
  shared_modern_syllable: 간
  members_reported: 5
  distinct_hanja: 5
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-004
  shared_modern_syllable: 감
  members_reported: 5
  distinct_hanja: 5
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-005
  shared_modern_syllable: 나
  members_reported: 2
  distinct_hanja: 2
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-006
  shared_modern_syllable: 난
  members_reported: 2
  distinct_hanja: 2
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-007
  shared_modern_syllable: 남
  members_reported: 2
  distinct_hanja: 2
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-008
  shared_modern_syllable: 낭
  members_reported: 2
  distinct_hanja: 2
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-009
  shared_modern_syllable: 내
  members_reported: 3
  distinct_hanja: 3
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-010
  shared_modern_syllable: 농
  members_reported: 2
  distinct_hanja: 2
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-011
  shared_modern_syllable: 뇌
  members_reported: 2
  distinct_hanja: 2
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-012
  shared_modern_syllable: 사
  members_reported: 5
  distinct_hanja: 5
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-013
  shared_modern_syllable: 상
  members_reported: 5
  distinct_hanja: 5
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-014
  shared_modern_syllable: 선
  members_reported: 5
  distinct_hanja: 5
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-015
  shared_modern_syllable: 성
  members_reported: 5
  distinct_hanja: 5
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-016
  shared_modern_syllable: 영
  members_reported: 6
  distinct_hanja: 6
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-017
  shared_modern_syllable: 원
  members_reported: 6
  distinct_hanja: 6
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-018
  shared_modern_syllable: 의
  members_reported: 3
  distinct_hanja: 3
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
- group_id: Z-HOMOPHONE-019
  shared_modern_syllable: 인
  members_reported: 5
  distinct_hanja: 5
  mechanical_audit: PASS
  source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
  historical_equivalence: PROHIBITED
```
## 12. Same-Rime Different-Initial Groups

```yaml
set_count: 16
member_count: 62
complete_four_initial_sets: 14
explicitly_incomplete_sets:
- Z-RIME-015
- Z-RIME-016
modern_scope: MODERN_ORTHOGRAPHIC_RIME_CONTROL
historical_scope: NO_HISTORICAL_RIME_BOUND
sets:
- set_id: Z-RIME-001
  modern_rime_key: ㅏ∅
  member_count: 4
  surface_members: 가(ㄱ), 나(ㄴ), 사(ㅅ), 아(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-002
  modern_rime_key: ㅏㄱ
  member_count: 4
  surface_members: 각(ㄱ), 낙(ㄴ), 삭(ㅅ), 악(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-003
  modern_rime_key: ㅏㄴ
  member_count: 4
  surface_members: 간(ㄱ), 난(ㄴ), 산(ㅅ), 안(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-004
  modern_rime_key: ㅏㅁ
  member_count: 4
  surface_members: 감(ㄱ), 남(ㄴ), 삼(ㅅ), 암(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-005
  modern_rime_key: ㅏㅇ
  member_count: 4
  surface_members: 강(ㄱ), 낭(ㄴ), 상(ㅅ), 앙(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-006
  modern_rime_key: ㅏㅂ
  member_count: 4
  surface_members: 갑(ㄱ), 납(ㄴ), 삽(ㅅ), 압(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-007
  modern_rime_key: ㅐ∅
  member_count: 4
  surface_members: 개(ㄱ), 내(ㄴ), 새(ㅅ), 애(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-008
  modern_rime_key: ㅐㅇ
  member_count: 4
  surface_members: 갱(ㄱ), 냉(ㄴ), 생(ㅅ), 앵(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-009
  modern_rime_key: ㅓ∅
  member_count: 4
  surface_members: 거(ㄱ), 너(ㄴ), 서(ㅅ), 어(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-010
  modern_rime_key: ㅗ∅
  member_count: 4
  surface_members: 고(ㄱ), 노(ㄴ), 소(ㅅ), 오(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-011
  modern_rime_key: ㅗㄱ
  member_count: 4
  surface_members: 곡(ㄱ), 녹(ㄴ), 속(ㅅ), 옥(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-012
  modern_rime_key: ㅗㅇ
  member_count: 4
  surface_members: 공(ㄱ), 농(ㄴ), 송(ㅅ), 옹(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-013
  modern_rime_key: ㅜ∅
  member_count: 4
  surface_members: 구(ㄱ), 누(ㄴ), 수(ㅅ), 우(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-014
  modern_rime_key: ㅜㄴ
  member_count: 4
  surface_members: 군(ㄱ), 눈(ㄴ), 순(ㅅ), 운(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: none
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-015
  modern_rime_key: ㅕㄴ
  member_count: 3
  surface_members: 견(ㄱ), 년(ㄴ), 연(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: ㅅ
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
- set_id: Z-RIME-016
  modern_rime_key: ㅕㅇ
  member_count: 3
  surface_members: 경(ㄱ), 녕(ㄴ), 영(ㅇ)
  mechanical_audit: PASS
  missing_expected_initial: ㅅ
  source_position_state: QUERY_ROUTE_ONLY
  modern_phonetic_rime_independently_verified: false
  historical_rime_bound: false
surface_hanja_members:
- Set: '`Z-RIME-002`'
  Surface syllable: '`낙`'
  Hanja: '`樂`'
  Usage word: '`낙원`'
  Current tag: '`SINO_SURFACE`'
- Set: '`Z-RIME-008`'
  Surface syllable: '`냉`'
  Hanja: '`冷`'
  Usage word: '`냉기`'
  Current tag: '`SINO_SURFACE`'
- Set: '`Z-RIME-010`'
  Surface syllable: '`노`'
  Hanja: '`老`'
  Usage word: '`노인`'
  Current tag: '`SINO_SURFACE`'
- Set: '`Z-RIME-011`'
  Surface syllable: '`녹`'
  Hanja: '`綠`'
  Usage word: '`녹색`'
  Current tag: '`SINO_SURFACE`'
- Set: '`Z-RIME-013`'
  Surface syllable: '`누`'
  Hanja: '`漏`'
  Usage word: '`누수`'
  Current tag: '`SINO_SURFACE`'
noninitial_hanja_members:
- Set: '`Z-RIME-005`'
  Non-initial surface: '`앙`'
  Hanja: '`央`'
  Usage word: '`중앙`'
  Current tag: '`SINO_NONINITIAL`'
- Set: '`Z-RIME-012`'
  Non-initial surface: '`옹`'
  Hanja: '`翁`'
  Usage word: '`노옹`'
  Current tag: '`SINO_NONINITIAL`'
- Set: '`Z-RIME-015`'
  Non-initial surface: '`년`'
  Hanja: '`年`'
  Usage word: '`작년`'
  Current tag: '`SINO_NONINITIAL`'
- Set: '`Z-RIME-016`'
  Non-initial surface: '`녕`'
  Hanja: '`寧`'
  Usage word: '`안녕`'
  Current tag: '`SINO_NONINITIAL`'
```
## 13. First-vs-Nonfirst Position Groups

```yaml
group_count: 16
cross_result_registry:
- relation_id: Y-POS-001
  target: ㅇ
  forms: 강 / 강이
  xy_same_lineage_declared: 'true'
  xy_verification: LINEAGE_LINK_VERIFIED
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: 종성 ㅇ 유지와 다음 음절 무음 초성 ㅇ을 분리
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-002
  target: ㅇ
  forms: 방 / 방을
  xy_same_lineage_declared: 'true'
  xy_verification: LINEAGE_LINK_VERIFIED
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: 종성 ㅇ 비연음 예시; 초성·종성 음가 비동일
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-003
  target: ㅇ
  forms: 이다 / 리다 / 깔리다
  xy_same_lineage_declared: 'true'
  xy_verification: LINEAGE_LINK_VERIFIED
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: 역사 초성 음가는 SCHOLARLY_RECONSTRUCTION로 제한
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-004
  target: ㅇ
  forms: ㆁ / ㅇ / ㅇ
  xy_same_lineage_declared: 'false'
  xy_verification: SOURCE_CONFLICT
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`UNSUPPORTED_LINEAGE_LINK`'
  yz_boundary: 자모 기능대조는 가능하나 same-lineage는 미확정
  canonical_3d_state: CROSS_RESULT_CONFLICT
- relation_id: Y-POS-005
  target: ㄱ
  forms: 목 / 목이
  xy_same_lineage_declared: 'true'
  xy_verification: LINEAGE_LINK_VERIFIED
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: 종성→다음 음절 초성 실현
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-006
  target: ㄱ
  forms: 깎다 / 깎아
  xy_same_lineage_declared: 'true'
  xy_verification: PARTIAL_CROSS_MATCH
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: ㄱ·ㄲ을 동일 자모로 병합하지 않음
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-007
  target: ㄱ
  forms: 식브다 / 십브다 / 싶다
  xy_same_lineage_declared: 'true'
  xy_verification: LINEAGE_LINK_VERIFIED
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: 역사형 자음변화는 DICTIONARY_REPORTED
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-008
  target: ㄱ
  forms: 삿기 / 새 / 새끼
  xy_same_lineage_declared: 'true'
  xy_verification: LINEAGE_LINK_VERIFIED
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: ㄱ·ㅺ·ㄲ 문자층 분리
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-009
  target: ㄴ
  forms: 여자 / 남녀
  xy_same_lineage_declared: 'true'
  xy_verification: LINEAGE_LINK_VERIFIED
  xy_cross_relation: PROHIBITED_FOR_X_NATIVE_LEXEME_COUNT
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: 동일 Hanja Identity의 현대 첫/비첫 위치 표면관계
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-010
  target: ㄴ
  forms: 연세 / 학년 / 몇 년
  xy_same_lineage_declared: 'true'
  xy_verification: SOURCE_POSITION_VERIFIED_WITH_PRONUNCIATION_UNRESOLVED
  xy_cross_relation: PROHIBITED_FOR_X_NATIVE_LEXEME_COUNT
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: 위치·의존명사 조건 검증; 일부 연쇄발음은 SOURCE_UNCERTAIN
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-011
  target: ㄴ
  forms: 이불 / 솜이불
  xy_same_lineage_declared: 'true'
  xy_verification: LINEAGE_LINK_VERIFIED
  xy_cross_relation: PARTIAL_CROSS_MATCH_X_솜_COMPONENT
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: 삽입 ㄴ은 표기에 없는 발음층
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-012
  target: ㄴ
  forms: 연필 / 색연필
  xy_same_lineage_declared: 'true'
  xy_verification: LINEAGE_LINK_VERIFIED
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: ㄴ 첨가와 비음화를 별 단계로 유지
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-013
  target: ㅅ
  forms: 옷 / 옷이
  xy_same_lineage_declared: 'true'
  xy_verification: LINEAGE_LINK_VERIFIED
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: 종성 중화와 모음 앞 실현 분리
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-014
  target: ㅅ
  forms: 낫다 / 나아 / 나으니
  xy_same_lineage_declared: 'true'
  xy_verification: LINEAGE_LINK_VERIFIED
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: 현대 ㅅ 불규칙 활용
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-015
  target: ㅅ
  forms: 붓다 / 부어 / 부으니
  xy_same_lineage_declared: 'true'
  xy_verification: LINEAGE_LINK_VERIFIED
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`POSITION_RELATION_VERIFIED`'
  yz_boundary: 현대 ㅅ 불규칙 활용
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- relation_id: Y-POS-016
  target: ㅅ
  forms: 짓다 / 지어 / 지으니
  xy_same_lineage_declared: 'false'
  xy_verification: SOURCE_CONFLICT
  xy_cross_relation: MISSING_COUNTERPART
  yz_verification: '`MISSING_SOURCE_LOCATION`'
  yz_boundary: 검색 색인만 확보; 직접 표제어·발음 상세 필요
  canonical_3d_state: CROSS_RESULT_CONFLICT
```
## 14. Orthographic ㅇ–Phonetic Ø Dataset

```yaml
ieung_zero_dataset:
  X:
    records_reported: 12
    orthographic_initial_ㅇ_and_phonetic_Ø_consistent: 12
    actual_coda_distribution:
      empty: 4
      coda_ㅇ_ŋ: 6
      coda_ㅂ_p_stop: 1
      coda_ㄹ_l: 1
    item_level_lexical_source_missing:
    - 앙금
    - 엉덩이
    - 옹기
    - 웅덩이
    - 응어리
    - 잉어
  Z:
    records_reported: 45
    orthographic_initial_ㅇ_coda_not_ㅇ: 14
    orthographic_initial_ㅇ_and_coda_ㅇ: 9
    non_ㅇ_initial_and_coda_ㅇ: 22
    anonymous_record_id_gap: 10
  Y:
    modern_position_refs:
    - Y-POS-001
    - Y-POS-002
    - Y-POS-004
    modern_onset_coda_split: VERIFIED
    historical_old_ieung_projection: PROHIBITED_WITHOUT_NEW_SOURCES
  cross_state: CROSS_CONFIRMED_MODERN_FIELD_SPLIT
```
## 15. Initial ㅇ–Coda ㅇ Separation

```yaml
canonical_field_split:
  modern_orthographic_initial_ㅇ: GRAPHEMIC_ONSET_SLOT
  modern_phonetic_initial: Ø_UNDER_BOUND_MODERN_GUIDANCE
  modern_coda_ㅇ: '[ŋ]'
  historical_initial_ㆁ_or_ㅇ: SOURCE_UNCERTAIN_OR_SCHOLARLY_RECONSTRUCTION
cross_state: CROSS_CONFIRMED_FOR_MODERN_FIELDS
historical_identity_merge: false
```
## 16. Historical–Modern Form Map

```yaml
lineage_count: 9
registry:
- lineage_id: Y-HIST-001
  object_identity: 초성 옛이응 ㆁ
  historical_form: ㆁ
  intermediate_form: ㅇ
  modern_form: ㅇ
  xy_verification: SOURCE_CONFLICT
  yz_verification: UNSUPPORTED_LINEAGE_LINK + MULTIPLE_LINEAGE_CANDIDATES
  source_support: SRC-007, SRC-008, SRC-002/004의 층별 자료
  unsupported_jumps: ㆁ → 현대 초성·종성 ㅇ을 하나의 직선계보로 병합한 점
  conflicting_sources: Y-POS-004의 same_lineage_source_supported=false와 Y-HIST-001의 선형 계보표현이 충돌
  canonical_3d_state: CROSS_RESULT_CONFLICT
  causality_judged: false
- lineage_id: Y-HIST-002
  object_identity: 깔리-
  historical_form: 이다
  intermediate_form: 리다
  modern_form: 깔리다
  xy_verification: LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION
  yz_verification: MODERN_HISTORICAL_LINK_VERIFIED + SCHOLARLY_RECONSTRUCTION
  source_support: SRC-012 사전 역사정보
  unsupported_jumps: 없음. 단, 한 어휘 계보를 ㅇ 전체 역사로 일반화 금지
  conflicting_sources: 정확 음가의 직접기록과 재구 방법은 없음
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  causality_judged: false
- lineage_id: Y-HIST-003
  object_identity: 이르-
  historical_form: 니르다
  intermediate_form: 이르다
  modern_form: 이르다
  xy_verification: LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION
  yz_verification: MODERN_HISTORICAL_LINK_VERIFIED + SOURCE_CONFLICT
  source_support: SRC-006
  unsupported_jumps: 세부 시기·중간 문헌형은 미세분화
  conflicting_sources: 현상 명칭과 periodization은 Source가 연구자 견해차를 열어 둠
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  causality_judged: false
- lineage_id: Y-HIST-004
  object_identity: 女
  historical_form: 녀
  intermediate_form: 여
  modern_form: 여자/남녀
  xy_verification: LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION
  yz_verification: POSITION_RELATION_VERIFIED; HISTORICAL_LINEAGE_RECLASSIFICATION_REQUIRED
  source_support: SRC-003, Z-HANJA-053
  unsupported_jumps: 시대변화와 현대 위치조건을 혼합
  conflicting_sources: Z는 Identity reading 녀와 usage 남녀를 분리하며 역사음은 비어 있음
  canonical_3d_state: CROSS_RESULT_CONFLICT
  causality_judged: false
- lineage_id: Y-HIST-005
  object_identity: 年
  historical_form: 년
  intermediate_form: 연
  modern_form: 연세/학년/몇 년
  xy_verification: LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION
  yz_verification: POSITION_RELATION_VERIFIED; HISTORICAL_LINEAGE_RECLASSIFICATION_REQUIRED
  source_support: SRC-003, Z-HANJA-054
  unsupported_jumps: 시대변화와 현대 위치·의존명사 조건을 혼합
  conflicting_sources: Z는 Identity reading 년과 usage 작년을 분리하며 역사음은 비어 있음
  canonical_3d_state: CROSS_RESULT_CONFLICT
  causality_judged: false
- lineage_id: Y-HIST-006
  object_identity: 같-
  historical_form: 다/다
  intermediate_form: 다 → 갓-/갓ㅎ-/갓ㅌ-
  modern_form: 같다
  xy_verification: LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION
  yz_verification: MODERN_HISTORICAL_LINK_VERIFIED + DICTIONARY_REPORTED
  source_support: SRC-009 사전 역사정보
  unsupported_jumps: 복수 표기를 단일 음성값으로 환산하지 않음
  conflicting_sources: 직접 역사 음성기록 없음
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  causality_judged: false
- lineage_id: Y-HIST-007
  object_identity: 싶-
  historical_form: 식브다
  intermediate_form: 십브다 → 시브다/시프다
  modern_form: 싶다
  xy_verification: LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION
  yz_verification: MODERN_HISTORICAL_LINK_VERIFIED + DICTIONARY_REPORTED
  source_support: SRC-010 사전 역사정보
  unsupported_jumps: 없음. 각 단계 발음은 문헌·사전보고
  conflicting_sources: 직접 음성기록 없음
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  causality_judged: false
- lineage_id: Y-HIST-008
  object_identity: 새끼
  historical_form: 삿기
  intermediate_form: 새/색기
  modern_form: 새끼
  xy_verification: LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION
  yz_verification: MODERN_HISTORICAL_LINK_VERIFIED + DICTIONARY_REPORTED
  source_support: SRC-011 사전 역사정보
  unsupported_jumps: ㅺ·ㄲ·ㄱ 문자 Identity를 병합하지 않음
  conflicting_sources: 정확 발생연대는 세기별 용례범위
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  causality_judged: false
- lineage_id: Y-HIST-009
  object_identity: 잎
  historical_form: 닢
  intermediate_form: 깻닢/나뭇닢
  modern_form: 잎
  xy_verification: SOURCE_CONFLICT
  yz_verification: MULTIPLE_LINEAGE_CANDIDATES + SOURCE_CONFLICT
  source_support: SRC-017
  unsupported_jumps: 정확 세기와 독립 역사사전 계보가 없음
  conflicting_sources: ㄴㄴ 첨가 분석 반론이 같은 해설에 병기됨
  canonical_3d_state: CROSS_RESULT_CONFLICT
  causality_judged: false
temporal_causality_judged: false
```
## 17. Pronunciation Claim Registry

```yaml
claim_count: 11
direct_audio_or_instrumental_attestation_count: 0
registry:
- claim_id: PRON-001
  form: 강이
  reported_pronunciation: '[강이]'
  xy_claim_type: DICTIONARY_REPORTED
  yz_directive_state: DICTIONARY_REPORTED
  source_subtype: OFFICIAL_EXPLANATORY_RESPONSE
  rule_or_change: ㅇ 받침 비연음
  source_ref: SRC-004
  xy_verification: SOURCE_POSITION_VERIFIED
  direct_attestation: false
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- claim_id: PRON-002
  form: 목이
  reported_pronunciation: '[모기]'
  xy_claim_type: OFFICIAL_NORM_EXAMPLE
  yz_directive_state: DICTIONARY_REPORTED
  source_subtype: OFFICIAL_NORM_EXAMPLE
  rule_or_change: 제13항 연음
  source_ref: SRC-002
  xy_verification: SOURCE_POSITION_VERIFIED
  direct_attestation: false
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- claim_id: PRON-003
  form: 깎아
  reported_pronunciation: '[까까]'
  xy_claim_type: OFFICIAL_NORM_EXAMPLE
  yz_directive_state: DICTIONARY_REPORTED
  source_subtype: OFFICIAL_NORM_EXAMPLE
  rule_or_change: 제13항 연음
  source_ref: SRC-002
  xy_verification: SOURCE_POSITION_VERIFIED
  direct_attestation: false
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- claim_id: PRON-004
  form: 옷
  reported_pronunciation: '[옫]'
  xy_claim_type: OFFICIAL_NORM_EXAMPLE
  yz_directive_state: DICTIONARY_REPORTED
  source_subtype: OFFICIAL_NORM_EXAMPLE
  rule_or_change: 제9항 음절 끝소리
  source_ref: SRC-016
  xy_verification: SOURCE_POSITION_VERIFIED
  direct_attestation: false
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- claim_id: PRON-005
  form: 옷이
  reported_pronunciation: '[오시]'
  xy_claim_type: OFFICIAL_NORM_EXAMPLE
  yz_directive_state: DICTIONARY_REPORTED
  source_subtype: OFFICIAL_NORM_EXAMPLE
  rule_or_change: 제13항 연음
  source_ref: SRC-016
  xy_verification: SOURCE_POSITION_VERIFIED
  direct_attestation: false
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- claim_id: PRON-006
  form: 솜이불
  reported_pronunciation: '[솜ː니불]'
  xy_claim_type: OFFICIAL_NORM_EXAMPLE
  yz_directive_state: DICTIONARY_REPORTED
  source_subtype: OFFICIAL_NORM_EXAMPLE
  rule_or_change: 제29항 ㄴ 첨가
  source_ref: SRC-002
  xy_verification: SOURCE_POSITION_VERIFIED
  direct_attestation: false
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- claim_id: PRON-007
  form: 색연필
  reported_pronunciation: '[생년필]'
  xy_claim_type: OFFICIAL_NORM_EXAMPLE
  yz_directive_state: DICTIONARY_REPORTED
  source_subtype: OFFICIAL_NORM_EXAMPLE
  rule_or_change: ㄴ 첨가+비음화
  source_ref: SRC-002
  xy_verification: SOURCE_POSITION_VERIFIED
  direct_attestation: false
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- claim_id: PRON-008
  form: 낫다/나아
  reported_pronunciation: '[낟ː따]/[나아]'
  xy_claim_type: DICTIONARY_REPORTED
  yz_directive_state: DICTIONARY_REPORTED
  source_subtype: OFFICIAL_DICTIONARY_ENTRY
  rule_or_change: ㅅ 불규칙 활용
  source_ref: SRC-014
  xy_verification: SOURCE_POSITION_VERIFIED
  direct_attestation: false
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- claim_id: PRON-009
  form: 붓다/부어
  reported_pronunciation: '[붇ː따]/[부어]'
  xy_claim_type: DICTIONARY_REPORTED
  yz_directive_state: DICTIONARY_REPORTED
  source_subtype: OFFICIAL_DICTIONARY_ENTRY
  rule_or_change: ㅅ 불규칙 활용
  source_ref: SRC-013
  xy_verification: SOURCE_POSITION_VERIFIED
  direct_attestation: false
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- claim_id: PRON-010
  form: 같다
  reported_pronunciation: '[갇따]'
  xy_claim_type: DICTIONARY_REPORTED
  yz_directive_state: DICTIONARY_REPORTED
  source_subtype: OFFICIAL_DICTIONARY_HISTORY
  rule_or_change: 현대 표준 발음
  source_ref: SRC-009
  xy_verification: SOURCE_POSITION_VERIFIED
  direct_attestation: false
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
- claim_id: PRON-011
  form: 싶다/싶어
  reported_pronunciation: '[십따]/[시퍼]'
  xy_claim_type: DICTIONARY_REPORTED
  yz_directive_state: DICTIONARY_REPORTED
  source_subtype: OFFICIAL_DICTIONARY_HISTORY
  rule_or_change: 현대 활용
  source_ref: SRC-010
  xy_verification: SOURCE_POSITION_VERIFIED
  direct_attestation: false
  canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
historical_phonetic_claims:
- object: 초성 ㆁ / 중세 초성 ㅇ
  value: 음가 존재 또는 조건부 음가
  source: SRC-008; SRC-007
  method_as_source_states: NOT_STATED
  confidence_as_source_states: LIMITED_EXPLANATORY_SOURCE
  direct_attestation: false
  current_state: SOURCE_UNCERTAIN
- object: 이다 둘째 음절 초성 ㅇ
  value: 후두 유성 마찰음
  source: SRC-012
  method_as_source_states: DICTIONARY_REPORTED_SCHOLARLY_EXPLANATION
  confidence_as_source_states: LEXEME_SCOPED
  direct_attestation: false
  current_state: SCHOLARLY_RECONSTRUCTION
```
## 18. No-Coda–Coda Relations

```yaml
no_coda_coda_relations:
  reported_relation_count: 10
  direct_lineage_snapshot_verified_count: 0
  status: SINGLE_SEAT_ONLY_WITH_MISSING_SOURCE_LOCATIONS
  source_seat: gpt.xy
  direct_records_available_in_3d_input: false
  required_action: Preserve as candidates; bind direct inflection snapshots before LINEAGE_LINK_VERIFIED.
```
## 19. Identity and Duplicate Map

```yaml
identity_and_duplicate_map:
  X:
    raw_lexical_entry_count: 60
    unique_surface_lemma_count: 60
    duplicate_inflation: 0
    direct_entry_reentry_duplicate_links: 13
  Y:
    source_record_count: 19
    unique_source_identity_count: 18
    duplicate_source_pair:
    - SRC-002
    - SRC-017
    duplicate_counted_as_independent: false
  Z:
    Hanja_entries: 80
    unique_Unicode_characters: 80
    unique_character_reading_pairs: 80
    duplicate_inflation: 0
    variant_relation: '拿–拏: VARIANT_LINKED_NOT_MERGED'
  groups:
    same_syllable_duplicate_entry_ids: 0
    same_rime_duplicate_onsets: 0
```
## 20. Raw Source Data

```yaml
raw_source_data:
  availability_boundary: The three direct inputs are 2D verification results, not the 1D source-data bytes. Raw source rows are reproduced only
    where a 2D result explicitly preserves them.
  old_hangul_and_lineage_rows:
  - Raw lineage: '`다 / 다`'
    Normalized endpoint: 같다
    Preserved: Raw form, period, source
    Prohibited replacement: 현대 표기로 Raw 대체
  - Raw lineage: '`식브다→십브다→시브다/시프다`'
    Normalized endpoint: 싶다
    Preserved: 단계순서와 원문형
    Prohibited replacement: 단일 인과로 축약
  - Raw lineage: '`삿기→새/색기`'
    Normalized endpoint: 새끼
    Preserved: ㅺ·ㄱ·ㄲ 표기층
    Prohibited replacement: 자모 Identity 자동병합
  - Raw lineage: '`이다→리다`'
    Normalized endpoint: 깔리다
    Preserved: 옛자모·시대·Source
    Prohibited replacement: 현대 ㅇ으로 자동치환
  - Raw lineage: '`니르다`'
    Normalized endpoint: 이르다
    Preserved: 역사형·현대형 분리
    Prohibited replacement: 한자어 두음법칙과 완전 동일시
  - Raw lineage: '`ㆁ / ㅇ`'
    Normalized endpoint: 현대 ㅇ 후보
    Preserved: 자모·음가·위치층
    Prohibited replacement: 단일 문자계보 확정
  historical_forms:
  - lineage_id: Y-HIST-001
    historical_state: ㆁ — 중세국어~16세기 말, 음가 존재가 Source에서 보고됨
    intermediate_states: 현대 ㅇ을 중간단계로 직접 놓은 결속은 Source가 단일 문자계보로 확정하지 않음
    modern_state: 현대 초성 ㅇ=무음 표기자리 / 종성 ㅇ=[ŋ]
  - lineage_id: Y-HIST-002
    historical_state: 이다 — 15세기 표기, 역사 초성 ㅇ 음가를 사전이 보고
    intermediate_states: 리다 — 18세기 중간형
    modern_state: 깔리다
  - lineage_id: Y-HIST-003
    historical_state: 니르다 — 중세 표기
    intermediate_states: 근대국어 시기 어두 ㄴ 탈락으로 설명
    modern_state: 이르다
  - lineage_id: Y-HIST-004
    historical_state: 녀를 역사단계로 둔 현재 필드
    intermediate_states: 여를 현대 단어 첫 위치 표면형으로 둔 현재 필드
    modern_state: 여자 / 남녀
  - lineage_id: Y-HIST-005
    historical_state: 년을 역사단계로 둔 현재 필드
    intermediate_states: 연을 현대 단어 첫 위치 표면형으로 둔 현재 필드
    modern_state: 연세 / 학년 / 몇 년
  - lineage_id: Y-HIST-006
    historical_state: 다 / 다
    intermediate_states: 갓-/갓ㅎ-/갓ㅌ- 등 복수 표기
    modern_state: 같다
  - lineage_id: Y-HIST-007
    historical_state: 식브다
    intermediate_states: 십브다 → 시브다/시프다
    modern_state: 싶다
  - lineage_id: Y-HIST-008
    historical_state: 삿기
    intermediate_states: 새 / 색기
    modern_state: 새끼
  - lineage_id: Y-HIST-009
    historical_state: 닢 — Source 해설
    intermediate_states: 깻닢·나뭇닢 분석 후보
    modern_state: 잎 / 깻잎 / 나뭇잎
  exact_1d_raw_bytes_directly_bound_to_3d: false
```
## 21. Normalized Source Data

```yaml
normalized_source_data:
  native_lexical_surfaces:
  - entry_id: X-ㅇ-E01
    surface: 아기
    part_of_speech: 명사
    target_code: '20235'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E02
    surface: 아이
    part_of_speech: 명사
    target_code: '62843'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E03
    surface: 아버지
    part_of_speech: 명사
    target_code: '71343'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E04
    surface: 어머니
    part_of_speech: 명사
    target_code: '74361'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E05
    surface: 언니
    part_of_speech: 명사
    target_code: '31971'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E06
    surface: 오빠
    part_of_speech: 명사
    target_code: '68006'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E07
    surface: 우리
    part_of_speech: 대명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    - UNCERTAIN_IDENTITY
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E08
    surface: 오늘
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E09
    surface: 어제
    part_of_speech: 명사
    target_code: '67075'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E10
    surface: 이제
    part_of_speech: 부사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    - UNCERTAIN_IDENTITY
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E11
    surface: 이마
    part_of_speech: 명사
    target_code: '71693'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E12
    surface: 이빨
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E13
    surface: 입
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E14
    surface: 얼음
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅇ-E15
    surface: 여름
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E01
    surface: 가슴
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E02
    surface: 가을
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E03
    surface: 개미
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E04
    surface: 거미
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E05
    surface: 겨울
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E06
    surface: 고기
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E07
    surface: 구름
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E08
    surface: 귀
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E09
    surface: 길
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E10
    surface: 김
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    - UNCERTAIN_IDENTITY
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E11
    surface: 가다
    part_of_speech: 동사
    target_code: '27500'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: VERIFIED
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E12
    surface: 가늘다
    part_of_speech: 형용사
    target_code: '62497'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: VERIFIED
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E13
    surface: 고맙다
    part_of_speech: 형용사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: UNVERIFIED_SOURCE_LOCATION
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E14
    surface: 그리다
    part_of_speech: 동사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: UNVERIFIED_SOURCE_LOCATION
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄱ-E15
    surface: 기르다
    part_of_speech: 동사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: UNVERIFIED_SOURCE_LOCATION
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E01
    surface: 나
    part_of_speech: 대명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E02
    surface: 너
    part_of_speech: 대명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E03
    surface: 나무
    part_of_speech: 명사
    target_code: '32750'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E04
    surface: 나라
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E05
    surface: 나이
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E06
    surface: 날
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    - UNCERTAIN_IDENTITY
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E07
    surface: 남
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E08
    surface: 낮
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E09
    surface: 냄새
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E10
    surface: 넋
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E11
    surface: 눈
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    - UNCERTAIN_IDENTITY
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E12
    surface: 누나
    part_of_speech: 명사
    target_code: '32205'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E13
    surface: 누이
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E14
    surface: 누룩
    part_of_speech: 명사
    target_code: '45604'
    access_state: DIRECT_ENTRY_VERIFIED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - SOURCE_IDENTITY_VERIFIED
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㄴ-E15
    surface: 늪
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E01
    surface: 사람
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E02
    surface: 사랑
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E03
    surface: 사슴
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E04
    surface: 살
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    - UNCERTAIN_IDENTITY
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E05
    surface: 새
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    - UNCERTAIN_IDENTITY
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E06
    surface: 샘
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    - UNCERTAIN_IDENTITY
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E07
    surface: 서리
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E08
    surface: 섬
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E09
    surface: 소
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E10
    surface: 소금
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E11
    surface: 손
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E12
    surface: 솜
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E13
    surface: 술
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    - UNCERTAIN_IDENTITY
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E14
    surface: 숨
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  - entry_id: X-ㅅ-E15
    surface: 숲
    part_of_speech: 명사
    target_code: null
    access_state: OFFICIAL_REENTRY_ROUTE_RECORDED
    root_stem_source_state: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
    verification_states:
    - MISSING_SOURCE_LOCATION
    - NORMALIZATION_VERIFIED
    cross_counterpart: MISSING_COUNTERPART
    lexical_class: NATIVE_KOREAN_AS_INTERNALLY_TAGGED_BY_DATA_X
    analysis_reserved: null
  hanja_identities:
  - entry_id: Z-HANJA-001
    hanja: 英
    codepoint: U+82F1
    selected_reading: 영
    modern_jamo: ㅇ·ㅕ·ㅇ
    usage_word: 영어
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-002
    hanja: 永
    codepoint: U+6C38
    selected_reading: 영
    modern_jamo: ㅇ·ㅕ·ㅇ
    usage_word: 영구
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-003
    hanja: 榮
    codepoint: U+69AE
    selected_reading: 영
    modern_jamo: ㅇ·ㅕ·ㅇ
    usage_word: 영광
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-004
    hanja: 迎
    codepoint: U+8FCE
    selected_reading: 영
    modern_jamo: ㅇ·ㅕ·ㅇ
    usage_word: 환영
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-005
    hanja: 映
    codepoint: U+6620
    selected_reading: 영
    modern_jamo: ㅇ·ㅕ·ㅇ
    usage_word: 영화
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-006
    hanja: 營
    codepoint: U+71DF
    selected_reading: 영
    modern_jamo: ㅇ·ㅕ·ㅇ
    usage_word: 경영
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-007
    hanja: 園
    codepoint: U+5712
    selected_reading: 원
    modern_jamo: ㅇ·ㅝ·ㄴ
    usage_word: 공원
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-008
    hanja: 遠
    codepoint: U+9060
    selected_reading: 원
    modern_jamo: ㅇ·ㅝ·ㄴ
    usage_word: 원격
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-009
    hanja: 元
    codepoint: U+5143
    selected_reading: 원
    modern_jamo: ㅇ·ㅝ·ㄴ
    usage_word: 원금
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-010
    hanja: 原
    codepoint: U+539F
    selected_reading: 원
    modern_jamo: ㅇ·ㅝ·ㄴ
    usage_word: 원래
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-011
    hanja: 院
    codepoint: U+9662
    selected_reading: 원
    modern_jamo: ㅇ·ㅝ·ㄴ
    usage_word: 병원
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-012
    hanja: 願
    codepoint: U+9858
    selected_reading: 원
    modern_jamo: ㅇ·ㅝ·ㄴ
    usage_word: 소원
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-013
    hanja: 人
    codepoint: U+4EBA
    selected_reading: 인
    modern_jamo: ㅇ·ㅣ·ㄴ
    usage_word: 인간
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-014
    hanja: 因
    codepoint: U+56E0
    selected_reading: 인
    modern_jamo: ㅇ·ㅣ·ㄴ
    usage_word: 원인
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-015
    hanja: 印
    codepoint: U+5370
    selected_reading: 인
    modern_jamo: ㅇ·ㅣ·ㄴ
    usage_word: 인쇄
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-016
    hanja: 引
    codepoint: U+5F15
    selected_reading: 인
    modern_jamo: ㅇ·ㅣ·ㄴ
    usage_word: 인용
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-017
    hanja: 認
    codepoint: U+8A8D
    selected_reading: 인
    modern_jamo: ㅇ·ㅣ·ㄴ
    usage_word: 인정
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-018
    hanja: 意
    codepoint: U+610F
    selected_reading: 의
    modern_jamo: ㅇ·ㅢ·∅
    usage_word: 의미
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-019
    hanja: 醫
    codepoint: U+91AB
    selected_reading: 의
    modern_jamo: ㅇ·ㅢ·∅
    usage_word: 의학
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-020
    hanja: 衣
    codepoint: U+8863
    selected_reading: 의
    modern_jamo: ㅇ·ㅢ·∅
    usage_word: 의복
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-021
    hanja: 家
    codepoint: U+5BB6
    selected_reading: 가
    modern_jamo: ㄱ·ㅏ·∅
    usage_word: 가정
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-022
    hanja: 歌
    codepoint: U+6B4C
    selected_reading: 가
    modern_jamo: ㄱ·ㅏ·∅
    usage_word: 가곡
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-023
    hanja: 價
    codepoint: U+50F9
    selected_reading: 가
    modern_jamo: ㄱ·ㅏ·∅
    usage_word: 가격
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-024
    hanja: 加
    codepoint: U+52A0
    selected_reading: 가
    modern_jamo: ㄱ·ㅏ·∅
    usage_word: 가산
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-025
    hanja: 可
    codepoint: U+53EF
    selected_reading: 가
    modern_jamo: ㄱ·ㅏ·∅
    usage_word: 가능
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-026
    hanja: 各
    codepoint: U+5404
    selected_reading: 각
    modern_jamo: ㄱ·ㅏ·ㄱ
    usage_word: 각각
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-027
    hanja: 角
    codepoint: U+89D2
    selected_reading: 각
    modern_jamo: ㄱ·ㅏ·ㄱ
    usage_word: 각도
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-028
    hanja: 刻
    codepoint: U+523B
    selected_reading: 각
    modern_jamo: ㄱ·ㅏ·ㄱ
    usage_word: 시각
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-029
    hanja: 覺
    codepoint: U+89BA
    selected_reading: 각
    modern_jamo: ㄱ·ㅏ·ㄱ
    usage_word: 감각
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-030
    hanja: 脚
    codepoint: U+811A
    selected_reading: 각
    modern_jamo: ㄱ·ㅏ·ㄱ
    usage_word: 각본
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-031
    hanja: 間
    codepoint: U+9593
    selected_reading: 간
    modern_jamo: ㄱ·ㅏ·ㄴ
    usage_word: 공간
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-032
    hanja: 簡
    codepoint: U+7C21
    selected_reading: 간
    modern_jamo: ㄱ·ㅏ·ㄴ
    usage_word: 간단
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-033
    hanja: 看
    codepoint: U+770B
    selected_reading: 간
    modern_jamo: ㄱ·ㅏ·ㄴ
    usage_word: 간호
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-034
    hanja: 干
    codepoint: U+5E72
    selected_reading: 간
    modern_jamo: ㄱ·ㅏ·ㄴ
    usage_word: 간섭
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-035
    hanja: 刊
    codepoint: U+520A
    selected_reading: 간
    modern_jamo: ㄱ·ㅏ·ㄴ
    usage_word: 간행
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-036
    hanja: 感
    codepoint: U+611F
    selected_reading: 감
    modern_jamo: ㄱ·ㅏ·ㅁ
    usage_word: 감정
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-037
    hanja: 減
    codepoint: U+6E1B
    selected_reading: 감
    modern_jamo: ㄱ·ㅏ·ㅁ
    usage_word: 감소
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-038
    hanja: 監
    codepoint: U+76E3
    selected_reading: 감
    modern_jamo: ㄱ·ㅏ·ㅁ
    usage_word: 감독
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-039
    hanja: 甘
    codepoint: U+7518
    selected_reading: 감
    modern_jamo: ㄱ·ㅏ·ㅁ
    usage_word: 감미
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-040
    hanja: 敢
    codepoint: U+6562
    selected_reading: 감
    modern_jamo: ㄱ·ㅏ·ㅁ
    usage_word: 용감
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-041
    hanja: 拿
    codepoint: U+62FF
    selected_reading: 나
    modern_jamo: ㄴ·ㅏ·∅
    usage_word: 나포
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-042
    hanja: 懦
    codepoint: U+61E6
    selected_reading: 나
    modern_jamo: ㄴ·ㅏ·∅
    usage_word: 나약
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-043
    hanja: 暖
    codepoint: U+6696
    selected_reading: 난
    modern_jamo: ㄴ·ㅏ·ㄴ
    usage_word: 난방
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-044
    hanja: 難
    codepoint: U+96E3
    selected_reading: 난
    modern_jamo: ㄴ·ㅏ·ㄴ
    usage_word: 난관
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-045
    hanja: 南
    codepoint: U+5357
    selected_reading: 남
    modern_jamo: ㄴ·ㅏ·ㅁ
    usage_word: 남부
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-046
    hanja: 男
    codepoint: U+7537
    selected_reading: 남
    modern_jamo: ㄴ·ㅏ·ㅁ
    usage_word: 남성
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-047
    hanja: 納
    codepoint: U+7D0D
    selected_reading: 납
    modern_jamo: ㄴ·ㅏ·ㅂ
    usage_word: 납부
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-048
    hanja: 娘
    codepoint: U+5A18
    selected_reading: 낭
    modern_jamo: ㄴ·ㅏ·ㅇ
    usage_word: 낭자
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-049
    hanja: 囊
    codepoint: U+56CA
    selected_reading: 낭
    modern_jamo: ㄴ·ㅏ·ㅇ
    usage_word: 낭종
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-050
    hanja: 內
    codepoint: U+5167
    selected_reading: 내
    modern_jamo: ㄴ·ㅐ·∅
    usage_word: 내부
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-051
    hanja: 耐
    codepoint: U+8010
    selected_reading: 내
    modern_jamo: ㄴ·ㅐ·∅
    usage_word: 내구
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-052
    hanja: 奈
    codepoint: U+5948
    selected_reading: 내
    modern_jamo: ㄴ·ㅐ·∅
    usage_word: 막무가내
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-053
    hanja: 女
    codepoint: U+5973
    selected_reading: 녀
    modern_jamo: ㄴ·ㅕ·∅
    usage_word: 남녀
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-054
    hanja: 年
    codepoint: U+5E74
    selected_reading: 년
    modern_jamo: ㄴ·ㅕ·ㄴ
    usage_word: 작년
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-055
    hanja: 念
    codepoint: U+5FF5
    selected_reading: 념
    modern_jamo: ㄴ·ㅕ·ㅁ
    usage_word: 신념
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-056
    hanja: 寧
    codepoint: U+5BE7
    selected_reading: 녕
    modern_jamo: ㄴ·ㅕ·ㅇ
    usage_word: 안녕
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-057
    hanja: 農
    codepoint: U+8FB2
    selected_reading: 농
    modern_jamo: ㄴ·ㅗ·ㅇ
    usage_word: 농업
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-058
    hanja: 濃
    codepoint: U+6FC3
    selected_reading: 농
    modern_jamo: ㄴ·ㅗ·ㅇ
    usage_word: 농도
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-059
    hanja: 腦
    codepoint: U+8166
    selected_reading: 뇌
    modern_jamo: ㄴ·ㅚ·∅
    usage_word: 뇌수
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-060
    hanja: 惱
    codepoint: U+60F1
    selected_reading: 뇌
    modern_jamo: ㄴ·ㅚ·∅
    usage_word: 번뇌
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-061
    hanja: 四
    codepoint: U+56DB
    selected_reading: 사
    modern_jamo: ㅅ·ㅏ·∅
    usage_word: 사방
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-062
    hanja: 事
    codepoint: U+4E8B
    selected_reading: 사
    modern_jamo: ㅅ·ㅏ·∅
    usage_word: 사건
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-063
    hanja: 史
    codepoint: U+53F2
    selected_reading: 사
    modern_jamo: ㅅ·ㅏ·∅
    usage_word: 역사
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-064
    hanja: 士
    codepoint: U+58EB
    selected_reading: 사
    modern_jamo: ㅅ·ㅏ·∅
    usage_word: 박사
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-065
    hanja: 師
    codepoint: U+5E2B
    selected_reading: 사
    modern_jamo: ㅅ·ㅏ·∅
    usage_word: 교사
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-066
    hanja: 上
    codepoint: U+4E0A
    selected_reading: 상
    modern_jamo: ㅅ·ㅏ·ㅇ
    usage_word: 상승
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-067
    hanja: 商
    codepoint: U+5546
    selected_reading: 상
    modern_jamo: ㅅ·ㅏ·ㅇ
    usage_word: 상업
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-068
    hanja: 相
    codepoint: U+76F8
    selected_reading: 상
    modern_jamo: ㅅ·ㅏ·ㅇ
    usage_word: 상호
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-069
    hanja: 想
    codepoint: U+60F3
    selected_reading: 상
    modern_jamo: ㅅ·ㅏ·ㅇ
    usage_word: 상상
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-070
    hanja: 常
    codepoint: U+5E38
    selected_reading: 상
    modern_jamo: ㅅ·ㅏ·ㅇ
    usage_word: 상시
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-071
    hanja: 成
    codepoint: U+6210
    selected_reading: 성
    modern_jamo: ㅅ·ㅓ·ㅇ
    usage_word: 성공
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-072
    hanja: 性
    codepoint: U+6027
    selected_reading: 성
    modern_jamo: ㅅ·ㅓ·ㅇ
    usage_word: 성격
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-073
    hanja: 聖
    codepoint: U+8056
    selected_reading: 성
    modern_jamo: ㅅ·ㅓ·ㅇ
    usage_word: 성인
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-074
    hanja: 城
    codepoint: U+57CE
    selected_reading: 성
    modern_jamo: ㅅ·ㅓ·ㅇ
    usage_word: 성벽
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-075
    hanja: 星
    codepoint: U+661F
    selected_reading: 성
    modern_jamo: ㅅ·ㅓ·ㅇ
    usage_word: 성좌
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-076
    hanja: 先
    codepoint: U+5148
    selected_reading: 선
    modern_jamo: ㅅ·ㅓ·ㄴ
    usage_word: 선행
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-077
    hanja: 線
    codepoint: U+7DDA
    selected_reading: 선
    modern_jamo: ㅅ·ㅓ·ㄴ
    usage_word: 선형
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-078
    hanja: 善
    codepoint: U+5584
    selected_reading: 선
    modern_jamo: ㅅ·ㅓ·ㄴ
    usage_word: 선의
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-079
    hanja: 選
    codepoint: U+9078
    selected_reading: 선
    modern_jamo: ㅅ·ㅓ·ㄴ
    usage_word: 선택
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  - entry_id: Z-HANJA-080
    hanja: 船
    codepoint: U+8239
    selected_reading: 선
    modern_jamo: ㅅ·ㅓ·ㄴ
    usage_word: 선박
    reading_link_state: HANJA_READING_LINK_VERIFIED@TIER_3
    usage_source_location: MISSING_STABLE_DETAIL_ID
    identity_state: HANJA_UNICODE_IDENTITY_VERIFIED
    reading_authority_state: TIER_3_TRANSFORMED_SOURCE_BOUND
    official_detail_crosscheck: MISSING_SOURCE_LOCATION
    historical_reading: null
  same_syllable_groups:
  - group_id: Z-HOMOPHONE-001
    shared_modern_syllable: 가
    members_reported: 5
    distinct_hanja: 5
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-002
    shared_modern_syllable: 각
    members_reported: 5
    distinct_hanja: 5
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-003
    shared_modern_syllable: 간
    members_reported: 5
    distinct_hanja: 5
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-004
    shared_modern_syllable: 감
    members_reported: 5
    distinct_hanja: 5
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-005
    shared_modern_syllable: 나
    members_reported: 2
    distinct_hanja: 2
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-006
    shared_modern_syllable: 난
    members_reported: 2
    distinct_hanja: 2
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-007
    shared_modern_syllable: 남
    members_reported: 2
    distinct_hanja: 2
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-008
    shared_modern_syllable: 낭
    members_reported: 2
    distinct_hanja: 2
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-009
    shared_modern_syllable: 내
    members_reported: 3
    distinct_hanja: 3
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-010
    shared_modern_syllable: 농
    members_reported: 2
    distinct_hanja: 2
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-011
    shared_modern_syllable: 뇌
    members_reported: 2
    distinct_hanja: 2
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-012
    shared_modern_syllable: 사
    members_reported: 5
    distinct_hanja: 5
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-013
    shared_modern_syllable: 상
    members_reported: 5
    distinct_hanja: 5
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-014
    shared_modern_syllable: 선
    members_reported: 5
    distinct_hanja: 5
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-015
    shared_modern_syllable: 성
    members_reported: 5
    distinct_hanja: 5
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-016
    shared_modern_syllable: 영
    members_reported: 6
    distinct_hanja: 6
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-017
    shared_modern_syllable: 원
    members_reported: 6
    distinct_hanja: 6
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-018
    shared_modern_syllable: 의
    members_reported: 3
    distinct_hanja: 3
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  - group_id: Z-HOMOPHONE-019
    shared_modern_syllable: 인
    members_reported: 5
    distinct_hanja: 5
    mechanical_audit: PASS
    source_position_state: TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING
    historical_equivalence: PROHIBITED
  same_rime_sets:
  - set_id: Z-RIME-001
    modern_rime_key: ㅏ∅
    member_count: 4
    surface_members: 가(ㄱ), 나(ㄴ), 사(ㅅ), 아(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-002
    modern_rime_key: ㅏㄱ
    member_count: 4
    surface_members: 각(ㄱ), 낙(ㄴ), 삭(ㅅ), 악(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-003
    modern_rime_key: ㅏㄴ
    member_count: 4
    surface_members: 간(ㄱ), 난(ㄴ), 산(ㅅ), 안(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-004
    modern_rime_key: ㅏㅁ
    member_count: 4
    surface_members: 감(ㄱ), 남(ㄴ), 삼(ㅅ), 암(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-005
    modern_rime_key: ㅏㅇ
    member_count: 4
    surface_members: 강(ㄱ), 낭(ㄴ), 상(ㅅ), 앙(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-006
    modern_rime_key: ㅏㅂ
    member_count: 4
    surface_members: 갑(ㄱ), 납(ㄴ), 삽(ㅅ), 압(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-007
    modern_rime_key: ㅐ∅
    member_count: 4
    surface_members: 개(ㄱ), 내(ㄴ), 새(ㅅ), 애(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-008
    modern_rime_key: ㅐㅇ
    member_count: 4
    surface_members: 갱(ㄱ), 냉(ㄴ), 생(ㅅ), 앵(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-009
    modern_rime_key: ㅓ∅
    member_count: 4
    surface_members: 거(ㄱ), 너(ㄴ), 서(ㅅ), 어(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-010
    modern_rime_key: ㅗ∅
    member_count: 4
    surface_members: 고(ㄱ), 노(ㄴ), 소(ㅅ), 오(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-011
    modern_rime_key: ㅗㄱ
    member_count: 4
    surface_members: 곡(ㄱ), 녹(ㄴ), 속(ㅅ), 옥(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-012
    modern_rime_key: ㅗㅇ
    member_count: 4
    surface_members: 공(ㄱ), 농(ㄴ), 송(ㅅ), 옹(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-013
    modern_rime_key: ㅜ∅
    member_count: 4
    surface_members: 구(ㄱ), 누(ㄴ), 수(ㅅ), 우(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-014
    modern_rime_key: ㅜㄴ
    member_count: 4
    surface_members: 군(ㄱ), 눈(ㄴ), 순(ㅅ), 운(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: none
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-015
    modern_rime_key: ㅕㄴ
    member_count: 3
    surface_members: 견(ㄱ), 년(ㄴ), 연(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: ㅅ
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  - set_id: Z-RIME-016
    modern_rime_key: ㅕㅇ
    member_count: 3
    surface_members: 경(ㄱ), 녕(ㄴ), 영(ㅇ)
    mechanical_audit: PASS
    missing_expected_initial: ㅅ
    source_position_state: QUERY_ROUTE_ONLY
    modern_phonetic_rime_independently_verified: false
    historical_rime_bound: false
  position_relations:
  - relation_id: Y-POS-001
    target: ㅇ
    forms: 강 / 강이
    xy_same_lineage_declared: 'true'
    xy_verification: LINEAGE_LINK_VERIFIED
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: 종성 ㅇ 유지와 다음 음절 무음 초성 ㅇ을 분리
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-002
    target: ㅇ
    forms: 방 / 방을
    xy_same_lineage_declared: 'true'
    xy_verification: LINEAGE_LINK_VERIFIED
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: 종성 ㅇ 비연음 예시; 초성·종성 음가 비동일
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-003
    target: ㅇ
    forms: 이다 / 리다 / 깔리다
    xy_same_lineage_declared: 'true'
    xy_verification: LINEAGE_LINK_VERIFIED
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: 역사 초성 음가는 SCHOLARLY_RECONSTRUCTION로 제한
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-004
    target: ㅇ
    forms: ㆁ / ㅇ / ㅇ
    xy_same_lineage_declared: 'false'
    xy_verification: SOURCE_CONFLICT
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`UNSUPPORTED_LINEAGE_LINK`'
    yz_boundary: 자모 기능대조는 가능하나 same-lineage는 미확정
    canonical_3d_state: CROSS_RESULT_CONFLICT
  - relation_id: Y-POS-005
    target: ㄱ
    forms: 목 / 목이
    xy_same_lineage_declared: 'true'
    xy_verification: LINEAGE_LINK_VERIFIED
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: 종성→다음 음절 초성 실현
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-006
    target: ㄱ
    forms: 깎다 / 깎아
    xy_same_lineage_declared: 'true'
    xy_verification: PARTIAL_CROSS_MATCH
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: ㄱ·ㄲ을 동일 자모로 병합하지 않음
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-007
    target: ㄱ
    forms: 식브다 / 십브다 / 싶다
    xy_same_lineage_declared: 'true'
    xy_verification: LINEAGE_LINK_VERIFIED
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: 역사형 자음변화는 DICTIONARY_REPORTED
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-008
    target: ㄱ
    forms: 삿기 / 새 / 새끼
    xy_same_lineage_declared: 'true'
    xy_verification: LINEAGE_LINK_VERIFIED
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: ㄱ·ㅺ·ㄲ 문자층 분리
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-009
    target: ㄴ
    forms: 여자 / 남녀
    xy_same_lineage_declared: 'true'
    xy_verification: LINEAGE_LINK_VERIFIED
    xy_cross_relation: PROHIBITED_FOR_X_NATIVE_LEXEME_COUNT
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: 동일 Hanja Identity의 현대 첫/비첫 위치 표면관계
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-010
    target: ㄴ
    forms: 연세 / 학년 / 몇 년
    xy_same_lineage_declared: 'true'
    xy_verification: SOURCE_POSITION_VERIFIED_WITH_PRONUNCIATION_UNRESOLVED
    xy_cross_relation: PROHIBITED_FOR_X_NATIVE_LEXEME_COUNT
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: 위치·의존명사 조건 검증; 일부 연쇄발음은 SOURCE_UNCERTAIN
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-011
    target: ㄴ
    forms: 이불 / 솜이불
    xy_same_lineage_declared: 'true'
    xy_verification: LINEAGE_LINK_VERIFIED
    xy_cross_relation: PARTIAL_CROSS_MATCH_X_솜_COMPONENT
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: 삽입 ㄴ은 표기에 없는 발음층
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-012
    target: ㄴ
    forms: 연필 / 색연필
    xy_same_lineage_declared: 'true'
    xy_verification: LINEAGE_LINK_VERIFIED
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: ㄴ 첨가와 비음화를 별 단계로 유지
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-013
    target: ㅅ
    forms: 옷 / 옷이
    xy_same_lineage_declared: 'true'
    xy_verification: LINEAGE_LINK_VERIFIED
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: 종성 중화와 모음 앞 실현 분리
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-014
    target: ㅅ
    forms: 낫다 / 나아 / 나으니
    xy_same_lineage_declared: 'true'
    xy_verification: LINEAGE_LINK_VERIFIED
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: 현대 ㅅ 불규칙 활용
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-015
    target: ㅅ
    forms: 붓다 / 부어 / 부으니
    xy_same_lineage_declared: 'true'
    xy_verification: LINEAGE_LINK_VERIFIED
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`POSITION_RELATION_VERIFIED`'
    yz_boundary: 현대 ㅅ 불규칙 활용
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - relation_id: Y-POS-016
    target: ㅅ
    forms: 짓다 / 지어 / 지으니
    xy_same_lineage_declared: 'false'
    xy_verification: SOURCE_CONFLICT
    xy_cross_relation: MISSING_COUNTERPART
    yz_verification: '`MISSING_SOURCE_LOCATION`'
    yz_boundary: 검색 색인만 확보; 직접 표제어·발음 상세 필요
    canonical_3d_state: CROSS_RESULT_CONFLICT
  pronunciation_claims:
  - claim_id: PRON-001
    form: 강이
    reported_pronunciation: '[강이]'
    xy_claim_type: DICTIONARY_REPORTED
    yz_directive_state: DICTIONARY_REPORTED
    source_subtype: OFFICIAL_EXPLANATORY_RESPONSE
    rule_or_change: ㅇ 받침 비연음
    source_ref: SRC-004
    xy_verification: SOURCE_POSITION_VERIFIED
    direct_attestation: false
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - claim_id: PRON-002
    form: 목이
    reported_pronunciation: '[모기]'
    xy_claim_type: OFFICIAL_NORM_EXAMPLE
    yz_directive_state: DICTIONARY_REPORTED
    source_subtype: OFFICIAL_NORM_EXAMPLE
    rule_or_change: 제13항 연음
    source_ref: SRC-002
    xy_verification: SOURCE_POSITION_VERIFIED
    direct_attestation: false
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - claim_id: PRON-003
    form: 깎아
    reported_pronunciation: '[까까]'
    xy_claim_type: OFFICIAL_NORM_EXAMPLE
    yz_directive_state: DICTIONARY_REPORTED
    source_subtype: OFFICIAL_NORM_EXAMPLE
    rule_or_change: 제13항 연음
    source_ref: SRC-002
    xy_verification: SOURCE_POSITION_VERIFIED
    direct_attestation: false
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - claim_id: PRON-004
    form: 옷
    reported_pronunciation: '[옫]'
    xy_claim_type: OFFICIAL_NORM_EXAMPLE
    yz_directive_state: DICTIONARY_REPORTED
    source_subtype: OFFICIAL_NORM_EXAMPLE
    rule_or_change: 제9항 음절 끝소리
    source_ref: SRC-016
    xy_verification: SOURCE_POSITION_VERIFIED
    direct_attestation: false
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - claim_id: PRON-005
    form: 옷이
    reported_pronunciation: '[오시]'
    xy_claim_type: OFFICIAL_NORM_EXAMPLE
    yz_directive_state: DICTIONARY_REPORTED
    source_subtype: OFFICIAL_NORM_EXAMPLE
    rule_or_change: 제13항 연음
    source_ref: SRC-016
    xy_verification: SOURCE_POSITION_VERIFIED
    direct_attestation: false
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - claim_id: PRON-006
    form: 솜이불
    reported_pronunciation: '[솜ː니불]'
    xy_claim_type: OFFICIAL_NORM_EXAMPLE
    yz_directive_state: DICTIONARY_REPORTED
    source_subtype: OFFICIAL_NORM_EXAMPLE
    rule_or_change: 제29항 ㄴ 첨가
    source_ref: SRC-002
    xy_verification: SOURCE_POSITION_VERIFIED
    direct_attestation: false
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - claim_id: PRON-007
    form: 색연필
    reported_pronunciation: '[생년필]'
    xy_claim_type: OFFICIAL_NORM_EXAMPLE
    yz_directive_state: DICTIONARY_REPORTED
    source_subtype: OFFICIAL_NORM_EXAMPLE
    rule_or_change: ㄴ 첨가+비음화
    source_ref: SRC-002
    xy_verification: SOURCE_POSITION_VERIFIED
    direct_attestation: false
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - claim_id: PRON-008
    form: 낫다/나아
    reported_pronunciation: '[낟ː따]/[나아]'
    xy_claim_type: DICTIONARY_REPORTED
    yz_directive_state: DICTIONARY_REPORTED
    source_subtype: OFFICIAL_DICTIONARY_ENTRY
    rule_or_change: ㅅ 불규칙 활용
    source_ref: SRC-014
    xy_verification: SOURCE_POSITION_VERIFIED
    direct_attestation: false
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - claim_id: PRON-009
    form: 붓다/부어
    reported_pronunciation: '[붇ː따]/[부어]'
    xy_claim_type: DICTIONARY_REPORTED
    yz_directive_state: DICTIONARY_REPORTED
    source_subtype: OFFICIAL_DICTIONARY_ENTRY
    rule_or_change: ㅅ 불규칙 활용
    source_ref: SRC-013
    xy_verification: SOURCE_POSITION_VERIFIED
    direct_attestation: false
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - claim_id: PRON-010
    form: 같다
    reported_pronunciation: '[갇따]'
    xy_claim_type: DICTIONARY_REPORTED
    yz_directive_state: DICTIONARY_REPORTED
    source_subtype: OFFICIAL_DICTIONARY_HISTORY
    rule_or_change: 현대 표준 발음
    source_ref: SRC-009
    xy_verification: SOURCE_POSITION_VERIFIED
    direct_attestation: false
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
  - claim_id: PRON-011
    form: 싶다/싶어
    reported_pronunciation: '[십따]/[시퍼]'
    xy_claim_type: DICTIONARY_REPORTED
    yz_directive_state: DICTIONARY_REPORTED
    source_subtype: OFFICIAL_DICTIONARY_HISTORY
    rule_or_change: 현대 활용
    source_ref: SRC-010
    xy_verification: SOURCE_POSITION_VERIFIED
    direct_attestation: false
    canonical_3d_state: PARTIALLY_CROSS_CONFIRMED
```
## 22. Raw-to-Normalized Lineage

```yaml
lineage_count: 6
raw_to_normalized_lineage:
- entry_id: RAW-NORM-001
  raw_value: '`다 / 다`'
  raw_source: gpt.y→gpt.yz bound historical/position data
  normalized_value: 같다
  normalization_operations: PRESERVE_RAW_AND_CONNECT_TO_NORMALIZED_ENDPOINT
  normalization_loss: 현대 표기로 Raw 대체
  verified_by:
  - gpt.xy
  - gpt.yz
  correction_history: Raw form, period, source
- entry_id: RAW-NORM-002
  raw_value: '`식브다→십브다→시브다/시프다`'
  raw_source: gpt.y→gpt.yz bound historical/position data
  normalized_value: 싶다
  normalization_operations: PRESERVE_RAW_AND_CONNECT_TO_NORMALIZED_ENDPOINT
  normalization_loss: 단일 인과로 축약
  verified_by:
  - gpt.xy
  - gpt.yz
  correction_history: 단계순서와 원문형
- entry_id: RAW-NORM-003
  raw_value: '`삿기→새/색기`'
  raw_source: gpt.y→gpt.yz bound historical/position data
  normalized_value: 새끼
  normalization_operations: PRESERVE_RAW_AND_CONNECT_TO_NORMALIZED_ENDPOINT
  normalization_loss: 자모 Identity 자동병합
  verified_by:
  - gpt.xy
  - gpt.yz
  correction_history: ㅺ·ㄱ·ㄲ 표기층
- entry_id: RAW-NORM-004
  raw_value: '`이다→리다`'
  raw_source: gpt.y→gpt.yz bound historical/position data
  normalized_value: 깔리다
  normalization_operations: PRESERVE_RAW_AND_CONNECT_TO_NORMALIZED_ENDPOINT
  normalization_loss: 현대 ㅇ으로 자동치환
  verified_by:
  - gpt.xy
  - gpt.yz
  correction_history: 옛자모·시대·Source
- entry_id: RAW-NORM-005
  raw_value: '`니르다`'
  raw_source: gpt.y→gpt.yz bound historical/position data
  normalized_value: 이르다
  normalization_operations: PRESERVE_RAW_AND_CONNECT_TO_NORMALIZED_ENDPOINT
  normalization_loss: 한자어 두음법칙과 완전 동일시
  verified_by:
  - gpt.xy
  - gpt.yz
  correction_history: 역사형·현대형 분리
- entry_id: RAW-NORM-006
  raw_value: '`ㆁ / ㅇ`'
  raw_source: gpt.y→gpt.yz bound historical/position data
  normalized_value: 현대 ㅇ 후보
  normalization_operations: PRESERVE_RAW_AND_CONNECT_TO_NORMALIZED_ENDPOINT
  normalization_loss: 단일 문자계보 확정
  verified_by:
  - gpt.xy
  - gpt.yz
  correction_history: 자모·음가·위치층
normalization_guard: Normalization is not source replacement.
```
## 23. 2d Verification Matrix

### `XYZ-VERIFY-001` — Exact 2D Result byte identities

```yaml
canonical_cross_state: CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Exact 2D Result byte identities
  judgment_state: PASS
  evidence_basis: Filename SHA-256 equals recalculated exact byte SHA-256.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Exact 2D Result byte identities
  judgment_state: PASS
  evidence_basis: Filename SHA-256 equals recalculated exact byte SHA-256.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Exact 2D Result byte identities
  judgment_state: PASS
  evidence_basis: Filename SHA-256 equals recalculated exact byte SHA-256.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
```
### `XYZ-VERIFY-002` — Modern Hangul NFC/NFD and syllable decomposition

```yaml
canonical_cross_state: CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Modern Hangul NFC/NFD and syllable decomposition
  judgment_state: PASS_60_OF_60
  evidence_basis: Independent mechanical recomputation in all three 2D results.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Modern Hangul NFC/NFD and syllable decomposition
  judgment_state: PASS_X60_Z80_RIME62
  evidence_basis: Independent mechanical recomputation in all three 2D results.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Modern Hangul NFC/NFD and syllable decomposition
  judgment_state: PASS_HANJA_READING80_AND_IEUNG45
  evidence_basis: Independent mechanical recomputation in all three 2D results.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
```
### `XYZ-VERIFY-003` — Native lexical surface inventory

```yaml
canonical_cross_state: PARTIALLY_CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Native lexical surface inventory
  judgment_state: 60 distinct; 13 exact target-code verified; 47 reentry-only
  evidence_basis: XY and XZ agree on typed counts and source-location boundary.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Native lexical surface inventory
  judgment_state: 60 distinct; 13 exact; 47 exact source locations missing
  evidence_basis: XY and XZ agree on typed counts and source-location boundary.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Native lexical surface inventory
  judgment_state: NOT_APPLICABLE
  evidence_basis: XY and XZ agree on typed counts and source-location boundary.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
```
### `XYZ-VERIFY-004` — Hanja Unicode identity

```yaml
canonical_cross_state: PARTIALLY_CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Hanja Unicode identity
  judgment_state: NOT_APPLICABLE
  evidence_basis: XZ and YZ independently reproduce codepoint/decomposition identity.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Hanja Unicode identity
  judgment_state: PASS_80_OF_80
  evidence_basis: XZ and YZ independently reproduce codepoint/decomposition identity.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Hanja Unicode identity
  judgment_state: PASS_80_OF_80
  evidence_basis: XZ and YZ independently reproduce codepoint/decomposition identity.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
```
### `XYZ-VERIFY-005` — Hanja reading and representative hun authority

```yaml
canonical_cross_state: PARTIALLY_CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Hanja reading and representative hun authority
  judgment_state: NOT_APPLICABLE
  evidence_basis: Both seats preserve the same source-authority limitation.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Hanja reading and representative hun authority
  judgment_state: TIER3_LINE_BOUND; OFFICIAL_XLS_AND_DETAILS_MISSING
  evidence_basis: Both seats preserve the same source-authority limitation.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Hanja reading and representative hun authority
  judgment_state: TIER3_SOURCE_BOUND; INDEPENDENT_OFFICIAL_CROSSCHECK_ZERO
  evidence_basis: Both seats preserve the same source-authority limitation.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
```
### `XYZ-VERIFY-006` — Hanja usage source location

```yaml
canonical_cross_state: PARTIALLY_CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Hanja usage source location
  judgment_state: NOT_APPLICABLE
  evidence_basis: Both seats classify exact usage location as missing.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Hanja usage source location
  judgment_state: 80 query routes; 0 detail word_no
  evidence_basis: Both seats classify exact usage location as missing.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Hanja usage source location
  judgment_state: 80 query URLs; 0 stable detail IDs
  evidence_basis: Both seats classify exact usage location as missing.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
```
### `XYZ-VERIFY-007` — Modern same-syllable different-Hanja groups

```yaml
canonical_cross_state: PARTIALLY_CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Modern same-syllable different-Hanja groups
  judgment_state: NOT_APPLICABLE
  evidence_basis: Group membership agrees; historical projection prohibited.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Modern same-syllable different-Hanja groups
  judgment_state: 19 groups mechanically verified
  evidence_basis: Group membership agrees; historical projection prohibited.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Modern same-syllable different-Hanja groups
  judgment_state: 19 groups modern-only; no historical identity inference
  evidence_basis: Group membership agrees; historical projection prohibited.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
```
### `XYZ-VERIFY-008` — Modern same-rime different-initial sets

```yaml
canonical_cross_state: PARTIALLY_CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Modern same-rime different-initial sets
  judgment_state: NOT_APPLICABLE
  evidence_basis: Modern orthographic set relation agrees; phonetic/historical scope open.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Modern same-rime different-initial sets
  judgment_state: 16 sets mechanically verified; 2 explicit onset gaps
  evidence_basis: Modern orthographic set relation agrees; phonetic/historical scope open.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Modern same-rime different-initial sets
  judgment_state: 16 modern orthographic sets; no historical rime bound
  evidence_basis: Modern orthographic set relation agrees; phonetic/historical scope open.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
```
### `XYZ-VERIFY-009` — Orthographic initial ㅇ, phonetic Ø and coda ㅇ [ŋ]

```yaml
canonical_cross_state: CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Orthographic initial ㅇ, phonetic Ø and coda ㅇ [ŋ]
  judgment_state: CROSS_VERIFIED_MODERN_SPLIT
  evidence_basis: All three seats preserve modern fields as distinct.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Orthographic initial ㅇ, phonetic Ø and coda ㅇ [ŋ]
  judgment_state: PASS_IEUNG_ZERO_ONSET_CODA_SEPARATION
  evidence_basis: All three seats preserve modern fields as distinct.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Orthographic initial ㅇ, phonetic Ø and coda ㅇ [ŋ]
  judgment_state: PASS_MODERN_LAYER; HISTORICAL_PROJECTION_PROHIBITED
  evidence_basis: All three seats preserve modern fields as distinct.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
```
### `XYZ-VERIFY-010` — Position relations

```yaml
canonical_cross_state: PARTIALLY_CROSS_CONFIRMED_WITH_CONFLICTS
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Position relations
  judgment_state: 14 verified/scoped; 2 source conflicts
  evidence_basis: XY and YZ agree on most relations and preserve Y-POS-004/Y-POS-016 gaps.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Position relations
  judgment_state: NOT_APPLICABLE_TO_Y_POSITION_LEDGER
  evidence_basis: XY and YZ agree on most relations and preserve Y-POS-004/Y-POS-016 gaps.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Position relations
  judgment_state: 14 verified; 1 unsupported lineage; 1 missing source
  evidence_basis: XY and YZ agree on most relations and preserve Y-POS-004/Y-POS-016 gaps.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
```
### `XYZ-VERIFY-011` — Historical–modern lineages

```yaml
canonical_cross_state: CROSS_RESULT_CONFLICT
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Historical–modern lineages
  judgment_state: 9 source-reported; 2 source conflicts
  evidence_basis: Seat classifications differ for ㆁ, 女, 年 and 잎/닢; all positions retained.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: true
  unresolved: true
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Historical–modern lineages
  judgment_state: NOT_APPLICABLE
  evidence_basis: Seat classifications differ for ㆁ, 女, 年 and 잎/닢; all positions retained.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: true
  unresolved: true
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Historical–modern lineages
  judgment_state: 5 verified; 2 reclassified as modern position; 1 unsupported; 1 multiple candidates
  evidence_basis: Seat classifications differ for ㆁ, 女, 年 and 잎/닢; all positions retained.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: true
  unresolved: true
```
### `XYZ-VERIFY-012` — Modern pronunciation claims

```yaml
canonical_cross_state: PARTIALLY_CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Modern pronunciation claims
  judgment_state: 11 source-position verified
  evidence_basis: Source-reported values agree; direct-observation boundary is added.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Modern pronunciation claims
  judgment_state: NOT_APPLICABLE
  evidence_basis: Source-reported values agree; direct-observation boundary is added.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Modern pronunciation claims
  judgment_state: 11 typed as dictionary/official reported; 0 direct recordings
  evidence_basis: Source-reported values agree; direct-observation boundary is added.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
```
### `XYZ-VERIFY-013` — Raw–normalized preservation

```yaml
canonical_cross_state: CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Raw–normalized preservation
  judgment_state: PASS_WITH_RAW_LOCATION_LIMITS
  evidence_basis: No 2D seat reports source replacement or Old Hangul loss.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Raw–normalized preservation
  judgment_state: PASS_NO_SEMANTIC_REWRITE
  evidence_basis: No 2D seat reports source replacement or Old Hangul loss.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Raw–normalized preservation
  judgment_state: PASS_WITH_LINEAGE_CORRECTIONS
  evidence_basis: No 2D seat reports source replacement or Old Hangul loss.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
```
### `XYZ-VERIFY-014` — Duplicate inflation

```yaml
canonical_cross_state: CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Duplicate inflation
  judgment_state: PASS_ZERO
  evidence_basis: Record links and identity counts remain separate.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Duplicate inflation
  judgment_state: PASS_ZERO
  evidence_basis: Record links and identity counts remain separate.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Duplicate inflation
  judgment_state: IDENTITY_MERGE_ZERO_IN_HOMOPHONE_GROUPS
  evidence_basis: Record links and identity counts remain separate.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
```
### `XYZ-VERIFY-015` — No-coda–coda relations

```yaml
canonical_cross_state: SINGLE_SEAT_ONLY
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: No-coda–coda relations
  judgment_state: 10 candidates; 0 direct snapshots
  evidence_basis: Only XY carries the registry; exact 1D records are not direct 3D inputs.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: No-coda–coda relations
  judgment_state: NOT_APPLICABLE
  evidence_basis: Only XY carries the registry; exact 1D records are not direct 3D inputs.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: No-coda–coda relations
  judgment_state: NOT_APPLICABLE
  evidence_basis: Only XY carries the registry; exact 1D records are not direct 3D inputs.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
```
### `XYZ-VERIFY-016` — Source-location insufficiency

```yaml
canonical_cross_state: CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Source-location insufficiency
  judgment_state: 47 X entries, examples, historical details unresolved
  evidence_basis: All three seats preserve missing-source-location states.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Source-location insufficiency
  judgment_state: HOLD_WITH_INSUFFICIENT_SOURCE_LOCATION
  evidence_basis: All three seats preserve missing-source-location states.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Source-location insufficiency
  judgment_state: Multiple missing stable detail/source locations
  evidence_basis: All three seats preserve missing-source-location states.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: false
```
### `XYZ-VERIFY-017` — Modern same syllable/rime to historical lineage

```yaml
canonical_cross_state: PARTIALLY_CROSS_CONFIRMED
seat_judgments:
- source_seat: HRTDB_A::gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  object_identity: Modern same syllable/rime to historical lineage
  judgment_state: NOT_APPLICABLE
  evidence_basis: XZ and YZ independently prohibit projection.
  source_locations: SEE_GPT_XY_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  object_identity: Modern same syllable/rime to historical lineage
  judgment_state: STRUCTURAL_EQUIVALENCE_PROHIBITED
  evidence_basis: XZ and YZ independently prohibit projection.
  source_locations: SEE_GPT_XZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
- source_seat: HRTDB_A::gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  object_identity: Modern same syllable/rime to historical lineage
  judgment_state: HISTORICAL_INFERENCE_PROHIBITED
  evidence_basis: XZ and YZ independently prohibit projection.
  source_locations: SEE_GPT_YZ_ORIGINAL_JUDGMENT
  conflict_with_other_seat: false
  unresolved: true
```
## 24. Cross-confirmed Data

```yaml
definition: All applicable seat judgments align within their stated scope.
count: 6
records:
- object_identity: Exact 2D Result byte identities
  xy_state: PASS
  xz_state: PASS
  yz_state: PASS
  canonical_state: CROSS_CONFIRMED
  evidence_basis: Filename SHA-256 equals recalculated exact byte SHA-256.
- object_identity: Modern Hangul NFC/NFD and syllable decomposition
  xy_state: PASS_60_OF_60
  xz_state: PASS_X60_Z80_RIME62
  yz_state: PASS_HANJA_READING80_AND_IEUNG45
  canonical_state: CROSS_CONFIRMED
  evidence_basis: Independent mechanical recomputation in all three 2D results.
- object_identity: Orthographic initial ㅇ, phonetic Ø and coda ㅇ [ŋ]
  xy_state: CROSS_VERIFIED_MODERN_SPLIT
  xz_state: PASS_IEUNG_ZERO_ONSET_CODA_SEPARATION
  yz_state: PASS_MODERN_LAYER; HISTORICAL_PROJECTION_PROHIBITED
  canonical_state: CROSS_CONFIRMED
  evidence_basis: All three seats preserve modern fields as distinct.
- object_identity: Raw–normalized preservation
  xy_state: PASS_WITH_RAW_LOCATION_LIMITS
  xz_state: PASS_NO_SEMANTIC_REWRITE
  yz_state: PASS_WITH_LINEAGE_CORRECTIONS
  canonical_state: CROSS_CONFIRMED
  evidence_basis: No 2D seat reports source replacement or Old Hangul loss.
- object_identity: Duplicate inflation
  xy_state: PASS_ZERO
  xz_state: PASS_ZERO
  yz_state: IDENTITY_MERGE_ZERO_IN_HOMOPHONE_GROUPS
  canonical_state: CROSS_CONFIRMED
  evidence_basis: Record links and identity counts remain separate.
- object_identity: Source-location insufficiency
  xy_state: 47 X entries, examples, historical details unresolved
  xz_state: HOLD_WITH_INSUFFICIENT_SOURCE_LOCATION
  yz_state: Multiple missing stable detail/source locations
  canonical_state: CROSS_CONFIRMED
  evidence_basis: All three seats preserve missing-source-location states.
universal_truth_claim: false
```
## 25. Partially Confirmed Data

```yaml
definition: At least two seats align or one seat is not applicable; missing/contrary positions remain explicit.
count: 9
records:
- object_identity: Native lexical surface inventory
  xy_state: 60 distinct; 13 exact target-code verified; 47 reentry-only
  xz_state: 60 distinct; 13 exact; 47 exact source locations missing
  yz_state: NOT_APPLICABLE
  canonical_state: PARTIALLY_CROSS_CONFIRMED
  evidence_basis: XY and XZ agree on typed counts and source-location boundary.
- object_identity: Hanja Unicode identity
  xy_state: NOT_APPLICABLE
  xz_state: PASS_80_OF_80
  yz_state: PASS_80_OF_80
  canonical_state: PARTIALLY_CROSS_CONFIRMED
  evidence_basis: XZ and YZ independently reproduce codepoint/decomposition identity.
- object_identity: Hanja reading and representative hun authority
  xy_state: NOT_APPLICABLE
  xz_state: TIER3_LINE_BOUND; OFFICIAL_XLS_AND_DETAILS_MISSING
  yz_state: TIER3_SOURCE_BOUND; INDEPENDENT_OFFICIAL_CROSSCHECK_ZERO
  canonical_state: PARTIALLY_CROSS_CONFIRMED
  evidence_basis: Both seats preserve the same source-authority limitation.
- object_identity: Hanja usage source location
  xy_state: NOT_APPLICABLE
  xz_state: 80 query routes; 0 detail word_no
  yz_state: 80 query URLs; 0 stable detail IDs
  canonical_state: PARTIALLY_CROSS_CONFIRMED
  evidence_basis: Both seats classify exact usage location as missing.
- object_identity: Modern same-syllable different-Hanja groups
  xy_state: NOT_APPLICABLE
  xz_state: 19 groups mechanically verified
  yz_state: 19 groups modern-only; no historical identity inference
  canonical_state: PARTIALLY_CROSS_CONFIRMED
  evidence_basis: Group membership agrees; historical projection prohibited.
- object_identity: Modern same-rime different-initial sets
  xy_state: NOT_APPLICABLE
  xz_state: 16 sets mechanically verified; 2 explicit onset gaps
  yz_state: 16 modern orthographic sets; no historical rime bound
  canonical_state: PARTIALLY_CROSS_CONFIRMED
  evidence_basis: Modern orthographic set relation agrees; phonetic/historical scope open.
- object_identity: Position relations
  xy_state: 14 verified/scoped; 2 source conflicts
  xz_state: NOT_APPLICABLE_TO_Y_POSITION_LEDGER
  yz_state: 14 verified; 1 unsupported lineage; 1 missing source
  canonical_state: PARTIALLY_CROSS_CONFIRMED_WITH_CONFLICTS
  evidence_basis: XY and YZ agree on most relations and preserve Y-POS-004/Y-POS-016 gaps.
- object_identity: Modern pronunciation claims
  xy_state: 11 source-position verified
  xz_state: NOT_APPLICABLE
  yz_state: 11 typed as dictionary/official reported; 0 direct recordings
  canonical_state: PARTIALLY_CROSS_CONFIRMED
  evidence_basis: Source-reported values agree; direct-observation boundary is added.
- object_identity: Modern same syllable/rime to historical lineage
  xy_state: NOT_APPLICABLE
  xz_state: STRUCTURAL_EQUIVALENCE_PROHIBITED
  yz_state: HISTORICAL_INFERENCE_PROHIBITED
  canonical_state: PARTIALLY_CROSS_CONFIRMED
  evidence_basis: XZ and YZ independently prohibit projection.
```
## 26. Single-Seat-Only Data

```yaml
definition: Present in one direct 2D result only; not promoted by absence of counterpart.
count: 1
records:
- object_identity: No-coda–coda relations
  xy_state: 10 candidates; 0 direct snapshots
  xz_state: NOT_APPLICABLE
  yz_state: NOT_APPLICABLE
  canonical_state: SINGLE_SEAT_ONLY
  evidence_basis: Only XY carries the registry; exact 1D records are not direct 3D inputs.
```
## 27. Source Conflicts

```yaml
gpt_xy_source_conflicts:
- Conflict: X-CF-01
  Surface: X
  Object: 동형어 번호
  Difference: 날·눈·길·김·살·새·샘·술 등은 여러 사전 의미/동형어가 가능함.
  Preservation: Target code 없는 재진입 항목은 선택 Sense를 확정하지 않음.
  State: UNRESOLVED
- Conflict: X-CF-02
  Surface: X
  Object: 발음 길이
  Difference: 일부 표제어의 장단 표시는 사전 항목별 확인이 필요함.
  Preservation: 이번 Normalized 발음은 음절 표면을 우선 보존하고 미검증 장단을 추가하지 않음.
  State: UNRESOLVED
- Conflict: X-CF-03
  Surface: X
  Object: 낮/넋/늪/숲
  Difference: 표기 종성과 대표 발음이 다름.
  Preservation: 낮 [낟], 넋 [넉], 늪 [늡], 숲 [숩]을 표기와 발음으로 분리.
  State: UNRESOLVED
- Conflict: X-CF-04
  Surface: X
  Object: 초성 ㅇ/종성 ㅇ
  Difference: 같은 문자 ㅇ이 위치에 따라 음가가 다름.
  Preservation: 초성 표기 ㅇ, 음성 Ø, 종성 [ŋ]을 별도 필드로 보존.
  State: UNRESOLVED
- Conflict: Y-CONFLICT-001
  Surface: Y
  Object: 초성 ㅇ의 중세 음가
  Difference: 끊어적기에서 나타난 초성 ㅇ은 음가가 있는 것으로 본다. ↔ 그 밖의 초성 ㅇ은 음가가 없는 것으로 본다.
  Preservation: CONTEXT_DEPENDENT_HISTORICAL_PHONOLOGY
  State: UNRESOLVED
- Conflict: Y-CONFLICT-002
  Surface: Y
  Object: ㄴㄴ 첨가 분석
  Difference: 사이시옷 첨가 뒤 ㄴ 첨가와 자음동화로 설명. ↔ 사이시옷 첨가 조건이 충족되지 않는다는 반론이 해설에 병기됨.
  Preservation: ANALYSIS_COMPETITION
  State: UNRESOLVED
- Conflict: Y-CONFLICT-003
  Surface: Y
  Object: 니르다→이르다 현상 명명
  Difference: 국립국어원 답변은 어두 ㄴ 탈락 및 두음법칙 적용 이전/이후로 설명. ↔ 온라인가나다는 상세 연구자 견해 차이 가능성을 열어 둠.
  Preservation: TERMINOLOGY_AND_PERIODIZATION
  State: UNRESOLVED
- Conflict: Y-CONFLICT-004
  Surface: Y
  Object: 짓다 활용 Source identity
  Difference: 공식 검색 색인에 지어·지으니 등 활용이 제시됨. ↔ 직접 표제어 상세 URL과 발음 필드를 확보하지 못함.
  Preservation: SOURCE_IDENTITY_WEAKNESS
  State: UNRESOLVED
- Conflict: XY-CONFLICT-001
  Surface: XY
  Object: Modern ㅇ vs historical ㆁ/ㅇ
  Difference: Modern phonology is direct norm; historical sound/character relation is reported and incomplete
  Preservation: Temporal and evidence-class split
  State: UNRESOLVED
- Conflict: XY-CONFLICT-002
  Surface: XY
  Object: Root=Lemma fields
  Difference: X normalized nominal roots lack item-level morphology source
  Preservation: Retain value as placeholder; do not promote
  State: UNRESOLVED
- Conflict: XY-CONFLICT-003
  Surface: XY
  Object: Definition/example source location
  Difference: Short glosses and examples are not bound to exact raw locations for all entries
  Preservation: MISSING_SOURCE_LOCATION
  State: UNRESOLVED
- Conflict: XY-CONFLICT-004
  Surface: XY
  Object: Source record count vs unique source identity
  Difference: Y SRC-002 and SRC-017 are same canonical document
  Preservation: Count records and unique identities separately
  State: RESOLVED_IN_VERIFICATION_CLASSIFICATION
- Conflict: XY-CONFLICT-005
  Surface: XY
  Object: No exact cross lexeme
  Difference: Consonant group overlap exists but same surface+lemma overlap is zero
  Preservation: No inferred lineage
  State: PRESERVED
gpt_xz_source_conflicts:
- conflict_id: XZ-CF-001
  subject: X_47_entries_without_target_code
  state: MISSING_SOURCE_LOCATION
  preservation: keep_official_reentry_route_and_do_not_claim_exact_entry_verification
- conflict_id: XZ-CF-002
  subject: X_9_homonym_or_sense_identities
  state: UNCERTAIN_IDENTITY
  preservation: do_not_select_sense_without_target_code
- conflict_id: XZ-CF-003
  subject: X_60_example_sentences
  state: MISSING_SOURCE_LOCATION
  preservation: reclassify_as_normalized_illustrative_examples_not_source_quotes
- conflict_id: XZ-CF-004
  subject: official_Hanja_XLS_vs_transformed_CSV
  state: SOURCE_CONFLICT
  preservation: transformed_CSV_remains_Tier3
- conflict_id: XZ-CF-005
  subject: Z_80_usage_words_without_detail_word_no
  state: MISSING_SOURCE_LOCATION
  preservation: query_URL_is_reentry_route_not_exact_source_position
- conflict_id: XZ-CF-006
  subject: Rime_43_Sino_members_outside_core_identity_registry
  state: UNCERTAIN_IDENTITY
  preservation: do_not_promote_to_full_Hanja_identity_record
- conflict_id: XZ-CF-007
  subject: SINO_SURFACE_and_SINO_NONINITIAL_members
  state: SOURCE_CONFLICT
  preservation: split_canonical_reading_from_usage_surface_and_position
- conflict_id: XZ-CF-008
  subject: anonymous_ieung_supplementary_records
  state: NORMALIZATION_ERROR
  preservation: values_preserved_but_stable_record_ID_required
- conflict_id: XZ-CF-009
  subject: variant_拿_拏
  state: UNCERTAIN_IDENTITY
  preservation: link_without_merge_and_materialize_separate_identity_only_with_source
- conflict_id: XZ-CF-010
  subject: orthographic_coda_vs_standard_pronunciation
  state: SOURCE_CONFLICT
  preservation: keep_낮_넋_늪_숲_spelling_and_pronunciation_separate
gpt_yz_source_conflicts:
- conflict_id: YZ-CONFLICT-001
  object_identity: 초성 ㆁ과 현대 ㅇ의 단일계보
  claim_a: Y-HIST-001
  source_a: Bound Data.Y position/history/conflict records
  claim_b: Y-POS-004
  source_b: Bound Data.Z identity/control/conflict records or Data.Y counter-position
  conflict_type: MODERN_HISTORICAL_LINK_CONFLICT
  resolved: false
  required_next_data: ㆁ·현대 초성 ㅇ·현대 종성 ㅇ을 별 객체후보로 병렬 보존하고 전문 국어사 Source를 추가한다.
- conflict_id: YZ-CONFLICT-002
  object_identity: 女의 녀/여 분류
  claim_a: Y-HIST-004
  source_a: Bound Data.Y position/history/conflict records
  claim_b: Z-HANJA-053 + SRC-003
  source_b: Bound Data.Z identity/control/conflict records or Data.Y counter-position
  conflict_type: CHANGE_PERIOD_CONFLICT
  resolved: false
  required_next_data: 역사단계가 아니라 동일 Hanja Identity의 현대 위치조건으로 재분류한다.
- conflict_id: YZ-CONFLICT-003
  object_identity: 年의 년/연 분류
  claim_a: Y-HIST-005
  source_a: Bound Data.Y position/history/conflict records
  claim_b: Z-HANJA-054 + SRC-003
  source_b: Bound Data.Z identity/control/conflict records or Data.Y counter-position
  conflict_type: CHANGE_PERIOD_CONFLICT
  resolved: false
  required_next_data: 역사단계가 아니라 현대 위치·의존명사 조건으로 재분류한다.
- conflict_id: YZ-CONFLICT-004
  object_identity: 현대 ㅇ의 표기·음가와 역사 초성의 투사
  claim_a: Y-POS-003/004
  source_a: Bound Data.Y position/history/conflict records
  claim_b: Z IEUNG-001..045
  source_b: Bound Data.Z identity/control/conflict records or Data.Y counter-position
  conflict_type: RECONSTRUCTION_CONFLICT
  resolved: false
  required_next_data: Z의 ㅇ 기록은 현대 철자·현대 음가층으로만 유지하고 역사 ㆁ/ㅇ에 소급하지 않는다.
- conflict_id: YZ-CONFLICT-005
  object_identity: 한자 Reading Source Authority
  claim_a: Z-HANJA-001..080
  source_a: Bound Data.Y position/history/conflict records
  claim_b: Z-CONFLICT-001/GAP-004
  source_b: Bound Data.Z identity/control/conflict records or Data.Y counter-position
  conflict_type: HANJA_READING_CONFLICT
  resolved: false
  required_next_data: 80개 독음은 변환 CSV Source-bound로 유지하고 공식 원 XLS·공식 한자사전 교차검증 전까지 독립 정본으로 승격하지 않는다.
- conflict_id: YZ-CONFLICT-006
  object_identity: 동음·동운모와 역사계보
  claim_a: Z-HOMOPHONE-001..019
  source_a: Bound Data.Y position/history/conflict records
  claim_b: Z-RIME-001..016
  source_b: Bound Data.Z identity/control/conflict records or Data.Y counter-position
  conflict_type: MODERN_HISTORICAL_LINK_CONFLICT
  resolved: false
  required_next_data: 현대 음절·현대 철자운모 Group만 검증하고 역사발음·역사운모 동일성은 미확정으로 둔다.
- conflict_id: YZ-CONFLICT-007
  object_identity: 짓다 Source Identity
  claim_a: Y-POS-016/Y-CONFLICT-004
  source_a: Bound Data.Y position/history/conflict records
  claim_b: SRC-015
  source_b: Bound Data.Z identity/control/conflict records or Data.Y counter-position
  conflict_type: MISSING_SOURCE_LOCATION
  resolved: false
  required_next_data: 활용 색인은 보존하되 직접 표제어·발음 상세가 결속되기 전 완전검증으로 승격하지 않는다.
deletion_count: 0
```
## 28. Cross-Result Conflicts

### `XYZ-CROSS-CONFLICT-001` — Historical ㆁ vs modern onset/coda ㅇ lineage

```yaml
cross_result_conflict:
  conflict_id: XYZ-CROSS-CONFLICT-001
  object_identity: Historical ㆁ vs modern onset/coda ㅇ lineage
  xy_state: SOURCE_CONFLICT / PARTIAL_CROSS_MATCH
  xz_state: Modern orthographic/phonetic split only; historical analysis excluded
  yz_state: UNSUPPORTED_LINEAGE_LINK + MULTIPLE_LINEAGE_CANDIDATES
  source_locations:
  - XY Y-POS-004/Y-HIST-001
  - XZ ㅇ–Ø–coda audit
  - YZ YZ-CONFLICT-001/004
  conflict_type: MODERN_HISTORICAL_LINK_CONFLICT
  correction_candidate: Split historical onset ㆁ, modern empty onset ㅇ and modern coda ㅇ as separate lineage candidates.
  correction_applied: false
  unresolved: true
```
### `XYZ-CROSS-CONFLICT-002` — 女 녀/여 classification

```yaml
cross_result_conflict:
  conflict_id: XYZ-CROSS-CONFLICT-002
  object_identity: 女 녀/여 classification
  xy_state: Historical lineage source-reported
  xz_state: Canonical reading vs usage surface field split required
  yz_state: Modern position relation; historical reading not verified
  source_locations:
  - XY Y-HIST-004/Y-POS-009
  - XZ affected surface/noninitial members
  - YZ YZ-CONFLICT-002
  conflict_type: POSITION_VS_HISTORICAL_CLASSIFICATION
  correction_candidate: Reclassify canonical 3D record as modern position-conditioned surface relation; retain historical claim as seat judgment
    only.
  correction_applied: true
  unresolved: Historical reading remains unresolved.
```
### `XYZ-CROSS-CONFLICT-003` — 年 년/연 classification

```yaml
cross_result_conflict:
  conflict_id: XYZ-CROSS-CONFLICT-003
  object_identity: 年 년/연 classification
  xy_state: Historical lineage source-reported
  xz_state: Canonical reading vs usage surface field split required
  yz_state: Modern position/dependent-noun relation; historical reading not verified
  source_locations:
  - XY Y-HIST-005/Y-POS-010
  - XZ affected surface/noninitial members
  - YZ YZ-CONFLICT-003
  conflict_type: POSITION_VS_HISTORICAL_CLASSIFICATION
  correction_candidate: Reclassify canonical 3D record as modern position/dependent-noun relation; preserve historical seat judgment.
  correction_applied: true
  unresolved: Historical reading and detailed chain pronunciations remain unresolved.
```
### `XYZ-CROSS-CONFLICT-004` — Hanja reading and representative hun authority

```yaml
cross_result_conflict:
  conflict_id: XYZ-CROSS-CONFLICT-004
  object_identity: Hanja reading and representative hun authority
  xy_state: NOT_APPLICABLE
  xz_state: 80 Tier3 transformed CSV rows; official XLS/detail verification HOLD
  yz_state: 80 source-bound reading links; independent official crosscheck 0
  source_locations:
  - XZ §6.1
  - YZ §7
  conflict_type: SOURCE_AUTHORITY_BOUNDARY
  correction_candidate: Retain Unicode Identity as verified; reading/hun as Tier3 transformed-source-bound.
  correction_applied: true
  unresolved: Official XLS and independent official detail sources required.
```
### `XYZ-CROSS-CONFLICT-005` — Modern same-syllable group vs historical reading lineage

```yaml
cross_result_conflict:
  conflict_id: XYZ-CROSS-CONFLICT-005
  object_identity: Modern same-syllable group vs historical reading lineage
  xy_state: NOT_APPLICABLE
  xz_state: Mechanical group structure verified; official detail missing
  yz_state: Modern same-syllable verified; historical equivalence prohibited
  source_locations:
  - XZ §8
  - YZ §10.1
  conflict_type: MODERN_HISTORICAL_PROJECTION_BOUNDARY
  correction_candidate: Name groups MODERN_SAME_SYLLABLE_GROUP and preserve Hanja identities separately.
  correction_applied: true
  unresolved: Historical readings absent.
```
### `XYZ-CROSS-CONFLICT-006` — Modern orthographic rime vs phonetic/historical rime

```yaml
cross_result_conflict:
  conflict_id: XYZ-CROSS-CONFLICT-006
  object_identity: Modern orthographic rime vs phonetic/historical rime
  xy_state: NOT_APPLICABLE
  xz_state: 16 mechanical sets; source locations incomplete
  yz_state: 16 modern orthographic sets; no historical or reconstructed rime bound
  source_locations:
  - XZ §9
  - YZ §10.2
  conflict_type: RIME_SCOPE_CONFLICT
  correction_candidate: Retain as MODERN_ORTHOGRAPHIC_RIME_CONTROL only.
  correction_applied: true
  unresolved: Modern phonetic and historical rime sources absent.
```
### `XYZ-CROSS-CONFLICT-007` — 60 unique X lexical surfaces vs verified unique Sense identities

```yaml
cross_result_conflict:
  conflict_id: XYZ-CROSS-CONFLICT-007
  object_identity: 60 unique X lexical surfaces vs verified unique Sense identities
  xy_state: 60 collected surfaces; 13 exact source identities
  xz_state: 60 unique records; 47 exact source locations missing
  yz_state: NOT_APPLICABLE
  source_locations:
  - XY §6/§14
  - XZ §5/§14
  conflict_type: QUANTITY_SEMANTICS
  correction_candidate: Separate reported/unique/source-verified counts.
  correction_applied: true
  unresolved: 47 target-code snapshots and 9 sense identities.
```
### `XYZ-CROSS-CONFLICT-008` — Pronunciation verification vs direct observation

```yaml
cross_result_conflict:
  conflict_id: XYZ-CROSS-CONFLICT-008
  object_identity: Pronunciation verification vs direct observation
  xy_state: 11 source-position verified claims
  xz_state: NOT_APPLICABLE
  yz_state: 11 dictionary/official reported; direct recordings 0
  source_locations:
  - XY §8
  - YZ §6
  conflict_type: CLAIM_TYPE_SCOPE
  correction_candidate: Canonical state DICTIONARY_OR_OFFICIAL_NORM_REPORTED; direct_attestation=false.
  correction_applied: true
  unresolved: Historical audio/direct instrumental evidence absent.
```
### `XYZ-CROSS-CONFLICT-009` — Root=Lemma normalization fields

```yaml
cross_result_conflict:
  conflict_id: XYZ-CROSS-CONFLICT-009
  object_identity: Root=Lemma normalization fields
  xy_state: Placeholders not morphologically proven
  xz_state: Internal native classification verified with source gaps
  yz_state: NOT_APPLICABLE
  source_locations:
  - XY §7/XY-CORR-002
  - XZ §5
  conflict_type: NORMALIZATION_VS_MORPHOLOGY
  correction_candidate: Keep values as normalization placeholders; no morphology promotion.
  correction_applied: true
  unresolved: Item-level morphological sources required.
```
### `XYZ-CROSS-CONFLICT-010` — 짓다 source identity

```yaml
cross_result_conflict:
  conflict_id: XYZ-CROSS-CONFLICT-010
  object_identity: 짓다 source identity
  xy_state: SOURCE_CONFLICT; direct detail absent
  xz_state: NOT_APPLICABLE
  yz_state: MISSING_SOURCE_LOCATION
  source_locations:
  - XY Y-POS-016/Y-CONFLICT-004
  - YZ YZ-CONFLICT-007
  conflict_type: MISSING_SOURCE_LOCATION
  correction_candidate: Retain relation candidate without full verification.
  correction_applied: true
  unresolved: true
```
## 29. Invalid Entries

```yaml
invalid_entries:
  mechanically_invalid_X_entries: 0
  mechanically_invalid_Hanja_entries: 0
  mechanically_invalid_same_syllable_members: 0
  mechanically_invalid_same_rime_members: 0
  nonexistent_member_proven: 0
  source_unverified_is_not_invalid: true
  normalization_error_candidates:
  - 10 anonymous ieung supplementary records lack stable IDs.
```
## 30. Uncertain Identities

```yaml
uncertain_identities:
  XY:
  - Input: X
    Object: 김
    State: UNCERTAIN_IDENTITY
    Reason: No individual target_code; homograph/polysemy risk
  - Input: X
    Object: 날
    State: UNCERTAIN_IDENTITY
    Reason: No individual target_code; homograph/polysemy risk
  - Input: X
    Object: 눈
    State: UNCERTAIN_IDENTITY
    Reason: No individual target_code; homograph/polysemy risk
  - Input: X
    Object: 살
    State: UNCERTAIN_IDENTITY
    Reason: No individual target_code; homograph/polysemy risk
  - Input: X
    Object: 새
    State: UNCERTAIN_IDENTITY
    Reason: No individual target_code; homograph/polysemy risk
  - Input: X
    Object: 샘
    State: UNCERTAIN_IDENTITY
    Reason: No individual target_code; homograph/polysemy risk
  - Input: X
    Object: 술
    State: UNCERTAIN_IDENTITY
    Reason: No individual target_code; homograph/polysemy risk
  - Input: X
    Object: 우리
    State: UNCERTAIN_IDENTITY
    Reason: No individual target_code; homograph/polysemy risk
  - Input: X
    Object: 이제
    State: UNCERTAIN_IDENTITY
    Reason: No individual target_code; homograph/polysemy risk
  - Input: Y
    Object: ㆁ and modern ㅇ complete lineage
    State: UNCERTAIN_IDENTITY
    Reason: Professional Middle Korean grammar re-verification required
  - Input: Y
    Object: 짓다 direct entry identity
    State: MISSING_SOURCE_LOCATION
    Reason: Search index only
  - Input: Y
    Object: 학년/몇 년 exact pronunciation
    State: MISSING_SOURCE_LOCATION
    Reason: Detailed dictionary item recheck required
  - Input: Y
    Object: ㄴ insertion mechanism
    State: SOURCE_CONFLICT
    Reason: Competing analysis preserved
  XZ_explicit_lemmas:
  - Lemma: '`김`'
    Reason: 복수 품사·동형어·다의 Sense 가능; individual target_code selection required
    State: '`UNCERTAIN_IDENTITY`'
  - Lemma: '`날`'
    Reason: 복수 품사·동형어·다의 Sense 가능; individual target_code selection required
    State: '`UNCERTAIN_IDENTITY`'
  - Lemma: '`눈`'
    Reason: 복수 품사·동형어·다의 Sense 가능; individual target_code selection required
    State: '`UNCERTAIN_IDENTITY`'
  - Lemma: '`살`'
    Reason: 복수 품사·동형어·다의 Sense 가능; individual target_code selection required
    State: '`UNCERTAIN_IDENTITY`'
  - Lemma: '`새`'
    Reason: 복수 품사·동형어·다의 Sense 가능; individual target_code selection required
    State: '`UNCERTAIN_IDENTITY`'
  - Lemma: '`샘`'
    Reason: 복수 품사·동형어·다의 Sense 가능; individual target_code selection required
    State: '`UNCERTAIN_IDENTITY`'
  - Lemma: '`술`'
    Reason: 복수 품사·동형어·다의 Sense 가능; individual target_code selection required
    State: '`UNCERTAIN_IDENTITY`'
  - Lemma: '`우리`'
    Reason: 복수 품사·동형어·다의 Sense 가능; individual target_code selection required
    State: '`UNCERTAIN_IDENTITY`'
  - Lemma: '`이제`'
    Reason: 복수 품사·동형어·다의 Sense 가능; individual target_code selection required
    State: '`UNCERTAIN_IDENTITY`'
  XZ_overlap_inventory:
    X_source_location_incomplete_entries: 47
    Z_official_word_detail_ID_missing: 80
    Z_historical_readings_not_stated: 80
    Rime_Sino_members_without_core_identity_record: 43
    Rime_surface_or_noninitial_context_field_gap: 9
    anonymous_ieung_record_ID_gap: 10
    note: Categories overlap and must not be summed as unique entities.
  YZ_reconstruction_uncertainties:
  - reconstruction_id: YZ-RECON-UNC-001
    object: 초성 ㆁ·중세 초성 ㅇ
    reason: 정확 IPA·방법·지역·시기별 변이가 결속되지 않음
    state: UNCERTAIN_RECONSTRUCTION
  - reconstruction_id: YZ-RECON-UNC-002
    object: 이다의 후두 유성 마찰음
    reason: 사전 보고는 있으나 재구 방법과 신뢰도 필드가 없음
    state: SCHOLARLY_RECONSTRUCTION_WITH_METHOD_GAP
  - reconstruction_id: YZ-RECON-UNC-003
    object: 학년·몇 년의 세부 연쇄발음
    reason: Data.Y 자체가 직접 사전 재확인을 요구
    state: SOURCE_UNCERTAIN
  - reconstruction_id: YZ-RECON-UNC-004
    object: 짓다 기본형·활용 발음
    reason: 검색 색인만 결속되고 직접 상세항목이 없음
    state: SOURCE_UNCERTAIN
  YZ_multiple_lineage_candidates:
  - candidate_id: YZ-MULTI-001
    object: ㆁ / 현대 초성 ㅇ / 현대 종성 ㅇ
    candidates:
    - historical_onset_old_ieung
    - modern_orthographic_empty_onset
    - modern_coda_velar_nasal
    reason: Source가 하나의 직선 문자·음가계보로 확정하지 않음
    state: MULTIPLE_LINEAGE_CANDIDATES
  - candidate_id: YZ-MULTI-002
    object: 잎 / 닢 / 합성어 ㄴ 첨가
    candidates:
    - historical_nip_lineage_explanation
    - synchronic_n_insertion_or_assimilation_analysis
    reason: 동일 해설에 경쟁분석이 병기됨
    state: MULTIPLE_LINEAGE_CANDIDATES
  - candidate_id: YZ-MULTI-003
    object: 니르다→이르다 현상 명명·시기
    candidates:
    - source_reported_initial_n_loss
    - broader_dueum_label_with_researcher_variation
    reason: 세부 periodization과 명명은 Source가 확정하지 않음
    state: MULTIPLE_LINEAGE_CANDIDATES
```
## 31. Access Failures

```yaml
access_failures:
  X:
    direct_entry_verified: 13
    official_reentry_route_only: 47
    exact_source_location_missing: 47
  Y:
    access_failures_preserved_by_xy: 3
    direct_detail_missing:
    - 짓다
    - 학년
    - 몇 년
  Z:
    official_XLS_exact_bytes: NOT_MATERIALIZED
    official_dictionary_detail_word_no_bound: 0
    query_route_only_usage_words: 80
```
## 32. Collection Gaps

```yaml
collection_gaps:
  XY_unresolved:
  - 47 X individual target-code and exact entry locations
  - 9 X homograph_or_polysemy identities
  - X nominal root source status
  - X exact raw definition and example provenance
  - 6 extra X zero-onset lexical item identities
  - 10 X no-coda/coda direct inflection snapshots
  - Y ㆁ_and_ㅇ complete historical lineage
  - Y_POS_010 exact compound pronunciations
  - Y_POS_016 direct lemma page
  - 니르다_to_이르다 terminology_and_periodization
  - ㄴ_insertion_analysis_competition
  - absence_of_same_lemma_independent_XY_sample
  XZ_unresolved:
  - id: XZ-U-001
    item: X_47_exact_dictionary_entry_snapshots
    blocking: true
  - id: XZ-U-002
    item: X_9_homonym_or_sense_target_codes
    blocking: scoped
  - id: XZ-U-003
    item: X_example_sentence_provenance
    blocking: scoped
  - id: XZ-U-004
    item: official_Hanja_XLS_exact_bytes_and_transform_reproduction
    blocking: true
  - id: XZ-U-005
    item: Z_80_official_dictionary_detail_word_numbers
    blocking: true
  - id: XZ-U-006
    item: Rime_43_Sino_member_full_identity_records
    blocking: true
  - id: XZ-U-007
    item: canonical_reading_vs_surface_position_for_9_members
    blocking: scoped
  - id: XZ-U-008
    item: stable_IDs_for_10_ieung_supplementary_records
    blocking: scoped
  - id: XZ-U-009
    item: full_variant_identity_for_拏_if_required
    blocking: scoped
  - id: XZ-U-010
    item: direct_source_positions_for_all_62_rime_members
    blocking: true
  YZ_unresolved:
  - exact_character_lineage_between_old_ieung_and_modern_ieung
  - medieval_initial_ieung_phonetic_value_by_period_and_region
  - dueum_terminology_and_periodization_for_native_niruda_lineage
  - nip_leaf_and_double_n_insertion_competing_analysis
  - direct_detail_identity_for_jitda
  - direct_pronunciation_entries_for_haknyeon_and_myeot_nyeon
  - original_hanja_XLS_and_transformation_reproducibility
  - independent_official_hanja_reading_crosscheck_for_80_identities
  - stable_dictionary_detail_locations_for_80_usage_words
  - historical_Korean_Hanja_readings
  - historical_reported_or_reconstructed_rimes
  - old_Hangul_extended_jamo_normalization_policy
  YZ_missing_intermediate_states:
  - object: ㆁ→현대 ㅇ 후보계보
    missing: 판본·시기별 문자기능 재편과 음가 변화단계
    state: MISSING_INTERMEDIATE_STATE
  - object: 니르다→이르다
    missing: 근대국어 세부 문헌형·정확 시기
    state: MISSING_INTERMEDIATE_STATE
  - object: 닢→잎 및 합성어형
    missing: 시기별 형태·발음·경쟁분석 Source
    state: MISSING_INTERMEDIATE_STATE
  - object: 같-/싶-/새끼 계보
    missing: 직접 음성기록 또는 단계별 음성 재구방법
    state: MISSING_INTERMEDIATE_STATE
  - object: 한자 80개 역사독음
    missing: historical_readings_if_source_states 전체
    state: MISSING_INTERMEDIATE_STATE
  YZ_unsupported_links:
  - link_id: YZ-UNSUP-001
    from: historical_ㆁ
    to: modern_onset_and_coda_ㅇ
    reason: 표면 자모 유사성과 교육자료만으로 단일 Identity 계보 확정 불가
    state: UNSUPPORTED_LINEAGE_LINK
  - link_id: YZ-UNSUP-002
    from: modern_same_syllable_hanja_group
    to: same_historical_pronunciation
    reason: Z의 historical_readings_if_source_states가 80개 모두 비어 있음
    state: PROHIBITED_FOR_CURRENT_DATASET
  - link_id: YZ-UNSUP-003
    from: modern_orthographic_rime
    to: historical_or_reconstructed_rime
    reason: 역사운모 Source가 결속되지 않음
    state: PROHIBITED_FOR_CURRENT_DATASET
  - link_id: YZ-UNSUP-004
    from: dictionary_query_url
    to: fully_materialized_usage_entry
    reason: 80개 stable word_no·정의·발음 위치가 미결속
    state: MISSING_SOURCE_LOCATION
```
## 33. Original Judgments

The exact three 2D Result texts are embedded verbatim below so individual judgments, source locations, conflicts and quantity tracks are not lost.

### HRTDB_A::gpt.xy — `225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562.A.md`

~~~text
---
document_type: HRTDB_A_2D_SOURCE_VERIFICATION_RESULT
document_class: LEXICAL_MORPHOLOGICAL_LINEAGE_CROSS_VERIFICATION_RESULT
repository: SeungeFlow/HRTDB_A
repository_seat_code: A
cycle_id: GLANG-SOURCE-COLLECTION-BASE-CONSONANTS-R01
stage_id: R02_2D_XY
stage_class: FUNCTION_1
instance: gpt.xy
fixed_seat: HRTDB_A::gpt.xy
occupation_class: SOURCE_IDENTITY_AND_LINEAGE_VERIFICATION
source_authority: 승이
directive_author: gpt.logi
directive_author_seat: HRTDB_A::gpt.xyzt
recipient: gpt.logi@HRTDB_A::gpt.xyzt
direct_input_count: 2
output_count: 1
analysis_performed: false
semantic_analysis_performed: false
center_position_analysis_performed: false
github_mutation: false
track_db_promotion: false
encoding: UTF-8
newline: LF
bom: false
state: VERIFICATION_COMPLETE_WITH_UNRESOLVED
verdict: PASS_2D_XY_SOURCE_VERIFICATION_COMPLETE_WITH_UNRESOLVED
---

# HRTDB_A::gpt.xy — Lexical–Morphological Source Verification

## 1. Directive Identity

```yaml
directive:
  transport_filename: 9f965a0cc01c2270b68cf26b66277a32a6ef70ad0592cf11461e060d0e2e6bc8.A(1).md
  normalized_filename: 9f965a0cc01c2270b68cf26b66277a32a6ef70ad0592cf11461e060d0e2e6bc8.A.md
  actual_sha256: 9f965a0cc01c2270b68cf26b66277a32a6ef70ad0592cf11461e060d0e2e6bc8
  exact_bytes: 8697
  line_count: 443
  encoding: UTF-8
  line_ending: LF
  bom: false
  recipient_instance: gpt.xy
  recipient_seat: HRTDB_A::gpt.xy
  cycle_id: GLANG-SOURCE-COLLECTION-BASE-CONSONANTS-R01
  stage_id: R02_2D_XY
  occupation_class: SOURCE_IDENTITY_AND_LINEAGE_VERIFICATION
  binding: PASS
```

```text
verification is not semantic analysis.
same surface is not same lexical identity.
same consonant is not same lineage.
```

## 2. Bound Input Identities

### 2.1 gpt.x Result

```yaml
input_x:
  transport_filename: 9492b02256ce64a5627ba9980b3338833859f4fa049a48b1d15866d6231914d8.A(1).md
  normalized_filename: 9492b02256ce64a5627ba9980b3338833859f4fa049a48b1d15866d6231914d8.A.md
  actual_sha256: 9492b02256ce64a5627ba9980b3338833859f4fa049a48b1d15866d6231914d8
  exact_bytes: 167957
  line_count: 4616
  encoding: UTF-8
  line_ending: LF
  bom: false
  producer: gpt.x
  fixed_seat: HRTDB_A::gpt.x
  stage_id: R01_1D_X
  occupation_class: DATA_SOURCE_COLLECTION
  termination_state: COLLECTION_PARTIAL_WITH_GAPS
  binding: PASS
```

### 2.2 gpt.y Result

```yaml
input_y:
  transport_filename: 5bda1cc62834c8b5baa459f4ca7721195c83538bdddaf9e8dd4c74781fc38892.A(1).md
  normalized_filename: 5bda1cc62834c8b5baa459f4ca7721195c83538bdddaf9e8dd4c74781fc38892.A.md
  actual_sha256: 5bda1cc62834c8b5baa459f4ca7721195c83538bdddaf9e8dd4c74781fc38892
  exact_bytes: 65498
  line_count: 948
  encoding: UTF-8
  line_ending: LF
  bom: false
  producer: gpt.y
  fixed_seat: HRTDB_A::gpt.y
  stage_id: R01_1D_Y
  occupation_class: DATA_SOURCE_COLLECTION
  termination_state: COLLECTION_COMPLETE
  binding: PASS
```

```yaml
direct_input_gate:
  required_count: 2
  observed_count: 2
  filename_hash_match: PASS
  exact_byte_hash_recalculation: PASS
  UTF_8: PASS
  LF: PASS
  no_BOM: PASS
  producer_and_seat: PASS
  cycle_match: PASS
  directive_is_not_result: PRESERVED
  verdict: PASS_DIRECT_INPUT_IDENTITY_BINDING
```

## 3. Input Integrity Check

```yaml
integrity:
  input_x:
    raw_bytes_preserved: true
    semantic_rewrite_by_gpt_xy: false
    source_conflicts_preserved: 4
    collection_gaps_preserved: 4
  input_y:
    raw_bytes_preserved: true
    semantic_rewrite_by_gpt_xy: false
    source_conflicts_preserved: 4
    collection_gaps_preserved: 6
    access_failures_preserved: 3
  input_modification: NOT_PERFORMED
  remote_mutation: NOT_PERFORMED
```

## 4. Verification Scope

```yaml
verification_scope:
  - surface_form
  - lemma
  - root
  - stem
  - morpheme_identity
  - inflected_forms
  - derived_forms
  - compound_boundary
  - standard_pronunciation
  - pronunciation_variant
  - first_and_nonfirst_position
  - modern_and_historical_form
  - orthographic_initial_ieung
  - phonetic_zero_onset
  - coda_ieung
  - no_coda_and_coda_relation
  - raw_and_normalized_lineage

prohibited_classifications:
  - SUPPORTED
  - CONTRADICTED
  - STRUCTURALLY_MEANINGFUL
  - SINGULARITY
  - CENTER_POSITION
```

## 5. Cross-source Inventory

| Group | Canonical family | X refs | Y refs | Relation | Independence decision |
|---|---|---|---|---|---|
| SRC-XY-G01 | https://korean.go.kr/kornorms/m/m_regltn.do?regltn_code=0002 | X:SRC-KORNORMS | Y:SRC-002, Y:SRC-017 | SAME_CANONICAL_DOCUMENT_DIFFERENT_EVIDENCE_LOCATION | 1 identity; not independent corroboration |
| SRC-XY-G02 | 한국어기초사전 domain | X search/API/statistics + 13 direct entries | Y SRC-013/014/015 | SAME_INSTITUTION_DIFFERENT_DOCUMENT_OR_ENTRY | Do not merge by institution |
| SRC-XY-G03 | 국립국어원 explanatory responses | X SRC-IEUNG-FAQ/QNA-2026 | Y SRC-004/005/006/008/016 | SAME_INSTITUTION_DIFFERENT_RESPONSE | Question and evidence location remain distinct |
| SRC-XY-G04 | 훈민정음/Hangeul public institution material | X SRC-HANGEUL | Y SRC-007/018/019 | RELATED_INSTITUTIONAL_FAMILY_NOT_SAME_DOCUMENT | Educational guide, article, and archive remain separate |

```yaml
source_quantity_audit:
  input_x_source_record_count: 21
  input_y_source_record_count: 19
  input_y_unique_source_identity_count: 18
  exact_cross_input_canonical_source_group_count: 1
  duplicate_source_counted_as_independent: false
  local_source_id_used_as_identity: false
```

## 6. Surface–Lemma Verification

### 6.1 Exact cross-input lexical intersection

```yaml
lexical_cross_intersection:
  x_unique_surface_lemma_records: 60
  y_exact_same_surface_same_lemma_matches: 0
  exact_cross_verified_lexeme_count: 0
  same_consonant_used_as_lineage_evidence: false
  state: NO_EXACT_CROSS_LEXEME
```

### 6.2 X lexical entry ledger

| Entry | Surface | POS | target_code | Access | Root/Stem source state | Verification states | Y counterpart |
|---|---|---|---|---|---|---|---|
| X-ㅇ-E01 | 아기 | 명사 | 20235 | DIRECT_ENTRY_VERIFIED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅇ-E02 | 아이 | 명사 | 62843 | DIRECT_ENTRY_VERIFIED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅇ-E03 | 아버지 | 명사 | 71343 | DIRECT_ENTRY_VERIFIED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅇ-E04 | 어머니 | 명사 | 74361 | DIRECT_ENTRY_VERIFIED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅇ-E05 | 언니 | 명사 | 31971 | DIRECT_ENTRY_VERIFIED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅇ-E06 | 오빠 | 명사 | 68006 | DIRECT_ENTRY_VERIFIED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅇ-E07 | 우리 | 대명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED,UNCERTAIN_IDENTITY | MISSING_COUNTERPART |
| X-ㅇ-E08 | 오늘 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅇ-E09 | 어제 | 명사 | 67075 | DIRECT_ENTRY_VERIFIED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅇ-E10 | 이제 | 부사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED,UNCERTAIN_IDENTITY | MISSING_COUNTERPART |
| X-ㅇ-E11 | 이마 | 명사 | 71693 | DIRECT_ENTRY_VERIFIED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅇ-E12 | 이빨 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅇ-E13 | 입 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅇ-E14 | 얼음 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅇ-E15 | 여름 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E01 | 가슴 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E02 | 가을 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E03 | 개미 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E04 | 거미 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E05 | 겨울 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E06 | 고기 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E07 | 구름 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E08 | 귀 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E09 | 길 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E10 | 김 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED,UNCERTAIN_IDENTITY | MISSING_COUNTERPART |
| X-ㄱ-E11 | 가다 | 동사 | 27500 | DIRECT_ENTRY_VERIFIED | VERIFIED | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E12 | 가늘다 | 형용사 | 62497 | DIRECT_ENTRY_VERIFIED | VERIFIED | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E13 | 고맙다 | 형용사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | UNVERIFIED_SOURCE_LOCATION | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E14 | 그리다 | 동사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | UNVERIFIED_SOURCE_LOCATION | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄱ-E15 | 기르다 | 동사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | UNVERIFIED_SOURCE_LOCATION | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E01 | 나 | 대명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E02 | 너 | 대명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E03 | 나무 | 명사 | 32750 | DIRECT_ENTRY_VERIFIED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E04 | 나라 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E05 | 나이 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E06 | 날 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED,UNCERTAIN_IDENTITY | MISSING_COUNTERPART |
| X-ㄴ-E07 | 남 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E08 | 낮 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E09 | 냄새 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E10 | 넋 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E11 | 눈 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED,UNCERTAIN_IDENTITY | MISSING_COUNTERPART |
| X-ㄴ-E12 | 누나 | 명사 | 32205 | DIRECT_ENTRY_VERIFIED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E13 | 누이 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E14 | 누룩 | 명사 | 45604 | DIRECT_ENTRY_VERIFIED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | SOURCE_IDENTITY_VERIFIED,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㄴ-E15 | 늪 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅅ-E01 | 사람 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅅ-E02 | 사랑 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅅ-E03 | 사슴 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅅ-E04 | 살 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED,UNCERTAIN_IDENTITY | MISSING_COUNTERPART |
| X-ㅅ-E05 | 새 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED,UNCERTAIN_IDENTITY | MISSING_COUNTERPART |
| X-ㅅ-E06 | 샘 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED,UNCERTAIN_IDENTITY | MISSING_COUNTERPART |
| X-ㅅ-E07 | 서리 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅅ-E08 | 섬 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅅ-E09 | 소 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅅ-E10 | 소금 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅅ-E11 | 손 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅅ-E12 | 솜 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅅ-E13 | 술 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED,UNCERTAIN_IDENTITY | MISSING_COUNTERPART |
| X-ㅅ-E14 | 숨 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |
| X-ㅅ-E15 | 숲 | 명사 | null | OFFICIAL_REENTRY_ROUTE_RECORDED | NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN | MISSING_SOURCE_LOCATION,NORMALIZATION_VERIFIED | MISSING_COUNTERPART |

### 6.3 Decision

```text
60 distinct X surface/Lemma records
≠
60 fully source-verified Sense identities.

13 direct target-code entries
+
47 official reentry candidates
=
60 collected lexical surfaces.

Verified Unique Identity Count = 13.
```

## 7. Root–Stem–Morpheme Verification

```yaml
root_stem_morpheme_audit:
  x_total_entries: 60
  x_nominal_pronominal_adverb_root_equals_lemma_count: 55
  x_predicate_count: 5
  x_direct_source_predicate_stem_count: 2
  x_reentry_only_predicate_stem_count: 3
  y_position_relation_count: 16
  y_same_lineage_source_supported_count: 14
  y_same_lineage_not_supported_count: 2

decision:
  nominal_root_fields: NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN
  predicate_stems_with_direct_target_code: SOURCE_IDENTITY_VERIFIED
  predicate_stems_with_reentry_only: MISSING_SOURCE_LOCATION
  y_pos_004: SOURCE_CONFLICT
  y_pos_016: SOURCE_CONFLICT
```

No source-less morpheme boundary was added by `gpt.xy`.

## 8. Pronunciation Verification

| Claim | Form | Pronunciation | Claim type | Rule/change | Source | Verification |
|---|---|---|---|---|---|---|
| PRON-001 | 강이 | [강이] | DICTIONARY_REPORTED | ㅇ 받침 비연음 | SRC-004 | SOURCE_POSITION_VERIFIED |
| PRON-002 | 목이 | [모기] | OFFICIAL_NORM_EXAMPLE | 제13항 연음 | SRC-002 | SOURCE_POSITION_VERIFIED |
| PRON-003 | 깎아 | [까까] | OFFICIAL_NORM_EXAMPLE | 제13항 연음 | SRC-002 | SOURCE_POSITION_VERIFIED |
| PRON-004 | 옷 | [옫] | OFFICIAL_NORM_EXAMPLE | 제9항 음절 끝소리 | SRC-016 | SOURCE_POSITION_VERIFIED |
| PRON-005 | 옷이 | [오시] | OFFICIAL_NORM_EXAMPLE | 제13항 연음 | SRC-016 | SOURCE_POSITION_VERIFIED |
| PRON-006 | 솜이불 | [솜ː니불] | OFFICIAL_NORM_EXAMPLE | 제29항 ㄴ 첨가 | SRC-002 | SOURCE_POSITION_VERIFIED |
| PRON-007 | 색연필 | [생년필] | OFFICIAL_NORM_EXAMPLE | ㄴ 첨가+비음화 | SRC-002 | SOURCE_POSITION_VERIFIED |
| PRON-008 | 낫다/나아 | [낟ː따]/[나아] | DICTIONARY_REPORTED | ㅅ 불규칙 활용 | SRC-014 | SOURCE_POSITION_VERIFIED |
| PRON-009 | 붓다/부어 | [붇ː따]/[부어] | DICTIONARY_REPORTED | ㅅ 불규칙 활용 | SRC-013 | SOURCE_POSITION_VERIFIED |
| PRON-010 | 같다 | [갇따] | DICTIONARY_REPORTED | 현대 표준 발음 | SRC-009 | SOURCE_POSITION_VERIFIED |
| PRON-011 | 싶다/싶어 | [십따]/[시퍼] | DICTIONARY_REPORTED | 현대 활용 | SRC-010 | SOURCE_POSITION_VERIFIED |

```yaml
pronunciation_audit:
  y_pronunciation_claim_count: 11
  official_norm_or_dictionary_report_count: 11
  directly_recorded_historical_audio_count: 0
  scholarly_or_dictionary_reconstruction_as_direct_observation: false
  unresolved_pronunciation_fields:
    - Y-POS-010 학년
    - Y-POS-010 몇_년
    - Y-POS-016 짓다_direct_detail
  spelling_pronunciation_separation: PASS_WITH_DECLARED_GAPS
```

## 9. ㅇ–Ø–Coda ㅇ Verification

```yaml
ieung_zero_coda_verification:
  input_x_zero_onset_records: 12
  input_y_modern_ieung_position_records:
    - Y-POS-001
    - Y-POS-002
    - Y-POS-004
  orthographic_initial_ieung: DISTINCT_FIELD
  phonetic_initial_zero: DISTINCT_FIELD
  coda_ieung_ng: DISTINCT_FIELD
  modern_relation_state: CROSS_VERIFIED
  historical_ㆁ_relation_state: PARTIAL_CROSS_MATCH
  identity_merge: false
```

```text
Modern initial ㅇ = orthographic onset slot with Ø
≠
Modern coda ㅇ = [ŋ]
≠
Historical ㆁ or context-dependent historical onset reports.
```

Six X phonological examples—`앙금·엉덩이·옹기·웅덩이·응어리·잉어`—have field-rule support but no item-level lexical Source Record in the 60-entry registry. Their position fields remain verified; lexical identity verification remains pending.

## 10. Position Relation Verification

| Relation | Target | Forms | Same-lineage declared | Verification | X relation |
|---|---|---|---|---|---|
| Y-POS-001 | ㅇ | 강 / 강이 | true | LINEAGE_LINK_VERIFIED | MISSING_COUNTERPART |
| Y-POS-002 | ㅇ | 방 / 방을 | true | LINEAGE_LINK_VERIFIED | MISSING_COUNTERPART |
| Y-POS-003 | ㅇ | 이다 / 리다 / 깔리다 | true | LINEAGE_LINK_VERIFIED | MISSING_COUNTERPART |
| Y-POS-004 | ㅇ | ㆁ / ㅇ / ㅇ | false | SOURCE_CONFLICT | MISSING_COUNTERPART |
| Y-POS-005 | ㄱ | 목 / 목이 | true | LINEAGE_LINK_VERIFIED | MISSING_COUNTERPART |
| Y-POS-006 | ㄱ | 깎다 / 깎아 | true | PARTIAL_CROSS_MATCH | MISSING_COUNTERPART |
| Y-POS-007 | ㄱ | 식브다 / 십브다 / 싶다 | true | LINEAGE_LINK_VERIFIED | MISSING_COUNTERPART |
| Y-POS-008 | ㄱ | 삿기 / 새 / 새끼 | true | LINEAGE_LINK_VERIFIED | MISSING_COUNTERPART |
| Y-POS-009 | ㄴ | 여자 / 남녀 | true | LINEAGE_LINK_VERIFIED | PROHIBITED_FOR_X_NATIVE_LEXEME_COUNT |
| Y-POS-010 | ㄴ | 연세 / 학년 / 몇 년 | true | SOURCE_POSITION_VERIFIED_WITH_PRONUNCIATION_UNRESOLVED | PROHIBITED_FOR_X_NATIVE_LEXEME_COUNT |
| Y-POS-011 | ㄴ | 이불 / 솜이불 | true | LINEAGE_LINK_VERIFIED | PARTIAL_CROSS_MATCH_X_솜_COMPONENT |
| Y-POS-012 | ㄴ | 연필 / 색연필 | true | LINEAGE_LINK_VERIFIED | MISSING_COUNTERPART |
| Y-POS-013 | ㅅ | 옷 / 옷이 | true | LINEAGE_LINK_VERIFIED | MISSING_COUNTERPART |
| Y-POS-014 | ㅅ | 낫다 / 나아 / 나으니 | true | LINEAGE_LINK_VERIFIED | MISSING_COUNTERPART |
| Y-POS-015 | ㅅ | 붓다 / 부어 / 부으니 | true | LINEAGE_LINK_VERIFIED | MISSING_COUNTERPART |
| Y-POS-016 | ㅅ | 짓다 / 지어 / 지으니 | false | SOURCE_CONFLICT | MISSING_COUNTERPART |

```yaml
position_relation_summary:
  raw_position_member_count: 40
  relation_group_count: 16
  lineage_link_verified_or_scoped_count: 14
  source_conflict_count: 2
  exact_x_counterpart_count: 0
  component_partial_match_count: 1
  x_native_scope_exclusions:
    - Y-POS-009
    - Y-POS-010
```

## 11. Historical–Modern Lineage Verification

| Lineage | Identity | Historical | Intermediate | Modern | Verification | X counterpart |
|---|---|---|---|---|---|---|
| Y-HIST-001 | 초성 옛이응 ㆁ | ㆁ | ㅇ | ㅇ | SOURCE_CONFLICT | MISSING_COUNTERPART |
| Y-HIST-002 | 깔리- | 이다 | 리다 | 깔리다 | LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION | MISSING_COUNTERPART |
| Y-HIST-003 | 이르- | 니르다 | 이르다 | 이르다 | LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION | MISSING_COUNTERPART |
| Y-HIST-004 | 女 | 녀 | 여 | 여자/남녀 | LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION | MISSING_COUNTERPART |
| Y-HIST-005 | 年 | 년 | 연 | 연세/학년/몇 년 | LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION | MISSING_COUNTERPART |
| Y-HIST-006 | 같- | 다/다 | 다 → 갓-/갓ㅎ-/갓ㅌ- | 같다 | LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION | MISSING_COUNTERPART |
| Y-HIST-007 | 싶- | 식브다 | 십브다 → 시브다/시프다 | 싶다 | LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION | MISSING_COUNTERPART |
| Y-HIST-008 | 새끼 | 삿기 | 새/색기 | 새끼 | LINEAGE_LINK_VERIFIED_AS_REPORTED_NOT_DIRECT_OBSERVATION | MISSING_COUNTERPART |
| Y-HIST-009 | 잎 | 닢 | 깻닢/나뭇닢 | 잎 | SOURCE_CONFLICT | MISSING_COUNTERPART |

```yaml
historical_lineage_summary:
  lineage_count: 9
  raw_historical_intermediate_modern_form_count: 29
  direct_observation_pronunciation_count: 0
  dictionary_or_scholarly_reported_lineage_count: 9
  source_conflict_lineage_count: 2
  exact_x_historical_counterpart_count: 0
```

Historical sequence was verified only as source-reported lineage. It was not converted into causality or structural meaning.

## 12. Raw–Normalized Audit

```yaml
raw_normalized_audit:
  x_unicode_nfc_records_checked: 60
  x_nfc_sha256_matches: 60
  x_nfd_jamo_decomposition_checked: 60
  x_nfd_jamo_decomposition_matches: 60
  x_syllable_decomposition_checked: 60
  x_syllable_decomposition_matches: 60
  y_raw_old_hangul_forms_preserved: true
  y_modernized_transcription_over_raw: false
  semantic_rewrite_verified_false: NOT_PROVEN_FOR_SHORT_GLOSSES
```

### 12.1 Reproducibility decision

- X의 60개 `normalized_nfc` 문자열과 표의 NFC SHA-256은 전부 재계산 일치했다.
- X의 60개 현대 한글 음절분해와 NFD Jamo 표기는 전부 재현됐다.
- Y의 옛한글 Raw Form은 현대형으로 덮어쓰지 않았다.
- X의 짧은 뜻풀이와 예문은 Exact Raw 위치가 완전히 결속되지 않았으므로 `RAW_MATCH_VERIFIED`로 승격하지 않았다.

## 13. Duplicate Audit

```yaml
duplicate_audit:
  x_raw_lexical_entry_count: 60
  x_unique_surface_lemma_count: 60
  x_duplicate_inflation_count: 0
  x_direct_entry_reentry_duplicate_links: 13
  duplicate_links_verified_within_input: 13
  y_source_record_count: 19
  y_unique_source_identity_count: 18
  y_duplicate_source_record_pair:
    - SRC-002
    - SRC-017
  exact_cross_lexical_duplicate_count: 0
  duplicate_link_is_identity_merge: false
```

## 14. Quantity Audit

```yaml
quantity_audit:
  x_lexical:
    reported_count: 60
    unique_identity_count: 60
    verified_unique_identity_count: 13
    duplicate_inflation_count: 0
    unresolved_source_location_count: 47
    uncertain_identity_count: 9

  x_zero_onset:
    reported_count: 12
    verified_position_relation_count: 12
    item_level_lexical_source_missing_count: 6

  x_no_coda_coda:
    reported_count: 10
    direct_lineage_snapshot_verified_count: 0
    unresolved_count: 10

  y_position:
    reported_relation_count: 16
    raw_position_member_count: 40
    source_supported_same_lineage_count: 14
    source_conflict_or_weak_count: 2

  y_historical:
    reported_lineage_count: 9
    source_reported_lineage_count: 9
    direct_observation_count: 0
    conflict_lineage_count: 2

  cross_input:
    exact_same_surface_same_lemma_count: 0
    cross_verified_system_relation_count: 3
    partial_cross_match_count: 3
    non_match_guard_count: 2
```

## 15. Source Conflicts

| Conflict | Surface | Object | Difference | Preservation | State |
|---|---|---|---|---|---|
| X-CF-01 | X | 동형어 번호 | 날·눈·길·김·살·새·샘·술 등은 여러 사전 의미/동형어가 가능함. | Target code 없는 재진입 항목은 선택 Sense를 확정하지 않음. | UNRESOLVED |
| X-CF-02 | X | 발음 길이 | 일부 표제어의 장단 표시는 사전 항목별 확인이 필요함. | 이번 Normalized 발음은 음절 표면을 우선 보존하고 미검증 장단을 추가하지 않음. | UNRESOLVED |
| X-CF-03 | X | 낮/넋/늪/숲 | 표기 종성과 대표 발음이 다름. | 낮 [낟], 넋 [넉], 늪 [늡], 숲 [숩]을 표기와 발음으로 분리. | UNRESOLVED |
| X-CF-04 | X | 초성 ㅇ/종성 ㅇ | 같은 문자 ㅇ이 위치에 따라 음가가 다름. | 초성 표기 ㅇ, 음성 Ø, 종성 [ŋ]을 별도 필드로 보존. | UNRESOLVED |
| Y-CONFLICT-001 | Y | 초성 ㅇ의 중세 음가 | 끊어적기에서 나타난 초성 ㅇ은 음가가 있는 것으로 본다. ↔ 그 밖의 초성 ㅇ은 음가가 없는 것으로 본다. | CONTEXT_DEPENDENT_HISTORICAL_PHONOLOGY | UNRESOLVED |
| Y-CONFLICT-002 | Y | ㄴㄴ 첨가 분석 | 사이시옷 첨가 뒤 ㄴ 첨가와 자음동화로 설명. ↔ 사이시옷 첨가 조건이 충족되지 않는다는 반론이 해설에 병기됨. | ANALYSIS_COMPETITION | UNRESOLVED |
| Y-CONFLICT-003 | Y | 니르다→이르다 현상 명명 | 국립국어원 답변은 어두 ㄴ 탈락 및 두음법칙 적용 이전/이후로 설명. ↔ 온라인가나다는 상세 연구자 견해 차이 가능성을 열어 둠. | TERMINOLOGY_AND_PERIODIZATION | UNRESOLVED |
| Y-CONFLICT-004 | Y | 짓다 활용 Source identity | 공식 검색 색인에 지어·지으니 등 활용이 제시됨. ↔ 직접 표제어 상세 URL과 발음 필드를 확보하지 못함. | SOURCE_IDENTITY_WEAKNESS | UNRESOLVED |
| XY-CONFLICT-001 | XY | Modern ㅇ vs historical ㆁ/ㅇ | Modern phonology is direct norm; historical sound/character relation is reported and incomplete | Temporal and evidence-class split | UNRESOLVED |
| XY-CONFLICT-002 | XY | Root=Lemma fields | X normalized nominal roots lack item-level morphology source | Retain value as placeholder; do not promote | UNRESOLVED |
| XY-CONFLICT-003 | XY | Definition/example source location | Short glosses and examples are not bound to exact raw locations for all entries | MISSING_SOURCE_LOCATION | UNRESOLVED |
| XY-CONFLICT-004 | XY | Source record count vs unique source identity | Y SRC-002 and SRC-017 are same canonical document | Count records and unique identities separately | RESOLVED_IN_VERIFICATION_CLASSIFICATION |
| XY-CONFLICT-005 | XY | No exact cross lexeme | Consonant group overlap exists but same surface+lemma overlap is zero | No inferred lineage | PRESERVED |

No conflict was deleted or force-resolved.

## 16. Missing Counterparts

| Registry | Input surface | Count | Counterpart state | Decision |
|---|---|---|---|---|
| MC-X-LEX | X 60 lexical entries | 60 | No exact same-surface same-lemma Y relation | Typed missing; not deletion |
| MC-X-C06 | X zero-onset/coda dataset | 12 | No exact same-lemma Y records; only field-level cross-verification | Keep 12 position records |
| MC-X-C08 | X no-coda/coda relations | 10 | No same-lemma Y relation; direct inflection snapshots absent | Keep as candidates |
| MC-Y-POS | Y position relations | 16 | No exact same-surface same-lemma X record | Two scope exceptions and one component partial match preserved |
| MC-Y-HIST | Y historical lineages | 9 | X contains no canonical historical lineage records | Do not backfill from modern surface |

The registries overlap in scope. Their counts must not be summed as one unique missing-object count without a later semantic identity map.

## 17. Uncertain Identities

| Input | Object | State | Reason |
|---|---|---|---|
| X | 김 | UNCERTAIN_IDENTITY | No individual target_code; homograph/polysemy risk |
| X | 날 | UNCERTAIN_IDENTITY | No individual target_code; homograph/polysemy risk |
| X | 눈 | UNCERTAIN_IDENTITY | No individual target_code; homograph/polysemy risk |
| X | 살 | UNCERTAIN_IDENTITY | No individual target_code; homograph/polysemy risk |
| X | 새 | UNCERTAIN_IDENTITY | No individual target_code; homograph/polysemy risk |
| X | 샘 | UNCERTAIN_IDENTITY | No individual target_code; homograph/polysemy risk |
| X | 술 | UNCERTAIN_IDENTITY | No individual target_code; homograph/polysemy risk |
| X | 우리 | UNCERTAIN_IDENTITY | No individual target_code; homograph/polysemy risk |
| X | 이제 | UNCERTAIN_IDENTITY | No individual target_code; homograph/polysemy risk |
| Y | ㆁ and modern ㅇ complete lineage | UNCERTAIN_IDENTITY | Professional Middle Korean grammar re-verification required |
| Y | 짓다 direct entry identity | MISSING_SOURCE_LOCATION | Search index only |
| Y | 학년/몇 년 exact pronunciation | MISSING_SOURCE_LOCATION | Detailed dictionary item recheck required |
| Y | ㄴ insertion mechanism | SOURCE_CONFLICT | Competing analysis preserved |

## 18. Proposed Corrections

| Correction | Target | Detected state | Applied verification correction | Class | Blocking |
|---|---|---|---|---|---|
| XY-CORR-001 | X metadata object-class label | OFFICIAL_LEXICAL_SURFACE_AND_ZERO_ONSET_SOURCE_DATA vs handoff OFFICIAL_LEXICAL_SURFACE_SOURCE_DATA | Preserve both labels; set canonical input class to frontmatter document_class and handoff label as compatible alias. | METADATA_CLASS_ALIAS | NONBLOCKING |
| XY-CORR-002 | X nominal root fields | 51 nouns, 3 pronouns, 1 adverb assign root=lemma without item-level morphological source | Reclassify root as NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN; do not delete value. | SOURCE_LOCATION_WEAKNESS | SCOPED |
| XY-CORR-003 | X predicate root/stem fields | Only 가다·가늘다 have direct target-code pages; 고맙다·그리다·기르다 use reentry routes | Keep forms but mark 3 predicate root/stem records MISSING_SOURCE_LOCATION. | SOURCE_LOCATION_WEAKNESS | SCOPED |
| XY-CORR-004 | X dictionary_definition capture type | Section states first meanings were shortened, while field name can be read as exact raw definition | Classify as SHORT_NORMALIZED_GLOSS unless exact entry text is captured; RAW_MATCH_VERIFIED not assigned. | RAW_NORMALIZED_BOUNDARY | SCOPED |
| XY-CORR-005 | X example sentences | 60 example sentences have no exact source location or source-example identifier | Mark all example_sentences as MISSING_SOURCE_LOCATION; do not treat as dictionary examples. | SOURCE_LOCATION_WEAKNESS | SCOPED |
| XY-CORR-006 | X 47 reentry-only entries | Official search route exists but individual target_code and exact entry snapshot are absent | Retain 47 as official reentry candidates; verified unique identity count remains 13. | IDENTITY_VERIFICATION_BOUNDARY | SCOPED |
| XY-CORR-007 | X zero-onset lexical identity | 12 phonological records use general official rules; 6 surface forms are outside the 60-entry lexical registry | Verify ㅇ/Ø/coda field relation, but require item-level lexical source for 앙금·엉덩이·옹기·웅덩이·응어리·잉어. | FIELD_RULE_VS_ITEM_IDENTITY | SCOPED |
| XY-CORR-008 | X no-coda/coda relations | 10 relations use search routes and are already INSUFFICIENT_SOURCE | Preserve forms as candidates; do not assign LINEAGE_LINK_VERIFIED until direct inflection snapshots are bound. | SOURCE_LOCATION_WEAKNESS | SCOPED |
| XY-CORR-009 | Y source quantity | 19 Source Records include SRC-002 and SRC-017 sharing one canonical URL | Report source_record_count=19 and unique_source_identity_count=18; do not count duplicate as independent corroboration. | DUPLICATE_SOURCE_IDENTITY | NONBLOCKING |
| XY-CORR-010 | Y-POS-004 ㆁ/ㅇ relation | same_lineage_source_supported=false and professional historical grammar recheck required | Retain PARTIAL_CROSS_MATCH + SOURCE_CONFLICT; prohibit identity merge. | HISTORICAL_LINEAGE_UNCERTAINTY | SCOPED |
| XY-CORR-011 | Y-POS-006 ㄱ/ㄲ grouping | Target consonant is ㄱ but observed coda/onset surface is ㄲ | Classify as consonant-family relation, not exact grapheme identity. | CONSONANT_IDENTITY_SCOPE | SCOPED |
| XY-CORR-012 | Y-POS-010 pronunciation | 학년/몇 년 pronunciations explicitly state detailed dictionary confirmation required | Keep position relation; mark pronunciation fields UNRESOLVED and MISSING_SOURCE_LOCATION. | PRONUNCIATION_SOURCE_WEAKNESS | SCOPED |
| XY-CORR-013 | Y-POS-016 짓다 | Only search-index route obtained; direct lemma page and detailed pronunciation absent | Retain SOURCE_CONFLICT; no full LINEAGE_LINK_VERIFIED status. | SOURCE_IDENTITY_WEAKNESS | SCOPED |
| XY-CORR-014 | Y historical pronunciation | Historical sound values are DICTIONARY_REPORTED or SCHOLARLY_REPORTED | Preserve as reconstruction/report, never RAW_MATCH_VERIFIED or direct observation. | RECONSTRUCTION_OBSERVATION_BOUNDARY | SCOPED |
| XY-CORR-015 | Y-HIST-003 terminology | 니르다→이르다 is reported as initial ㄴ loss with terminology/periodization open | Preserve Y-CONFLICT-003 and prohibit automatic identity with modern Sino-Korean 두음법칙. | TERMINOLOGY_PERIODIZATION_CONFLICT | SCOPED |
| XY-CORR-016 | Y-HIST-009 ㄴ insertion account | Official explanation contains competing analysis | Preserve Y-CONFLICT-002; no forced resolution. | ANALYSIS_COMPETITION | SCOPED |
| XY-CORR-017 | Cross-input lexical identity | Exact same surface + same lemma pair count is 0 | Do not create lexical lineage from same consonant group; classify all unmatched records as typed MISSING_COUNTERPART. | NO_EXACT_CROSS_LEXEME | NONBLOCKING |
| XY-CORR-018 | 솜 vs 솜이불 | X has 솜; Y has compound 솜+이불 | PARTIAL_CROSS_MATCH only at component position; compound is not same lexical identity. | COMPOUND_COMPONENT_BOUNDARY | SCOPED |
| XY-CORR-019 | 입 vs 잎 | Modern pronunciation can converge to [입], but orthography and lemma differ | Record NON_MATCH_GUARD; same pronunciation is not same lexical identity. | HOMOPHONE_IDENTITY_GUARD | NONBLOCKING |
| XY-CORR-020 | Modern ㅇ vs historical ㆁ | X verifies modern initial ㅇ=Ø and coda ㅇ=[ŋ]; Y reports historical ㆁ/ㅇ complexity | CROSS_VERIFIED for modern field split; PARTIAL_CROSS_MATCH for historical lineage. | TEMPORAL_SCOPE_BOUNDARY | SCOPED |

## 19. Applied Corrections

```yaml
applied_corrections:
  input_bytes_modified: false
  verification_result_classifications_applied: 20
  applied_items:
    - XY-CORR-001_metadata_class_alias
    - XY-CORR-002_nominal_root_placeholder
    - XY-CORR-003_predicate_root_stem_source_state
    - XY-CORR-004_short_gloss_capture_type
    - XY-CORR-005_example_sentence_source_state
    - XY-CORR-006_reentry_only_identity_boundary
    - XY-CORR-007_zero_onset_field_rule_vs_item_identity
    - XY-CORR-008_no_coda_direct_snapshot_pending
    - XY-CORR-009_Y_source_identity_deduplication
    - XY-CORR-010_Y_POS_004_conflict_preservation
    - XY-CORR-011_Y_POS_006_consonant_family_scope
    - XY-CORR-012_Y_POS_010_pronunciation_unresolved
    - XY-CORR-013_Y_POS_016_source_identity_weakness
    - XY-CORR-014_historical_reconstruction_boundary
    - XY-CORR-015_니르다_이르다_terminology_conflict
    - XY-CORR-016_ㄴ_insertion_analysis_competition
    - XY-CORR-017_no_exact_cross_lexeme
    - XY-CORR-018_솜_솜이불_component_nonmerge
    - XY-CORR-019_입_잎_homophone_nonmerge
    - XY-CORR-020_modern_ieung_historical_old_ieung_scope
```

Applied means applied to this verification result only. It does not mean that either 1d input was rewritten.

## 20. Unresolved

```yaml
unresolved:
  - 47 X individual target-code and exact entry locations
  - 9 X homograph_or_polysemy identities
  - X nominal root source status
  - X exact raw definition and example provenance
  - 6 extra X zero-onset lexical item identities
  - 10 X no-coda/coda direct inflection snapshots
  - Y ㆁ_and_ㅇ complete historical lineage
  - Y_POS_010 exact compound pronunciations
  - Y_POS_016 direct lemma page
  - 니르다_to_이르다 terminology_and_periodization
  - ㄴ_insertion_analysis_competition
  - absence_of_same_lemma_independent_XY_sample
```

## 21. Required Next Data

| Next data | Input | Required item | Purpose |
|---|---|---|---|
| ND-001 | X | 47 individual target_code and exact entry snapshots | Upgrade source identity and exact sense verification |
| ND-002 | X | Exact raw definition and example locations | Distinguish raw dictionary capture from normalized short gloss |
| ND-003 | X | Morphological source for nominal root fields | Verify or null root placeholders |
| ND-004 | X | Direct inflection snapshots for 10 no-coda/coda pairs | Permit lineage-link verification |
| ND-005 | X | Item-level sources for 앙금·엉덩이·옹기·웅덩이·응어리·잉어 | Verify lexical identity separately from general phonological rule |
| ND-006 | Y | Direct detailed entry for 짓다 | Resolve Y-POS-016 source identity weakness |
| ND-007 | Y | Direct dictionary pronunciation for 학년·몇 년 | Resolve Y-POS-010 pronunciation |
| ND-008 | Y | Professional Middle Korean sources for ㆁ/ㅇ | Verify character and sound lineage |
| ND-009 | Y | Professional periodization for 니르다→이르다 | Resolve terminology/time boundary |
| ND-010 | Y | Additional evidence for ㄴ insertion analyses | Preserve or resolve competition |
| ND-011 | XY | At least one same-lemma dataset collected independently by X and Y | Enable lexical CROSS_VERIFIED relation rather than field-level only |
| ND-012 | XY | Versioned source snapshots or archived pages | Improve reproducibility of dynamic dictionary and Q&A pages |

## 22. Handoff to gpt.logi

```yaml
handoff:
  from:
    instance: gpt.xy
    fixed_seat: HRTDB_A::gpt.xy
    occupation_class: SOURCE_IDENTITY_AND_LINEAGE_VERIFICATION
  to: gpt.logi@HRTDB_A::gpt.xyzt

  direct_inputs:
    X:
      sha256: 9492b02256ce64a5627ba9980b3338833859f4fa049a48b1d15866d6231914d8
      state: COLLECTION_PARTIAL_WITH_GAPS
    Y:
      sha256: 5bda1cc62834c8b5baa459f4ca7721195c83538bdddaf9e8dd4c74781fc38892
      state: COLLECTION_COMPLETE

  verified:
    exact_input_binding: true
    X_NFC_hashes_60_of_60: true
    X_NFD_and_syllable_decomposition_60_of_60: true
    modern_ieung_zero_coda_split: true
    source_record_vs_unique_identity_split: true
    conflict_and_missing_preserved: true

  not_verified:
    exact_same_lexeme_cross_relation: true
    full_X_source_identity_60_of_60: true
    historical_pronunciation_as_direct_observation: true
    complete_ㆁ_ㅇ_lineage: true
    all_morpheme_roots: true

  result_state: VERIFICATION_COMPLETE_WITH_UNRESOLVED
  next_action:
    - bind_required_next_data
    - do_not_promote_to_semantic_analysis
    - do_not_merge_identity_by_same_consonant
```

### Final Guard

```text
verification is not semantic analysis.
dictionary meaning is not structural meaning.
same surface is not same lexical identity.
same pronunciation is not same lemma.
same consonant is not same lineage.
historical reconstruction is not direct observation.
reported sequence is not causation.
normalization is not source replacement.
correction is not deletion.
missing counterpart is not permission to infer.
relation is not merge.
Result is not Track DB.
```

## Final Verdict

```yaml
final_verdict:
  exact_direct_input_binding: PASS
  surface_lemma_verification: COMPLETE_WITH_SOURCE_LOCATION_GAPS
  root_stem_morpheme_verification: COMPLETE_WITH_UNRESOLVED
  pronunciation_verification: COMPLETE_WITH_UNRESOLVED
  ieung_zero_coda_verification: COMPLETE_WITH_HISTORICAL_BOUNDARY
  position_relation_verification: COMPLETE_WITH_UNRESOLVED
  historical_lineage_verification: COMPLETE_AS_SOURCE_REPORTED
  raw_normalized_verification: PASS
  duplicate_audit: PASS
  quantity_audit: PASS_WITH_TYPED_COUNTS
  conflict_preservation: PASS
  semantic_analysis_performed: false
  github_mutation: false
  track_db_promotion: false
  state: VERIFICATION_COMPLETE_WITH_UNRESOLVED
  verdict: PASS_2D_XY_SOURCE_VERIFICATION_COMPLETE_WITH_UNRESOLVED
```

~~~

### HRTDB_A::gpt.xz — `1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5.A.md`

~~~text
---
document_type: HRTDB_A_2D_SOURCE_VERIFICATION_RESULT
document_class: LEXICAL_HANJA_RIME_IDENTITY_CROSS_VERIFICATION
object_identity:
  object_id: HRTDB_A_R02_2D_XZ_GLANG_BASE_CONSONANTS_SOURCE_VERIFICATION
  object_class: HRTDB_A_SOURCE_IDENTITY_AND_DATASET_VERIFICATION_RESULT
  state: HOLD_WITH_INSUFFICIENT_SOURCE_LOCATION
repository: SeungeFlow/HRTDB_A
repository_seat_code: A
cycle_id: GLANG-SOURCE-COLLECTION-BASE-CONSONANTS-R01
stage_id: R02_2D_XZ
generation:
  generated_by: gpt.xz
  fixed_seat: HRTDB_A::gpt.xz
  occupation_class: SOURCE_IDENTITY_AND_DATASET_VERIFICATION
  source_authority: 승이
  coordination_authority: gpt.logi
  coordination_seat: HRTDB_A::gpt.xyzt
execution:
  verification_execution: COMPLETE
  semantic_or_structural_meaning_analysis: false
  new_web_search: false
  new_external_fact_addition: false
  input_rewrite: false
  github_mutation: false
  track_db_promotion: false
output_contract:
  output_count: 1
  encoding: UTF-8
  line_ending: LF
  bom: false
  final_newline: true
  filename_rule: <exact_body_sha256>.A.md
---

# gpt.xz — 공식 어휘자료·한자 Identity·동음·동일 운모 Dataset 교차검산

## 1. Directive Identity

```yaml
directive:
  normalized_filename: aed925af2925e532d5b1a542ab9e146d8d2b537ed088e42dbe6894ec455738f7.A.md
  transport_filename: aed925af2925e532d5b1a542ab9e146d8d2b537ed088e42dbe6894ec455738f7.A(1).md
  actual_sha256: aed925af2925e532d5b1a542ab9e146d8d2b537ed088e42dbe6894ec455738f7
  exact_byte_count: 7777
  recipient_instance: gpt.xz
  recipient_seat: HRTDB_A::gpt.xz
  cycle_id: GLANG-SOURCE-COLLECTION-BASE-CONSONANTS-R01
  stage_id: R02_2D_XZ
  occupation_class: SOURCE_IDENTITY_AND_DATASET_VERIFICATION
  directive_state: INPUT_BINDING_REQUIRED
  binding_result: PASS
```

```text
Verification is not structural-meaning analysis.
Same syllable is not same Hanja.
Same rime is not structural equivalence.
```

## 2. Bound Input Identities

```yaml
bound_direct_inputs:
  - coordinate: X
    role: OFFICIAL_LEXICAL_SURFACE_AND_ZERO_ONSET_SOURCE_DATA
    normalized_filename: 9492b02256ce64a5627ba9980b3338833859f4fa049a48b1d15866d6231914d8.A.md
    transport_filename: 9492b02256ce64a5627ba9980b3338833859f4fa049a48b1d15866d6231914d8.A(2).md
    actual_sha256: 9492b02256ce64a5627ba9980b3338833859f4fa049a48b1d15866d6231914d8
    exact_byte_count: 167957
    producer: gpt.x
    fixed_seat: HRTDB_A::gpt.x
    stage_id: R01_1D_X
    collection_state: COLLECTION_PARTIAL_WITH_GAPS

  - coordinate: Z
    role: HANJA_IDENTITY_AND_RIME_CONTROL_SOURCE_DATA
    normalized_filename: 42b4178a22efc8e81ece1bdc31f2c9be4116920f6b8e1b67023ae9442da18a3a.A.md
    transport_filename: 42b4178a22efc8e81ece1bdc31f2c9be4116920f6b8e1b67023ae9442da18a3a.A(2).md
    actual_sha256: 42b4178a22efc8e81ece1bdc31f2c9be4116920f6b8e1b67023ae9442da18a3a
    exact_byte_count: 353635
    producer: gpt.z
    fixed_seat: HRTDB_A::gpt.z
    stage_id: R01_1D_Z
    collection_state: COLLECTION_PARTIAL_WITH_GAPS

direct_input_count: 2
binding_state: PASS_EXACT_INPUT_IDENTITIES
```

## 3. Input Integrity Check

```yaml
input_integrity:
  directive:
    filename_hash_matches_actual_bytes: true
    utf8: true
    lf_only: true
    bom: false
    final_newline: true
    lf_count: 365
    rendered_line_surface: 366

  Data_X:
    filename_hash_matches_actual_bytes: true
    utf8: true
    lf_only: true
    bom: false
    final_newline: true
    lf_count: 4616
    rendered_line_surface: 4617

  Data_Z:
    filename_hash_matches_actual_bytes: true
    utf8: true
    lf_only: true
    bom: false
    final_newline: true
    lf_count: 10423
    rendered_line_surface: 10424

  cycle_match: PASS
  upstream_directive_identity:
    gpt_x: PASS_5d460cb0da8f39b31b6fb01600bdbac070963ef83a911ab831ac320deccdcff1
    gpt_z: PASS_8b80ec059ed167eee6434e3551a74f44b89055f210e0f6c3de16f543eaf19b7b
  decision: PASS_INPUT_INTEGRITY
```

## 4. Verification Scope

```yaml
verification_scope:
  included:
    - lexical_native_or_sino_classification
    - Hanja_Unicode_identity
    - Hanja_reading_and_representative_hun_source_position
    - same_syllable_different_Hanja_group
    - same_medial_coda_different_initial_set
    - modern_Hangul_mechanical_decomposition
    - NFC_and_NFD
    - orthographic_initial_ieung_vs_phonetic_zero_onset_vs_coda_ieung
    - raw_normalized_lineage
    - duplicate_inflation
    - source_conflict_and_uncertainty_preservation

  excluded:
    - common_semantic_structure
    - structural_direction
    - hypothesis_support_or_contradiction
    - structural_equivalence
    - invented_source_completion
```

## 5. Native–Sino Classification Audit

### 5.1 X lexical surface

```yaml
Data_X_lexical_audit:
  entries_reported: 60
  unique_entry_ids: 60
  unique_lexical_surfaces: 60
  initial_group_counts:
    ㅇ: 15
    ㄱ: 15
    ㄴ: 15
    ㅅ: 15

  internally_tagged_native_korean: 60
  explicit_Hanja_morpheme_in_identity_field: 0
  exact_direct_dictionary_entry_verified: 13
  official_reentry_route_only: 47
  exact_source_location_missing: 47
  explicit_uncertain_sense_identity_count: 9

  classification_result:
    internal_separation: PASS
    full_source_position_verification: HOLD
```

X의 60개 Entry는 내부 Schema에서 모두 `NATIVE_KOREAN`으로 분리되어 있고 Hanja Identity가 혼입되지 않았다. 그러나 47개는 검색 재진입 URL만 있고 개별 `target_code`와 Exact Entry Snapshot이 없으므로 `LEXICAL_CLASS_VERIFIED`로 일괄 승격할 수 없다.

### 5.2 X–Z collision guard

```yaml
same_surface_cross_class:
  exact_X_lexeme_and_Z_Hanja_reading_overlaps:
    - surface: 나
      X_identity: native_pronoun_lexeme
      Z_identities: [拿, 懦]
      decision: KEEP_SEPARATE
    - surface: 남
      X_identity: native_lexeme_other_person
      Z_identities: [南, 男]
      decision: KEEP_SEPARATE

  rule: same_Hangul_surface_is_not_same_lexical_or_Hanja_identity
```

### 5.3 Normalized examples

```yaml
example_sentence_audit:
  X_example_sentence_count: 60
  exact_source_location_bound_count: 0
  decision: RECLASSIFY_AS_NORMALIZED_ILLUSTRATIVE_EXAMPLE
  prohibited_use: SOURCE_EVIDENCE
```

각 Entry의 예문은 Source의 정확한 문장 위치가 결속되지 않았다. 따라서 사전 인용문이 아니라 정규화된 설명용 예문으로만 유지해야 한다.

## 6. Hanja Identity Audit

```yaml
Data_Z_Hanja_identity_audit:
  entries_reported: 80
  unique_entry_ids: 80
  unique_Unicode_characters: 80
  unique_character_reading_pairs: 80
  duplicate_character_identity_count: 0
  duplicate_character_reading_pair_count: 0

  character_codepoint_match:
    checked: 80
    passed: 80
    failed: 0

  Unicode_name_match:
    checked: 80
    passed: 80
    failed: 0

  reading_initial_group_match:
    checked: 80
    passed: 80
    failed: 0

  word_Hanja_morpheme_position_match:
    checked: 80
    passed: 80
    failed: 0

  identity_state: HANJA_IDENTITY_VERIFIED
```

### 6.1 Source authority boundary

```yaml
Hanja_source_authority:
  transformed_CSV_exact_line_bound_count: 80
  transformed_CSV_tier: TIER_3_TRANSFORMED_FROM_ASSOCIATION_XLS
  original_official_XLS_exact_bytes: NOT_MATERIALIZED
  official_dictionary_query_route_bound_count: 80
  official_dictionary_detail_word_no_bound_count: 0
  reading_and_hun_full_official_verification: HOLD
  usage_source_position_verification: HOLD
```

Unicode Scalar Identity와 기계분해는 검증됐지만, 한국 한자음·대표 훈은 변환 CSV의 정확한 행에만 결속되어 있다. 원 공식 XLS와 변환 재현물이 없으므로 `Tier 1 official identity`로 승격하지 않는다.

### 6.2 Variant relation

```yaml
variant_audit:
  object_a: 拿
  object_b: 拏
  relation: VARIANT_LINKED_NOT_MERGED
  duplicate_inflation: false
  source_relation_present: true
  full_separate_identity_record_for_variant: false
  decision: DUPLICATE_LINK_VERIFIED_WITH_NEXT_DATA
```

## 7. Unicode Identity Audit

```yaml
Unicode_audit:
  X_modern_Hangul_surface_entries:
    checked: 60
    NFC_match: 60
    NFD_match: 60
    syllable_decomposition_match: 60
    initial_group_match: 60
    errors: 0

  Z_Hanja_and_reading_entries:
    checked: 80
    Hanja_codepoint_match: 80
    Hanja_Unicode_name_match: 80
    reading_NFC_match: 80
    reading_NFD_match: 80
    reading_syllable_decomposition_match: 80
    errors: 0

  old_Hangul_or_extended_Jamo_in_selected_core: 0
  modern_substitution_without_source: 0
  state: JAMO_DECOMPOSITION_VERIFIED
```

## 8. Same-Syllable Different-Hanja Audit

| Group | Shared syllable | Members reported | Distinct Hanja | Mechanical audit | Source-position state |
|---|---:|---:|---:|---|---|
| `Z-HOMOPHONE-001` | `가` | 5 | 5 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-002` | `각` | 5 | 5 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-003` | `간` | 5 | 5 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-004` | `감` | 5 | 5 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-005` | `나` | 2 | 2 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-006` | `난` | 2 | 2 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-007` | `남` | 2 | 2 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-008` | `낭` | 2 | 2 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-009` | `내` | 3 | 3 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-010` | `농` | 2 | 2 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-011` | `뇌` | 2 | 2 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-012` | `사` | 5 | 5 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-013` | `상` | 5 | 5 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-014` | `선` | 5 | 5 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-015` | `성` | 5 | 5 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-016` | `영` | 6 | 6 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-017` | `원` | 6 | 6 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-018` | `의` | 3 | 3 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |
| `Z-HOMOPHONE-019` | `인` | 5 | 5 | PASS | `TIER3_LINE_BOUND / OFFICIAL_DETAIL_MISSING` |

```yaml
same_syllable_group_summary:
  groups_reported: 19
  groups_mechanically_verified: 19
  total_group_members_reported: 75
  total_unique_member_entry_ids: 75
  duplicate_Hanja_members_removed: 0
  invalid_mechanical_members: 0
  singleton_Hanja_entries_outside_groups: 5
  official_detail_source_verified_members: 0
  transformed_CSV_line_bound_members: 75
  query_route_only_usage_members: 75
  state: SYLLABLE_GROUP_VERIFIED_MECHANICALLY_SOURCE_LOCATION_HOLD
```

Group의 음절·한자·Codepoint·Entry ID 관계는 모두 재현됐다. 그러나 각 용례는 표준국어대사전 Query URL만 있고 상세 `word_no`가 없으므로 공식 상세 Source 위치 검증은 완료되지 않았다.

## 9. Same-Rime Different-Initial Audit

| Set | Rime key | Members | Surface members | Mechanical audit | Missing expected initial | Source-position state |
|---|---|---:|---|---|---|---|
| `Z-RIME-001` | `ㅏ∅` | 4 | 가(ㄱ), 나(ㄴ), 사(ㅅ), 아(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-002` | `ㅏㄱ` | 4 | 각(ㄱ), 낙(ㄴ), 삭(ㅅ), 악(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-003` | `ㅏㄴ` | 4 | 간(ㄱ), 난(ㄴ), 산(ㅅ), 안(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-004` | `ㅏㅁ` | 4 | 감(ㄱ), 남(ㄴ), 삼(ㅅ), 암(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-005` | `ㅏㅇ` | 4 | 강(ㄱ), 낭(ㄴ), 상(ㅅ), 앙(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-006` | `ㅏㅂ` | 4 | 갑(ㄱ), 납(ㄴ), 삽(ㅅ), 압(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-007` | `ㅐ∅` | 4 | 개(ㄱ), 내(ㄴ), 새(ㅅ), 애(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-008` | `ㅐㅇ` | 4 | 갱(ㄱ), 냉(ㄴ), 생(ㅅ), 앵(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-009` | `ㅓ∅` | 4 | 거(ㄱ), 너(ㄴ), 서(ㅅ), 어(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-010` | `ㅗ∅` | 4 | 고(ㄱ), 노(ㄴ), 소(ㅅ), 오(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-011` | `ㅗㄱ` | 4 | 곡(ㄱ), 녹(ㄴ), 속(ㅅ), 옥(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-012` | `ㅗㅇ` | 4 | 공(ㄱ), 농(ㄴ), 송(ㅅ), 옹(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-013` | `ㅜ∅` | 4 | 구(ㄱ), 누(ㄴ), 수(ㅅ), 우(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-014` | `ㅜㄴ` | 4 | 군(ㄱ), 눈(ㄴ), 순(ㅅ), 운(ㅇ) | PASS | `none` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-015` | `ㅕㄴ` | 3 | 견(ㄱ), 년(ㄴ), 연(ㅇ) | PASS | `ㅅ` | `QUERY_ROUTE_ONLY` |
| `Z-RIME-016` | `ㅕㅇ` | 3 | 경(ㄱ), 녕(ㄴ), 영(ㅇ) | PASS | `ㅅ` | `QUERY_ROUTE_ONLY` |

```yaml
same_rime_summary:
  sets_reported: 16
  sets_mechanically_verified: 16
  total_members_reported: 62
  decomposition_verified_members: 62
  invalid_mechanical_members: 0

  complete_four_initial_sets: 14
  explicitly_incomplete_sets: 2
  incomplete_sets:
    - set_id: Z-RIME-015
      missing_initial: ㅅ
    - set_id: Z-RIME-016
      missing_initial: ㅅ
  forced_completion_detected: false

  members_linked_to_core_Hanja_registry: 16
  native_members_cross_linkable_to_X: 3
  native_member_links:
    - Z-RIME-007/새 -> X-ㅅ-E05
    - Z-RIME-009/너 -> X-ㄴ-E02
    - Z-RIME-014/눈 -> X-ㄴ-E11
  Sino_members_without_full_core_Hanja_identity_record: 43
  query_route_only_source_members: 62

  state: RIME_SET_VERIFIED_MECHANICALLY_SOURCE_LOCATION_HOLD
```

### 9.1 Surface and non-initial Hanja members

| Set | Surface syllable | Hanja | Usage word | Current tag |
|---|---|---|---|---|
| `Z-RIME-002` | `낙` | `樂` | `낙원` | `SINO_SURFACE` |
| `Z-RIME-008` | `냉` | `冷` | `냉기` | `SINO_SURFACE` |
| `Z-RIME-010` | `노` | `老` | `노인` | `SINO_SURFACE` |
| `Z-RIME-011` | `녹` | `綠` | `녹색` | `SINO_SURFACE` |
| `Z-RIME-013` | `누` | `漏` | `누수` | `SINO_SURFACE` |

| Set | Non-initial surface | Hanja | Usage word | Current tag |
|---|---|---|---|---|
| `Z-RIME-005` | `앙` | `央` | `중앙` | `SINO_NONINITIAL` |
| `Z-RIME-012` | `옹` | `翁` | `노옹` | `SINO_NONINITIAL` |
| `Z-RIME-015` | `년` | `年` | `작년` | `SINO_NONINITIAL` |
| `Z-RIME-016` | `녕` | `寧` | `안녕` | `SINO_NONINITIAL` |

```yaml
required_field_split:
  affected_member_count: 9
  required_fields:
    - canonical_Hanja_reading
    - usage_surface_syllable
    - morpheme_position
    - initial_or_noninitial_context
    - pronunciation
    - source_detail_id
  decision: RESTORE_IDENTITY_READING_VS_USAGE_SURFACE_SPLIT
```

`SINO_SURFACE`와 `SINO_NONINITIAL` 표지는 문제를 감지했지만 Canonical Reading과 실제 용례표면을 별도 Identity Field로 완전히 고정하지 않았다. 이 9개 Member는 해당 Field가 복구될 때까지 음운규칙의 증거로 사용하지 않는다.

## 10. Jamo Decomposition Audit

```yaml
mechanical_reproduction:
  algorithm:
    modern_Hangul_range: U+AC00..U+D7A3
    initial_count: 19
    medial_count: 21
    final_index_count_including_empty: 28

  X:
    entry_decomposition_checked: 60
    declared_equals_recomputed: 60
    declared_errors: 0

  Z:
    Hanja_reading_decomposition_checked: 80
    declared_equals_recomputed: 80
    declared_errors: 0

  Rime:
    member_syllable_decomposition_checked: 62
    shared_medial_coda_match: 62
    onset_match: 62
    declared_errors: 0

  state: JAMO_DECOMPOSITION_VERIFIED
```

## 11. ㅇ–Ø–Coda ㅇ Audit

```yaml
Data_X_ieung_audit:
  records_reported: 12
  orthographic_initial_ㅇ_and_phonetic_Ø_consistent: 12
  actual_coda_distribution:
    empty: 4
    coda_ㅇ_ŋ: 6
    coda_ㅂ_p_stop: 1
    coda_ㄹ_l: 1
  initial_ㅇ_recorded_as_ŋ_errors: 0
  coda_ㅇ_recorded_as_silent_errors: 0

Data_Z_ieung_audit:
  records_reported: 45
  flag_decomposition_match: 45
  orthographic_initial_ㅇ_coda_not_ㅇ: 14
  orthographic_initial_ㅇ_and_coda_ㅇ: 9
  non_ㅇ_initial_and_coda_ㅇ: 22
  initial_ㅇ_recorded_as_ŋ_errors: 0
  coda_ㅇ_recorded_as_silent_errors: 0

cross_verdict: PASS_IEUNG_ZERO_ONSET_CODA_SEPARATION
```

### 11.1 Anonymous supplementary records

```yaml
anonymous_ieung_records:
  count: 10
  readings: ["강", "앙", "갱", "냉", "생", "앵", "공", "송", "옹", "경"]
  current_entry_id: null
  source_state: RIME_CONTROL_MEMBER
  mechanical_flags: PASS
  identity_addressability: FAIL
  correction: assign_stable_rime_member_or_cross_record_ids
```

기계값은 맞지만 10개 Supplementary Record의 `entry_id`가 `null`이다. Group Member 자체의 존재 여부와 별개로, 검산 가능한 Record Identity를 부여해야 한다.

## 12. Raw–Normalized Audit

```yaml
raw_normalized_audit:
  X:
    raw_source_form_preserved: 60
    normalized_NFC_present: 60
    decomposed_NFD_present: 60
    raw_to_normalized_identity_match: 60
    semantic_rewrite_detected: 0

  Z:
    raw_Hanja_character_preserved: 80
    raw_Korean_reading_preserved: 80
    Unicode_codepoint_present: 80
    normalized_Jamo_present: 80
    word_usage_separate_from_Hanja_identity: 80
    semantic_rewrite_detected: 0

  structural_analysis_reserved_fields_non_null:
    X: 0
    Z: 0

  state: RAW_NORMALIZED_AUDIT_PASS
```

## 13. Duplicate Audit

```yaml
duplicate_audit:
  X:
    reported_entries: 60
    unique_entry_ids: 60
    unique_surfaces: 60
    duplicate_inflation: 0
    direct_entry_vs_search_route_links: 13
    decision: DUPLICATE_LINK_VERIFIED

  Z:
    reported_Hanja_entries: 80
    unique_entry_ids: 80
    unique_characters: 80
    unique_character_reading_pairs: 80
    duplicate_inflation: 0
    one_Hanja_multiple_words_counted_as_new_identity: 0
    repository_view_vs_raw_CSV_double_counted: false
    decision: DUPLICATE_LINK_VERIFIED

  group_members:
    same_syllable_duplicate_entry_ids: 0
    same_syllable_duplicate_characters_within_group: 0
    rime_duplicate_onsets_within_set: 0

  state: PASS_NO_DUPLICATE_INFLATION
```

## 14. Quantity Audit

```yaml
quantity_audit:
  native_entries_reported: 60
  native_unique_identities: 60
  native_exact_entry_source_verified: 13
  native_source_location_incomplete: 47

  Hanja_entries_reported: 80
  Hanja_unique_Unicode_identities: 80
  Hanja_reading_hun_Tier3_line_bound: 80
  Hanja_usage_detail_source_verified: 0
  Hanja_usage_source_location_incomplete: 80

  same_syllable_groups: 19
  same_syllable_group_members: 75
  same_rime_sets: 16
  same_rime_members: 62

  duplicate_inflation: 0
  mechanically_invalid_entries: 0
  mechanically_verified_unique_total_by_distinct_object_class: 140

  verified_unique_total_is_not_one_authority_level: true
  promotion_ready_total: NOT_COMPUTABLE_UNTIL_SOURCE_GAPS_CLOSED
```

## 15. Source Conflicts

```yaml
source_conflicts:
  - conflict_id: XZ-CF-001
    subject: X_47_entries_without_target_code
    state: MISSING_SOURCE_LOCATION
    preservation: keep_official_reentry_route_and_do_not_claim_exact_entry_verification

  - conflict_id: XZ-CF-002
    subject: X_9_homonym_or_sense_identities
    state: UNCERTAIN_IDENTITY
    preservation: do_not_select_sense_without_target_code

  - conflict_id: XZ-CF-003
    subject: X_60_example_sentences
    state: MISSING_SOURCE_LOCATION
    preservation: reclassify_as_normalized_illustrative_examples_not_source_quotes

  - conflict_id: XZ-CF-004
    subject: official_Hanja_XLS_vs_transformed_CSV
    state: SOURCE_CONFLICT
    preservation: transformed_CSV_remains_Tier3

  - conflict_id: XZ-CF-005
    subject: Z_80_usage_words_without_detail_word_no
    state: MISSING_SOURCE_LOCATION
    preservation: query_URL_is_reentry_route_not_exact_source_position

  - conflict_id: XZ-CF-006
    subject: Rime_43_Sino_members_outside_core_identity_registry
    state: UNCERTAIN_IDENTITY
    preservation: do_not_promote_to_full_Hanja_identity_record

  - conflict_id: XZ-CF-007
    subject: SINO_SURFACE_and_SINO_NONINITIAL_members
    state: SOURCE_CONFLICT
    preservation: split_canonical_reading_from_usage_surface_and_position

  - conflict_id: XZ-CF-008
    subject: anonymous_ieung_supplementary_records
    state: NORMALIZATION_ERROR
    preservation: values_preserved_but_stable_record_ID_required

  - conflict_id: XZ-CF-009
    subject: variant_拿_拏
    state: UNCERTAIN_IDENTITY
    preservation: link_without_merge_and_materialize_separate_identity_only_with_source

  - conflict_id: XZ-CF-010
    subject: orthographic_coda_vs_standard_pronunciation
    state: SOURCE_CONFLICT
    preservation: keep_낮_넋_늪_숲_spelling_and_pronunciation_separate
```

## 16. Invalid Group Members

```yaml
invalid_group_member_audit:
  same_syllable_mechanical_invalid_count: 0
  same_rime_mechanical_invalid_count: 0
  nonexistent_member_proven_by_current_inputs: 0
  forced_completion_detected: false

  source_unverified_is_not_invalid:
    same_syllable_members_missing_official_detail: 75
    same_rime_members_missing_official_detail: 62

  decision:
    mechanical_group_structure: PASS
    full_source_verified_group_structure: HOLD
```

## 17. Uncertain Identities

### 17.1 X explicit uncertain lexical identities

| Lemma | Reason | State |
|---|---|---|
| `김` | 복수 품사·동형어·다의 Sense 가능; individual target_code selection required | `UNCERTAIN_IDENTITY` |
| `날` | 복수 품사·동형어·다의 Sense 가능; individual target_code selection required | `UNCERTAIN_IDENTITY` |
| `눈` | 복수 품사·동형어·다의 Sense 가능; individual target_code selection required | `UNCERTAIN_IDENTITY` |
| `살` | 복수 품사·동형어·다의 Sense 가능; individual target_code selection required | `UNCERTAIN_IDENTITY` |
| `새` | 복수 품사·동형어·다의 Sense 가능; individual target_code selection required | `UNCERTAIN_IDENTITY` |
| `샘` | 복수 품사·동형어·다의 Sense 가능; individual target_code selection required | `UNCERTAIN_IDENTITY` |
| `술` | 복수 품사·동형어·다의 Sense 가능; individual target_code selection required | `UNCERTAIN_IDENTITY` |
| `우리` | 복수 품사·동형어·다의 Sense 가능; individual target_code selection required | `UNCERTAIN_IDENTITY` |
| `이제` | 복수 품사·동형어·다의 Sense 가능; individual target_code selection required | `UNCERTAIN_IDENTITY` |

### 17.2 Z and cross-dataset uncertainty

```yaml
uncertain_identity_inventory:
  X_explicit_homonym_or_sense_uncertainty: 9
  X_source_location_incomplete_entries: 47

  Z_official_word_detail_ID_missing: 80
  Z_historical_readings_not_stated: 80
  Z_variant_relation_without_full_variant_record: 1

  Rime_Sino_members_without_core_identity_record: 43
  Rime_surface_or_noninitial_context_field_gap: 9
  anonymous_ieung_record_ID_gap: 10

  note: categories_overlap_and_must_not_be_summed_as_unique_entities
```

## 18. Proposed Corrections

```yaml
proposed_corrections:
  - correction_id: XZ-CORR-001
    target: Data_X_47_reentry_only_entries
    action: bind_individual_target_code_exact_entry_snapshot_and_source_position
    state_after_application: SOURCE_POSITION_VERIFIED

  - correction_id: XZ-CORR-002
    target: Data_X_9_uncertain_lemmas
    action: select_or_split_dictionary_sense_identity_by_target_code
    state_after_application: LEXICAL_CLASS_VERIFIED_OR_RETAIN_UNCERTAIN

  - correction_id: XZ-CORR-003
    target: Data_X_example_sentences
    action: add_source_sentence_location_or_label_as_generated_normalized_example
    state_after_application: SOURCE_CLAIM_BOUNDARY_RESTORED

  - correction_id: XZ-CORR-004
    target: Data_Z_Hanja_reading_and_hun
    action: bind_official_XLS_exact_bytes_and_reproducible_transform_or_official_Hanja_dictionary_entries
    state_after_application: HANJA_READING_HUN_SOURCE_VERIFIED

  - correction_id: XZ-CORR-005
    target: Data_Z_80_usage_words
    action: bind_stdict_word_no_definition_location_and_exact_morpheme_position
    state_after_application: SOURCE_POSITION_VERIFIED

  - correction_id: XZ-CORR-006
    target: Rime_43_unregistered_Sino_members
    action: create_full_Hanja_identity_records_with_character_codepoint_reading_hun_word_Hanja_position_and_sources
    state_after_application: HANJA_IDENTITY_VERIFIED

  - correction_id: XZ-CORR-007
    target: Rime_3_native_members
    action: add_explicit_cross_refs_to_X_entry_IDs
    mappings:
      - Z-RIME-007/새 -> X-ㅅ-E05
      - Z-RIME-009/너 -> X-ㄴ-E02
      - Z-RIME-014/눈 -> X-ㄴ-E11
    state_after_application: LEXICAL_CLASS_LINK_VERIFIED

  - correction_id: XZ-CORR-008
    target: 9_surface_or_noninitial_Hanja_members
    action: split_canonical_reading_usage_surface_morpheme_position_and_pronunciation
    state_after_application: IDENTITY_SURFACE_POSITION_VERIFIED

  - correction_id: XZ-CORR-009
    target: 10_anonymous_ieung_records
    action: assign_stable_record_ID_and_parent_rime_member_ref
    state_after_application: NORMALIZATION_ERROR_CLOSED

  - correction_id: XZ-CORR-010
    target: 拿_拏_variant_relation
    action: preserve_relation_and_add_separate_full_identity_record_only_if_source_authorizes
    state_after_application: DUPLICATE_LINK_VERIFIED

  - correction_id: XZ-CORR-011
    target: Z-RIME-015_and_Z-RIME-016
    action: preserve_missing_ㅅ_without_forced_completion
    state_after_application: RIME_SET_VERIFIED_WITH_EXPLICIT_GAP

  - correction_id: XZ-CORR-012
    target: all_inputs
    action: retain_all_analysis_reserved_fields_as_null
    state_after_application: NO_SEMANTIC_ANALYSIS
```

## 19. Unresolved

```yaml
unresolved:
  - id: XZ-U-001
    item: X_47_exact_dictionary_entry_snapshots
    blocking: true

  - id: XZ-U-002
    item: X_9_homonym_or_sense_target_codes
    blocking: scoped

  - id: XZ-U-003
    item: X_example_sentence_provenance
    blocking: scoped

  - id: XZ-U-004
    item: official_Hanja_XLS_exact_bytes_and_transform_reproduction
    blocking: true

  - id: XZ-U-005
    item: Z_80_official_dictionary_detail_word_numbers
    blocking: true

  - id: XZ-U-006
    item: Rime_43_Sino_member_full_identity_records
    blocking: true

  - id: XZ-U-007
    item: canonical_reading_vs_surface_position_for_9_members
    blocking: scoped

  - id: XZ-U-008
    item: stable_IDs_for_10_ieung_supplementary_records
    blocking: scoped

  - id: XZ-U-009
    item: full_variant_identity_for_拏_if_required
    blocking: scoped

  - id: XZ-U-010
    item: direct_source_positions_for_all_62_rime_members
    blocking: true
```

## 20. Required Next Data

```yaml
required_next_data:
  - request_id: XZ-ND-001
    object: X_47_individual_KRDICT_entries
    required_fields: [target_code, exact_URL, sense_number, part_of_speech, origin_class, pronunciation, definition_location]

  - request_id: XZ-ND-002
    object: X_9_homonym_sense_disambiguation
    lemmas: [김, 날, 눈, 살, 새, 샘, 술, 우리, 이제]

  - request_id: XZ-ND-003
    object: official_Hanja_source
    required: original_XLS_exact_bytes_or_official_entry_level_Hanja_dictionary_sources

  - request_id: XZ-ND-004
    object: reproducible_CSV_transform_manifest
    required_fields: [input_hash, transform_code, output_hash, row_lineage]

  - request_id: XZ-ND-005
    object: Z_80_STDICT_detail_entries
    required_fields: [word_no, exact_entry_URL, Hanja_form, pronunciation, definition_location, morpheme_position]

  - request_id: XZ-ND-006
    object: Rime_43_unregistered_Sino_identities
    required_fields: [character, codepoint, canonical_reading, representative_hun, usage_word_Hanja, position, official_sources]

  - request_id: XZ-ND-007
    object: Rime_62_member_detail_sources
    required_fields: [exact_entry_ID, exact_location, pronunciation, lexical_class]

  - request_id: XZ-ND-008
    object: stable_cross_record_ID_map
    required_for: 10_anonymous_ieung_records

  - request_id: XZ-ND-009
    object: variant_拏_identity_source
    required_only_if: separate_identity_record_is_promoted

  - request_id: XZ-ND-010
    object: X_example_sentence_provenance_or_reclassification_manifest
```

## 21. Handoff to gpt.logi

```yaml
handoff:
  from:
    instance: gpt.xz
    fixed_seat: HRTDB_A::gpt.xz
    stage_id: R02_2D_XZ
    occupation_class: SOURCE_IDENTITY_AND_DATASET_VERIFICATION

  to:
    recipient: gpt.logi
    recipient_seat: HRTDB_A::gpt.xyzt

  verification_summary:
    exact_input_binding: PASS
    native_Hanja_internal_separation: PASS_WITH_SOURCE_GAPS
    Hanja_Unicode_identity: PASS_80_OF_80
    same_syllable_mechanical_audit: PASS_19_OF_19
    same_rime_mechanical_audit: PASS_16_OF_16
    Jamo_decomposition: PASS
    ieung_zero_onset_coda_split: PASS
    duplicate_inflation: PASS_ZERO
    source_position_gate: HOLD

  completion_state: HOLD_WITH_INSUFFICIENT_SOURCE_LOCATION

  prohibited:
    - promote_to_Track_DB
    - infer_common_semantic_structure
    - infer_structural_equivalence
    - repair_missing_sources_from_memory
    - delete_conflicts
    - GitHub_mutation
```

## Final Guard

```text
same syllable is not same Hanja.
same rime is not structural equivalence.
Unicode equality is not semantic equality.
orthographic initial ㅇ is not coda ㅇ.
orthographic initial ㅇ is not phonetic /ŋ/.
phonetic zero onset is not an empty data record.
query URL is not exact dictionary entry identity.
transformed CSV is not original official XLS.
source collection is not structural analysis.
classification verification is not meaning analysis.
relation is not merge.
Result is not Track DB.
```

~~~

### HRTDB_A::gpt.yz — `552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e.A.md`

~~~text
---
document_type: HRTDB_A_2D_SOURCE_VERIFICATION_RESULT
document_class: HISTORICAL_PRONUNCIATION_HANJA_RELATION_CROSS_VERIFICATION_RESULT
object_identity:
  object_id: HRTDB_A_GLANG_R01_YZ_HISTORICAL_PRONUNCIATION_HANJA_VERIFICATION
  object_class: HRTDB_A_2D_SOURCE_VERIFICATION_RESULT
  state: VERIFICATION_COMPLETE_WITH_UNRESOLVED
  title: GLANG R01 — Historical Pronunciation·Hanja Identity·Position·Rime Cross-verification

generation:
  generated_by: gpt.yz
  fixed_seat: HRTDB_A::gpt.yz
  cycle_id: GLANG-SOURCE-COLLECTION-BASE-CONSONANTS-R01
  stage_id: R02_2D_YZ
  occupation_class: HISTORICAL_RELATION_AND_SOURCE_CLAIM_VERIFICATION
  source_authority: 승이
  directive_author: gpt.logi
  directive_author_seat: HRTDB_A::gpt.xyzt

execution_binding:
  directive:
    normalized_filename: 10cd6ac702fad248f7ca5c243d5ae8fffb05834dc212d311acfda4fc764c5698.A.md
    exact_byte_sha256: 10cd6ac702fad248f7ca5c243d5ae8fffb05834dc212d311acfda4fc764c5698
    exact_byte_count: 8817
  direct_input_count: 2
  direct_inputs:
    - role: GPT_Y_RESULT
      normalized_filename: 5bda1cc62834c8b5baa459f4ca7721195c83538bdddaf9e8dd4c74781fc38892.A.md
      exact_byte_sha256: 5bda1cc62834c8b5baa459f4ca7721195c83538bdddaf9e8dd4c74781fc38892
      exact_byte_count: 65498
      producer: gpt.y
      seat: HRTDB_A::gpt.y
      stage_id: R01_1D_Y
      state: COLLECTION_COMPLETE
    - role: GPT_Z_RESULT
      normalized_filename: 42b4178a22efc8e81ece1bdc31f2c9be4116920f6b8e1b67023ae9442da18a3a.A.md
      exact_byte_sha256: 42b4178a22efc8e81ece1bdc31f2c9be4116920f6b8e1b67023ae9442da18a3a
      exact_byte_count: 353635
      producer: gpt.z
      seat: HRTDB_A::gpt.z
      stage_id: R01_1D_Z
      state: COLLECTION_PARTIAL_WITH_GAPS
  exact_identity_binding: PASS
  new_web_search: false
  new_url_addition: false
  input_mutation: false

output_contract:
  output_count: 1
  filename_rule: <exact_body_sha256>.A.md
  encoding: UTF-8
  line_ending: LF
  bom: false
  final_newline: true
  github_mutation: false
  track_db_promotion: false

content_addressing:
  algorithm: SHA-256
  canonical_hash_surface: FILENAME
  self_hash_inside_content: prohibited
---

# GLANG R01 — gpt.yz Source Cross-verification

## 1. Directive Identity

```yaml
directive_identity:
  received_filename: 10cd6ac702fad248f7ca5c243d5ae8fffb05834dc212d311acfda4fc764c5698.A(1).md
  normalized_filename: 10cd6ac702fad248f7ca5c243d5ae8fffb05834dc212d311acfda4fc764c5698.A.md
  expected_sha256: 10cd6ac702fad248f7ca5c243d5ae8fffb05834dc212d311acfda4fc764c5698
  actual_sha256: 10cd6ac702fad248f7ca5c243d5ae8fffb05834dc212d311acfda4fc764c5698
  exact_byte_count: 8817
  recipient_instance: gpt.yz
  recipient_seat: HRTDB_A::gpt.yz
  cycle_id: GLANG-SOURCE-COLLECTION-BASE-CONSONANTS-R01
  stage_id: R02_2D_YZ
  exact_identity_check: PASS
```

## 2. Bound Input Identities

| Role | Normalized filename | Exact bytes | Actual SHA-256 | Producer / Seat | State | Binding |
|---|---|---:|---|---|---|---|
| gpt.y Result | `5bda1cc62834c8b5baa459f4ca7721195c83538bdddaf9e8dd4c74781fc38892.A.md` | 65,498 | `5bda1cc62834c8b5baa459f4ca7721195c83538bdddaf9e8dd4c74781fc38892` | `gpt.y / HRTDB_A::gpt.y` | `COLLECTION_COMPLETE` | `PASS` |
| gpt.z Result | `42b4178a22efc8e81ece1bdc31f2c9be4116920f6b8e1b67023ae9442da18a3a.A.md` | 353,635 | `42b4178a22efc8e81ece1bdc31f2c9be4116920f6b8e1b67023ae9442da18a3a` | `gpt.z / HRTDB_A::gpt.z` | `COLLECTION_PARTIAL_WITH_GAPS` | `PASS_WITH_GAPS_PRESERVED` |

## 3. Input Integrity Check

```yaml
input_integrity:
  exact_direct_input_count: 2
  observed_direct_input_count: 2
  filename_hash_matches_actual_bytes:
    gpt_y_result: true
    gpt_z_result: true
  cycle_match: true
  producer_seat_match: true
  input_bytes_modified: false
  hidden_context_inherited: false

  gpt_y_inventory:
    source_count: 19
    position_relation_count: 16
    historical_lineage_count: 9
    pronunciation_claim_count: 11
    source_conflict_count: 4
    collection_gap_count: 6

  gpt_z_inventory:
    hanja_identity_count: 80
    same_syllable_group_count: 19
    same_rime_set_count: 16
    modern_ieung_position_record_count: 45
    source_conflict_count: 3
    uncertain_identity_count: 2
    collection_gap_count: 4

  mechanical_unicode_verification:
    records_checked: 80
    character_codepoint_match: 80
    hangul_jamo_decomposition_match: 80
    nfc_match: 80
    nfd_match: 80
    mismatch_count: 0
```

## 4. Verification Scope

```text
검산한다:
- 역사형–현대형 Identity의 Source 결속
- 직접기록·사전보고·학술재구·불확실 추정의 분리
- Hanja Character Identity와 현대 한국 한자음의 Source 결속
- 현대 표면초성과 역사초성의 분리
- 첫 위치·비첫 위치·종성 위치의 분리
- 현대 철자운모와 역사·재구운모의 분리
- Raw·현대전사·Unicode Normalization의 분리

판정하지 않는다:
- 역사변화의 구조적 의미
- 시간순서의 인과성
- 공통 의미나 자모 방향
- 가설 지지·반박
- Source 없는 본래초성·역사음·재구음
```

## 5. Historical–Modern Identity Audit

### `Y-HIST-001` — 초성 옛이응 ㆁ

```yaml
lineage_audit:
  lineage_id: Y-HIST-001
  object_identity: "초성 옛이응 ㆁ"
  historical_state: >-
    ㆁ — 중세국어~16세기 말, 음가 존재가 Source에서 보고됨
  intermediate_states: >-
    현대 ㅇ을 중간단계로 직접 놓은 결속은 Source가 단일 문자계보로 확정하지 않음
  modern_state: >-
    현대 초성 ㅇ=무음 표기자리 / 종성 ㅇ=[ŋ]
  source_support: >-
    SRC-007, SRC-008, SRC-002/004의 층별 자료
  unsupported_jumps: >-
    ㆁ → 현대 초성·종성 ㅇ을 하나의 직선계보로 병합한 점
  conflicting_sources: >-
    Y-POS-004의 same_lineage_source_supported=false와 Y-HIST-001의 선형 계보표현이 충돌
  verification_state: "UNSUPPORTED_LINEAGE_LINK + MULTIPLE_LINEAGE_CANDIDATES"
```
### `Y-HIST-002` — 깔리-

```yaml
lineage_audit:
  lineage_id: Y-HIST-002
  object_identity: "깔리-"
  historical_state: >-
    이다 — 15세기 표기, 역사 초성 ㅇ 음가를 사전이 보고
  intermediate_states: >-
    리다 — 18세기 중간형
  modern_state: >-
    깔리다
  source_support: >-
    SRC-012 사전 역사정보
  unsupported_jumps: >-
    없음. 단, 한 어휘 계보를 ㅇ 전체 역사로 일반화 금지
  conflicting_sources: >-
    정확 음가의 직접기록과 재구 방법은 없음
  verification_state: "MODERN_HISTORICAL_LINK_VERIFIED + SCHOLARLY_RECONSTRUCTION"
```
### `Y-HIST-003` — 이르-

```yaml
lineage_audit:
  lineage_id: Y-HIST-003
  object_identity: "이르-"
  historical_state: >-
    니르다 — 중세 표기
  intermediate_states: >-
    근대국어 시기 어두 ㄴ 탈락으로 설명
  modern_state: >-
    이르다
  source_support: >-
    SRC-006
  unsupported_jumps: >-
    세부 시기·중간 문헌형은 미세분화
  conflicting_sources: >-
    현상 명칭과 periodization은 Source가 연구자 견해차를 열어 둠
  verification_state: "MODERN_HISTORICAL_LINK_VERIFIED + SOURCE_CONFLICT"
```
### `Y-HIST-004` — 女

```yaml
lineage_audit:
  lineage_id: Y-HIST-004
  object_identity: "女"
  historical_state: >-
    녀를 역사단계로 둔 현재 필드
  intermediate_states: >-
    여를 현대 단어 첫 위치 표면형으로 둔 현재 필드
  modern_state: >-
    여자 / 남녀
  source_support: >-
    SRC-003, Z-HANJA-053
  unsupported_jumps: >-
    시대변화와 현대 위치조건을 혼합
  conflicting_sources: >-
    Z는 Identity reading 녀와 usage 남녀를 분리하며 역사음은 비어 있음
  verification_state: "POSITION_RELATION_VERIFIED; HISTORICAL_LINEAGE_RECLASSIFICATION_REQUIRED"
```
### `Y-HIST-005` — 年

```yaml
lineage_audit:
  lineage_id: Y-HIST-005
  object_identity: "年"
  historical_state: >-
    년을 역사단계로 둔 현재 필드
  intermediate_states: >-
    연을 현대 단어 첫 위치 표면형으로 둔 현재 필드
  modern_state: >-
    연세 / 학년 / 몇 년
  source_support: >-
    SRC-003, Z-HANJA-054
  unsupported_jumps: >-
    시대변화와 현대 위치·의존명사 조건을 혼합
  conflicting_sources: >-
    Z는 Identity reading 년과 usage 작년을 분리하며 역사음은 비어 있음
  verification_state: "POSITION_RELATION_VERIFIED; HISTORICAL_LINEAGE_RECLASSIFICATION_REQUIRED"
```
### `Y-HIST-006` — 같-

```yaml
lineage_audit:
  lineage_id: Y-HIST-006
  object_identity: "같-"
  historical_state: >-
    다 / 다
  intermediate_states: >-
    갓-/갓ㅎ-/갓ㅌ- 등 복수 표기
  modern_state: >-
    같다
  source_support: >-
    SRC-009 사전 역사정보
  unsupported_jumps: >-
    복수 표기를 단일 음성값으로 환산하지 않음
  conflicting_sources: >-
    직접 역사 음성기록 없음
  verification_state: "MODERN_HISTORICAL_LINK_VERIFIED + DICTIONARY_REPORTED"
```
### `Y-HIST-007` — 싶-

```yaml
lineage_audit:
  lineage_id: Y-HIST-007
  object_identity: "싶-"
  historical_state: >-
    식브다
  intermediate_states: >-
    십브다 → 시브다/시프다
  modern_state: >-
    싶다
  source_support: >-
    SRC-010 사전 역사정보
  unsupported_jumps: >-
    없음. 각 단계 발음은 문헌·사전보고
  conflicting_sources: >-
    직접 음성기록 없음
  verification_state: "MODERN_HISTORICAL_LINK_VERIFIED + DICTIONARY_REPORTED"
```
### `Y-HIST-008` — 새끼

```yaml
lineage_audit:
  lineage_id: Y-HIST-008
  object_identity: "새끼"
  historical_state: >-
    삿기
  intermediate_states: >-
    새 / 색기
  modern_state: >-
    새끼
  source_support: >-
    SRC-011 사전 역사정보
  unsupported_jumps: >-
    ㅺ·ㄲ·ㄱ 문자 Identity를 병합하지 않음
  conflicting_sources: >-
    정확 발생연대는 세기별 용례범위
  verification_state: "MODERN_HISTORICAL_LINK_VERIFIED + DICTIONARY_REPORTED"
```
### `Y-HIST-009` — 잎 / 닢

```yaml
lineage_audit:
  lineage_id: Y-HIST-009
  object_identity: "잎 / 닢"
  historical_state: >-
    닢 — Source 해설
  intermediate_states: >-
    깻닢·나뭇닢 분석 후보
  modern_state: >-
    잎 / 깻잎 / 나뭇잎
  source_support: >-
    SRC-017
  unsupported_jumps: >-
    정확 세기와 독립 역사사전 계보가 없음
  conflicting_sources: >-
    ㄴㄴ 첨가 분석 반론이 같은 해설에 병기됨
  verification_state: "MULTIPLE_LINEAGE_CANDIDATES + SOURCE_CONFLICT"
```


### 5.10 Historical lineage classification summary

```yaml
historical_lineage_summary:
  reported: 9
  modern_historical_link_verified:
    count: 5
    ids: [Y-HIST-002, Y-HIST-003, Y-HIST-006, Y-HIST-007, Y-HIST-008]
  reclassified_as_modern_position_relation:
    count: 2
    ids: [Y-HIST-004, Y-HIST-005]
  unsupported_single_lineage:
    count: 1
    ids: [Y-HIST-001]
  multiple_lineage_candidates_or_source_conflict:
    count: 1
    ids: [Y-HIST-009]
```

## 6. Pronunciation Claim-Type Audit

### 6.1 Modern pronunciation registry

| Claim | Form | Reported value | Directive state | Source subtype | Direct recording boundary |
|---|---|---|---|---|---|
| `PRON-001` | 강이 | [강이] | `DICTIONARY_REPORTED` | `OFFICIAL_EXPLANATORY_RESPONSE` | direct_attestation=false |
| `PRON-002` | 목이 | [모기] | `DICTIONARY_REPORTED` | `OFFICIAL_NORM_EXAMPLE` | direct_attestation=false |
| `PRON-003` | 깎아 | [까까] | `DICTIONARY_REPORTED` | `OFFICIAL_NORM_EXAMPLE` | direct_attestation=false |
| `PRON-004` | 옷 | [옫] | `DICTIONARY_REPORTED` | `OFFICIAL_NORM_EXAMPLE` | direct_attestation=false |
| `PRON-005` | 옷이 | [오시] | `DICTIONARY_REPORTED` | `OFFICIAL_NORM_EXAMPLE` | direct_attestation=false |
| `PRON-006` | 솜이불 | [솜ː니불] | `DICTIONARY_REPORTED` | `OFFICIAL_NORM_EXAMPLE` | direct_attestation=false |
| `PRON-007` | 색연필 | [생년필] | `DICTIONARY_REPORTED` | `OFFICIAL_NORM_EXAMPLE` | direct_attestation=false |
| `PRON-008` | 낫다/나아 | [낟ː따]/[나아] | `DICTIONARY_REPORTED` | `OFFICIAL_DICTIONARY_ENTRY` | direct_attestation=false |
| `PRON-009` | 붓다/부어 | [붇ː따]/[부어] | `DICTIONARY_REPORTED` | `OFFICIAL_DICTIONARY_ENTRY` | direct_attestation=false |
| `PRON-010` | 같다 | [갇따] | `DICTIONARY_REPORTED` | `OFFICIAL_DICTIONARY_HISTORY` | direct_attestation=false |
| `PRON-011` | 싶다/싶어 | [십따]/[시퍼] | `DICTIONARY_REPORTED` | `OFFICIAL_DICTIONARY_HISTORY` | direct_attestation=false |

```yaml
pronunciation_claim_summary:
  reported_claim_count: 11
  typed_claim_count: 11
  directly_attested_audio_or_instrumental_record_count: 0
  dictionary_or_official_norm_reported_count: 11
  claim_type_correction:
    OFFICIAL_NORM_EXAMPLE: PRESERVE_AS_SOURCE_SUBTYPE
    directive_level_state: DICTIONARY_REPORTED
```

### 6.2 Historical phonetic claims

```yaml
historical_phonetic_claims:
  - object: "초성 ㆁ / 중세 초성 ㅇ"
    value: "음가 존재 또는 조건부 음가"
    source: "SRC-008; SRC-007"
    method_as_source_states: NOT_STATED
    confidence_as_source_states: LIMITED_EXPLANATORY_SOURCE
    direct_attestation: false
    current_state: SOURCE_UNCERTAIN

  - object: "이다 둘째 음절 초성 ㅇ"
    value: "후두 유성 마찰음"
    source: "SRC-012"
    method_as_source_states: DICTIONARY_REPORTED_SCHOLARLY_EXPLANATION
    confidence_as_source_states: LEXEME_SCOPED
    direct_attestation: false
    current_state: SCHOLARLY_RECONSTRUCTION
```

```text
문헌 표기 ≠ 직접 음성기록.
사전이 보고한 재구음 ≠ AI가 독립 생성한 재구음.
```

## 7. Hanja Reading Lineage Audit

### 7.1 Global decision

```yaml
hanja_reading_global_audit:
  character_identity_count: 80
  unique_character_count: 80
  unicode_scalar_identity_verified: 80
  modern_hangul_decomposition_verified: 80

  korean_reading_link:
    source: TIER_3_TRANSFORMED_HANJA_CSV
    source_bound_count: 80
    independent_official_identity_crosscheck_count: 0
    verification_state: HANJA_READING_LINK_VERIFIED_WITH_SOURCE_AUTHORITY_BOUNDARY

  representative_hun:
    source_bound_count: 80
    exhaustive_meaning_claim: false

  usage_word:
    official_dictionary_query_url_bound_count: 80
    stable_detail_id_materialized_count: 0
    verification_state: MISSING_SOURCE_LOCATION

  historical_reading:
    stated_by_selected_Z_records: 0
    verified_cross_input_historical_hanja_links: 0
```

### 7.2 Identity ledger

| Entry | Hanja | Codepoint | Selected reading | Modern Jamo | Usage word | Reading link | Usage location |
|---|---|---|---|---|---|---|---|
| `Z-HANJA-001` | 英 | `U+82F1` | 영 | `ㅇ·ㅕ·ㅇ` | 영어 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-002` | 永 | `U+6C38` | 영 | `ㅇ·ㅕ·ㅇ` | 영구 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-003` | 榮 | `U+69AE` | 영 | `ㅇ·ㅕ·ㅇ` | 영광 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-004` | 迎 | `U+8FCE` | 영 | `ㅇ·ㅕ·ㅇ` | 환영 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-005` | 映 | `U+6620` | 영 | `ㅇ·ㅕ·ㅇ` | 영화 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-006` | 營 | `U+71DF` | 영 | `ㅇ·ㅕ·ㅇ` | 경영 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-007` | 園 | `U+5712` | 원 | `ㅇ·ㅝ·ㄴ` | 공원 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-008` | 遠 | `U+9060` | 원 | `ㅇ·ㅝ·ㄴ` | 원격 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-009` | 元 | `U+5143` | 원 | `ㅇ·ㅝ·ㄴ` | 원금 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-010` | 原 | `U+539F` | 원 | `ㅇ·ㅝ·ㄴ` | 원래 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-011` | 院 | `U+9662` | 원 | `ㅇ·ㅝ·ㄴ` | 병원 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-012` | 願 | `U+9858` | 원 | `ㅇ·ㅝ·ㄴ` | 소원 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-013` | 人 | `U+4EBA` | 인 | `ㅇ·ㅣ·ㄴ` | 인간 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-014` | 因 | `U+56E0` | 인 | `ㅇ·ㅣ·ㄴ` | 원인 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-015` | 印 | `U+5370` | 인 | `ㅇ·ㅣ·ㄴ` | 인쇄 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-016` | 引 | `U+5F15` | 인 | `ㅇ·ㅣ·ㄴ` | 인용 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-017` | 認 | `U+8A8D` | 인 | `ㅇ·ㅣ·ㄴ` | 인정 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-018` | 意 | `U+610F` | 의 | `ㅇ·ㅢ·∅` | 의미 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-019` | 醫 | `U+91AB` | 의 | `ㅇ·ㅢ·∅` | 의학 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-020` | 衣 | `U+8863` | 의 | `ㅇ·ㅢ·∅` | 의복 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-021` | 家 | `U+5BB6` | 가 | `ㄱ·ㅏ·∅` | 가정 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-022` | 歌 | `U+6B4C` | 가 | `ㄱ·ㅏ·∅` | 가곡 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-023` | 價 | `U+50F9` | 가 | `ㄱ·ㅏ·∅` | 가격 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-024` | 加 | `U+52A0` | 가 | `ㄱ·ㅏ·∅` | 가산 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-025` | 可 | `U+53EF` | 가 | `ㄱ·ㅏ·∅` | 가능 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-026` | 各 | `U+5404` | 각 | `ㄱ·ㅏ·ㄱ` | 각각 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-027` | 角 | `U+89D2` | 각 | `ㄱ·ㅏ·ㄱ` | 각도 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-028` | 刻 | `U+523B` | 각 | `ㄱ·ㅏ·ㄱ` | 시각 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-029` | 覺 | `U+89BA` | 각 | `ㄱ·ㅏ·ㄱ` | 감각 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-030` | 脚 | `U+811A` | 각 | `ㄱ·ㅏ·ㄱ` | 각본 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-031` | 間 | `U+9593` | 간 | `ㄱ·ㅏ·ㄴ` | 공간 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-032` | 簡 | `U+7C21` | 간 | `ㄱ·ㅏ·ㄴ` | 간단 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-033` | 看 | `U+770B` | 간 | `ㄱ·ㅏ·ㄴ` | 간호 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-034` | 干 | `U+5E72` | 간 | `ㄱ·ㅏ·ㄴ` | 간섭 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-035` | 刊 | `U+520A` | 간 | `ㄱ·ㅏ·ㄴ` | 간행 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-036` | 感 | `U+611F` | 감 | `ㄱ·ㅏ·ㅁ` | 감정 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-037` | 減 | `U+6E1B` | 감 | `ㄱ·ㅏ·ㅁ` | 감소 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-038` | 監 | `U+76E3` | 감 | `ㄱ·ㅏ·ㅁ` | 감독 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-039` | 甘 | `U+7518` | 감 | `ㄱ·ㅏ·ㅁ` | 감미 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-040` | 敢 | `U+6562` | 감 | `ㄱ·ㅏ·ㅁ` | 용감 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-041` | 拿 | `U+62FF` | 나 | `ㄴ·ㅏ·∅` | 나포 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-042` | 懦 | `U+61E6` | 나 | `ㄴ·ㅏ·∅` | 나약 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-043` | 暖 | `U+6696` | 난 | `ㄴ·ㅏ·ㄴ` | 난방 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-044` | 難 | `U+96E3` | 난 | `ㄴ·ㅏ·ㄴ` | 난관 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-045` | 南 | `U+5357` | 남 | `ㄴ·ㅏ·ㅁ` | 남부 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-046` | 男 | `U+7537` | 남 | `ㄴ·ㅏ·ㅁ` | 남성 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-047` | 納 | `U+7D0D` | 납 | `ㄴ·ㅏ·ㅂ` | 납부 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-048` | 娘 | `U+5A18` | 낭 | `ㄴ·ㅏ·ㅇ` | 낭자 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-049` | 囊 | `U+56CA` | 낭 | `ㄴ·ㅏ·ㅇ` | 낭종 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-050` | 內 | `U+5167` | 내 | `ㄴ·ㅐ·∅` | 내부 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-051` | 耐 | `U+8010` | 내 | `ㄴ·ㅐ·∅` | 내구 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-052` | 奈 | `U+5948` | 내 | `ㄴ·ㅐ·∅` | 막무가내 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-053` | 女 | `U+5973` | 녀 | `ㄴ·ㅕ·∅` | 남녀 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-054` | 年 | `U+5E74` | 년 | `ㄴ·ㅕ·ㄴ` | 작년 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-055` | 念 | `U+5FF5` | 념 | `ㄴ·ㅕ·ㅁ` | 신념 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-056` | 寧 | `U+5BE7` | 녕 | `ㄴ·ㅕ·ㅇ` | 안녕 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-057` | 農 | `U+8FB2` | 농 | `ㄴ·ㅗ·ㅇ` | 농업 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-058` | 濃 | `U+6FC3` | 농 | `ㄴ·ㅗ·ㅇ` | 농도 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-059` | 腦 | `U+8166` | 뇌 | `ㄴ·ㅚ·∅` | 뇌수 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-060` | 惱 | `U+60F1` | 뇌 | `ㄴ·ㅚ·∅` | 번뇌 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-061` | 四 | `U+56DB` | 사 | `ㅅ·ㅏ·∅` | 사방 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-062` | 事 | `U+4E8B` | 사 | `ㅅ·ㅏ·∅` | 사건 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-063` | 史 | `U+53F2` | 사 | `ㅅ·ㅏ·∅` | 역사 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-064` | 士 | `U+58EB` | 사 | `ㅅ·ㅏ·∅` | 박사 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-065` | 師 | `U+5E2B` | 사 | `ㅅ·ㅏ·∅` | 교사 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-066` | 上 | `U+4E0A` | 상 | `ㅅ·ㅏ·ㅇ` | 상승 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-067` | 商 | `U+5546` | 상 | `ㅅ·ㅏ·ㅇ` | 상업 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-068` | 相 | `U+76F8` | 상 | `ㅅ·ㅏ·ㅇ` | 상호 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-069` | 想 | `U+60F3` | 상 | `ㅅ·ㅏ·ㅇ` | 상상 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-070` | 常 | `U+5E38` | 상 | `ㅅ·ㅏ·ㅇ` | 상시 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-071` | 成 | `U+6210` | 성 | `ㅅ·ㅓ·ㅇ` | 성공 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-072` | 性 | `U+6027` | 성 | `ㅅ·ㅓ·ㅇ` | 성격 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-073` | 聖 | `U+8056` | 성 | `ㅅ·ㅓ·ㅇ` | 성인 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-074` | 城 | `U+57CE` | 성 | `ㅅ·ㅓ·ㅇ` | 성벽 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-075` | 星 | `U+661F` | 성 | `ㅅ·ㅓ·ㅇ` | 성좌 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-076` | 先 | `U+5148` | 선 | `ㅅ·ㅓ·ㄴ` | 선행 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-077` | 線 | `U+7DDA` | 선 | `ㅅ·ㅓ·ㄴ` | 선형 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-078` | 善 | `U+5584` | 선 | `ㅅ·ㅓ·ㄴ` | 선의 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-079` | 選 | `U+9078` | 선 | `ㅅ·ㅓ·ㄴ` | 선택 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |
| `Z-HANJA-080` | 船 | `U+8239` | 선 | `ㅅ·ㅓ·ㄴ` | 선박 | `HANJA_READING_LINK_VERIFIED@TIER_3` | `MISSING_STABLE_DETAIL_ID` |

### 7.3 Cross-input Hanja links

```yaml
cross_input_hanja_links:
  - hanja: 女
    z_entry: Z-HANJA-053
    selected_identity_reading: 녀
    y_records: [Y-POS-009, Y-HIST-004]
    verified_relation: "동일 Character Identity 아래 현대 단어 첫 위치 여 / 비첫 위치 녀"
    historical_reading_verified: false
    state: POSITION_RELATION_VERIFIED

  - hanja: 年
    z_entry: Z-HANJA-054
    selected_identity_reading: 년
    y_records: [Y-POS-010, Y-HIST-005]
    verified_relation: "동일 Character Identity 아래 현대 단어 첫 위치 연 / 비첫 위치·의존명사 년"
    historical_reading_verified: false
    state: POSITION_RELATION_VERIFIED
```

```text
Identity reading 녀·년
≠ 모든 실제 용례의 표면초성.

여·연의 현대 위치형
≠ Source 없는 별도 역사 한자음.
```

## 8. Surface–Historical Initial Audit

```yaml
initial_layer_audit:
  modern_orthographic_initial:
    source: Data.Z Unicode/Hangul decomposition
    state: VERIFIED_MODERN_ORTHOGRAPHY

  modern_phonetic_initial:
    orthographic_ㅇ: "phonetic Ø under bound modern guidance"
    state: PRONUNCIATION_CLAIM_TYPED

  modern_coda_ㅇ:
    value: "[ŋ]"
    state: PRONUNCIATION_CLAIM_TYPED

  historical_initial_ㆁ_or_ㅇ:
    source: Data.Y historical explanation
    state: SOURCE_UNCERTAIN_OR_SCHOLARLY_RECONSTRUCTION

  prohibited_projection:
    - modern_initial_ㅇ_to_historical_ㆁ_identity
    - modern_coda_ㅇ_to_historical_onset_ㆁ_identity
    - Z_initial_group_to_original_historical_initial
```

### 8.1 Modern ㅇ cross-check

```yaml
modern_ieung_crosscheck:
  Data_Y_support:
    - Y-POS-001
    - Y-POS-002
    - Y-POS-004
  Data_Z_record_count: 45
  state_distribution:
    orthographic_initial_true_phonetic_zero_true_coda_true: 9
    orthographic_initial_true_phonetic_zero_true_coda_false: 14
    orthographic_initial_false_phonetic_zero_false_coda_true: 22
  modern_layer_consistency: PASS
  historical_projection: PROHIBITED
```

### 8.2 Position-conditioned surface initial

```yaml
position_conditioned_initial:
  女:
    identity_character: 女
    selected_reading: 녀
    first_position_surface: 여
    nonfirst_surface: 녀
    state: POSITION_RELATION_VERIFIED
  年:
    identity_character: 年
    selected_reading: 년
    first_position_surface: 연
    nonfirst_or_dependent_surface: 년
    state: POSITION_RELATION_VERIFIED
  historical_causality: NOT_JUDGED
```

## 9. Position Relation Audit

| Position group | Object | Verification state | Boundary |
|---|---|---|---|
| `Y-POS-001` | ㅇ/강 | `POSITION_RELATION_VERIFIED` | 종성 ㅇ 유지와 다음 음절 무음 초성 ㅇ을 분리 |
| `Y-POS-002` | ㅇ/방 | `POSITION_RELATION_VERIFIED` | 종성 ㅇ 비연음 예시; 초성·종성 음가 비동일 |
| `Y-POS-003` | ㅇ/깔리다 | `POSITION_RELATION_VERIFIED` | 역사 초성 음가는 SCHOLARLY_RECONSTRUCTION로 제한 |
| `Y-POS-004` | ㆁ/ㅇ | `UNSUPPORTED_LINEAGE_LINK` | 자모 기능대조는 가능하나 same-lineage는 미확정 |
| `Y-POS-005` | ㄱ/목 | `POSITION_RELATION_VERIFIED` | 종성→다음 음절 초성 실현 |
| `Y-POS-006` | ㄱ계열/깎다 | `POSITION_RELATION_VERIFIED` | ㄱ·ㄲ을 동일 자모로 병합하지 않음 |
| `Y-POS-007` | ㄱ계보/싶다 | `POSITION_RELATION_VERIFIED` | 역사형 자음변화는 DICTIONARY_REPORTED |
| `Y-POS-008` | ㄱ계보/새끼 | `POSITION_RELATION_VERIFIED` | ㄱ·ㅺ·ㄲ 문자층 분리 |
| `Y-POS-009` | 女 녀/여 | `POSITION_RELATION_VERIFIED` | 동일 Hanja Identity의 현대 첫/비첫 위치 표면관계 |
| `Y-POS-010` | 年 년/연 | `POSITION_RELATION_VERIFIED` | 위치·의존명사 조건 검증; 일부 연쇄발음은 SOURCE_UNCERTAIN |
| `Y-POS-011` | 솜+이불 | `POSITION_RELATION_VERIFIED` | 삽입 ㄴ은 표기에 없는 발음층 |
| `Y-POS-012` | 색+연필 | `POSITION_RELATION_VERIFIED` | ㄴ 첨가와 비음화를 별 단계로 유지 |
| `Y-POS-013` | ㅅ/옷 | `POSITION_RELATION_VERIFIED` | 종성 중화와 모음 앞 실현 분리 |
| `Y-POS-014` | ㅅ/낫다 | `POSITION_RELATION_VERIFIED` | 현대 ㅅ 불규칙 활용 |
| `Y-POS-015` | ㅅ/붓다 | `POSITION_RELATION_VERIFIED` | 현대 ㅅ 불규칙 활용 |
| `Y-POS-016` | ㅅ/짓다 | `MISSING_SOURCE_LOCATION` | 검색 색인만 확보; 직접 표제어·발음 상세 필요 |

```yaml
position_quantity:
  reported: 16
  position_relation_verified: 14
  unsupported_same_lineage: 1
  missing_source_location: 1
  position_and_period_mixed_records_reclassified: [Y-POS-009, Y-POS-010]
```

## 10. Modern/Historical Rime Separation Audit

### 10.1 Same modern syllable / different Hanja Identity

| Group | Shared modern syllable | Members | Entry IDs | Modern state | Historical state |
|---|---:|---:|---|---|---|
| `Z-HOMOPHONE-001` | 가 | 5 | `Z-HANJA-021, Z-HANJA-022, Z-HANJA-023, Z-HANJA-024, Z-HANJA-025` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-002` | 각 | 5 | `Z-HANJA-026, Z-HANJA-027, Z-HANJA-028, Z-HANJA-029, Z-HANJA-030` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-003` | 간 | 5 | `Z-HANJA-031, Z-HANJA-032, Z-HANJA-033, Z-HANJA-034, Z-HANJA-035` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-004` | 감 | 5 | `Z-HANJA-036, Z-HANJA-037, Z-HANJA-038, Z-HANJA-039, Z-HANJA-040` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-005` | 나 | 2 | `Z-HANJA-041, Z-HANJA-042` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-006` | 난 | 2 | `Z-HANJA-043, Z-HANJA-044` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-007` | 남 | 2 | `Z-HANJA-045, Z-HANJA-046` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-008` | 낭 | 2 | `Z-HANJA-048, Z-HANJA-049` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-009` | 내 | 3 | `Z-HANJA-050, Z-HANJA-051, Z-HANJA-052` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-010` | 농 | 2 | `Z-HANJA-057, Z-HANJA-058` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-011` | 뇌 | 2 | `Z-HANJA-059, Z-HANJA-060` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-012` | 사 | 5 | `Z-HANJA-061, Z-HANJA-062, Z-HANJA-063, Z-HANJA-064, Z-HANJA-065` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-013` | 상 | 5 | `Z-HANJA-066, Z-HANJA-067, Z-HANJA-068, Z-HANJA-069, Z-HANJA-070` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-014` | 선 | 5 | `Z-HANJA-076, Z-HANJA-077, Z-HANJA-078, Z-HANJA-079, Z-HANJA-080` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-015` | 성 | 5 | `Z-HANJA-071, Z-HANJA-072, Z-HANJA-073, Z-HANJA-074, Z-HANJA-075` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-016` | 영 | 6 | `Z-HANJA-001, Z-HANJA-002, Z-HANJA-003, Z-HANJA-004, Z-HANJA-005, Z-HANJA-006` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-017` | 원 | 6 | `Z-HANJA-007, Z-HANJA-008, Z-HANJA-009, Z-HANJA-010, Z-HANJA-011, Z-HANJA-012` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-018` | 의 | 3 | `Z-HANJA-018, Z-HANJA-019, Z-HANJA-020` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |
| `Z-HOMOPHONE-019` | 인 | 5 | `Z-HANJA-013, Z-HANJA-014, Z-HANJA-015, Z-HANJA-016, Z-HANJA-017` | `MODERN_SAME_SYLLABLE_GROUP_VERIFIED` | `HISTORICAL_EQUIVALENCE_PROHIBITED` |

```yaml
same_syllable_audit:
  group_count: 19
  member_hanja_identity_merge_count: 0
  modern_same_syllable_group_verified: 19
  historical_same_reading_verified: 0
  historical_lineage_inference: PROHIBITED
```

### 10.2 Same modern orthographic rime / different initial

| Set | Modern rime key | Members | Syllables | Modern layer | Historical layer |
|---|---|---:|---|---|---|
| `Z-RIME-001` | `ㅏ∅` | 4 | 가, 나, 사, 아 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-002` | `ㅏㄱ` | 4 | 각, 낙, 삭, 악 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-003` | `ㅏㄴ` | 4 | 간, 난, 산, 안 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-004` | `ㅏㅁ` | 4 | 감, 남, 삼, 암 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-005` | `ㅏㅇ` | 4 | 강, 낭, 상, 앙 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-006` | `ㅏㅂ` | 4 | 갑, 납, 삽, 압 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-007` | `ㅐ∅` | 4 | 개, 내, 새, 애 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-008` | `ㅐㅇ` | 4 | 갱, 냉, 생, 앵 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-009` | `ㅓ∅` | 4 | 거, 너, 서, 어 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-010` | `ㅗ∅` | 4 | 고, 노, 소, 오 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-011` | `ㅗㄱ` | 4 | 곡, 녹, 속, 옥 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-012` | `ㅗㅇ` | 4 | 공, 농, 송, 옹 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-013` | `ㅜ∅` | 4 | 구, 누, 수, 우 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-014` | `ㅜㄴ` | 4 | 군, 눈, 순, 운 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-015` | `ㅕㄴ` | 3 | 견, 년, 연 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |
| `Z-RIME-016` | `ㅕㅇ` | 3 | 경, 녕, 영 | `MODERN_ORTHOGRAPHIC_RIME_VERIFIED` | `NO_HISTORICAL_RIME_BOUND` |

```yaml
same_rime_audit:
  set_count: 16
  control_member_count: 62
  modern_orthographic_rime_verified: 16
  modern_phonetic_rime_independently_verified: 0
  historical_reported_rime_bound: 0
  scholarly_reconstructed_rime_bound: 0
  projection_errors_found_in_Z_output: 0
  projection_in_future_use: PROHIBITED
```

```text
Modern Orthographic Rime
≠ Modern Phonetic Rime by default
≠ Historical Reported Rime
≠ Scholarly Reconstructed Rime.
```

## 11. Reconstruction Audit

```yaml
reconstruction_audit:
  - object: "초성 ㆁ / 중세 초성 ㅇ"
    value: "음가 존재·조건부 음가"
    source: "SRC-007, SRC-008"
    method_as_source_states: NOT_STATED
    confidence_as_source_states: SOURCE_LIMITED
    direct_attestation: false
    current_state: SOURCE_UNCERTAIN

  - object: "이다의 역사 초성 ㅇ"
    value: "후두 유성 마찰음"
    source: "SRC-012"
    method_as_source_states: DICTIONARY_REPORTED
    confidence_as_source_states: SINGLE_LEXEME_BOUND
    direct_attestation: false
    current_state: SCHOLARLY_RECONSTRUCTION
```

```yaml
reconstruction_quantity:
  explicit_historical_phonetic_claim_objects: 2
  scholarly_reconstruction_typed: 1
  source_uncertain_historical_phonetic_claim: 1
  ai_generated_reconstruction_count: 0
```

## 12. Raw–Normalized Audit

| Raw lineage | Normalized endpoint | Preserved | Prohibited replacement |
|---|---|---|---|
| `다 / 다` | 같다 | Raw form, period, source | 현대 표기로 Raw 대체 |
| `식브다→십브다→시브다/시프다` | 싶다 | 단계순서와 원문형 | 단일 인과로 축약 |
| `삿기→새/색기` | 새끼 | ㅺ·ㄱ·ㄲ 표기층 | 자모 Identity 자동병합 |
| `이다→리다` | 깔리다 | 옛자모·시대·Source | 현대 ㅇ으로 자동치환 |
| `니르다` | 이르다 | 역사형·현대형 분리 | 한자어 두음법칙과 완전 동일시 |
| `ㆁ / ㅇ` | 현대 ㅇ 후보 | 자모·음가·위치층 | 단일 문자계보 확정 |

```yaml
raw_normalized_verification:
  raw_old_hangul_preserved: true
  modern_transcription_replaces_raw: false
  unicode_normalization_applied_to_modern_hangul_only: true
  old_jamo_loss_detected_in_source_output: false
  historical_pronunciation_generated_from_spelling: false
  normalization_boundary: PASS_WITH_LINEAGE_CORRECTIONS
```

## 13. Quantity Audit

```yaml
quantity_audit:
  position_groups_reported: 16
  position_groups_verified: 14
  position_groups_unsupported_same_lineage: 1
  position_groups_missing_source_location: 1

  historical_lineages_reported: 9
  historical_lineages_verified: 5
  lineages_reclassified_as_modern_position_relation: 2
  unsupported_single_lineages: 1
  multiple_lineage_candidates: 1

  pronunciation_claims_reported: 11
  pronunciation_claims_typed: 11
  directly_attested_recordings: 0

  reconstructed_claims: 1
  uncertain_reconstructions: 1

  hanja_identity_records: 80
  hanja_unicode_identity_verified: 80
  hanja_reading_links_source_bound: 80
  hanja_reading_links_independently_officially_crosschecked: 0
  hanja_historical_links: 0
  hanja_modern_position_links: 2

  same_syllable_groups: 19
  same_rime_sets: 16
  modern_ieung_records: 45

  unsupported_links: 4
  unresolved_conflicts: 7
```

## 14. Source Conflicts

### `YZ-CONFLICT-001`

```yaml
conflict:
  conflict_id: YZ-CONFLICT-001
  object_identity: "초성 ㆁ과 현대 ㅇ의 단일계보"
  claim_a: "Y-HIST-001"
  source_a: "Bound Data.Y position/history/conflict records"
  claim_b: "Y-POS-004"
  source_b: "Bound Data.Z identity/control/conflict records or Data.Y counter-position"
  conflict_type: MODERN_HISTORICAL_LINK_CONFLICT
  resolved: false
  required_next_data: >-
    ㆁ·현대 초성 ㅇ·현대 종성 ㅇ을 별 객체후보로 병렬 보존하고 전문 국어사 Source를 추가한다.
```
### `YZ-CONFLICT-002`

```yaml
conflict:
  conflict_id: YZ-CONFLICT-002
  object_identity: "女의 녀/여 분류"
  claim_a: "Y-HIST-004"
  source_a: "Bound Data.Y position/history/conflict records"
  claim_b: "Z-HANJA-053 + SRC-003"
  source_b: "Bound Data.Z identity/control/conflict records or Data.Y counter-position"
  conflict_type: CHANGE_PERIOD_CONFLICT
  resolved: false
  required_next_data: >-
    역사단계가 아니라 동일 Hanja Identity의 현대 위치조건으로 재분류한다.
```
### `YZ-CONFLICT-003`

```yaml
conflict:
  conflict_id: YZ-CONFLICT-003
  object_identity: "年의 년/연 분류"
  claim_a: "Y-HIST-005"
  source_a: "Bound Data.Y position/history/conflict records"
  claim_b: "Z-HANJA-054 + SRC-003"
  source_b: "Bound Data.Z identity/control/conflict records or Data.Y counter-position"
  conflict_type: CHANGE_PERIOD_CONFLICT
  resolved: false
  required_next_data: >-
    역사단계가 아니라 현대 위치·의존명사 조건으로 재분류한다.
```
### `YZ-CONFLICT-004`

```yaml
conflict:
  conflict_id: YZ-CONFLICT-004
  object_identity: "현대 ㅇ의 표기·음가와 역사 초성의 투사"
  claim_a: "Y-POS-003/004"
  source_a: "Bound Data.Y position/history/conflict records"
  claim_b: "Z IEUNG-001..045"
  source_b: "Bound Data.Z identity/control/conflict records or Data.Y counter-position"
  conflict_type: RECONSTRUCTION_CONFLICT
  resolved: false
  required_next_data: >-
    Z의 ㅇ 기록은 현대 철자·현대 음가층으로만 유지하고 역사 ㆁ/ㅇ에 소급하지 않는다.
```
### `YZ-CONFLICT-005`

```yaml
conflict:
  conflict_id: YZ-CONFLICT-005
  object_identity: "한자 Reading Source Authority"
  claim_a: "Z-HANJA-001..080"
  source_a: "Bound Data.Y position/history/conflict records"
  claim_b: "Z-CONFLICT-001/GAP-004"
  source_b: "Bound Data.Z identity/control/conflict records or Data.Y counter-position"
  conflict_type: HANJA_READING_CONFLICT
  resolved: false
  required_next_data: >-
    80개 독음은 변환 CSV Source-bound로 유지하고 공식 원 XLS·공식 한자사전 교차검증 전까지 독립 정본으로 승격하지 않는다.
```
### `YZ-CONFLICT-006`

```yaml
conflict:
  conflict_id: YZ-CONFLICT-006
  object_identity: "동음·동운모와 역사계보"
  claim_a: "Z-HOMOPHONE-001..019"
  source_a: "Bound Data.Y position/history/conflict records"
  claim_b: "Z-RIME-001..016"
  source_b: "Bound Data.Z identity/control/conflict records or Data.Y counter-position"
  conflict_type: MODERN_HISTORICAL_LINK_CONFLICT
  resolved: false
  required_next_data: >-
    현대 음절·현대 철자운모 Group만 검증하고 역사발음·역사운모 동일성은 미확정으로 둔다.
```
### `YZ-CONFLICT-007`

```yaml
conflict:
  conflict_id: YZ-CONFLICT-007
  object_identity: "짓다 Source Identity"
  claim_a: "Y-POS-016/Y-CONFLICT-004"
  source_a: "Bound Data.Y position/history/conflict records"
  claim_b: "SRC-015"
  source_b: "Bound Data.Z identity/control/conflict records or Data.Y counter-position"
  conflict_type: MISSING_SOURCE_LOCATION
  resolved: false
  required_next_data: >-
    활용 색인은 보존하되 직접 표제어·발음 상세가 결속되기 전 완전검증으로 승격하지 않는다.
```


## 15. Multiple Lineage Candidates

```yaml
multiple_lineage_candidates:
  - candidate_id: YZ-MULTI-001
    object: "ㆁ / 현대 초성 ㅇ / 현대 종성 ㅇ"
    candidates:
      - historical_onset_old_ieung
      - modern_orthographic_empty_onset
      - modern_coda_velar_nasal
    reason: "Source가 하나의 직선 문자·음가계보로 확정하지 않음"
    state: MULTIPLE_LINEAGE_CANDIDATES

  - candidate_id: YZ-MULTI-002
    object: "잎 / 닢 / 합성어 ㄴ 첨가"
    candidates:
      - historical_nip_lineage_explanation
      - synchronic_n_insertion_or_assimilation_analysis
    reason: "동일 해설에 경쟁분석이 병기됨"
    state: MULTIPLE_LINEAGE_CANDIDATES

  - candidate_id: YZ-MULTI-003
    object: "니르다→이르다 현상 명명·시기"
    candidates:
      - source_reported_initial_n_loss
      - broader_dueum_label_with_researcher_variation
    reason: "세부 periodization과 명명은 Source가 확정하지 않음"
    state: MULTIPLE_LINEAGE_CANDIDATES
```

## 16. Unsupported Links

```yaml
unsupported_links:
  - link_id: YZ-UNSUP-001
    from: historical_ㆁ
    to: modern_onset_and_coda_ㅇ
    reason: "표면 자모 유사성과 교육자료만으로 단일 Identity 계보 확정 불가"
    state: UNSUPPORTED_LINEAGE_LINK

  - link_id: YZ-UNSUP-002
    from: modern_same_syllable_hanja_group
    to: same_historical_pronunciation
    reason: "Z의 historical_readings_if_source_states가 80개 모두 비어 있음"
    state: PROHIBITED_FOR_CURRENT_DATASET

  - link_id: YZ-UNSUP-003
    from: modern_orthographic_rime
    to: historical_or_reconstructed_rime
    reason: "역사운모 Source가 결속되지 않음"
    state: PROHIBITED_FOR_CURRENT_DATASET

  - link_id: YZ-UNSUP-004
    from: dictionary_query_url
    to: fully_materialized_usage_entry
    reason: "80개 stable word_no·정의·발음 위치가 미결속"
    state: MISSING_SOURCE_LOCATION
```

## 17. Missing Intermediate States

```yaml
missing_intermediate_states:
  - object: "ㆁ→현대 ㅇ 후보계보"
    missing: "판본·시기별 문자기능 재편과 음가 변화단계"
    state: MISSING_INTERMEDIATE_STATE
  - object: "니르다→이르다"
    missing: "근대국어 세부 문헌형·정확 시기"
    state: MISSING_INTERMEDIATE_STATE
  - object: "닢→잎 및 합성어형"
    missing: "시기별 형태·발음·경쟁분석 Source"
    state: MISSING_INTERMEDIATE_STATE
  - object: "같-/싶-/새끼 계보"
    missing: "직접 음성기록 또는 단계별 음성 재구방법"
    state: MISSING_INTERMEDIATE_STATE
  - object: "한자 80개 역사독음"
    missing: "historical_readings_if_source_states 전체"
    state: MISSING_INTERMEDIATE_STATE
```

## 18. Uncertain Reconstructions

```yaml
uncertain_reconstructions:
  - reconstruction_id: YZ-RECON-UNC-001
    object: "초성 ㆁ·중세 초성 ㅇ"
    reason: "정확 IPA·방법·지역·시기별 변이가 결속되지 않음"
    state: UNCERTAIN_RECONSTRUCTION

  - reconstruction_id: YZ-RECON-UNC-002
    object: "이다의 후두 유성 마찰음"
    reason: "사전 보고는 있으나 재구 방법과 신뢰도 필드가 없음"
    state: SCHOLARLY_RECONSTRUCTION_WITH_METHOD_GAP

  - reconstruction_id: YZ-RECON-UNC-003
    object: "학년·몇 년의 세부 연쇄발음"
    reason: "Data.Y 자체가 직접 사전 재확인을 요구"
    state: SOURCE_UNCERTAIN

  - reconstruction_id: YZ-RECON-UNC-004
    object: "짓다 기본형·활용 발음"
    reason: "검색 색인만 결속되고 직접 상세항목이 없음"
    state: SOURCE_UNCERTAIN
```

## 19. Proposed Corrections

| Correction | Target | Proposed append-only correction | State |
|---|---|---|---|
| `YZ-CORR-001` | `Y-HIST-001` | Split ㆁ, modern onset ㅇ and modern coda ㅇ into separate lineage candidates; remove linear identity claim. | `PROPOSED_APPEND_ONLY_CORRECTION` |
| `YZ-CORR-002` | `Y-HIST-004` | Reclassify 女 녀/여 from Historical Lineage to modern Position Relation under one Hanja Identity. | `PROPOSED_APPEND_ONLY_CORRECTION` |
| `YZ-CORR-003` | `Y-HIST-005` | Reclassify 年 년/연 from Historical Lineage to modern Position/Dependent-noun Relation. | `PROPOSED_APPEND_ONLY_CORRECTION` |
| `YZ-CORR-004` | `Y-HIST-001 source fields` | Bind modern onset/coda pronunciation to modern norm sources and historical phonetic claims to historical sources separately. | `PROPOSED_APPEND_ONLY_CORRECTION` |
| `YZ-CORR-005` | `Y-POS-010` | Mark 학년·몇 년 detailed chain pronunciations SOURCE_UNCERTAIN until direct dictionary entries are materialized. | `PROPOSED_APPEND_ONLY_CORRECTION` |
| `YZ-CORR-006` | `Y-POS-016` | Retain the relation as MISSING_SOURCE_LOCATION; do not mark same-lineage fully verified. | `PROPOSED_APPEND_ONLY_CORRECTION` |
| `YZ-CORR-007` | `Z-HANJA-001..080` | Keep Unicode identity mechanically verified but label Korean reading/hun as TIER_3_TRANSFORMED_SOURCE_BOUND. | `PROPOSED_APPEND_ONLY_CORRECTION` |
| `YZ-CORR-008` | `Z morpheme usages` | Keep query URLs, but mark 80 usage links as missing stable detail IDs/evidence locations. | `PROPOSED_APPEND_ONLY_CORRECTION` |
| `YZ-CORR-009` | `Z-HOMOPHONE-001..019` | Rename scope explicitly to MODERN_SAME_SYLLABLE_GROUP; prohibit historical same-reading inference. | `PROPOSED_APPEND_ONLY_CORRECTION` |
| `YZ-CORR-010` | `Z-RIME-001..016` | Rename scope explicitly to MODERN_ORTHOGRAPHIC_RIME_CONTROL; keep historical reported/reconstructed rime null. | `PROPOSED_APPEND_ONLY_CORRECTION` |
| `YZ-CORR-011` | `Z IEUNG-001..045` | Keep modern orthographic ㅇ / phonetic Ø / coda [ŋ] layers; prohibit linkage to historical ㆁ without new sources. | `PROPOSED_APPEND_ONLY_CORRECTION` |
| `YZ-CORR-012` | `Y-HIST-009` | Preserve 닢/잎 and competing ㄴㄴ-addition analyses as MULTIPLE_LINEAGE_CANDIDATES. | `PROPOSED_APPEND_ONLY_CORRECTION` |

```text
제안 교정은 원초 Data Byte 수정이 아니다.
후속 Result가 적용할 독립 Correction Position이다.
```

## 20. Unresolved

```yaml
unresolved:
  - exact_character_lineage_between_old_ieung_and_modern_ieung
  - medieval_initial_ieung_phonetic_value_by_period_and_region
  - dueum_terminology_and_periodization_for_native_niruda_lineage
  - nip_leaf_and_double_n_insertion_competing_analysis
  - direct_detail_identity_for_jitda
  - direct_pronunciation_entries_for_haknyeon_and_myeot_nyeon
  - original_hanja_XLS_and_transformation_reproducibility
  - independent_official_hanja_reading_crosscheck_for_80_identities
  - stable_dictionary_detail_locations_for_80_usage_words
  - historical_Korean_Hanja_readings
  - historical_reported_or_reconstructed_rimes
  - old_Hangul_extended_jamo_normalization_policy
```

## 21. Required Next Data

```yaml
required_next_data:
  - next_data_id: YZ-NEXT-001
    item: "한국어문회 원 XLS Exact Byte·SHA-256와 CSV 변환 재현 절차"
    state: NEXT_DATA_REQUIRED
  - next_data_id: YZ-NEXT-002
    item: "80개 한자 Identity별 공공·공식 한자사전 상세 독음·훈 위치"
    state: NEXT_DATA_REQUIRED
  - next_data_id: YZ-NEXT-003
    item: "80개 표준국어대사전 용례의 안정적인 word_no·정의·발음 위치"
    state: NEXT_DATA_REQUIRED
  - next_data_id: YZ-NEXT-004
    item: "초성 옛이응 ㆁ과 중세 초성 ㅇ의 전문 국어사 문법·논문 Source"
    state: NEXT_DATA_REQUIRED
  - next_data_id: YZ-NEXT-005
    item: "ㆁ·ㅇ 문자계보와 음가 변화를 분리한 판본·시기별 자료"
    state: NEXT_DATA_REQUIRED
  - next_data_id: YZ-NEXT-006
    item: "니르다→이르다의 세부 시기·중간 문헌형·현상 명명 연구"
    state: NEXT_DATA_REQUIRED
  - next_data_id: YZ-NEXT-007
    item: "닢/잎 및 ㄴㄴ 첨가 경쟁분석의 독립 연구 Source"
    state: NEXT_DATA_REQUIRED
  - next_data_id: YZ-NEXT-008
    item: "짓다 직접 표제어·발음·활용 상세 페이지"
    state: NEXT_DATA_REQUIRED
  - next_data_id: YZ-NEXT-009
    item: "학년·몇 년 등 연쇄발음 직접 사전 항목"
    state: NEXT_DATA_REQUIRED
  - next_data_id: YZ-NEXT-010
    item: "역사 한국 한자음 및 역사운모를 직접 제시하는 별도 Dataset"
    state: NEXT_DATA_REQUIRED
  - next_data_id: YZ-NEXT-011
    item: "옛한글·확장자모를 보존하는 Unicode/판본 표본"
    state: NEXT_DATA_REQUIRED
  - next_data_id: YZ-NEXT-012
    item: "실제 말뭉치 기반 첫 위치·비첫 위치 용례와 빈도 자료"
    state: NEXT_DATA_REQUIRED
required_next_data_count: 12
```

## 22. Handoff to gpt.logi

```yaml
handoff:
  from: gpt.yz@HRTDB_A::gpt.yz
  to: gpt.logi@HRTDB_A::gpt.xyzt

  object_class: HRTDB_A_2D_SOURCE_VERIFICATION_RESULT
  cycle_id: GLANG-SOURCE-COLLECTION-BASE-CONSONANTS-R01
  stage_id: R02_2D_YZ
  completion_state: VERIFICATION_COMPLETE_WITH_UNRESOLVED

  strongest_verified_positions:
    - five_dictionary_reported_modern_historical_lineages
    - fourteen_position_relations
    - eleven_pronunciation_claims_typed_as_reported_not_direct_recordings
    - eighty_unique_Hanja_Unicode_identities
    - eighty_modern_Hangul_decompositions
    - nineteen_modern_same_syllable_groups_without_identity_merge
    - sixteen_modern_orthographic_rime_control_sets
    - modern_initial_ieung_phonetic_zero_vs_coda_ng_separation
    - two_modern_Hanja_position_links_for_Female_and_Year

  required_corrections:
    - split_old_ieung_and_modern_ieung_lineage_candidates
    - reclassify_Female_and_Year_records_as_modern_position_relations
    - preserve_Tier3_Hanja_reading_source_boundary
    - mark_dictionary_query_locations_as_not_materialized
    - label_homophone_and_rime_sets_as_modern_only
    - preserve_all_source_conflicts_and_multiple_lineage_candidates

  prohibited:
    - structural_meaning_judgment
    - temporal_causality_judgment
    - source_less_original_initial_restoration
    - AI_generated_reconstruction
    - same_modern_syllable_historical_lineage_merge
    - modern_rime_historical_rime_projection
    - GitHub_mutation
    - Track_DB_promotion

  verdict: VERIFICATION_COMPLETE_WITH_UNRESOLVED
```

## Final Guard

```text
Historical reconstruction is not direct observation.
Dictionary-reported pronunciation is not recorded audio.
Old spelling is not an automatically recovered phonetic value.

Same Character Identity is not Same Surface Initial in every position.
Same modern sound is not same historical lineage.
Same modern syllable is not same Hanja Identity.
Same modern rime is not same historical rime.

ㆁ is not automatically modern onset ㅇ.
Modern onset ㅇ is not coda ㅇ.
Position difference is not time difference.
Temporal sequence is not causation.

Multiple lineage candidates are not one merged lineage.
Verification is not structural interpretation.
Result is not Track DB.
Relation is not merge.
```

~~~

## 34. Errors and Limitations

```yaml
errors_and_limitations:
  direct_1d_source_bytes_not_direct_inputs_to_3d: true
  X_exact_entry_locations_missing: 47
  X_uncertain_sense_identities: 9
  X_no_coda_coda_direct_snapshots_missing: 10
  Hanja_official_XLS_not_materialized: true
  Hanja_official_detail_locations_missing: 80
  Rime_unregistered_Sino_identities: 43
  Rime_surface_position_field_gaps: 9
  anonymous_ieung_ID_gaps: 10
  historical_Hanja_readings_missing: 80
  historical_rimes_missing: true
  old_ieung_lineage_unresolved: true
  historical_reconstruction_method_gaps: true
  structural_analysis_performed: false
```
## 35. Proposed Corrections

```yaml
proposed_correction_count: 44
correction_ledger:
- correction_id: XY-CORR-001
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X metadata object-class label
  original_value: OFFICIAL_LEXICAL_SURFACE_AND_ZERO_ONSET_SOURCE_DATA vs handoff OFFICIAL_LEXICAL_SURFACE_SOURCE_DATA
  detected_error_or_limitation: OFFICIAL_LEXICAL_SURFACE_AND_ZERO_ONSET_SOURCE_DATA vs handoff OFFICIAL_LEXICAL_SURFACE_SOURCE_DATA
  proposed_correction: Preserve both labels; set canonical input class to frontmatter document_class and handoff label as compatible alias.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: NONBLOCKING
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Preserve both labels; set canonical input class to frontmatter document_class and handoff label as compatible alias.
  input_bytes_modified: false
- correction_id: XY-CORR-002
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X nominal root fields
  original_value: 51 nouns, 3 pronouns, 1 adverb assign root=lemma without item-level morphological source
  detected_error_or_limitation: 51 nouns, 3 pronouns, 1 adverb assign root=lemma without item-level morphological source
  proposed_correction: Reclassify root as NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN; do not delete value.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Reclassify root as NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN; do not delete value.
  input_bytes_modified: false
- correction_id: XY-CORR-003
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X predicate root/stem fields
  original_value: Only 가다·가늘다 have direct target-code pages; 고맙다·그리다·기르다 use reentry routes
  detected_error_or_limitation: Only 가다·가늘다 have direct target-code pages; 고맙다·그리다·기르다 use reentry routes
  proposed_correction: Keep forms but mark 3 predicate root/stem records MISSING_SOURCE_LOCATION.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Keep forms but mark 3 predicate root/stem records MISSING_SOURCE_LOCATION.
  input_bytes_modified: false
- correction_id: XY-CORR-004
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X dictionary_definition capture type
  original_value: Section states first meanings were shortened, while field name can be read as exact raw definition
  detected_error_or_limitation: Section states first meanings were shortened, while field name can be read as exact raw definition
  proposed_correction: Classify as SHORT_NORMALIZED_GLOSS unless exact entry text is captured; RAW_MATCH_VERIFIED not assigned.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Classify as SHORT_NORMALIZED_GLOSS unless exact entry text is captured; RAW_MATCH_VERIFIED not assigned.
  input_bytes_modified: false
- correction_id: XY-CORR-005
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X example sentences
  original_value: 60 example sentences have no exact source location or source-example identifier
  detected_error_or_limitation: 60 example sentences have no exact source location or source-example identifier
  proposed_correction: Mark all example_sentences as MISSING_SOURCE_LOCATION; do not treat as dictionary examples.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Mark all example_sentences as MISSING_SOURCE_LOCATION; do not treat as dictionary examples.
  input_bytes_modified: false
- correction_id: XY-CORR-006
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X 47 reentry-only entries
  original_value: Official search route exists but individual target_code and exact entry snapshot are absent
  detected_error_or_limitation: Official search route exists but individual target_code and exact entry snapshot are absent
  proposed_correction: Retain 47 as official reentry candidates; verified unique identity count remains 13.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Retain 47 as official reentry candidates; verified unique identity count remains 13.
  input_bytes_modified: false
- correction_id: XY-CORR-007
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X zero-onset lexical identity
  original_value: 12 phonological records use general official rules; 6 surface forms are outside the 60-entry lexical registry
  detected_error_or_limitation: 12 phonological records use general official rules; 6 surface forms are outside the 60-entry lexical registry
  proposed_correction: Verify ㅇ/Ø/coda field relation, but require item-level lexical source for 앙금·엉덩이·옹기·웅덩이·응어리·잉어.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Verify ㅇ/Ø/coda field relation, but require item-level lexical source for 앙금·엉덩이·옹기·웅덩이·응어리·잉어.
  input_bytes_modified: false
- correction_id: XY-CORR-008
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X no-coda/coda relations
  original_value: 10 relations use search routes and are already INSUFFICIENT_SOURCE
  detected_error_or_limitation: 10 relations use search routes and are already INSUFFICIENT_SOURCE
  proposed_correction: Preserve forms as candidates; do not assign LINEAGE_LINK_VERIFIED until direct inflection snapshots are bound.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Preserve forms as candidates; do not assign LINEAGE_LINK_VERIFIED until direct inflection snapshots are bound.
  input_bytes_modified: false
- correction_id: XY-CORR-009
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y source quantity
  original_value: 19 Source Records include SRC-002 and SRC-017 sharing one canonical URL
  detected_error_or_limitation: 19 Source Records include SRC-002 and SRC-017 sharing one canonical URL
  proposed_correction: Report source_record_count=19 and unique_source_identity_count=18; do not count duplicate as independent corroboration.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: NONBLOCKING
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Report source_record_count=19 and unique_source_identity_count=18; do not count duplicate as independent corroboration.
  input_bytes_modified: false
- correction_id: XY-CORR-010
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y-POS-004 ㆁ/ㅇ relation
  original_value: same_lineage_source_supported=false and professional historical grammar recheck required
  detected_error_or_limitation: same_lineage_source_supported=false and professional historical grammar recheck required
  proposed_correction: Retain PARTIAL_CROSS_MATCH + SOURCE_CONFLICT; prohibit identity merge.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Retain PARTIAL_CROSS_MATCH + SOURCE_CONFLICT; prohibit identity merge.
  input_bytes_modified: false
- correction_id: XY-CORR-011
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y-POS-006 ㄱ/ㄲ grouping
  original_value: Target consonant is ㄱ but observed coda/onset surface is ㄲ
  detected_error_or_limitation: Target consonant is ㄱ but observed coda/onset surface is ㄲ
  proposed_correction: Classify as consonant-family relation, not exact grapheme identity.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Classify as consonant-family relation, not exact grapheme identity.
  input_bytes_modified: false
- correction_id: XY-CORR-012
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y-POS-010 pronunciation
  original_value: 학년/몇 년 pronunciations explicitly state detailed dictionary confirmation required
  detected_error_or_limitation: 학년/몇 년 pronunciations explicitly state detailed dictionary confirmation required
  proposed_correction: Keep position relation; mark pronunciation fields UNRESOLVED and MISSING_SOURCE_LOCATION.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Keep position relation; mark pronunciation fields UNRESOLVED and MISSING_SOURCE_LOCATION.
  input_bytes_modified: false
- correction_id: XY-CORR-013
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y-POS-016 짓다
  original_value: Only search-index route obtained; direct lemma page and detailed pronunciation absent
  detected_error_or_limitation: Only search-index route obtained; direct lemma page and detailed pronunciation absent
  proposed_correction: Retain SOURCE_CONFLICT; no full LINEAGE_LINK_VERIFIED status.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Retain SOURCE_CONFLICT; no full LINEAGE_LINK_VERIFIED status.
  input_bytes_modified: false
- correction_id: XY-CORR-014
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y historical pronunciation
  original_value: Historical sound values are DICTIONARY_REPORTED or SCHOLARLY_REPORTED
  detected_error_or_limitation: Historical sound values are DICTIONARY_REPORTED or SCHOLARLY_REPORTED
  proposed_correction: Preserve as reconstruction/report, never RAW_MATCH_VERIFIED or direct observation.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Preserve as reconstruction/report, never RAW_MATCH_VERIFIED or direct observation.
  input_bytes_modified: false
- correction_id: XY-CORR-015
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y-HIST-003 terminology
  original_value: 니르다→이르다 is reported as initial ㄴ loss with terminology/periodization open
  detected_error_or_limitation: 니르다→이르다 is reported as initial ㄴ loss with terminology/periodization open
  proposed_correction: Preserve Y-CONFLICT-003 and prohibit automatic identity with modern Sino-Korean 두음법칙.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Preserve Y-CONFLICT-003 and prohibit automatic identity with modern Sino-Korean 두음법칙.
  input_bytes_modified: false
- correction_id: XY-CORR-016
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y-HIST-009 ㄴ insertion account
  original_value: Official explanation contains competing analysis
  detected_error_or_limitation: Official explanation contains competing analysis
  proposed_correction: Preserve Y-CONFLICT-002; no forced resolution.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Preserve Y-CONFLICT-002; no forced resolution.
  input_bytes_modified: false
- correction_id: XY-CORR-017
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Cross-input lexical identity
  original_value: Exact same surface + same lemma pair count is 0
  detected_error_or_limitation: Exact same surface + same lemma pair count is 0
  proposed_correction: Do not create lexical lineage from same consonant group; classify all unmatched records as typed MISSING_COUNTERPART.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: NONBLOCKING
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Do not create lexical lineage from same consonant group; classify all unmatched records as typed MISSING_COUNTERPART.
  input_bytes_modified: false
- correction_id: XY-CORR-018
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: 솜 vs 솜이불
  original_value: X has 솜; Y has compound 솜+이불
  detected_error_or_limitation: X has 솜; Y has compound 솜+이불
  proposed_correction: PARTIAL_CROSS_MATCH only at component position; compound is not same lexical identity.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: PARTIAL_CROSS_MATCH only at component position; compound is not same lexical identity.
  input_bytes_modified: false
- correction_id: XY-CORR-019
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: 입 vs 잎
  original_value: Modern pronunciation can converge to [입], but orthography and lemma differ
  detected_error_or_limitation: Modern pronunciation can converge to [입], but orthography and lemma differ
  proposed_correction: Record NON_MATCH_GUARD; same pronunciation is not same lexical identity.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: NONBLOCKING
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Record NON_MATCH_GUARD; same pronunciation is not same lexical identity.
  input_bytes_modified: false
- correction_id: XY-CORR-020
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Modern ㅇ vs historical ㆁ
  original_value: X verifies modern initial ㅇ=Ø and coda ㅇ=[ŋ]; Y reports historical ㆁ/ㅇ complexity
  detected_error_or_limitation: X verifies modern initial ㅇ=Ø and coda ㅇ=[ŋ]; Y reports historical ㆁ/ㅇ complexity
  proposed_correction: CROSS_VERIFIED for modern field split; PARTIAL_CROSS_MATCH for historical lineage.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: CROSS_VERIFIED for modern field split; PARTIAL_CROSS_MATCH for historical lineage.
  input_bytes_modified: false
- correction_id: XZ-CORR-001
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Data_X_47_reentry_only_entries
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Data_X_47_reentry_only_entries
  proposed_correction: bind_individual_target_code_exact_entry_snapshot_and_source_position
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: SOURCE_POSITION_VERIFIED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-002
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Data_X_9_uncertain_lemmas
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Data_X_9_uncertain_lemmas
  proposed_correction: select_or_split_dictionary_sense_identity_by_target_code
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: LEXICAL_CLASS_VERIFIED_OR_RETAIN_UNCERTAIN
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-003
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Data_X_example_sentences
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Data_X_example_sentences
  proposed_correction: add_source_sentence_location_or_label_as_generated_normalized_example
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: SOURCE_CLAIM_BOUNDARY_RESTORED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-004
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Data_Z_Hanja_reading_and_hun
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Data_Z_Hanja_reading_and_hun
  proposed_correction: bind_official_XLS_exact_bytes_and_reproducible_transform_or_official_Hanja_dictionary_entries
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: HANJA_READING_HUN_SOURCE_VERIFIED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-005
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Data_Z_80_usage_words
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Data_Z_80_usage_words
  proposed_correction: bind_stdict_word_no_definition_location_and_exact_morpheme_position
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: SOURCE_POSITION_VERIFIED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-006
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Rime_43_unregistered_Sino_members
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Rime_43_unregistered_Sino_members
  proposed_correction: create_full_Hanja_identity_records_with_character_codepoint_reading_hun_word_Hanja_position_and_sources
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: HANJA_IDENTITY_VERIFIED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-007
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Rime_3_native_members
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Rime_3_native_members
  proposed_correction: add_explicit_cross_refs_to_X_entry_IDs
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: CLASSIFICATION_OR_LINKAGE
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: LEXICAL_CLASS_LINK_VERIFIED
  input_bytes_modified: false
  additional_fields:
    mappings:
    - Z-RIME-007/새 -> X-ㅅ-E05
    - Z-RIME-009/너 -> X-ㄴ-E02
    - Z-RIME-014/눈 -> X-ㄴ-E11
- correction_id: XZ-CORR-008
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: 9_surface_or_noninitial_Hanja_members
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: 9_surface_or_noninitial_Hanja_members
  proposed_correction: split_canonical_reading_usage_surface_morpheme_position_and_pronunciation
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: IDENTITY_SURFACE_POSITION_VERIFIED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-009
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: 10_anonymous_ieung_records
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: 10_anonymous_ieung_records
  proposed_correction: assign_stable_record_ID_and_parent_rime_member_ref
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: NORMALIZATION_ERROR_CLOSED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-010
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: 拿_拏_variant_relation
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: 拿_拏_variant_relation
  proposed_correction: preserve_relation_and_add_separate_full_identity_record_only_if_source_authorizes
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: CLASSIFICATION_OR_LINKAGE
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: DUPLICATE_LINK_VERIFIED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-011
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Z-RIME-015_and_Z-RIME-016
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Z-RIME-015_and_Z-RIME-016
  proposed_correction: preserve_missing_ㅅ_without_forced_completion
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: CLASSIFICATION_OR_LINKAGE
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: RIME_SET_VERIFIED_WITH_EXPLICIT_GAP
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-012
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: all_inputs
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: all_inputs
  proposed_correction: retain_all_analysis_reserved_fields_as_null
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: CLASSIFICATION_OR_LINKAGE
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: NO_SEMANTIC_ANALYSIS
  input_bytes_modified: false
  additional_fields: {}
- correction_id: YZ-CORR-001
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-HIST-001
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-HIST-001
  proposed_correction: Split ㆁ, modern onset ㅇ and modern coda ㅇ into separate lineage candidates; remove linear identity claim.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Split ㆁ, modern onset ㅇ and modern coda ㅇ into separate lineage candidates; remove linear identity claim.
  input_bytes_modified: false
- correction_id: YZ-CORR-002
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-HIST-004
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-HIST-004
  proposed_correction: Reclassify 女 녀/여 from Historical Lineage to modern Position Relation under one Hanja Identity.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Reclassify 女 녀/여 from Historical Lineage to modern Position Relation under one Hanja Identity.
  input_bytes_modified: false
- correction_id: YZ-CORR-003
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-HIST-005
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-HIST-005
  proposed_correction: Reclassify 年 년/연 from Historical Lineage to modern Position/Dependent-noun Relation.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Reclassify 年 년/연 from Historical Lineage to modern Position/Dependent-noun Relation.
  input_bytes_modified: false
- correction_id: YZ-CORR-004
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-HIST-001 source fields
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-HIST-001 source fields
  proposed_correction: Bind modern onset/coda pronunciation to modern norm sources and historical phonetic claims to historical sources separately.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Bind modern onset/coda pronunciation to modern norm sources and historical phonetic claims to historical sources separately.
  input_bytes_modified: false
- correction_id: YZ-CORR-005
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-POS-010
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-POS-010
  proposed_correction: Mark 학년·몇 년 detailed chain pronunciations SOURCE_UNCERTAIN until direct dictionary entries are materialized.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Mark 학년·몇 년 detailed chain pronunciations SOURCE_UNCERTAIN until direct dictionary entries are materialized.
  input_bytes_modified: false
- correction_id: YZ-CORR-006
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-POS-016
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-POS-016
  proposed_correction: Retain the relation as MISSING_SOURCE_LOCATION; do not mark same-lineage fully verified.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Retain the relation as MISSING_SOURCE_LOCATION; do not mark same-lineage fully verified.
  input_bytes_modified: false
- correction_id: YZ-CORR-007
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Z-HANJA-001..080
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Z-HANJA-001..080
  proposed_correction: Keep Unicode identity mechanically verified but label Korean reading/hun as TIER_3_TRANSFORMED_SOURCE_BOUND.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Keep Unicode identity mechanically verified but label Korean reading/hun as TIER_3_TRANSFORMED_SOURCE_BOUND.
  input_bytes_modified: false
- correction_id: YZ-CORR-008
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Z morpheme usages
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Z morpheme usages
  proposed_correction: Keep query URLs, but mark 80 usage links as missing stable detail IDs/evidence locations.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Keep query URLs, but mark 80 usage links as missing stable detail IDs/evidence locations.
  input_bytes_modified: false
- correction_id: YZ-CORR-009
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Z-HOMOPHONE-001..019
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Z-HOMOPHONE-001..019
  proposed_correction: Rename scope explicitly to MODERN_SAME_SYLLABLE_GROUP; prohibit historical same-reading inference.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Rename scope explicitly to MODERN_SAME_SYLLABLE_GROUP; prohibit historical same-reading inference.
  input_bytes_modified: false
- correction_id: YZ-CORR-010
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Z-RIME-001..016
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Z-RIME-001..016
  proposed_correction: Rename scope explicitly to MODERN_ORTHOGRAPHIC_RIME_CONTROL; keep historical reported/reconstructed rime null.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Rename scope explicitly to MODERN_ORTHOGRAPHIC_RIME_CONTROL; keep historical reported/reconstructed rime null.
  input_bytes_modified: false
- correction_id: YZ-CORR-011
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Z IEUNG-001..045
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Z IEUNG-001..045
  proposed_correction: Keep modern orthographic ㅇ / phonetic Ø / coda [ŋ] layers; prohibit linkage to historical ㆁ without new sources.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Keep modern orthographic ㅇ / phonetic Ø / coda [ŋ] layers; prohibit linkage to historical ㆁ without new sources.
  input_bytes_modified: false
- correction_id: YZ-CORR-012
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-HIST-009
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-HIST-009
  proposed_correction: Preserve 닢/잎 and competing ㄴㄴ-addition analyses as MULTIPLE_LINEAGE_CANDIDATES.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Preserve 닢/잎 and competing ㄴㄴ-addition analyses as MULTIPLE_LINEAGE_CANDIDATES.
  input_bytes_modified: false
```
## 36. Applied Corrections

```yaml
applied_to_draft_classification_count: 36
input_bytes_modified: false
applied_corrections:
- correction_id: XY-CORR-001
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X metadata object-class label
  original_value: OFFICIAL_LEXICAL_SURFACE_AND_ZERO_ONSET_SOURCE_DATA vs handoff OFFICIAL_LEXICAL_SURFACE_SOURCE_DATA
  detected_error_or_limitation: OFFICIAL_LEXICAL_SURFACE_AND_ZERO_ONSET_SOURCE_DATA vs handoff OFFICIAL_LEXICAL_SURFACE_SOURCE_DATA
  proposed_correction: Preserve both labels; set canonical input class to frontmatter document_class and handoff label as compatible alias.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: NONBLOCKING
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Preserve both labels; set canonical input class to frontmatter document_class and handoff label as compatible alias.
  input_bytes_modified: false
- correction_id: XY-CORR-002
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X nominal root fields
  original_value: 51 nouns, 3 pronouns, 1 adverb assign root=lemma without item-level morphological source
  detected_error_or_limitation: 51 nouns, 3 pronouns, 1 adverb assign root=lemma without item-level morphological source
  proposed_correction: Reclassify root as NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN; do not delete value.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Reclassify root as NORMALIZATION_PLACEHOLDER_NOT_MORPHOLOGICALLY_PROVEN; do not delete value.
  input_bytes_modified: false
- correction_id: XY-CORR-003
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X predicate root/stem fields
  original_value: Only 가다·가늘다 have direct target-code pages; 고맙다·그리다·기르다 use reentry routes
  detected_error_or_limitation: Only 가다·가늘다 have direct target-code pages; 고맙다·그리다·기르다 use reentry routes
  proposed_correction: Keep forms but mark 3 predicate root/stem records MISSING_SOURCE_LOCATION.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Keep forms but mark 3 predicate root/stem records MISSING_SOURCE_LOCATION.
  input_bytes_modified: false
- correction_id: XY-CORR-004
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X dictionary_definition capture type
  original_value: Section states first meanings were shortened, while field name can be read as exact raw definition
  detected_error_or_limitation: Section states first meanings were shortened, while field name can be read as exact raw definition
  proposed_correction: Classify as SHORT_NORMALIZED_GLOSS unless exact entry text is captured; RAW_MATCH_VERIFIED not assigned.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Classify as SHORT_NORMALIZED_GLOSS unless exact entry text is captured; RAW_MATCH_VERIFIED not assigned.
  input_bytes_modified: false
- correction_id: XY-CORR-005
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X example sentences
  original_value: 60 example sentences have no exact source location or source-example identifier
  detected_error_or_limitation: 60 example sentences have no exact source location or source-example identifier
  proposed_correction: Mark all example_sentences as MISSING_SOURCE_LOCATION; do not treat as dictionary examples.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Mark all example_sentences as MISSING_SOURCE_LOCATION; do not treat as dictionary examples.
  input_bytes_modified: false
- correction_id: XY-CORR-006
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X 47 reentry-only entries
  original_value: Official search route exists but individual target_code and exact entry snapshot are absent
  detected_error_or_limitation: Official search route exists but individual target_code and exact entry snapshot are absent
  proposed_correction: Retain 47 as official reentry candidates; verified unique identity count remains 13.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Retain 47 as official reentry candidates; verified unique identity count remains 13.
  input_bytes_modified: false
- correction_id: XY-CORR-007
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X zero-onset lexical identity
  original_value: 12 phonological records use general official rules; 6 surface forms are outside the 60-entry lexical registry
  detected_error_or_limitation: 12 phonological records use general official rules; 6 surface forms are outside the 60-entry lexical registry
  proposed_correction: Verify ㅇ/Ø/coda field relation, but require item-level lexical source for 앙금·엉덩이·옹기·웅덩이·응어리·잉어.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Verify ㅇ/Ø/coda field relation, but require item-level lexical source for 앙금·엉덩이·옹기·웅덩이·응어리·잉어.
  input_bytes_modified: false
- correction_id: XY-CORR-008
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: X no-coda/coda relations
  original_value: 10 relations use search routes and are already INSUFFICIENT_SOURCE
  detected_error_or_limitation: 10 relations use search routes and are already INSUFFICIENT_SOURCE
  proposed_correction: Preserve forms as candidates; do not assign LINEAGE_LINK_VERIFIED until direct inflection snapshots are bound.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Preserve forms as candidates; do not assign LINEAGE_LINK_VERIFIED until direct inflection snapshots are bound.
  input_bytes_modified: false
- correction_id: XY-CORR-009
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y source quantity
  original_value: 19 Source Records include SRC-002 and SRC-017 sharing one canonical URL
  detected_error_or_limitation: 19 Source Records include SRC-002 and SRC-017 sharing one canonical URL
  proposed_correction: Report source_record_count=19 and unique_source_identity_count=18; do not count duplicate as independent corroboration.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: NONBLOCKING
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Report source_record_count=19 and unique_source_identity_count=18; do not count duplicate as independent corroboration.
  input_bytes_modified: false
- correction_id: XY-CORR-010
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y-POS-004 ㆁ/ㅇ relation
  original_value: same_lineage_source_supported=false and professional historical grammar recheck required
  detected_error_or_limitation: same_lineage_source_supported=false and professional historical grammar recheck required
  proposed_correction: Retain PARTIAL_CROSS_MATCH + SOURCE_CONFLICT; prohibit identity merge.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Retain PARTIAL_CROSS_MATCH + SOURCE_CONFLICT; prohibit identity merge.
  input_bytes_modified: false
- correction_id: XY-CORR-011
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y-POS-006 ㄱ/ㄲ grouping
  original_value: Target consonant is ㄱ but observed coda/onset surface is ㄲ
  detected_error_or_limitation: Target consonant is ㄱ but observed coda/onset surface is ㄲ
  proposed_correction: Classify as consonant-family relation, not exact grapheme identity.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Classify as consonant-family relation, not exact grapheme identity.
  input_bytes_modified: false
- correction_id: XY-CORR-012
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y-POS-010 pronunciation
  original_value: 학년/몇 년 pronunciations explicitly state detailed dictionary confirmation required
  detected_error_or_limitation: 학년/몇 년 pronunciations explicitly state detailed dictionary confirmation required
  proposed_correction: Keep position relation; mark pronunciation fields UNRESOLVED and MISSING_SOURCE_LOCATION.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Keep position relation; mark pronunciation fields UNRESOLVED and MISSING_SOURCE_LOCATION.
  input_bytes_modified: false
- correction_id: XY-CORR-013
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y-POS-016 짓다
  original_value: Only search-index route obtained; direct lemma page and detailed pronunciation absent
  detected_error_or_limitation: Only search-index route obtained; direct lemma page and detailed pronunciation absent
  proposed_correction: Retain SOURCE_CONFLICT; no full LINEAGE_LINK_VERIFIED status.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Retain SOURCE_CONFLICT; no full LINEAGE_LINK_VERIFIED status.
  input_bytes_modified: false
- correction_id: XY-CORR-014
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y historical pronunciation
  original_value: Historical sound values are DICTIONARY_REPORTED or SCHOLARLY_REPORTED
  detected_error_or_limitation: Historical sound values are DICTIONARY_REPORTED or SCHOLARLY_REPORTED
  proposed_correction: Preserve as reconstruction/report, never RAW_MATCH_VERIFIED or direct observation.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Preserve as reconstruction/report, never RAW_MATCH_VERIFIED or direct observation.
  input_bytes_modified: false
- correction_id: XY-CORR-015
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y-HIST-003 terminology
  original_value: 니르다→이르다 is reported as initial ㄴ loss with terminology/periodization open
  detected_error_or_limitation: 니르다→이르다 is reported as initial ㄴ loss with terminology/periodization open
  proposed_correction: Preserve Y-CONFLICT-003 and prohibit automatic identity with modern Sino-Korean 두음법칙.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Preserve Y-CONFLICT-003 and prohibit automatic identity with modern Sino-Korean 두음법칙.
  input_bytes_modified: false
- correction_id: XY-CORR-016
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Y-HIST-009 ㄴ insertion account
  original_value: Official explanation contains competing analysis
  detected_error_or_limitation: Official explanation contains competing analysis
  proposed_correction: Preserve Y-CONFLICT-002; no forced resolution.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Preserve Y-CONFLICT-002; no forced resolution.
  input_bytes_modified: false
- correction_id: XY-CORR-017
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Cross-input lexical identity
  original_value: Exact same surface + same lemma pair count is 0
  detected_error_or_limitation: Exact same surface + same lemma pair count is 0
  proposed_correction: Do not create lexical lineage from same consonant group; classify all unmatched records as typed MISSING_COUNTERPART.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: NONBLOCKING
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Do not create lexical lineage from same consonant group; classify all unmatched records as typed MISSING_COUNTERPART.
  input_bytes_modified: false
- correction_id: XY-CORR-018
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: 솜 vs 솜이불
  original_value: X has 솜; Y has compound 솜+이불
  detected_error_or_limitation: X has 솜; Y has compound 솜+이불
  proposed_correction: PARTIAL_CROSS_MATCH only at component position; compound is not same lexical identity.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: PARTIAL_CROSS_MATCH only at component position; compound is not same lexical identity.
  input_bytes_modified: false
- correction_id: XY-CORR-019
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: 입 vs 잎
  original_value: Modern pronunciation can converge to [입], but orthography and lemma differ
  detected_error_or_limitation: Modern pronunciation can converge to [입], but orthography and lemma differ
  proposed_correction: Record NON_MATCH_GUARD; same pronunciation is not same lexical identity.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: NONBLOCKING
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Record NON_MATCH_GUARD; same pronunciation is not same lexical identity.
  input_bytes_modified: false
- correction_id: XY-CORR-020
  source_seat: gpt.xy
  source_result_sha256: 225c090140493b07d2068847f6817e31a08d85eed1bdbe1faf7c1c61a07a9562
  target: Modern ㅇ vs historical ㆁ
  original_value: X verifies modern initial ㅇ=Ø and coda ㅇ=[ŋ]; Y reports historical ㆁ/ㅇ complexity
  detected_error_or_limitation: X verifies modern initial ㅇ=Ø and coda ㅇ=[ŋ]; Y reports historical ㆁ/ㅇ complexity
  proposed_correction: CROSS_VERIFIED for modern field split; PARTIAL_CROSS_MATCH for historical lineage.
  correction_basis: XY 2D verification result table with source/result locations preserved in the original judgment.
  blocking_scope: SCOPED
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: CROSS_VERIFIED for modern field split; PARTIAL_CROSS_MATCH for historical lineage.
  input_bytes_modified: false
- correction_id: XZ-CORR-007
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Rime_3_native_members
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Rime_3_native_members
  proposed_correction: add_explicit_cross_refs_to_X_entry_IDs
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: CLASSIFICATION_OR_LINKAGE
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: LEXICAL_CLASS_LINK_VERIFIED
  input_bytes_modified: false
  additional_fields:
    mappings:
    - Z-RIME-007/새 -> X-ㅅ-E05
    - Z-RIME-009/너 -> X-ㄴ-E02
    - Z-RIME-014/눈 -> X-ㄴ-E11
- correction_id: XZ-CORR-010
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: 拿_拏_variant_relation
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: 拿_拏_variant_relation
  proposed_correction: preserve_relation_and_add_separate_full_identity_record_only_if_source_authorizes
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: CLASSIFICATION_OR_LINKAGE
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: DUPLICATE_LINK_VERIFIED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-011
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Z-RIME-015_and_Z-RIME-016
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Z-RIME-015_and_Z-RIME-016
  proposed_correction: preserve_missing_ㅅ_without_forced_completion
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: CLASSIFICATION_OR_LINKAGE
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: RIME_SET_VERIFIED_WITH_EXPLICIT_GAP
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-012
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: all_inputs
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: all_inputs
  proposed_correction: retain_all_analysis_reserved_fields_as_null
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: CLASSIFICATION_OR_LINKAGE
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: NO_SEMANTIC_ANALYSIS
  input_bytes_modified: false
  additional_fields: {}
- correction_id: YZ-CORR-001
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-HIST-001
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-HIST-001
  proposed_correction: Split ㆁ, modern onset ㅇ and modern coda ㅇ into separate lineage candidates; remove linear identity claim.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Split ㆁ, modern onset ㅇ and modern coda ㅇ into separate lineage candidates; remove linear identity claim.
  input_bytes_modified: false
- correction_id: YZ-CORR-002
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-HIST-004
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-HIST-004
  proposed_correction: Reclassify 女 녀/여 from Historical Lineage to modern Position Relation under one Hanja Identity.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Reclassify 女 녀/여 from Historical Lineage to modern Position Relation under one Hanja Identity.
  input_bytes_modified: false
- correction_id: YZ-CORR-003
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-HIST-005
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-HIST-005
  proposed_correction: Reclassify 年 년/연 from Historical Lineage to modern Position/Dependent-noun Relation.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Reclassify 年 년/연 from Historical Lineage to modern Position/Dependent-noun Relation.
  input_bytes_modified: false
- correction_id: YZ-CORR-004
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-HIST-001 source fields
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-HIST-001 source fields
  proposed_correction: Bind modern onset/coda pronunciation to modern norm sources and historical phonetic claims to historical sources separately.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Bind modern onset/coda pronunciation to modern norm sources and historical phonetic claims to historical sources separately.
  input_bytes_modified: false
- correction_id: YZ-CORR-005
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-POS-010
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-POS-010
  proposed_correction: Mark 학년·몇 년 detailed chain pronunciations SOURCE_UNCERTAIN until direct dictionary entries are materialized.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Mark 학년·몇 년 detailed chain pronunciations SOURCE_UNCERTAIN until direct dictionary entries are materialized.
  input_bytes_modified: false
- correction_id: YZ-CORR-006
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-POS-016
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-POS-016
  proposed_correction: Retain the relation as MISSING_SOURCE_LOCATION; do not mark same-lineage fully verified.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Retain the relation as MISSING_SOURCE_LOCATION; do not mark same-lineage fully verified.
  input_bytes_modified: false
- correction_id: YZ-CORR-007
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Z-HANJA-001..080
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Z-HANJA-001..080
  proposed_correction: Keep Unicode identity mechanically verified but label Korean reading/hun as TIER_3_TRANSFORMED_SOURCE_BOUND.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Keep Unicode identity mechanically verified but label Korean reading/hun as TIER_3_TRANSFORMED_SOURCE_BOUND.
  input_bytes_modified: false
- correction_id: YZ-CORR-008
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Z morpheme usages
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Z morpheme usages
  proposed_correction: Keep query URLs, but mark 80 usage links as missing stable detail IDs/evidence locations.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Keep query URLs, but mark 80 usage links as missing stable detail IDs/evidence locations.
  input_bytes_modified: false
- correction_id: YZ-CORR-009
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Z-HOMOPHONE-001..019
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Z-HOMOPHONE-001..019
  proposed_correction: Rename scope explicitly to MODERN_SAME_SYLLABLE_GROUP; prohibit historical same-reading inference.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Rename scope explicitly to MODERN_SAME_SYLLABLE_GROUP; prohibit historical same-reading inference.
  input_bytes_modified: false
- correction_id: YZ-CORR-010
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Z-RIME-001..016
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Z-RIME-001..016
  proposed_correction: Rename scope explicitly to MODERN_ORTHOGRAPHIC_RIME_CONTROL; keep historical reported/reconstructed rime null.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Rename scope explicitly to MODERN_ORTHOGRAPHIC_RIME_CONTROL; keep historical reported/reconstructed rime null.
  input_bytes_modified: false
- correction_id: YZ-CORR-011
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Z IEUNG-001..045
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Z IEUNG-001..045
  proposed_correction: Keep modern orthographic ㅇ / phonetic Ø / coda [ŋ] layers; prohibit linkage to historical ㆁ without new sources.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Keep modern orthographic ㅇ / phonetic Ø / coda [ŋ] layers; prohibit linkage to historical ㆁ without new sources.
  input_bytes_modified: false
- correction_id: YZ-CORR-012
  source_seat: gpt.yz
  source_result_sha256: 552b9ec01fa66ad808c4926f3d45ec3a846bb515b56e71d994aae04a1253789e
  target: Y-HIST-009
  original_value: SEE_ORIGINAL_GPT_YZ_JUDGMENT
  detected_error_or_limitation: Y-HIST-009
  proposed_correction: Preserve 닢/잎 and competing ㄴㄴ-addition analyses as MULTIPLE_LINEAGE_CANDIDATES.
  correction_basis: YZ historical/Hanja/position/rime cross-verification result.
  blocking_scope: APPEND_ONLY_CLASSIFICATION
  draft_application_state: APPLIED_TO_3D_CLASSIFICATION_WITH_ORIGINAL_PRESERVED
  corrected_value: Preserve 닢/잎 and competing ㄴㄴ-addition analyses as MULTIPLE_LINEAGE_CANDIDATES.
  input_bytes_modified: false
```
## 37. Correction Pending

```yaml
pending_count: 8
pending_reason: New source bytes, stable IDs or exact source locations are required.
correction_pending:
- correction_id: XZ-CORR-001
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Data_X_47_reentry_only_entries
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Data_X_47_reentry_only_entries
  proposed_correction: bind_individual_target_code_exact_entry_snapshot_and_source_position
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: SOURCE_POSITION_VERIFIED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-002
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Data_X_9_uncertain_lemmas
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Data_X_9_uncertain_lemmas
  proposed_correction: select_or_split_dictionary_sense_identity_by_target_code
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: LEXICAL_CLASS_VERIFIED_OR_RETAIN_UNCERTAIN
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-003
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Data_X_example_sentences
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Data_X_example_sentences
  proposed_correction: add_source_sentence_location_or_label_as_generated_normalized_example
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: SOURCE_CLAIM_BOUNDARY_RESTORED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-004
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Data_Z_Hanja_reading_and_hun
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Data_Z_Hanja_reading_and_hun
  proposed_correction: bind_official_XLS_exact_bytes_and_reproducible_transform_or_official_Hanja_dictionary_entries
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: HANJA_READING_HUN_SOURCE_VERIFIED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-005
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Data_Z_80_usage_words
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Data_Z_80_usage_words
  proposed_correction: bind_stdict_word_no_definition_location_and_exact_morpheme_position
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: SOURCE_POSITION_VERIFIED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-006
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: Rime_43_unregistered_Sino_members
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: Rime_43_unregistered_Sino_members
  proposed_correction: create_full_Hanja_identity_records_with_character_codepoint_reading_hun_word_Hanja_position_and_sources
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: HANJA_IDENTITY_VERIFIED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-008
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: 9_surface_or_noninitial_Hanja_members
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: 9_surface_or_noninitial_Hanja_members
  proposed_correction: split_canonical_reading_usage_surface_morpheme_position_and_pronunciation
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: IDENTITY_SURFACE_POSITION_VERIFIED
  input_bytes_modified: false
  additional_fields: {}
- correction_id: XZ-CORR-009
  source_seat: gpt.xz
  source_result_sha256: 1a737918cf10e4dd79ca4e936a6a4618388f3db0ad24ccbcac467d077782bdf5
  target: 10_anonymous_ieung_records
  original_value: SEE_ORIGINAL_GPT_XZ_JUDGMENT
  detected_error_or_limitation: 10_anonymous_ieung_records
  proposed_correction: assign_stable_record_ID_and_parent_rime_member_ref
  correction_basis: XZ source/identity/dataset verification result and its exact audit locations.
  blocking_scope: SOURCE_DATA_REQUIRED
  draft_application_state: CORRECTION_PENDING_SOURCE_DATA
  corrected_value: NORMALIZATION_ERROR_CLOSED
  input_bytes_modified: false
  additional_fields: {}
```
## 38. Unresolved

```yaml
seat_position_count: 34
unresolved:
- source_seat: gpt.xy
  item: 47 X individual target-code and exact entry locations
- source_seat: gpt.xy
  item: 9 X homograph_or_polysemy identities
- source_seat: gpt.xy
  item: X nominal root source status
- source_seat: gpt.xy
  item: X exact raw definition and example provenance
- source_seat: gpt.xy
  item: 6 extra X zero-onset lexical item identities
- source_seat: gpt.xy
  item: 10 X no-coda/coda direct inflection snapshots
- source_seat: gpt.xy
  item: Y ㆁ_and_ㅇ complete historical lineage
- source_seat: gpt.xy
  item: Y_POS_010 exact compound pronunciations
- source_seat: gpt.xy
  item: Y_POS_016 direct lemma page
- source_seat: gpt.xy
  item: 니르다_to_이르다 terminology_and_periodization
- source_seat: gpt.xy
  item: ㄴ_insertion_analysis_competition
- source_seat: gpt.xy
  item: absence_of_same_lemma_independent_XY_sample
- source_seat: gpt.xz
  id: XZ-U-001
  item: X_47_exact_dictionary_entry_snapshots
  blocking: true
- source_seat: gpt.xz
  id: XZ-U-002
  item: X_9_homonym_or_sense_target_codes
  blocking: scoped
- source_seat: gpt.xz
  id: XZ-U-003
  item: X_example_sentence_provenance
  blocking: scoped
- source_seat: gpt.xz
  id: XZ-U-004
  item: official_Hanja_XLS_exact_bytes_and_transform_reproduction
  blocking: true
- source_seat: gpt.xz
  id: XZ-U-005
  item: Z_80_official_dictionary_detail_word_numbers
  blocking: true
- source_seat: gpt.xz
  id: XZ-U-006
  item: Rime_43_Sino_member_full_identity_records
  blocking: true
- source_seat: gpt.xz
  id: XZ-U-007
  item: canonical_reading_vs_surface_position_for_9_members
  blocking: scoped
- source_seat: gpt.xz
  id: XZ-U-008
  item: stable_IDs_for_10_ieung_supplementary_records
  blocking: scoped
- source_seat: gpt.xz
  id: XZ-U-009
  item: full_variant_identity_for_拏_if_required
  blocking: scoped
- source_seat: gpt.xz
  id: XZ-U-010
  item: direct_source_positions_for_all_62_rime_members
  blocking: true
- source_seat: gpt.yz
  item: exact_character_lineage_between_old_ieung_and_modern_ieung
- source_seat: gpt.yz
  item: medieval_initial_ieung_phonetic_value_by_period_and_region
- source_seat: gpt.yz
  item: dueum_terminology_and_periodization_for_native_niruda_lineage
- source_seat: gpt.yz
  item: nip_leaf_and_double_n_insertion_competing_analysis
- source_seat: gpt.yz
  item: direct_detail_identity_for_jitda
- source_seat: gpt.yz
  item: direct_pronunciation_entries_for_haknyeon_and_myeot_nyeon
- source_seat: gpt.yz
  item: original_hanja_XLS_and_transformation_reproducibility
- source_seat: gpt.yz
  item: independent_official_hanja_reading_crosscheck_for_80_identities
- source_seat: gpt.yz
  item: stable_dictionary_detail_locations_for_80_usage_words
- source_seat: gpt.yz
  item: historical_Korean_Hanja_readings
- source_seat: gpt.yz
  item: historical_reported_or_reconstructed_rimes
- source_seat: gpt.yz
  item: old_Hangul_extended_jamo_normalization_policy
resolution_by_majority: PROHIBITED
```
## 39. Required Next Data

```yaml
seat_request_count: 34
required_next_data:
- source_seat: gpt.xy
  Next data: ND-001
  Input: X
  Required item: 47 individual target_code and exact entry snapshots
  Purpose: Upgrade source identity and exact sense verification
- source_seat: gpt.xy
  Next data: ND-002
  Input: X
  Required item: Exact raw definition and example locations
  Purpose: Distinguish raw dictionary capture from normalized short gloss
- source_seat: gpt.xy
  Next data: ND-003
  Input: X
  Required item: Morphological source for nominal root fields
  Purpose: Verify or null root placeholders
- source_seat: gpt.xy
  Next data: ND-004
  Input: X
  Required item: Direct inflection snapshots for 10 no-coda/coda pairs
  Purpose: Permit lineage-link verification
- source_seat: gpt.xy
  Next data: ND-005
  Input: X
  Required item: Item-level sources for 앙금·엉덩이·옹기·웅덩이·응어리·잉어
  Purpose: Verify lexical identity separately from general phonological rule
- source_seat: gpt.xy
  Next data: ND-006
  Input: Y
  Required item: Direct detailed entry for 짓다
  Purpose: Resolve Y-POS-016 source identity weakness
- source_seat: gpt.xy
  Next data: ND-007
  Input: Y
  Required item: Direct dictionary pronunciation for 학년·몇 년
  Purpose: Resolve Y-POS-010 pronunciation
- source_seat: gpt.xy
  Next data: ND-008
  Input: Y
  Required item: Professional Middle Korean sources for ㆁ/ㅇ
  Purpose: Verify character and sound lineage
- source_seat: gpt.xy
  Next data: ND-009
  Input: Y
  Required item: Professional periodization for 니르다→이르다
  Purpose: Resolve terminology/time boundary
- source_seat: gpt.xy
  Next data: ND-010
  Input: Y
  Required item: Additional evidence for ㄴ insertion analyses
  Purpose: Preserve or resolve competition
- source_seat: gpt.xy
  Next data: ND-011
  Input: XY
  Required item: At least one same-lemma dataset collected independently by X and Y
  Purpose: Enable lexical CROSS_VERIFIED relation rather than field-level only
- source_seat: gpt.xy
  Next data: ND-012
  Input: XY
  Required item: Versioned source snapshots or archived pages
  Purpose: Improve reproducibility of dynamic dictionary and Q&A pages
- source_seat: gpt.xz
  request_id: XZ-ND-001
  object: X_47_individual_KRDICT_entries
  required_fields:
  - target_code
  - exact_URL
  - sense_number
  - part_of_speech
  - origin_class
  - pronunciation
  - definition_location
- source_seat: gpt.xz
  request_id: XZ-ND-002
  object: X_9_homonym_sense_disambiguation
  lemmas:
  - 김
  - 날
  - 눈
  - 살
  - 새
  - 샘
  - 술
  - 우리
  - 이제
- source_seat: gpt.xz
  request_id: XZ-ND-003
  object: official_Hanja_source
  required: original_XLS_exact_bytes_or_official_entry_level_Hanja_dictionary_sources
- source_seat: gpt.xz
  request_id: XZ-ND-004
  object: reproducible_CSV_transform_manifest
  required_fields:
  - input_hash
  - transform_code
  - output_hash
  - row_lineage
- source_seat: gpt.xz
  request_id: XZ-ND-005
  object: Z_80_STDICT_detail_entries
  required_fields:
  - word_no
  - exact_entry_URL
  - Hanja_form
  - pronunciation
  - definition_location
  - morpheme_position
- source_seat: gpt.xz
  request_id: XZ-ND-006
  object: Rime_43_unregistered_Sino_identities
  required_fields:
  - character
  - codepoint
  - canonical_reading
  - representative_hun
  - usage_word_Hanja
  - position
  - official_sources
- source_seat: gpt.xz
  request_id: XZ-ND-007
  object: Rime_62_member_detail_sources
  required_fields:
  - exact_entry_ID
  - exact_location
  - pronunciation
  - lexical_class
- source_seat: gpt.xz
  request_id: XZ-ND-008
  object: stable_cross_record_ID_map
  required_for: 10_anonymous_ieung_records
- source_seat: gpt.xz
  request_id: XZ-ND-009
  object: variant_拏_identity_source
  required_only_if: separate_identity_record_is_promoted
- source_seat: gpt.xz
  request_id: XZ-ND-010
  object: X_example_sentence_provenance_or_reclassification_manifest
- source_seat: gpt.yz
  next_data_id: YZ-NEXT-001
  item: 한국어문회 원 XLS Exact Byte·SHA-256와 CSV 변환 재현 절차
  state: NEXT_DATA_REQUIRED
- source_seat: gpt.yz
  next_data_id: YZ-NEXT-002
  item: 80개 한자 Identity별 공공·공식 한자사전 상세 독음·훈 위치
  state: NEXT_DATA_REQUIRED
- source_seat: gpt.yz
  next_data_id: YZ-NEXT-003
  item: 80개 표준국어대사전 용례의 안정적인 word_no·정의·발음 위치
  state: NEXT_DATA_REQUIRED
- source_seat: gpt.yz
  next_data_id: YZ-NEXT-004
  item: 초성 옛이응 ㆁ과 중세 초성 ㅇ의 전문 국어사 문법·논문 Source
  state: NEXT_DATA_REQUIRED
- source_seat: gpt.yz
  next_data_id: YZ-NEXT-005
  item: ㆁ·ㅇ 문자계보와 음가 변화를 분리한 판본·시기별 자료
  state: NEXT_DATA_REQUIRED
- source_seat: gpt.yz
  next_data_id: YZ-NEXT-006
  item: 니르다→이르다의 세부 시기·중간 문헌형·현상 명명 연구
  state: NEXT_DATA_REQUIRED
- source_seat: gpt.yz
  next_data_id: YZ-NEXT-007
  item: 닢/잎 및 ㄴㄴ 첨가 경쟁분석의 독립 연구 Source
  state: NEXT_DATA_REQUIRED
- source_seat: gpt.yz
  next_data_id: YZ-NEXT-008
  item: 짓다 직접 표제어·발음·활용 상세 페이지
  state: NEXT_DATA_REQUIRED
- source_seat: gpt.yz
  next_data_id: YZ-NEXT-009
  item: 학년·몇 년 등 연쇄발음 직접 사전 항목
  state: NEXT_DATA_REQUIRED
- source_seat: gpt.yz
  next_data_id: YZ-NEXT-010
  item: 역사 한국 한자음 및 역사운모를 직접 제시하는 별도 Dataset
  state: NEXT_DATA_REQUIRED
- source_seat: gpt.yz
  next_data_id: YZ-NEXT-011
  item: 옛한글·확장자모를 보존하는 Unicode/판본 표본
  state: NEXT_DATA_REQUIRED
- source_seat: gpt.yz
  next_data_id: YZ-NEXT-012
  item: 실제 말뭉치 기반 첫 위치·비첫 위치 용례와 빈도 자료
  state: NEXT_DATA_REQUIRED
```
## 40. Analysis Reserved Confirmation

```yaml
analysis_reserved:
  first_axis_hypothesis: null
  structural_direction: null
  semantic_structure: null
  supports_hypothesis: null
  contradicts_hypothesis: null
  singularity_candidate: null
  residual_structure: null
  hidden_transition: null
all_reserved_fields_null: true
analysis_performed: false
```
## 41. 4d Final Review Checklist

```yaml
review_checklist:
- item: 세 2d Result의 Exact Identity가 결속됐다.
  state: true
- item: 각 2d Seat 판단이 분리 보존됐다.
  state: true
- item: 모든 핵심 Entry에 Source 위치가 있다.
  state: false
  note: Missing source locations preserved explicitly.
- item: Raw와 Normalized가 분리됐다.
  state: true
- item: 고유어·한자어·한자 Identity가 구분됐다.
  state: true
- item: 어근·어간·활용·파생의 중복이 정리됐다.
  state: false
  note: Root/stem and inflection source gaps remain.
- item: ㅇ·Ø·종성 ㅇ이 분리됐다.
  state: true
- item: 현대형·역사형·재구음 상태가 구분됐다.
  state: true
- item: 동음 한자 Group의 Member가 검산됐다.
  state: true
- item: 동일 중성종성 Set의 Member가 검산됐다.
  state: true
- item: Conflict·Uncertainty·Gap이 삭제되지 않았다.
  state: true
- item: Correction 전후 계보가 보존됐다.
  state: true
- item: Analysis Reserved 필드가 null이다.
  state: true
- item: Track DB 요소를 생성하지 않았다.
  state: true
ready_for_4d_review: true
draft_has_unresolved: true
```
## 42. Handoff to gpt.logi

```yaml
handoff:
  from: gpt.xyz@HRTDB_A::gpt.xyz
  to: gpt.logi@HRTDB_A::gpt.xyzt
  cycle_id: GLANG-SOURCE-COLLECTION-BASE-CONSONANTS-R01
  stage_id: R03_3D_XYZ
  result_class: SOURCE_COLLECTION_RESULT_DATA_DRAFT
  completion_state: RESULT_DATA_DRAFT_COMPLETE_WITH_UNRESOLVED
  bound_2d_result_count: 3
  cross_confirmed_record_count: 6
  partially_confirmed_record_count: 9
  single_seat_only_record_count: 1
  cross_result_conflict_count: 10
  correction_ledger_count: 44
  applied_draft_correction_count: 36
  pending_correction_count: 8
  analysis_reserved_null: true
  github_mutation: false
  track_db_promotion: false
  next_stage: 4D_FINAL_VERIFICATION
  direct_to_gpt_lang: false
  termination: RESULT_DATA_DRAFT_READY_FOR_4D_FINAL_VERIFICATION
```
## Final Guard

```text
relation is not merge.
cross-confirmation is not universal truth.
conflict is not noise.
correction is not deletion.
maximum-unfolded is not uncontrolled duplication.
same surface is not same lexical identity.
same modern syllable is not same Hanja Identity.
same modern rime is not same historical rime.
historical reconstruction is not direct observation.
position difference is not time difference.
temporal sequence is not causation.
Result.Data Draft is not Final Result.Data.
Result.Data is not Track DB.
```
~~~~~

---

# Final Guard

```text
verified relation state is not universally verified source data.
candidate data is not source-closed data.
mechanical identity is not semantic identity.
reported pronunciation is not direct acoustic observation.
modern orthographic relation is not historical relation.
conflict is not noise.
correction is not deletion.
Result.Data is not Track DB.
relation is not merge.
```
