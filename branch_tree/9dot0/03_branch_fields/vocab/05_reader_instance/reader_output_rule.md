# Reader output rule

## status

pass: 31
role: AI DB reader output rule
db_modification: false

## purpose

This rule defines how read-only DB query results should be reported back to gpt.direct.

## required output fields

A reader query report should include:

- query mode
- query term or status
- DB path
- table/count summary when relevant
- selected rows
- Raw URL coordinates
- guard statement

## compactness rule

Return compact rows first.

Do not dump entire tables.

Default limit should be small.

Increase limit only when gpt.direct asks.

## source identity rule

Every context answer should preserve:

```text
repo | branch | commit | path | line_no | raw_url | context
```

## interpretation rule

The reader script returns DB rows.

It does not interpret final meaning.

Interpretation is performed by gpt.direct after checking source identity and guard.

## escalation rule

If the DB result is insufficient, use Raw URL or source path to inspect the original md source.

Do not guess from DB frequency alone.

## guard

DB output is derived evidence.

Original source remains the md file and Raw URL.
