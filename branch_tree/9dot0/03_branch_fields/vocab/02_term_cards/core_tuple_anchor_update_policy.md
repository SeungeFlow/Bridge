# core tuple anchor update policy

## status

pass: 77
role: exact-matched core tuple anchor update policy
card_update_execution: false
db_query_execution: false
term_card_finalization: false
base_commit_repo_9dot0: fdfca702857b2a7b4c9a8adf90474dcb7d01e02a

## purpose

This policy defines how exact source anchors may later be added to the first core tuple term-card candidates.

The target cards are:

```text
C
m
t
p
?
```

## source basis

The basis is the PASS72 runtime anchor enrichment report and PASS75 exact-anchor review report.

PASS75 classified these cards as exact matched:

```text
C
m
t
p
?
```

## update principle

Do not finalize card meaning.

Do not rewrite candidate interpretations.

Only add a controlled anchor section or anchor table.

The first card-update batch should preserve all existing candidate and guard language.

## allowed update shape

A future update may add a section like:

```text
## source anchors — PASS72 enrichment

term | status | repo | branch | commit | path | line_no | raw_url | context
...
```

## forbidden update shape

Do not add:

```text
final_definition: true
FINAL
confirmed meaning
proof
branch completion
```

## batch size

The first update should be small.

Recommended batch:

```text
C
m
t
p
?
```

## review rule

Before modifying card files, the update source rows must be reviewed.

If a row is only variant-matched, it must not be used for exact core-card update.

For this batch, use only exact-matched rows.

## guard

Anchor update strengthens traceability.

Anchor update does not finalize definition.

DB output is derived evidence.

Original source remains in md files and Raw URLs.
