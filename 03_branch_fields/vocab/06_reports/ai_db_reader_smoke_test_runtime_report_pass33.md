# AI DB reader smoke test runtime report — pass33

## status

pass: 33
recorded_in_pass: 34
role: AI DB reader read-only smoke test summary
repo_9dot0_commit_at_smoke_test: ee91aea31f6021fcd49f214301e8618375547937
recording_commit_base: ee91aea31f6021fcd49f214301e8618375547937

## judgment

PASS33_AI_DB_READER_READ_ONLY_SMOKE_TEST_DONE

The AI DB reader read-only smoke test succeeded.

The DB checksum before and after the read-only queries matched.

The Git repo remained clean.

## runtime paths

- runtime_dir: `/home/gogiseung/seungeflow_runtime/vocab_reader`
- db_path: `/home/gogiseung/seungeflow_runtime/vocab_reader/vocab_reader.sqlite`
- smoke_report: `/home/gogiseung/seungeflow_runtime/vocab_reader/ai_db_reader_smoke_test_report_pass33.md`

## DB file policy

The live SQLite DB is not committed to GitHub.

This markdown file is only a tracked summary report.

## read-only verification

```text
db_sha_before=419d90b3779f83dba45ffc88126ede38aad16842d84c051ff702642ab01eb0af
db_sha_after=419d90b3779f83dba45ffc88126ede38aad16842d84c051ff702642ab01eb0af
read_only_checksum_check=OK
smoke_output_check=OK
```

## summary counts

```text
scan_run=1
source_file=8
readme_source=8
vocab_term=1710
term_status=1710
term_occurrence=3855
raw_url_index=3855
term_relation_candidate=0
term_card_candidate=0
reader_query_log=0

filtered_candidate=2305
demoted_common=985
structural_trigger_candidate=403
core_token_candidate=162
```

## readme_sources preview

```text
1|repo_9dot0_branch_field|SeungeFlow/9Dot0|main|README.md
2|repo_9dot0_branch_field|SeungeFlow/9Dot0|main|03_branch_fields/market/README.md
3|repo_9dot0_branch_field|SeungeFlow/9Dot0|main|03_branch_fields/sohosa/README.md
4|repo_9dot0_branch_field|SeungeFlow/9Dot0|main|03_branch_fields/history/README.md
5|repo_9dot0_branch_field|SeungeFlow/9Dot0|main|03_branch_fields/vocab/README.md
6|repo_seungeflow_primary_observer|SeungeFlow/SeungeFlow|Y_Branch|README.md
7|repo_seungeflow_primary_observer|SeungeFlow/SeungeFlow|main|README.md
8|repo_seungeflow_primary_observer|SeungeFlow/SeungeFlow|first_flow|README.md
```

## core token preview

```text
C|core_token_candidate|15|20|3
?|core_token_candidate|15|17|3
m|core_token_candidate|15|14|3
p|core_token_candidate|15|12|4
t|core_token_candidate|15|12|4
Ctp24|core_token_candidate|15|12|2
A|core_token_candidate|15|11|3
Core|core_token_candidate|15|11|2
S₄|core_token_candidate|15|10|1
Path|core_token_candidate|15|9|1
C=(m,t,p,?)|core_token_candidate|15|8|3
S₁|core_token_candidate|15|8|1
S₂|core_token_candidate|15|5|1
S₃|core_token_candidate|15|5|1
Ctp|core_token_candidate|15|4|2
C=tp|core_token_candidate|15|3|1
S4|core_token_candidate|15|1|1
```

## term query preview

### C

```text
C|C|core_token_candidate|15|20

Representative context:
SeungeFlow/SeungeFlow|Y_Branch|README.md|100|C = (m,t,p,?)
SeungeFlow/SeungeFlow|Y_Branch|README.md|156|C축:
SeungeFlow/SeungeFlow|first_flow|README.md|345|C = t × p
SeungeFlow/SeungeFlow|first_flow|README.md|347|C : 구조
SeungeFlow/SeungeFlow|main|README.md|267|C = (m, t, p, ?)
```

### Ctp24

```text
Ctp24|Ctp24|core_token_candidate|15|12

Representative context:
SeungeFlow/SeungeFlow|Y_Branch|README.md|5|Y_Branch는 ... Ctp24로 ... 분류하며 ...
SeungeFlow/SeungeFlow|Y_Branch|README.md|127|## 5. Ctp24 Matrix Filter
SeungeFlow/SeungeFlow|Y_Branch|README.md|129|Ctp24는 Y_Branch의 1차 구조필터이다.
SeungeFlow/SeungeFlow|Y_Branch|README.md|165|Ctp24는 새 입력을 다음으로 분류한다.
SeungeFlow/SeungeFlow|main|README.md|157|이곳에는 Ctp24 작업, ComplexTest, Event, Context...
```

### Y_Branch

```text
Y_Branch|Y_Branch|structural_trigger_candidate|13|32

Representative context:
SeungeFlow/9Dot0|main|README.md|78|- Y_Branch README.md
SeungeFlow/SeungeFlow|Y_Branch|README.md|1|# Y_Branch
SeungeFlow/SeungeFlow|Y_Branch|README.md|18|이 문서는 Y_Branch의 first gateway이다.
SeungeFlow/SeungeFlow|Y_Branch|README.md|32|Y_Branch는 운영체제가 아니다. Y_Branch는 운영체계다.
SeungeFlow/SeungeFlow|Y_Branch|README.md|283|Y_Branch = State Machine + Validator Loop
```

## query modes tested

```text
summary
readme_sources
core
status structural_trigger_candidate
term C
term Ctp24
term Y_Branch
context C
```

## meaning

The AI DB reader can now retrieve selected source identity, term status, occurrence counts, Raw URL coordinates, and compact context without loading the whole repository into context.window.

## guard

The DB output is derived evidence.

The DB is not the original source.

High frequency is not final meaning priority.

Original source remains in md files and Raw URLs.
