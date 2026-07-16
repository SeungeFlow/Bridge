# SQLite build report rule

## status

pass: 20
role: build report rule
db_build: false

## purpose

Every DB build must create a markdown report.

The report allows gpt.direct to inspect DB build results without reading the DB directly.

## required report fields

A build report should include:

- DB path
- input CSV path
- schema path
- Repo.9Dot0 commit
- source scope
- row counts
- source_file count
- vocab_term count
- term_occurrence count
- guard statement

## source scope statement

The first SQLite MVP build must state:

`Selected README source import only. No whole-repo scan.`

## DB file policy

Do not commit live SQLite DB files by default.

Commit build reports and schema instead.

## future Oracle transition

Local Linux runtime is the testbed.

Oracle free server may later become remote runtime.

The build report must make migration easier by recording paths and counts.
