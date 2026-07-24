# README vocab core-token rule v3

## status

pass: 14
role: README vocab core-token rescue rule
base_filtered_preview_report: 03_branch_fields/vocab/06_reports/readme_vocab_scan_filtered_preview_pass10.md
base_filtered_preview_commit: 7aba83cd9b3ae0461e9dafd7a38a63b509c8d8eb

## why v3 exists

v2 improved structural vocab extraction.

However, v2 demoted several short tokens that are structurally important inside Repo.SeungeFlow / Repo.9Dot0:

- C
- m
- t
- p
- ?
- S
- A
- Path
- Core

These tokens are short, but they are not always common words.

In this workflow, they may be core structural operators.

## core-token principle

Shortness is not enough reason to demote a token.

A token may be structurally important if it appears as:

- C=(m,t,p,?)
- C=tp
- Ctp
- Ctp24
- S1 / S2 / S3 / S4
- S₁ / S₂ / S₃ / S₄
- Axis Selection
- Path
- Core
- dot / diff / orbit / COG / 9dot0
- source identity / guard / relation context

## exact core tokens

The following exact tokens must be rescued:

- C
- m
- t
- p
- ?
- S
- A
- Path
- Core

## context-sensitive rescue

A short token is stronger when the line contains:

- Ctp
- Ctp24
- C=(m,t,p,?)
- C=tp
- source identity
- guard
- relation
- field
- boundary
- Axis
- Selection
- Path
- Core
- S1
- S2
- S3
- S4
- 9dot0

## category model

v3 should separate tokens into:

1. raw_occurrence
2. demoted_common
3. filtered_candidate
4. core_token_candidate
5. structural_trigger_candidate

## no overpromotion

Rescuing C / m / t / p does not mean final interpretation.

It only keeps them visible for AI DB reader inspection.

## report policy

v3 scan should produce:

- markdown summary report
- CSV occurrence report
- top structural trigger candidates
- top core token candidates
- top demoted common tokens

## guard

v3 is not a DB build.

v3 is still a selected README-only preview scanner.
