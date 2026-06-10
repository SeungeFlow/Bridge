# Ctp / Ctp24 anchor update policy

## status

pass: 91
role: exact-matched Ctp/Ctp24 anchor update policy
card_update_execution: false
db_query_execution: false
term_card_finalization: false
base_commit_repo_9dot0: 9ba207e180af64b4321e0b985e86194d623bb0ae

## purpose

This policy defines how exact source anchors may later be added to the `Ctp` and `Ctp24` term-card candidates.

The target cards are:

```text
Ctp
Ctp24
```

## source basis

The basis is the PASS72 runtime anchor enrichment report and PASS75 exact-anchor review report.

PASS75 classified these cards as exact matched:

```text
Ctp
Ctp24
```

## position after core tuple

The first core tuple anchor cycle has already been completed:

```text
C
m
t
p
?
```

Ctp and Ctp24 are handled after the core tuple because they function as structure-operation / structure-filter names rather than the first tuple members themselves.

## update principle

Do not finalize card meaning.

Do not rewrite candidate interpretations.

Only add a controlled anchor section or anchor table.

The future card-update pass should preserve all existing candidate/guard language.

## allowed update shape

A future update may add a controlled section like this:

```markdown
## source anchors — PASS72 enrichment

## status

anchor_status: CANDIDATE_ENRICHED
anchor_source: PASS72 runtime anchor enrichment report
anchor_update_pass: <pass>
final_definition: false

## anchor rows

```text
term | status | repo | branch | commit | path | line_no | raw_url | context
...
```
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
1. Ctp
2. Ctp24
```

Reason:

```text
Ctp is the structural operation/formula name.
Ctp24 is the matrix/filter expansion name.
```

## guard

Anchor update strengthens traceability.

Anchor update does not finalize definition.

DB output is derived evidence.

Original source remains in md files and Raw URLs.
