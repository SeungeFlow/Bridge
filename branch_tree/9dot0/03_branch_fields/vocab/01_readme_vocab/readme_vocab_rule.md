# README vocab rule

## one-line rule

README.md words are the baseline vocab.

## why README.md

README.md is the surface where a Repo, Branch, or Directory explains itself.

Therefore README.md vocab is not random word frequency.
It is the representative vocabulary selected by that source-field.

## extraction rule

Do not start from all files.

Start from selected README.md files.

Then search other files through README-based vocab.

## missing term rule

If a needed structural term is not present in the relevant README.md, update the README.md first.

Do not silently add the term only to the DB.

## DB rule

The DB is a derived Seed.Base-like reader field.

It should not replace original md sources.

It should connect:

- word
- Raw URL
- repo
- branch
- commit
- path
- line context
- source role
- relation candidate

## term card rule

Not every word becomes an md file.

Only structural trigger terms become term cards.

A term card should contain:

- surface forms
- core meaning
- Ctp position candidate
- Raw URL source links
- relation candidates
- guard

## language rule

Korean, English, and Hanja are not separate silos.

A term may have:

- Korean surface
- Hanja layer
- English equivalent
- aliases
- source-field usage

## guard

vocab.branch is not a word list.

vocab.branch is the first branch-field that structurally decomposes the surface of thought.
