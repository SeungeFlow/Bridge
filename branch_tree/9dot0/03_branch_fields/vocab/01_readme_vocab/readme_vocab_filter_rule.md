# README vocab filter rule v2

## status

pass: 10
role: README vocab filter rule
base_preview_report: 03_branch_fields/vocab/06_reports/readme_vocab_scan_preview_pass6.md
base_preview_commit: 00937b38ee3aa47030153649988ea17ce133e0a9

## why v2 exists

The first preview scan proved that the README-only scan works.

However, it also showed that common particles, grammatical words, plain numbers, and generic English words rise to the top.

This is not failure.

This is the first filter-improvement signal.

## v1 slippage examples

The following terms are useful as raw evidence but weak as structural triggers:

- text
- 는
- 를
- 은
- 이
- 의
- 것
- plain numbers such as 1, 2, 3, 4, 5, 6, 7
- generic markdown or prose words

## v2 goal

v2 should separate:

1. raw occurrence
2. filtered vocab candidate
3. structural trigger candidate

## structural trigger preference

A term becomes stronger when it is:

- present in README.md
- repeated across multiple README sources
- related to source identity
- related to Ctp / Ctp24 / S1-S4
- related to dot / diff / orbit / COG / 9dot0
- related to guard / relation / boundary / field
- related to branch names
- related to DB reader operation
- related to vocab.branch itself
- written as a path-like or source-like term
- written as a mixed structural token such as 9dot0, Ctp24, Y_Branch

## language policy

Do not separate Korean, English, and Hanja into silos.

A structural term may appear as:

- Korean surface
- English surface
- Hanja surface
- mixed token
- path token
- formula-like token

## particle/common-word policy

Remove or demote Korean particles and generic function words.

Examples:

- 은
- 는
- 이
- 가
- 을
- 를
- 의
- 와
- 과
- 에
- 로
- 으로
- 것
- 수
- 있다
- 아니다
- 않는다
- 먼저

These may remain in raw CSV, but should not rise in filtered structural candidate lists.

## numeric policy

Plain numbers should be demoted.

Exceptions:

- 0
- 9
- 9dot0
- Ctp24
- S1
- S2
- S3
- S4
- numbered schema/path tokens when attached to words

## report policy

v2 scan should produce:

- markdown summary report
- CSV occurrence report
- filtered structural candidate table
- demoted common-token table

## guard

v2 still does not create the final vocab DB.

v2 is only a better preview scanner.

The DB is a later pass.
