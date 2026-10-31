---
license: apache-2.0
task_categories:
- text-classification
language:
- vi
- ko
pretty_name: julia-1-swe training and evaluation data
size_categories:
- 10K<n<100K
tags:
- synthetic
- ticket-triage
- sdlc
- multilingual
- zorch
configs:
- config_name: default
  data_files:
  - {split: train, path: data/train_union/train.jsonl}
  - {split: validation, path: data/train_union/validation.jsonl}
- config_name: eval_tasks
  data_files:
  - {split: r118, path: data/eval_tasks/r118.jsonl}
  - {split: r119, path: data/eval_tasks/r119.jsonl}
  - {split: r121, path: data/eval_tasks/r121.jsonl}
- config_name: r118
  data_files:
  - {split: train, path: data/r118/train.jsonl}
  - {split: validation, path: data/r118/validation.jsonl}
  - {split: validation_hard, path: data/r118/validation_hard.jsonl}
- config_name: r119
  data_files:
  - {split: validation, path: data/r119/validation.jsonl}
  - {split: validation_hard, path: data/r119/validation_hard.jsonl}
- config_name: r120
  data_files:
  - {split: train, path: data/r120/train.jsonl}
  - {split: augmentation, path: data/r120/augmentation.jsonl}
- config_name: r121
  data_files:
  - {split: validation, path: data/r121/validation.jsonl}
  - {split: validation_hard, path: data/r121/validation_hard.jsonl}
- config_name: r122
  data_files:
  - {split: train, path: data/r122/train.jsonl}
  - {split: augmentation, path: data/r122/augmentation.jsonl}
- config_name: r126
  data_files:
  - {split: train, path: data/r126/train.jsonl}
  - {split: augmentation, path: data/r126/augmentation.jsonl}
- config_name: r132
  data_files:
  - {split: train, path: data/r132/train.jsonl}
  - {split: augmentation, path: data/r132/augmentation.jsonl}
- config_name: r133
  data_files:
  - {split: train, path: data/r133/train.jsonl}
  - {split: augmentation, path: data/r133/augmentation.jsonl}
- config_name: r134
  data_files:
  - {split: train, path: data/r134/train.jsonl}
  - {split: augmentation, path: data/r134/augmentation.jsonl}
---

# julia-1-swe-data

The exact training and evaluation data for [niko0xdev/julia-1-swe](https://huggingface.co/niko0xdev/julia-1-swe), a Zorch SDLC ticket triage model with three classification heads: **role**, **action** and **risk**. All data is synthetic: generated Vietnamese (with and without diacritics) and Korean ticket titles. No real tickets were used.

The rows come from the `data/v3/noisy_vi_ko_compositional_r118` to `r134` rounds of the [julia-1-zorch](https://github.com/niko0xdev/julia-1-zorch) repository.

## What was used for julia-1-swe

| Config / split | Rows | Used for julia-1-swe |
|---|---|---|
| `default` / `train` | 63,324 | **Training** (R134 `train.jsonl` + R126 `augmentation.jsonl`, deduplicated) |
| `default` / `validation` | 3,564 | **Validation and checkpoint selection** (R118 + R119 + R121 `validation_hard`, 1,188 tasks x 3 heads) |
| `eval_tasks` / `r118`, `r119`, `r121` | 396 each | **Reported evaluation** (task-level, exact match over all three heads) |

The training union was built with `data/train_union/build_latest_union.py` (copied from `scripts/linux/build_latest_union.py`). It concatenates R134 `train.jsonl` (50,670 rows) and R126 `augmentation.jsonl` (12,672 rows), drops exact duplicates on (state, question, target), and removes any row whose normalized title appears in the evaluation sets (0 were removed). Result: 63,324 rows from 21,108 tickets.

## Per-round configs

Each round is also provided on its own. "Contained in training" was checked by exact match of (state, question, target) against `default/train`.

| Config | Split | Rows | Contained in julia-1-swe training | Description |
|---|---|---|---|---|
| `r118` | train | 9,504 | Yes (100% of unique rows) | Base compositional training split (1,584 tasks, two title forms each) |
| `r118` | validation | 1,188 | No (evaluation) | 396 held-out label combinations |
| `r118` | validation_hard | 1,188 | No (evaluation) | Same rows as `validation`, used by the trainer interface |
| `r119` | validation | 1,188 | No (evaluation) | Holdout |
| `r119` | validation_hard | 1,188 | No (evaluation) | Same rows as `validation` |
| `r120` | train | 23,760 | Yes (100%) | R118 train plus compact, reordered, noisy augmentation |
| `r120` | augmentation | 14,256 | Yes (100%) | R120 augmentation rows only |
| `r121` | validation | 1,188 | No (evaluation) | Holdout with an explicit risk cue in every title |
| `r121` | validation_hard | 1,188 | No (evaluation) | Same rows as `validation` |
| `r122` | train | 37,998 | Yes (100%) | R120 train plus action-focused short titles |
| `r122` | augmentation | 14,238 | Yes (100%) | R122 augmentation rows only |
| `r126` | train | 50,670 | Yes (100%) | R122 train plus informal no-diacritic Vietnamese |
| `r126` | augmentation | 12,672 | **Yes, directly** | R126 augmentation rows only (part of the union) |
| `r132` | train | 41,166 | Yes (100%) | R122 train plus Korean `업무:` context titles |
| `r132` | augmentation | 3,168 | Yes (100%) | R132 augmentation rows only |
| `r133` | train | 47,502 | Yes (100%) | R122 train plus explicit-risk titles in holdout style |
| `r133` | augmentation | 9,504 | Yes (100%) | R133 augmentation rows only |
| `r134` | train | 50,670 | **Yes, directly** | R122 train plus R132 and R133 augmentations (part of the union) |
| `r134` | augmentation | 12,672 | Yes (100%) | R132 and R133 augmentation rows only |

The training rounds are cumulative, so every training or augmentation file from R118 to R134 is a subset of `default/train`. None of the R118, R119 or R121 validation rows appear in training. Each round folder also has its `stats.json` and, where available, the generator notes as `NOTES.md`. Rounds R123 to R125 and R127 to R131 are not in the repository.

## Data structure

### Head rows (`default` and per-round configs)

One row per ticket per head:

```json
{"meta": {"decision": "role", "language": "vi", "scenario_id": "r118-vi-product-implement-normal-v0",
          "source": "synthetic_compositional_r118", "style": "shared_vocabulary_train", "variant": "paraphrase_0"},
 "options": ["product", "business_analysis", "research", "design", "frontend", "mobile", "backend", "data", "ai", "qa", "devops", "security"],
 "question": "Which role should own this task?",
 "state": {"title": "làm mới quy tắc gói cước cho khách hàng mới"},
 "target": 0, "type": "choice"}
```

| Field | Description |
|---|---|
| `state.title` | Ticket title (the only input field in this data) |
| `question` | Head question: role, action or risk (see Labels) |
| `options` | Label list for the head |
| `target` | Index of the correct label in `options` |
| `type` | Always `choice` |
| `meta.decision` | Head: `role`, `action` or `risk` |
| `meta.language` | `vi`, `vi_nodiac` (Vietnamese without diacritics) or `ko` |
| `meta.scenario_id` | Generated scenario id (encodes round, language and labels) |
| `meta.source` | Generator round |
| `meta.style`, `meta.variant` | Title style and paraphrase variant |

### Task rows (`eval_tasks`)

One row per ticket with all three expected labels:

```json
{"expected": {"action": "implement", "risk": "security", "role": "product"},
 "meta": {"lang": "vi", "source": "synthetic_compositional_r118", "style": "shared_vocabulary_holdout"},
 "task": {"id": "r118-vi-product-implement-security", "title": "quy tắc gói cước cho khách hàng mới: làm mới bảo vệ tài khoản"}}
```

## Labels

| Head | Question | Labels |
|---|---|---|
| role (12) | Which role should own this task? | product, business_analysis, research, design, frontend, mobile, backend, data, ai, qa, devops, security |
| action (11) | What kind of work is this task? | implement, document, fix, test, research, review, analyze, investigate, design, deploy, refactor |
| risk (5) | What is the main risk category of this task? | normal, production, security, data_sensitive, architecture |

### Label counts (tickets per label, `default` config)

| role | train | validation |
|---|---|---|
| devops | 1,848 | 81 |
| design | 1,840 | 69 |
| business_analysis | 1,814 | 87 |
| qa | 1,808 | 93 |
| mobile | 1,778 | 96 |
| data | 1,760 | 99 |
| research | 1,757 | 96 |
| ai | 1,745 | 111 |
| backend | 1,729 | 102 |
| product | 1,713 | 111 |
| security | 1,665 | 123 |
| frontend | 1,651 | 120 |

| action | train | validation |
|---|---|---|
| fix | 2,086 | 69 |
| design | 2,044 | 72 |
| refactor | 1,956 | 102 |
| deploy | 1,952 | 105 |
| test | 1,914 | 111 |
| investigate | 1,900 | 111 |
| implement | 1,868 | 120 |
| research | 1,867 | 117 |
| analyze | 1,862 | 123 |
| review | 1,860 | 126 |
| document | 1,799 | 132 |

| risk | train | validation |
|---|---|---|
| production | 4,266 | 234 |
| architecture | 4,226 | 243 |
| security | 4,212 | 237 |
| data_sensitive | 4,208 | 240 |
| normal | 4,196 | 234 |

### Language split (head rows)

| Language | train | validation |
|---|---|---|
| vi_nodiac (Vietnamese without diacritics) | 28,494 | 1,188 |
| ko | 18,990 | 1,188 |
| vi | 15,840 | 1,188 |

Each `eval_tasks` split has 132 tasks per language.

### Styles in `default`

Train: compact_noisy_composition 14,256; action_focused_short 14,235; no_diacritic_short_noisy 12,672; explicit_risk_holdout_style 9,504; shared_vocabulary_train 9,489; shared_korean_work_context 3,168. Validation: shared_vocabulary_holdout (R118), reordered_shared_vocabulary (R119), explicit_risk_holdout (R121), 1,188 rows each.

## How the data was created

- **R118** generates titles from shared role, action and risk phrase banks in three language forms, then holds out 20% of the label combinations per language for validation (seed 20261118). Every phrase cue used in validation also occurs in training.
- **R119** is a separate holdout in a reordered shared-vocabulary style (seed 20261119).
- **R121** is a holdout on the combinations reserved by R118, with titles not present in the R120 training file. Every title carries an explicit risk cue (seed 20261121).
- **R120, R122, R126, R132, R133, R134** are training-only augmentations that use only R118 training combinations: compact and noisy titles (R120), action-focused short titles (R122), informal no-diacritic Vietnamese with abbreviations and typos (R126), Korean `업무:` context (R132), explicit-risk titles in the R121 separator style (R133), and R132 + R133 together (R134).
- Per the generator notes, no real tickets or real test examples were read during generation.
- Of the 315 label combinations in the evaluation sets, 308 also occur in the training union, according to `data/train_union/stats.json`.

## Intended use

- Reproducing or extending the julia-1-swe fine-tune.
- Benchmarking small multi-head triage classifiers on Vietnamese and Korean ticket titles.
- Not a measure of accuracy on real tickets.

## Limitations

- **Synthetic only.** Titles are generated from phrase banks. They are short, title-only inputs with no descriptions or acceptance criteria.
- **Train and evaluation come from the same generator family.** The evaluation sets share vocabulary and phrase cues with training and hold out label combinations, not vocabulary. Scores measure in-distribution compositional generalization. 308 of the 315 evaluation label combinations also appear in training.
- **Small evaluation sets.** 396 tasks per set, 1,188 in total.
- **No English.** Despite the base model supporting English, this data contains only Vietnamese and Korean.
- **Cumulative rounds.** Per-round training files overlap heavily. Do not combine them without deduplicating.

## Related

- Model: [niko0xdev/julia-1-swe](https://huggingface.co/niko0xdev/julia-1-swe)
- Code: [niko0xdev/julia-1-zorch](https://github.com/niko0xdev/julia-1-zorch)
- Related dataset with the same label schema (not used to train julia-1-swe): [niko0xdev/zorch-triage-dataset](https://huggingface.co/datasets/niko0xdev/zorch-triage-dataset)

## Citation

```bibtex
@misc{julia1swedata2026,
  title        = {julia-1-swe-data: Synthetic Vietnamese and Korean SDLC Ticket Triage Data},
  author       = {niko0xdev},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/datasets/niko0xdev/julia-1-swe-data}}
}
```
