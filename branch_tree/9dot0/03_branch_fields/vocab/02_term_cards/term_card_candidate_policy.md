# term-card candidate policy

## status

pass: 40
role: term-card candidate policy
final_term_card: false
base_commit_repo_9dot0: 92f5c4e62fa41f0b69e6760df850935ededa3c5e

## purpose

This document defines how vocab.branch should create term-card candidates.

A term-card candidate is not a final definition.

It is a controlled source-linked surface for later structural interpretation.

## core principle

vocab.branch is not a vocabulary notebook.

```text
vocab.branch는 단어장이 아니라, 생각의 표면을 구조적으로 해체하는 첫 branch.
```

## minimal connector rule

Repo, Branch, Directory, and md files are connected by:

1. word
2. Raw URL

A word connects meaning.

A Raw URL fixes source identity.

## term-card candidate role

A term-card candidate should collect:

- term
- candidate status
- README baseline presence
- DB status
- source identity
- Raw URL coordinates
- compact source contexts
- structural role candidate
- guard

## not allowed

A term-card candidate must not claim:

- final definition
- final structural judgment
- branch completion
- source proof
- whole-repo coverage

## first source law

README.md remains the first vocabulary law.

If a needed structural term is missing from the relevant README.md, update the README.md first.

## DB relation

The SQLite DB is a derived reader field.

DB output can suggest candidate cards.

DB output does not finalize cards.

## first batch principle

The first batch should prioritize core tokens that allow later Ctp operation:

```text
C
m
t
p
?
Ctp
Ctp24
```

Then it should add source-identity operators:

```text
Y_Branch
Seed.Base
Raw URL
source identity
README baseline
```

## guard

Term-card candidate = controlled starting surface.

Term-card candidate ≠ final interpretation.
