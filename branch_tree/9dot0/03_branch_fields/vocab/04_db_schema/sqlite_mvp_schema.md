# SQLite MVP schema

## status

pass: 18
role: SQLite MVP schema design
db_build: false
base_commit_repo_9dot0: 9f424dc81aac3d961f19c64c05adac241d75cec0

## purpose

This schema defines the first local SQLite structure for vocab.branch.

The DB is not a word list.

The DB is a derived Seed.Base-like reader field that allows an AI instance to read selected source through:

- README vocab
- word triggers
- Raw URL source identity
- repo / branch / commit / path
- line context
- source role
- structural token status
- relation candidates

## final reader

The final reader is an AI instance.

The AI reader should not load entire repositories into context.window.

It should use SQLite reports and Raw URLs to select only necessary source units.

## minimal connector rule

Repo, Branch, Directory, and md files are connected by:

1. word
2. Raw URL

A word connects meaning.
A Raw URL fixes source identity.

## MVP table map

### scan_run

Records each scanner execution.

### source_file

Stores source identity.

### readme_source

Marks README.md baseline sources.

### vocab_term

Stores normalized terms.

### term_occurrence

Stores where each term appears.

### raw_url_index

Stores Raw URL access coordinates.

### term_status

Stores status such as raw, demoted_common, filtered_candidate, core_token_candidate, structural_trigger_candidate.

### term_relation_candidate

Stores non-final relation candidates.

### term_card_candidate

Stores candidates for future md term cards.

### reader_query_log

Records AI reader query attempts.

## source status rule

A DB row is not original source.

Original source remains the md file at Raw URL.

The DB is a derived index.

## not included in MVP

MVP does not include:

- etymology
- origin history
- Hanja deep decomposition
- rendering glyph data
- music_language slippage analysis
- final relation judgment

These may branch later into history, rendering, music_language, and Y_Branch layers.

## guard

Do not treat SQLite output as final interpretation.

Do not silently add terms outside README vocab baseline.

If a needed term is missing from README.md, update the relevant README.md first.
