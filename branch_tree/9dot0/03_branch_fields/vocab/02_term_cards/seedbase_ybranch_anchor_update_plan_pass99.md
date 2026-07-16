# Seed.Base / Y_Branch anchor update plan — pass99

## status

pass: 99
role: plan for exact-anchor Seed.Base/Y_Branch card update batch
execution: false
term_card_finalization: false

## target batch

```text
Seed.Base
Y_Branch
```

## current committed cards

| order | term      | file                                                                          | PASS75 review status |
| ----: | --------- | ----------------------------------------------------------------------------- | -------------------- |
|     1 | Seed.Base | `03_branch_fields/vocab/02_term_cards/cards/Seed_Base.term_card_candidate.md` | exact matched        |
|     2 | Y_Branch  | `03_branch_fields/vocab/02_term_cards/cards/Y_Branch.term_card_candidate.md`  | exact matched        |

## prior completed batches

The first core tuple anchor update cycle has been completed:

| term | completed pass |
| ---- | -------------: |
| C    |         PASS80 |
| m    |         PASS82 |
| t    |         PASS84 |
| p    |         PASS86 |
| ?    |         PASS88 |

The Ctp/Ctp24 anchor update cycle has been completed:

| term  | completed pass |
| ----- | -------------: |
| Ctp   |         PASS94 |
| Ctp24 |         PASS96 |

## intended update

Each Seed.Base/Y_Branch card may later receive a controlled section:

```text
source anchors — PASS72 enrichment
```

This section should preserve:

```text
term
status
repo
branch
commit
path
line_no
raw_url
context
```

## update order

Recommended order:

```text
1. Seed.Base
2. Y_Branch
```

## first execution candidate

The next safe execution pass should update only Seed.Base first.

Then Y_Branch should be updated in a separate pass after review.

## source of anchor rows

Use PASS72 runtime report:

```text
/home/gogiseung/seungeflow_runtime/vocab_reader/term_card_anchor_enrichment_report_pass72.md
```

Do not rerun the DB query in the card-update pass unless explicitly instructed.

## expected guard after update

Each updated card must still say:

```text
This card is a candidate.
This card is not a final definition.
DB output is derived evidence.
Original source remains in md files and Raw URLs.
```

## not included

This plan does not update:

```text
Raw URL
source identity
README baseline
vocab.branch
```

Those require variant-aware review.

## stop conditions

Stop the update if:

```text
runtime report missing
anchor rows cannot be isolated
target card already has a PASS72 anchor section
git status contains non-target changes
DB/runtime files appear inside repo
```

## guard

This plan prepares card updates.

It does not execute card updates.

It does not finalize definitions.
