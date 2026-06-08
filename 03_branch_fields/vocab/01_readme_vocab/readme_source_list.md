# README vocab source list

## status

pass: 4
role: baseline README source list
commit_base_repo_9dot0: 3e9383c6a761f78fb5c68112c1b1e1549580bc85

## principle

README.md is the baseline vocab surface.

vocab.branch does not begin from whole-repository word extraction.  
vocab.branch begins from representative README.md vocab.

A README.md is treated as:

- branch entry surface
- representative observation surface
- vocab baseline
- source-role boundary

## source classes

### A. Repo.9Dot0 current branch-field README sources

These are the first local realization surfaces.

| repo | branch | commit | path | role |
|---|---|---:|---|---|
| SeungeFlow/9Dot0 | main | 3e9383c6a761f78fb5c68112c1b1e1549580bc85 | README.md | Repo.9Dot0 entry surface |
| SeungeFlow/9Dot0 | main | 3e9383c6a761f78fb5c68112c1b1e1549580bc85 | 03_branch_fields/market/README.md | branch.market surface |
| SeungeFlow/9Dot0 | main | 3e9383c6a761f78fb5c68112c1b1e1549580bc85 | 03_branch_fields/sohosa/README.md | branch.sohosa surface |
| SeungeFlow/9Dot0 | main | 3e9383c6a761f78fb5c68112c1b1e1549580bc85 | 03_branch_fields/history/README.md | branch.history surface |
| SeungeFlow/9Dot0 | main | 3e9383c6a761f78fb5c68112c1b1e1549580bc85 | 03_branch_fields/vocab/README.md | branch.vocab surface |

### B. Repo.SeungeFlow primary observer README sources

These README files are higher-order observer/source documents.

| repo | branch | commit | path | role |
|---|---|---:|---|---|
| SeungeFlow/SeungeFlow | Y_Branch | 32f8b248dc7e9ec5c1856b78b4ee207b8861d315 | README.md | source identity / Ctp / Ctp24 / S1-S4 / guard operating surface |
| SeungeFlow/SeungeFlow | main | 85802d707160da1a1cfb2bfacfe9cea222a3c77c | README.md | representative entry surface |
| SeungeFlow/SeungeFlow | first_flow | 1fa5f28ca7647da445a5b2ef130f3852845ccb68 | README.md | structure-body protection / original protection field |

### C. Repo.SeungeFlow functional branch README sources

These are not first baseline sources, but they support later function-layer expansion.

| repo | branch | commit | path | role |
|---|---|---:|---|---|
| SeungeFlow/SeungeFlow | seed_base | 76a6d52648dd5ff82b7532c3d9a53ee9046306a3 | README.md | Seed.Base entry surface |
| SeungeFlow/SeungeFlow | seed_base | 76a6d52648dd5ff82b7532c3d9a53ee9046306a3 | README_for_AI.md | AI reading support |
| SeungeFlow/SeungeFlow | seed_base | 76a6d52648dd5ff82b7532c3d9a53ee9046306a3 | README_of/README_of_SeungeFlow_Thinking.md | thinking_flow source boundary |
| SeungeFlow/SeungeFlow | seed_base | 76a6d52648dd5ff82b7532c3d9a53ee9046306a3 | README_of/README_of_Structure_Principle.md | schema source boundary |
| SeungeFlow/SeungeFlow | music_language | c2f5ffb30c8d603e70c6aaed3ba6c38e410fbccc | README.md | repetition / boundary / residue / slippage reading surface |
| SeungeFlow/SeungeFlow | rendering | f29dfd35a574641c39ebe243230a487ec1eaba22 | README.md | draw / cut / show surface |
| SeungeFlow/SeungeFlow | epluone | 882c06e5bceec8483b93c847ca8165f50a9c111e | BackData/10_capital_market_hints/README.md | capital market hint surface |
| SeungeFlow/SeungeFlow | epluone | 882c06e5bceec8483b93c847ca8165f50a9c111e | BackData/08_root_support/sohosa_hyangsa/README.md | sohosa / hyangsa root-support surface |

## raw URL rule

Raw URL format:

https://raw.githubusercontent.com/{owner}/{repo}/{commit}/{path}

Raw URL fixes source identity together with:

- repo
- branch
- commit hash
- path
- source status
- file role

## pass order

1. Fix README source list.
2. Extract README vocab only.
3. Normalize word forms.
4. Connect words to Raw URLs.
5. Store occurrence data in local SQLite/PostgreSQL.
6. Create term cards only for structural trigger terms.
7. Leave etymology/origin to later history branch expansion.

## guard

Do not treat this list as final.

This list is a first baseline for vocab.branch pass planning.
