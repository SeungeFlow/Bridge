# DB build guard

## status

pass: 18
role: guard for future DB build
db_build: false

## pass18 rule

Pass18 does not build a database.

Pass18 only designs the SQLite MVP schema.

## future DB build conditions

A future DB build may begin only after:

1. README vocab source list is committed.
2. v3 core-token preview reports are committed.
3. schema_v0_1.sql is reviewed.
4. DB output path is outside tracked source by default.
5. A report-first rule is defined.

## output location rule

A local SQLite DB should first be created under a local runtime path, for example:

`~/seungeflow_runtime/vocab_reader/vocab_reader.sqlite`

Do not commit the live SQLite DB file by default.

Commit only:

- schema
- build script
- report
- small sample export if needed

## source safety

The DB must not replace md source files.

The DB points back to Raw URLs.

## no whole-repo scan

The first DB build must use selected README sources only.

Whole-repo occurrence expansion is a later pass.

## guard

If the DB grows faster than the README vocab baseline, stop.

README.md is the vocabulary law.
