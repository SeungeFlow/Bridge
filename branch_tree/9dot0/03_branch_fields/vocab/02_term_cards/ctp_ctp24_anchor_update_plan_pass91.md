# Ctp / Ctp24 anchor update plan — pass91

## status

pass: 91
role: plan for exact-anchor Ctp/Ctp24 card update batch
execution: false
term_card_finalization: false

## target batch

```text
Ctp
Ctp24
```

## current committed cards

| order | term  | file                                                                      | PASS75 review status |
| ----: | ----- | ------------------------------------------------------------------------- | -------------------- |
|     1 | Ctp   | `03_branch_fields/vocab/02_term_cards/cards/Ctp.term_card_candidate.md`   | exact matched        |
|     2 | Ctp24 | `03_branch_fields/vocab/02_term_cards/cards/Ctp24.term_card_candidate.md` | exact matched        |

## prior completed batch

The first core tuple anchor update cycle has been completed:

| term | completed pass |
| ---- | -------------: |
| C    |         PASS80 |
| m    |         PASS82 |
| t    |         PASS84 |
| p    |         PASS86 |
| ?    |         PASS88 |

## intended update

Each Ctp/Ctp24 card may later receive a controlled section:

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
1. Ctp
2. Ctp24
```

## first execution candidate

The next safe execution pass should update only Ctp first.

Then Ctp24 should be updated in a separate pass after review.

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
Seed.Base
Y_Branch
vocab.branch
```

Those may be handled in later batches.

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
