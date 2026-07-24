# term-card anchor enrichment policy

## status

pass: 70
role: term-card anchor enrichment policy
anchor_enrichment_execution: false
db_query_execution: false
base_commit_repo_9dot0: d08467dd00b8af9a5b922b0adaed216e0b000d4a

## purpose

This policy defines how term-card candidates may later be enriched with exact source anchors.

Anchor enrichment means adding DB-derived source identity rows such as:

```text
repo | branch | commit | path | line_no | raw_url | context
```

to existing term-card candidates or to a separate enrichment report.

## current state

The first term-card candidate ring has been committed.

Current candidate cards:

```text
C
m
t
p
?
Ctp
Ctp24
Raw URL
source identity
README baseline
Seed.Base
Y_Branch
vocab.branch
```

## source principle

The DB is not original source.

The DB is a derived Seed.Base-like reader field.

Original source remains in md files and Raw URLs.

## enrichment principle

Do not edit individual cards directly in the first enrichment pass.

First create a separate anchor enrichment report.

After review, individual card updates may be done in later controlled passes.

## read-only rule

Anchor enrichment must use read-only DB access.

The DB checksum should be compared before and after query execution.

## no whole-repo scan

Anchor enrichment must not scan the whole repo.

It must query the existing SQLite MVP DB only.

## exact anchor requirement

Every enriched row should preserve:

```text
term | status | repo | branch | commit | path | line_no | raw_url | context
```

## missing term rule

If a term does not match exactly in the DB, record it as:

```text
NO_EXACT_TERM_MATCH
```

Do not invent anchors.

If a concept-card term is phrase-based, query known variants only under gpt.direct instruction.

## guard

Anchor enrichment does not finalize term definitions.

Anchor enrichment only strengthens source traceability.

Term-card candidate remains candidate.
