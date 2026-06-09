# AI DB reader query policy

## status

pass: 31
role: AI DB reader read-only query policy
db_modification: false
base_commit_repo_9dot0: fc9fe8bf7960e987cd1b03c62f7d293be296f070

## purpose

This document defines how an AI instance should read the vocab.branch SQLite MVP DB.

The AI reader should not load entire repositories into context.window.

The AI reader should query:

- README baseline sources
- vocab terms
- structural token statuses
- term occurrences
- Raw URL coordinates
- compact line context

## source principle

The DB is not original source.

The DB is a derived Seed.Base-like reader field.

Original source remains in md files and Raw URLs.

## read-only rule

The first AI DB reader must use read-only SQLite access.

No insert, update, delete, schema migration, rebuild, or scan is allowed in reader mode.

## query modes

The first reader script should support:

- summary
- readme_sources
- term
- status
- context
- source
- core

## expected reader behavior

The reader should return compact results.

The reader should preserve source identity:

```text
repo | branch | commit | path | raw_url | line_no | context
```

## AI handoff rule

When another AI instance asks for a term, gpt.direct should provide:

1. term status
2. occurrence count
3. top source rows
4. Raw URL coordinates
5. compact context
6. guard statement

## guard

Do not treat high frequency as meaning priority.

Do not treat DB status as final interpretation.

Do not infer beyond source rows.

If source meaning matters, follow Raw URL back to the original md source.
