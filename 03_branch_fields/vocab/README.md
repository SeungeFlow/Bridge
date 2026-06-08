# vocab.branch

## status

directory_branch_field: true
future_git_branch_candidate: vocab.branch
future_repo_candidate: true

## one-line definition

vocab.branch는 단어장이 아니다.  
vocab.branch는 생각의 표면을 구조적으로 해체하는 첫 branch-field이다.

## purpose

vocab.branch exists to make AI instances operate as DB readers.

It connects:

- README.md vocab
- words as structural triggers
- Raw URL source identity
- Repo / Branch / Directory / md file paths
- Ctp structure-operation reading
- Hunminjeongeum Haerye-based vector decomposition
- local SQLite / PostgreSQL reader index

## core principle

The minimal connectors between Repo, Branch, Directory, and md files are:

1. word
2. Raw URL

A word connects meaning.  
A Raw URL fixes source identity.

## not a word list

vocab.branch is not a vocabulary notebook.

It does not collect all words.  
It does not index the entire repository blindly.  
It does not treat Korean, English, and Hanja as separate silos.

## README.md as baseline

The vocabulary baseline comes from README.md files.

If a needed structural term is not present in the relevant README.md,  
the README.md must be updated first.

The DB is rebuilt or re-indexed from README vocab.

## AI reader

The final reader is an AI instance.

The AI reader should not load the whole repository into context.window.  
It should use vocab.branch and DB reports to select only necessary source files.

## phase-transition path

directory  
→ branch  
→ repo

This directory is the first place where the direction of vocab.branch is placed.
