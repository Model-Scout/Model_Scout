---
license: apache-2.0
task_categories:
- text-classification
language:
- en
- vi
- ko
pretty_name: Zorch Ticket Triage
size_categories:
- 1K<n<10K
tags:
- synthetic
- ticket-triage
- jira
- sdlc
- multilingual
configs:
- config_name: default
  data_files:
  - {split: train, path: prepared/train.jsonl}
  - {split: validation, path: prepared/val.jsonl}
  - {split: test, path: prepared/test.jsonl}
- config_name: short_with_meta
  data_files:
  - {split: train, path: prepared/with_meta/train.jsonl}
  - {split: validation, path: prepared/with_meta/val.jsonl}
  - {split: test, path: prepared/with_meta/test.jsonl}
- config_name: long
  data_files:
  - {split: train, path: prepared/long/train.jsonl}
  - {split: validation, path: prepared/long/val.jsonl}
  - {split: test, path: prepared/long/test.jsonl}
- config_name: long_with_meta
  data_files:
  - {split: train, path: prepared/long/with_meta/train.jsonl}
  - {split: validation, path: prepared/long/with_meta/val.jsonl}
  - {split: test, path: prepared/long/with_meta/test.jsonl}
- config_name: mixed
  data_files:
  - {split: train, path: prepared/long/mixed/train.jsonl}
  - {split: validation, path: prepared/long/mixed/val.jsonl}
  - {split: test, path: prepared/long/mixed/test.jsonl}
- config_name: raw
  data_files:
  - {split: train, path: train_split.jsonl}
  - {split: validation, path: val.jsonl}
- config_name: repo_format
  data_files:
  - {split: train, path: repo_format/train.jsonl}
  - {split: validation, path: repo_format/validation.jsonl}
---

# Zorch Ticket Triage

A synthetic, multilingual (English, Vietnamese, Korean) dataset for triaging software tickets in the Zorch SDLC orchestration setting. Each ticket gets three labels:

- **role**: which role should own the task
- **action**: what kind of work the task is
- **risk**: the main risk category of the task

All data is synthetic and template-generated. Names, tenants, URLs, emails and CVE ids are fictitious (`*.example`, `zorch.io`).

Related model: [niko0xdev/julia-1-swe](https://huggingface.co/niko0xdev/julia-1-swe), a Julia-1 based triage model with the same label schema. Note that `julia-1-swe` was fine-tuned on the separate R126/R134 compositional sets from the [julia-1-zorch](https://github.com/niko0xdev/julia-1-zorch) repository, not on the files in this dataset.

## Configurations and files

| Config | Files | train | validation | test | Format |
|---|---|---|---|---|---|
| `default` | `prepared/{train,val,test}.jsonl` | 1,536 | 196 | 196 | chat `messages`, short titles, deduplicated, leak-free |
| `short_with_meta` | `prepared/with_meta/*.jsonl` | 1,536 | 196 | 196 | same rows plus metadata |
| `long` | `prepared/long/*.jsonl` | 2,294 | 196 | 196 | chat `messages`, full ticket bodies |
| `long_with_meta` | `prepared/long/with_meta/*.jsonl` | 2,294 | 196 | 196 | same rows plus metadata |
| `mixed` | `prepared/long/mixed/*.jsonl` | 3,830 | 392 | 392 | short and long rows of the same split, shuffled |
| `raw` | `train_split.jsonl`, `val.jsonl` | 5,600 | 600 | | original generated rows (see Limitations: leaky split) |
| `repo_format` | `repo_format/*.jsonl` | 16,800 | 1,800 | | one row per head, built from `raw` |

Other files:

- `train.jsonl` (6,200 rows): all original source rows, equal to `train_split.jsonl` plus `val.jsonl`.
- `prepared/extras/train_all_copies.jsonl` and `train_all_copies_with_meta.jsonl` (4,640 rows): every source copy of the `default` train groups, differing only by the trailing `#number`.
- `labels.json`: the label schema.
- `prepared/prepare.py`, `prepared/long/build_long.py`, `prepared/long/long_pools.py`: scripts that rebuild the prepared and long variants. `prepared/stats.json` and `prepared/long/stats.json` hold counts and validation results.
- `prepared/README.md`, `prepared/long/README.md`: detailed build notes.

## Data structure

### Chat format (`default`, `long`, `mixed`)

```json
{"messages": [
  {"role": "system", "content": "You triage Zorch tickets into role, action, and risk labels."},
  {"role": "user", "content": "Ticket:\nCI pipeline returns 500 when tenant is null #676\n\nReturn JSON with keys role, action, risk."},
  {"role": "assistant", "content": "{\"role\": \"backend\", \"action\": \"fix\", \"risk\": \"production\"}"}
]}
```

### With metadata (`short_with_meta`)

```json
{"messages": [...], "text": "GraphQL gateway dbt 모델 #983", "lang": "ko",
 "labels": {"role": "data", "action": "implement", "risk": "data_sensitive"},
 "split": "train", "group_id": "13b6e9e60299", "template": "{C} dbt 모델", "n_copies_in_source": 3}
```

### Repo format (`repo_format`)

```json
{"state": {"title": "Review PR touching JWT rotation #5849"},
 "question": "Which role should own this task?", "type": "choice",
 "options": ["product", "business_analysis", "research", "design", "frontend", "mobile", "backend", "data", "ai", "qa", "devops", "security"],
 "target": 6,
 "meta": {"scenario_id": "zorch_triage_train-0", "decision": "role", "source": "zorch_triage_train"}}
```

### Fields

| Field | Description |
|---|---|
| `messages` | System, user and assistant turns. The assistant turn is the JSON label object. |
| `text` | Ticket title (short variant). |
| `lang` | `en`, `vi` or `ko`. |
| `labels` | Object with `role`, `action`, `risk`. |
| `split` | Split the row belongs to. |
| `group_id` | Id of the normalized-text group used for leak-free splitting. |
| `template` | Generator template (`{C}` is the component slot). |
| `n_copies_in_source` | Number of source copies collapsed into this row. |
| `seed_text`, `seed_group_id` | (long) Short record the long row was built from. |
| `accented` | (long) Whether Vietnamese text keeps diacritics. |
| `variant`, `title_used`, `style`, `sections` | (long) Build choices: formatting style and composed sections. |
| `target_tokens`, `user_tokens_qwen`, `total_tokens_qwen`, `total_tokens_llama` | (long) Length target and measured token counts. |
| `state` | (repo_format) Ticket fields, here only `title`. |
| `question`, `options`, `type` | (repo_format) Head question, label list, `choice`. |
| `target` | (repo_format) Index of the correct label in `options`. |
| `meta` | (repo_format) `scenario_id`, `decision` (head), `source`. |

## Labels

| Head | Labels |
|---|---|
| role (12) | product, business_analysis, research, design, frontend, mobile, backend, data, ai, qa, devops, security |
| action (11) | implement, document, fix, test, research, review, analyze, investigate, design, deploy, refactor |
| risk (5) | normal, production, security, data_sensitive, architecture |

### Distribution (`default` config)

| Language | train | validation | test |
|---|---|---|---|
| en | 1,121 | 143 | 143 |
| vi | 260 | 33 | 33 |
| ko | 155 | 20 | 20 |

| role | train | val | test |
|---|---|---|---|
| backend | 360 | 46 | 46 |
| frontend | 194 | 25 | 25 |
| devops | 158 | 20 | 20 |
| research | 137 | 17 | 17 |
| business_analysis | 125 | 16 | 16 |
| data | 123 | 16 | 16 |
| qa | 95 | 12 | 12 |
| mobile | 94 | 12 | 12 |
| security | 94 | 12 | 12 |
| product | 63 | 8 | 8 |
| ai | 63 | 8 | 8 |
| design | 30 | 4 | 4 |

| action | train | val | test |
|---|---|---|---|
| fix | 515 | 66 | 66 |
| implement | 193 | 25 | 25 |
| deploy | 158 | 20 | 20 |
| document | 125 | 16 | 16 |
| investigate | 125 | 16 | 16 |
| research | 106 | 13 | 13 |
| test | 95 | 12 | 12 |
| analyze | 95 | 12 | 12 |
| review | 62 | 8 | 8 |
| refactor | 32 | 4 | 4 |
| design | 30 | 4 | 4 |

| risk | train | val | test |
|---|---|---|---|
| normal | 666 | 85 | 85 |
| production | 453 | 58 | 58 |
| architecture | 200 | 25 | 25 |
| data_sensitive | 154 | 20 | 20 |
| security | 63 | 8 | 8 |

Source rows (`train.jsonl`, 6,200): en 4,375, vi 1,016, ko 809.

## How it was created

1. **Generation.** 6,200 source tickets from 38 title templates x 40 components (x 10 field slots for 5 templates). Role and action are fully determined by the template; risk by the template in about 94% of rows.
2. **Cleaning** (`prepared/prepare.py`). 382 rows (6.2%) carried a random, contradictory risk label and were dropped. The 5,818 clean rows were collapsed to 1,928 unique normalized texts (strip trailing `#number`, NFC, lowercase, collapse whitespace).
3. **Splitting.** About 80/10/10, stratified by template, seed 42, grouped so that no normalized text appears in more than one split. All labels and all 22 label combinations appear in every split.
4. **Long variant** (`prepared/long/build_long.py`). Each long row is seeded from one short record, keeps its label and split, and adds a full ticket body (about 200 to 1,500 Qwen tokens) assembled from hand-written sentence pools: description, repro steps, logs, acceptance criteria, comments and noise, in 5 formatting styles. About 70% of Vietnamese long rows keep diacritics.
5. **Repo format.** `raw` rows converted to one row per head for the julia-1-zorch trainer.

## Intended use

- Training and benchmarking small classifiers or SFT models for role / action / risk ticket triage.
- Testing robustness to long, noisy ticket bodies (`long`, `mixed`).
- Not a measure of real-world triage accuracy.

## Limitations and biases

- **Synthetic and templated.** Only 38 title templates, and every template appears in train, validation and test. Scores on these splits measure in-template generalization and will be near 100%. Evaluate on real tickets before trusting a model.
- **`raw` and `repo_format` are leaky.** 521 of 600 source validation rows (87%) share a normalized text with `train_split.jsonl`. Do not report results on these splits; use `default` or `long`.
- **Short Vietnamese has no diacritics.** None of the 1,016 Vietnamese source rows use accents, so models may underperform on accented Vietnamese (the long variant partly addresses this).
- **Class imbalance.** backend and fix dominate; design, refactor and risk=security are small (4 to 8 rows per class in validation and test).
- **Sentence pool artifacts** in the long variant, with smaller pools for vi and ko than for en.
- English dominates (about 73% of rows).

## Citation

```bibtex
@misc{zorchtriage2026,
  title        = {Zorch Ticket Triage: A Synthetic Multilingual Dataset for SDLC Ticket Routing},
  author       = {niko0xdev},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/datasets/niko0xdev/zorch-triage-dataset}}
}
```
