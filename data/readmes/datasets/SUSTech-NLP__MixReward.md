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
  - nl
  - uk
  - sv
  - hi
  - fa
  - multilingual
tags:
  - reward-model
  - rlhf
  - preference
  - pairwise
  - multilingual
  - evaluation
pretty_name: "MixReward: Multilingual Preference Dataset"
size_categories:
  - 10K<n<100K
---

# MixReward: A Large-Scale Multilingual Preference Dataset

## Overview

**MixReward** is a large-scale, high-quality multilingual preference dataset comprising **64,528 examples** across **6 domains** and **103 languages**. It is designed to train unified reasoning reward models that support multiple evaluation paradigms (pairwise, listwise, and pointwise).

This dataset is introduced in the following paper, accepted at **ICML 2026** (the 43rd International Conference on Machine Learning):

> **UniRRM: Unified Reasoning Reward Models Across Languages and Evaluation Paradigms** [[Paper]](https://icml.cc/virtual/2026/poster/61930)

## Dataset Construction

MixReward is constructed through a rigorous four-stage pipeline:

1. **Data Curation**: Raw data from 9 high-quality community datasets are refined through hierarchical cleaning, including semantic density filtering (via InsTagger) and ensemble-based difficulty filtering for math tasks.
2. **Language Identification & Expansion**: FastText + large-scale reasoning model (Qwen3-235B) + human verification for language labeling. English data are translated into other languages using Gemini-2.5-Flash.
3. **Data Verification**: Qwen3-235B and GPT-OSS-120B serve as verifiers, screening data based on verification agreement rates with position-swapped evaluations.
4. **Format Unification**: Data are unified into pairwise format with chosen/rejected response pairs.

## Data Sources

| Source | Count | Percentage | Domain |
|--------|-------|------------|--------|
| translation | 21,469 | 33.3% | Multi-domain (translated) |
| ultrafeedback | 15,547 | 24.1% | Chat, Instruction Following |
| wildchat | 8,893 | 13.8% | Chat |
| PKU-SafeRLHF | 7,500 | 11.6% | Safety |
| MATH-500-Multilingual | 3,553 | 5.5% | Math |
| arena-human-preference | 2,768 | 4.3% | Chat, Instruction Following |
| HumanEval-XL-Python | 1,644 | 2.5% | Code |
| tulu-3-pref-personas-instruction-following | 1,450 | 2.2% | Instruction Following |
| math12k | 1,129 | 1.7% | Math |
| HelpSteer3 | 575 | 0.9% | Reasoning |

## Domain Distribution

| Domain | Count | Percentage |
|--------|-------|------------|
| Instruction Following | 13,186 | 20.4% |
| Code | 13,099 | 20.3% |
| Chat | 12,302 | 19.1% |
| Reasoning | 10,617 | 16.5% |
| Safety | 7,823 | 12.1% |
| Math | 7,501 | 11.6% |

## Language Coverage

The dataset covers **103 languages**, with the following top-10 distribution:

| Language | Count | Percentage |
|----------|-------|------------|
| English (en) | 20,961 | 32.5% |
| French (fr) | 4,546 | 7.0% |
| Spanish (es) | 4,169 | 6.5% |
| Italian (it) | 2,996 | 4.6% |
| German (de) | 2,869 | 4.4% |
| Russian (ru) | 1,897 | 2.9% |
| Turkish (tr) | 1,800 | 2.8% |
| Portuguese (pt) | 1,509 | 2.3% |
| Chinese (zh) | 1,463 | 2.3% |
| Polish (pl) | 1,176 | 1.8% |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | int | Unique sample identifier |
| `prompt` | string | The input prompt/query |
| `chosen` | string | The preferred (higher quality) response |
| `rejected` | string | The rejected (lower quality) response |
| `language` | string | ISO 639 language code |
| `domain` | string | Task domain (Chat, Code, Math, Reasoning, Safety, Instruction Following) |
| `data_source` | string | Original dataset source |
| `tags_num` | float | Number of semantic tags extracted by InsTagger (used for filtering) |

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("SUSTech-NLP/MixReward")

# Access a sample
sample = dataset["train"][0]
print(sample["prompt"])
print(sample["chosen"])
print(sample["rejected"])
```

## Statistics

- **Total samples**: 64,528
- **Languages**: 103
- **Domains**: 6
- **Format**: Pairwise (chosen/rejected)
- **Prompt length**: mean 520.5 chars, median 265 chars
- **Chosen length**: mean 1,214.7 chars, median 779 chars
- **Rejected length**: mean 888.8 chars, median 581 chars

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
