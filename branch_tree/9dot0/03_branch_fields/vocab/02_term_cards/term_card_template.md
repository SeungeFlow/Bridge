# term-card template

## status

term:
card_status: CANDIDATE
final_definition: false
source_scope:
created_from:
updated_by:

## 1. surface

```text
<term>
```

## 2. candidate role

Describe the role this term may play in vocab.branch.

Do not finalize meaning.

## 3. DB status

```text
status:
occurrence_count:
source_count:
```

## 4. README baseline presence

```text
readme_source_presence:
```

## 5. source identity rows

Each row should preserve:

```text
repo | branch | commit | path | line_no | raw_url
```

## 6. compact source context

Use compact context only.

Do not paste long source blocks.

## 7. structural role candidate

Examples:

```text
core_token_candidate
structural_trigger_candidate
source_identity_operator
README_baseline_operator
```

## 8. relation candidates

List only candidate relations.

Example:

```text
C ↔ m,t,p,?
Ctp ↔ Ctp24
Y_Branch ↔ source identity
Raw URL ↔ source coordinate
```

## 9. guard

This card is not a final definition.

This card is not final interpretation.

Original source remains in md files and Raw URLs.

## 10. next action

Possible next actions:

```text
query DB
inspect Raw URL
update README baseline
promote to individual term-card file
link to branch.market / branch.sohosa / branch.history
```
