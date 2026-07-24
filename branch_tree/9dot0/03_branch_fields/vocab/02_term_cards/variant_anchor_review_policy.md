# variant-aware anchor review policy

## status

pass: 107
role: variant-aware anchor review policy
card_update_execution: false
db_query_execution: false
term_card_finalization: false
base_commit_repo_9dot0: 192fcb173a839ba1879034731953ce27d89b144c

## purpose

This policy defines how the remaining variant-aware term-card candidates should be reviewed before anchor insertion.

Target cards:

- Raw URL
- source identity
- README baseline
- vocab.branch

## source basis

The basis is the PASS72 runtime anchor enrichment report and PASS75 exact-anchor review report.

PASS75 identified these cards as requiring variant-aware review before individual card update.

## why variant-aware review is required

Some card surfaces are conceptual phrases, file/field labels, or branch names rather than simple exact DB terms.

Examples:

- Raw URL
- source identity
- README baseline
- vocab.branch

These may be represented in the DB by component rows or related token variants such as:

- Raw
- URL
- source
- identity
- README
- readme_source
- vocab
- branch

## review principle

Do not insert variant anchors directly.

First classify rows into:

- valid structural anchor
- component-only anchor
- ambiguous anchor
- reject

## no invention rule

Do not invent anchors.

Do not infer a raw URL if the runtime row does not provide one.

Do not treat a component token as full phrase evidence unless the relation is explicitly justified.

## allowed future update shape

A future card update may add a controlled section only after review:

section title: source anchors — PASS72 enrichment

table columns:

term | variant_status | repo | branch | commit | path | line_no | raw_url | context

## forbidden update shape

Do not add:

- final_definition: true
- FINAL
- confirmed meaning
- proof
- branch completion

## recommended review order

1. Raw URL
2. source identity
3. README baseline
4. vocab.branch

## guard

Variant-aware review strengthens traceability.

Variant-aware review does not finalize definitions.

DB output is derived evidence.

Original source remains in md files and Raw URLs.
