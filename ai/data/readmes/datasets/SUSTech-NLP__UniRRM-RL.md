---
license: apache-2.0
task_categories:
  - text-generation
  - text-classification
language:
  - en
  - fr
  - es
  - it
  - de
  - ru
  - tr
  - pt
  - zh
  - pl
  - ar
  - ko
  - ja
  - id
  - vi
  - multilingual
tags:
  - reward-model
  - reinforcement-learning
  - grpo
  - reasoning
  - multilingual
  - evaluation
  - pairwise
  - listwise
pretty_name: "UniRRM-RL: Reinforcement Learning Data for Unified Reasoning Reward Model"
size_categories:
  - 10K<n<100K
---

# UniRRM-RL: Reinforcement Learning Data for Unified Reasoning Reward Models

## Overview

**UniRRM-RL** is the reinforcement learning (RL) dataset used in the second training stage of UniRRM, a Unified Reasoning Reward Model. It contains **32,832 samples** in a hybrid format combining both **pairwise** (chosen/rejected) and **listwise** (ABCD four-choice) evaluation paradigms, covering **106 languages** and multiple domains.

This dataset is introduced in the following paper, accepted at **ICML 2026** (the 43rd International Conference on Machine Learning):

> **UniRRM: Unified Reasoning Reward Models Across Languages and Evaluation Paradigms** [[Paper]](https://icml.cc/virtual/2026/poster/61930)

## Dataset Construction

The RL dataset is derived from [MixReward](https://huggingface.co/datasets/SUSTech-NLP/MixReward) and further processed to support GRPO-based reinforcement learning:

1. **Pairwise Data** (59.6%): Traditional chosen/rejected preference pairs from MixReward.
2. **Listwise Data** (40.4%): Four candidate responses (A/B/C/D) with a ground-truth label indicating the best response, enabling multi-candidate evaluation training.

## RL Training with GRPO

While SFT establishes the basic reasoning structure, the RL stage further optimizes the model using **Group Relative Policy Optimization (GRPO)** with a composite reward signal:

- **Format Reward (𝑟_fmt)**: Ensures structured output compliance (analysis → rubrics → evaluation → scores → judgment).
- **Outcome Consistency Reward (𝑟_acc)**: Binary reward measuring alignment between predicted judgment and ground-truth label.
- **Rubric Quality Reward (𝑟_rubric)**: A teacher model assigns a scalar quality score (1–5) evaluating the relevance, specificity, and comprehensiveness of generated rubrics.

The final reward is: `R_total = 0.8 × r_fmt + 0.15 × r_acc + 0.05 × r_rubric`

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | float | Sample identifier |
| `prompt` | string | The input prompt/query |
| `chosen` | string \| null | Preferred response (pairwise format, null for listwise) |
| `rejected` | string \| null | Rejected response (pairwise format, null for listwise) |
| `language` | string | ISO 639 language code |
| `domain` | string \| null | Task domain (Chat, Code, Math, Reasoning, Safety, Instruction Following) |
| `data_source` | string | Original dataset source |
| `tags_num` | float | Number of semantic tags |
| `responseA` | string \| null | Candidate response A (listwise format, null for pairwise) |
| `responseB` | string \| null | Candidate response B (listwise format, null for pairwise) |
| `responseC` | string \| null | Candidate response C (listwise format, null for pairwise) |
| `responseD` | string \| null | Candidate response D (listwise format, null for pairwise) |
| `ground_truth` | string \| null | Best response label: A/B/C/D (listwise format, null for pairwise) |

## Two Data Formats

### Pairwise Format (19,582 samples, 59.6%)
Samples with `chosen` and `rejected` fields populated, `responseA-D` and `ground_truth` are null.

### Listwise Format (13,250 samples, 40.4%)
Samples with `responseA`, `responseB`, `responseC`, `responseD`, and `ground_truth` populated, `chosen` and `rejected` are null.

**Ground-truth distribution (listwise)**:

| Label | Count | Percentage |
|-------|-------|------------|
| A | 3,967 | 29.9% |
| B | 3,303 | 24.9% |
| C | 3,091 | 23.3% |
| D | 2,889 | 21.8% |

## Domain Distribution

| Domain | Count | Percentage |
|--------|-------|------------|
| Safety | 5,806 | 17.7% |
| Instruction Following | 5,111 | 15.6% |
| Chat | 4,974 | 15.1% |
| Code | 4,848 | 14.8% |
| Reasoning | 4,275 | 13.0% |
| Math | 2,181 | 6.6% |

## Language Coverage

The dataset covers **106 languages**, with the top-10:

| Language | Count | Percentage |
|----------|-------|------------|
| English (en) | 8,879 | 27.0% |
| French (fr) | 2,396 | 7.3% |
| Spanish (es) | 2,363 | 7.2% |
| German (de) | 1,889 | 5.8% |
| Italian (it) | 1,815 | 5.5% |
| Russian (ru) | 1,118 | 3.4% |
| Chinese (zh) | 1,075 | 3.3% |
| Turkish (tr) | 862 | 2.6% |
| Polish (pl) | 842 | 2.6% |
| Portuguese (pt) | 772 | 2.4% |

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("SUSTech-NLP/UniRRM-RL")

# Filter pairwise samples
pairwise = dataset["train"].filter(lambda x: x["chosen"] is not None)

# Filter listwise samples
listwise = dataset["train"].filter(lambda x: x["responseA"] is not None)

print(f"Pairwise: {len(pairwise)}, Listwise: {len(listwise)}")
```

## Related Datasets

- [**MixReward**](https://huggingface.co/datasets/SUSTech-NLP/MixReward): The source multilingual preference dataset (64,528 samples, 103 languages, 6 domains)
- [**UniRRM-SFT**](https://huggingface.co/datasets/SUSTech-NLP/UniRRM-SFT): The SFT dataset for the first training stage

## Training Pipeline

UniRRM uses a two-stage training pipeline:

1. **Stage 1 - SFT** ([UniRRM-SFT](https://huggingface.co/datasets/SUSTech-NLP/UniRRM-SFT)): Initializes the model with structured reasoning capabilities.
2. **Stage 2 - RL** (this dataset): Further optimizes the model using GRPO with composite rewards for format compliance, outcome consistency, and rubric quality.

## Citation

```bibtex
@inproceedings{
lai2026unirrm,
title={Uni{RRM}: Unified Reasoning Reward Models Across Languages and Evaluation Paradigms},
author={Peng Lai and Yichao Du and Junchao Wu and Weibo Gao and Linan Yue and Longyue Wang and Weihua Luo and Derek F. Wong and Guanhua Chen},
booktitle={Forty-third International Conference on Machine Learning},
year={2026},
url={https://openreview.net/forum?id=laiK6TlhL2}
}
```

## License

This dataset is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
