# readme_source gap fix policy

## status

pass: 25
role: readme_source gap fix policy
db_modification: false
base_commit_repo_9dot0: c671e01f22201b43fe518fb07cd786eb3672d3c4

## observed gap

The first local SQLite MVP DB build succeeded, but the build report showed:

```text
source_file=8
readme_source=0
```

## judgment

This is not a DB build failure.

The MVP import created source_file rows, vocab_term rows, term_occurrence rows, and raw_url_index rows.

However, it did not separately register README baseline sources in the readme_source table.

## meaning

source_file records source identity.

readme_source records which source_file rows are part of the README.md vocab baseline.

Therefore, readme_source should be populated from source_file rows that were imported from selected README source units.

## correction principle

Do not rebuild the whole DB first.

Do not rescan repositories.

First, populate readme_source from existing source_file rows.

## expected target

The current MVP DB has 8 source_file rows from selected README sources.

Therefore the first correction should produce:

```text
readme_source=8
```

unless source_file count changes.

## source class proposal

The readme_source rows should use baseline classes such as:

- repo_9dot0_branch_field
- repo_seungeflow_primary_observer
- readme_baseline_candidate

## guard

readme_source population is metadata correction.

It does not change original source.

It does not finalize interpretation.

It does not make DB rows source facts.

Raw URLs remain source coordinates.
