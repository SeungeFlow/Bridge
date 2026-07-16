# SQLite runtime build policy

## status

pass: 20
role: local SQLite runtime build policy
db_build: false
base_commit_repo_9dot0: 0a2056fcac77cb64a7a8817b736d930cec791502

## purpose

This document defines how a local SQLite runtime DB may later be built for vocab.branch.

The live SQLite DB is a runtime artifact.

The live SQLite DB is not the source.

## source principle

Original source remains in md files and Raw URLs.

SQLite stores derived index rows.

The DB helps AI instances become DB readers.

## runtime path

Default local runtime path:

`~/seungeflow_runtime/vocab_reader/`

Default DB path:

`~/seungeflow_runtime/vocab_reader/vocab_reader.sqlite`

## tracked vs untracked

Tracked in GitHub:

- schema SQL
- build script
- build policy
- build reports
- small CSV/markdown previews when useful

Not tracked by default:

- live `.sqlite`
- WAL files
- SHM files
- large generated runtime cache

## build input

The first DB build should use committed preview CSV from selected README sources:

`03_branch_fields/vocab/06_reports/readme_vocab_scan_core_filtered_preview_pass14.csv`

## no whole-repo scan

The first DB build must not scan the whole repo.

It only imports selected README scan results.

## future expansion

Future passes may add:

- all README expansion
- source occurrence expansion
- term card generation
- history/etymology branch integration
- renderer glyph integration
- music_language slippage/residue layer
- Y_Branch relation/guard layer

## guard

Do not confuse DB convenience with source truth.

DB rows are derived.

Raw URL remains the source coordinate.
