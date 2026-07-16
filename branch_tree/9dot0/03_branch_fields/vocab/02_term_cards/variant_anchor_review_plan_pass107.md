# variant-aware anchor review plan — pass107

## status

pass: 107
role: plan for variant-aware anchor review
execution: false
term_card_finalization: false

## target batch

- Raw URL
- source identity
- README baseline
- vocab.branch

## current committed cards

| order | term            | file                                                                                | PASS75 review status        |
| ----: | --------------- | ----------------------------------------------------------------------------------- | --------------------------- |
|     1 | Raw URL         | `03_branch_fields/vocab/02_term_cards/cards/Raw_URL.term_card_candidate.md`         | variant matched             |
|     2 | source identity | `03_branch_fields/vocab/02_term_cards/cards/source_identity.term_card_candidate.md` | variant / component matched |
|     3 | README baseline | `03_branch_fields/vocab/02_term_cards/cards/README_baseline.term_card_candidate.md` | variant / component matched |
|     4 | vocab.branch    | `03_branch_fields/vocab/02_term_cards/cards/vocab_branch.term_card_candidate.md`    | review before card update   |

## completed exact anchor cycles

- C / m / t / p / ?
- Ctp / Ctp24
- Seed.Base / Y_Branch

## intended review output

The next review pass should produce a markdown review report before card updates.

Recommended report path:

03_branch_fields/vocab/06_reports/variant_anchor_review_report_pass108.md

## review table shape

Each target card should be reviewed with a table like:

card | query term | row term | variant_status | accept_for_card_update | reason

## review classes

- EXACT_PHRASE
- VALID_COMPONENT
- CONTEXTUAL_BRANCH_MATCH
- AMBIGUOUS
- REJECT

## source of review rows

Use PASS72 runtime report:

/home/gogiseung/seungeflow_runtime/vocab_reader/term_card_anchor_enrichment_report_pass72.md

Do not rerun the DB query unless explicitly instructed.

## recommended execution sequence

### stage 1

Create variant anchor review report.

### stage 2

Commit variant anchor review report.

### stage 3

Update variant cards one at a time only after review.

Recommended future order:

1. Raw URL
2. source identity
3. README baseline
4. vocab.branch

## stop conditions

Stop the review if:

- runtime report missing
- target card already has a PASS72 anchor section
- variant rows cannot be isolated
- git status contains non-target changes
- DB/runtime files appear inside repo

## not included

This plan does not update any card files.

This plan does not finalize any term meaning.

## guard

This plan prepares variant-aware review.

It does not execute card updates.

It does not finalize definitions.
