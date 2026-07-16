# term-card anchor enrichment plan — pass70

## status

pass: 70
role: anchor enrichment preparation plan
execution: false
final_definition: false

## objective

Prepare the first read-only anchor enrichment run for 13 committed term-card candidates.

## target cards

| order | card term       | file                                           | query term candidate                         |
| ----: | --------------- | ---------------------------------------------- | -------------------------------------------- |
|     1 | C               | `cards/C.term_card_candidate.md`               | `C`                                          |
|     2 | m               | `cards/m.term_card_candidate.md`               | `m`                                          |
|     3 | t               | `cards/t.term_card_candidate.md`               | `t`                                          |
|     4 | p               | `cards/p.term_card_candidate.md`               | `p`                                          |
|     5 | ?               | `cards/question_mark.term_card_candidate.md`   | `?`                                          |
|     6 | Ctp             | `cards/Ctp.term_card_candidate.md`             | `Ctp`                                        |
|     7 | Ctp24           | `cards/Ctp24.term_card_candidate.md`           | `Ctp24`                                      |
|     8 | Raw URL         | `cards/Raw_URL.term_card_candidate.md`         | `Raw URL`, `Raw`, `URL`, `raw_url`           |
|     9 | source identity | `cards/source_identity.term_card_candidate.md` | `source identity`, `source`, `identity`      |
|    10 | README baseline | `cards/README_baseline.term_card_candidate.md` | `README baseline`, `README`, `readme_source` |
|    11 | Seed.Base       | `cards/Seed_Base.term_card_candidate.md`       | `Seed.Base`                                  |
|    12 | Y_Branch        | `cards/Y_Branch.term_card_candidate.md`        | `Y_Branch`                                   |
|    13 | vocab.branch    | `cards/vocab_branch.term_card_candidate.md`    | `vocab.branch`                               |

## first enrichment output

The first execution pass should produce a runtime markdown report first:

```text
~/seungeflow_runtime/vocab_reader/term_card_anchor_enrichment_report_pass72.md
```

Then a GitHub summary report may be created later under:

```text
03_branch_fields/vocab/06_reports/
```

## recommended execution stages

### stage 1

Run batch read-only query and create runtime report.

### stage 2

Verify DB checksum before and after.

### stage 3

Review missing term matches.

### stage 4

Create GitHub summary report.

### stage 5

Only after review, update individual term-card files if needed.

## expected match notes

Likely exact matches:

```text
C
m
t
p
?
Ctp
Ctp24
Y_Branch
vocab.branch
Seed.Base
```

Possible partial or variant matches:

```text
Raw URL
source identity
README baseline
```

For phrase-based terms, do not force exact match.

Record exact or variant status clearly.

## guard

This plan prepares anchor enrichment.

It does not execute DB queries.

It does not modify cards.

It does not finalize term meaning.
