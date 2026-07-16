# Seed.Base / Y_Branch anchor update policy

## status

pass: 99
role: exact-matched Seed.Base/Y_Branch anchor update policy
card_update_execution: false
db_query_execution: false
term_card_finalization: false
base_commit_repo_9dot0: 76150d8c7c99df7426f919cb548884cf1bbbf623

## purpose

This policy defines how exact source anchors may later be added to the `Seed.Base` and `Y_Branch` term-card candidates.

The target cards are:

```text
Seed.Base
Y_Branch
```

## source basis

The basis is the PASS72 runtime anchor enrichment report and PASS75 exact-anchor review report.

PASS75 classified these cards as exact matched:

```text
Seed.Base
Y_Branch
```

## position after core and Ctp cycles

The following anchor cycles have already been completed:

```text
C / m / t / p / ?
Ctp / Ctp24
```

Seed.Base and Y_Branch are handled after these because they are source-field / branch-surface names rather than the first tuple or operation/filter names.

## update principle

Do not finalize card meaning.

Do not rewrite candidate interpretations.

Only add a controlled anchor section or anchor table.

The future card-update pass should preserve all existing candidate/guard language.

## allowed update shape

A future update may add a controlled section containing:

```text
source anchors — PASS72 enrichment
anchor_status: CANDIDATE_ENRICHED
anchor_source: PASS72 runtime anchor enrichment report
anchor_update_pass: <pass>
final_definition: false
term | status | repo | branch | commit | path | line_no | raw_url | context
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

## recommended batch order

Recommended order:

```text
1. Seed.Base
2. Y_Branch
```

Reason:

```text
Seed.Base is the source-memory / seed-field name.
Y_Branch is the branch-surface / observer-branch name.
```

## guard

Anchor update strengthens traceability.

Anchor update does not finalize definition.

DB output is derived evidence.

Original source remains in md files and Raw URLs.
