# core tuple anchor update plan — pass77

## status

pass: 77
role: plan for first exact-anchor card update batch
execution: false
term_card_finalization: false

## target batch

```text
C
m
t
p
?
```

## current committed cards

| order | term | file                                                                              | PASS75 review status |
| ----: | ---- | --------------------------------------------------------------------------------- | -------------------- |
|     1 | C    | `03_branch_fields/vocab/02_term_cards/cards/C.term_card_candidate.md`             | exact matched        |
|     2 | m    | `03_branch_fields/vocab/02_term_cards/cards/m.term_card_candidate.md`             | exact matched        |
|     3 | t    | `03_branch_fields/vocab/02_term_cards/cards/t.term_card_candidate.md`             | exact matched        |
|     4 | p    | `03_branch_fields/vocab/02_term_cards/cards/p.term_card_candidate.md`             | exact matched        |
|     5 | ?    | `03_branch_fields/vocab/02_term_cards/cards/question_mark.term_card_candidate.md` | exact matched        |

## intended update

Each card may later receive a new controlled section:

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
1. C
2. m
3. t
4. p
5. ?
```

Reason:

```text
C is the formed-state anchor.
m/t/p/? are internal tuple members.
```

## first execution candidate

The next safe execution pass may update only C first.

Alternative:

Update all five in one batch only if the anchor rows are already compact and reviewed.

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
Ctp
Ctp24
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
