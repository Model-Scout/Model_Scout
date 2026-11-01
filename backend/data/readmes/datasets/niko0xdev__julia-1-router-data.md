---
license: apache-2.0
task_categories:
- text-classification
language:
- vi
- ko
- en
pretty_name: julia-1-router training and evaluation data
size_categories:
- 10K<n<100K
tags:
- synthetic
- model-routing
- llm-router
- multilingual
configs:
- config_name: default
  data_files:
  - {split: train, path: data/train.jsonl}
  - {split: dev, path: data/dev.jsonl}
  - {split: heldout_combo, path: data/heldout_combo.jsonl}
  - {split: heldout_style, path: data/heldout_style.jsonl}
- config_name: tasks
  data_files:
  - {split: train, path: data/train_tasks.jsonl}
  - {split: dev, path: data/dev_tasks.jsonl}
  - {split: heldout_combo, path: data/heldout_combo_tasks.jsonl}
  - {split: heldout_style, path: data/heldout_style_tasks.jsonl}
---

# julia-1-router-data

This is the synthetic training and evaluation data for [niko0xdev/julia-1-router](https://huggingface.co/niko0xdev/julia-1-router), a prompt router that picks one model tier: **small**, **medium**, **large** or **reasoning**. Prompts are in Vietnamese (with and without diacritics), Korean and English.

**All data is synthetic.** No real user prompts were used for training or evaluation, and the held-out sets are synthetic too.

**Current version: rt008.** This is the training mix that produced the published checkpoint that meets the synthetic gate (accuracy above 95% and under-routing below 2% on both held-out sets). The held-out files are byte-identical to the original rt001 held-outs and have never been edited.

## Splits

| Split | Prompts | Task families | Use |
|---|---|---|---|
| train | 60,000 | 174 | Training julia-1-router (rt008) |
| dev | 1,200 | 174 (same as train) | Checkpoint selection only (in-distribution) |
| heldout_combo | 1,200 | 20 held-out families | Evaluation: unseen families and unseen slot items, train-time styles |
| heldout_style | 1,200 | 20 held-out families | Evaluation: unseen families, unseen slot items and 5 unseen wrapper styles |

Each split is balanced across tiers (25% each). The language mix is vi 30%, vi_nodiac 25%, ko 25% and en 20%:

| Split | vi | vi_nodiac | ko | en |
|---|---|---|---|---|
| train | 18,000 | 15,000 | 15,000 | 12,000 |
| dev | 360 | 300 | 300 | 240 |
| heldout_combo | 360 | 300 | 300 | 240 |
| heldout_style | 360 | 300 | 300 | 240 |

| Tier | train | dev | heldout_combo | heldout_style |
|---|---|---|---|---|
| small | 15,000 | 300 | 300 | 300 |
| medium | 15,000 | 300 | 300 | 300 |
| large | 15,000 | 300 | 300 | 300 |
| reasoning | 15,000 | 300 | 300 | 300 |

## Configs and structure

`default` holds trainer rows in the [julia-1-zorch](https://github.com/niko0xdev/julia-1-zorch) format:

```json
{"state": {"title": "..."},
 "question": "Which model tier should handle this prompt?",
 "options": ["small", "medium", "large", "reasoning"], "type": "choice", "target": 3,
 "meta": {"decision": "route", "language": "vi", "family": "...", "style": "...",
          "split": "train", "scenario_id": "...", "source": "synthetic_router_rt008"}}
```

`tasks` holds the same prompts in task format for exact-match evaluation helpers.

## Held-out design (frozen since rt001)

- 20 families never used in training (5 per tier).
- Held-out 20% of every slot pool (topics, concepts, sentences, and so on).
- `heldout_style` wraps those prompts in 5 wrapper styles that never appear in training.
- Train/dev only use train families and train styles. Leak checks each round: family overlap, title overlap, style overlap, and (from later rounds) fulltext overlap and forbidden-motif filters.

## Iteration history

Train-only families were added across rt002 through rt008 from held-out error analysis. rt006 terse families were dropped after a regression. rt007/rt008 added Vietnamese-heavy boundary families and a forbidden-motif filter so train patterns stay away from held-out wording. Confidence-based escalate-one-tier was evaluated on train-side OOD/dev only and was not adopted for the published model.

Published model metrics on these held-outs (rt008 checkpoint): heldout_combo accuracy 98.42%, under-routing 0.17%; heldout_style accuracy 96.00%, under-routing 0.17%.

## License

Apache 2.0.
