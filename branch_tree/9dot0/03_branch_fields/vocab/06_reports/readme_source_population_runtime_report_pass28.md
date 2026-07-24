# readme_source population runtime report — pass28

## status

pass: 28
recorded_in_pass: 29
role: readme_source metadata correction summary
repo_9dot0_commit_at_population: c6ed2c89656a42cb04beda4cce5d2503be2daf52
recording_commit_base: c6ed2c89656a42cb04beda4cce5d2503be2daf52

## judgment

PASS28_README_SOURCE_POPULATION_APPLIED

The readme_source metadata correction was successfully applied to the local runtime SQLite DB.

## runtime paths

- runtime_dir: `/home/gogiseung/seungeflow_runtime/vocab_reader`
- db_path: `/home/gogiseung/seungeflow_runtime/vocab_reader/vocab_reader.sqlite`
- backup_path: `/home/gogiseung/seungeflow_runtime/vocab_reader/vocab_reader.pre_pass28.sqlite.bak`
- runtime_report: `/home/gogiseung/seungeflow_runtime/vocab_reader/readme_source_population_report_pass28.md`

## DB file policy

The live SQLite DB is not committed to GitHub.

The pre-pass28 backup is not committed to GitHub.

This markdown file is only a tracked summary report.

## source scope

Selected README source import only.

No whole-repository scan.

No DB rebuild.

## DB counts after population

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
```

## readme_source rows

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

## correction result

```text
readme_source_before=0
inserted=8
readme_source_after=8
dry_run=0
unknown_class=0
README_SOURCE_POPULATION_CHECK=OK
```

## meaning

source_file records source identity.

readme_source records which source_file rows are part of the README.md vocab baseline.

The first SQLite MVP DB now has README baseline metadata registered.

## guard

This is metadata correction.

This is not final interpretation.

This does not make DB rows original source facts.

Original source remains in md files and Raw URLs.
