# readme_source population report rule

## status

pass: 25
role: readme_source population report rule
db_modification: false

## purpose

When readme_source metadata is populated in a later pass, a markdown report must be generated.

The report allows gpt.direct to inspect the correction without reading the DB directly.

## required fields

The report should include:

- db_path
- source_file_before
- readme_source_before
- inserted
- skipped_existing
- unknown_class
- readme_source_after
- dry_run status
- guard statement

## expected first correction

For the current MVP DB, the expected correction is approximately:

```text
source_file_before=8
readme_source_before=0
inserted=8
readme_source_after=8
```

## guard

The report is a runtime correction report.

Do not commit the live SQLite DB by default.

Commit only the markdown summary report if useful.

Do not treat readme_source metadata as final interpretation.
