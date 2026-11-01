---
dataset_info:
  features:
  - name: uid
    dtype: string
  - name: region_en
    dtype: string
  - name: language_code
    dtype: string
  - name: motivation_category
    dtype: string
  - name: article_local
    dtype: string
  - name: article_en
    dtype: string
  - name: seed_instruction_local
    dtype: string
  splits:
  - name: train
    num_bytes: 266839886
    num_examples: 242078
  - name: validation
    num_bytes: 33344457
    num_examples: 30240
  - name: test
    num_bytes: 33337068
    num_examples: 30240
  download_size: 184625868
  dataset_size: 333521411
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
license: cc-by-4.0
task_categories:
- text-generation
language:
- ar
- de
- el
- en
- es
- fr
- hi
- id
- it
- ja
- ko
- ms
- nl
- pl
- pt
- ro
- ru
- sv
- th
- tr
- uk
- vi
- zh
tags:
- safety
- jailbreak
- fake-news
- disinformation
- multilingual
- benchmark
pretty_name: JailNewsBench
size_categories:
- 100K<n<1M
---

# JailNewsBench

**JailNewsBench** is a large-scale multilingual benchmark for evaluating the robustness of large language models (LLMs) against **jailbreak-induced fake news generation**. Each instance pairs a real news article with a seed instruction designed to elicit harmful or malicious content from LLMs, framed as legitimate news writing.

This dataset accompanies the paper:

> **JailNewsBench: Multi-Lingual and Regional Benchmark for Fake News Generation under Jailbreak Attacks**
> Masahiro Kaneko, Ayana Niwa, Timothy Baldwin
> *The Fourteenth International Conference on Learning Representations (ICLR 2026)*
> [arXiv:2603.01291](https://arxiv.org/abs/2603.01291)

Code: [https://github.com/kanekomasahiro/jail_news_bench](https://github.com/kanekomasahiro/jail_news_bench)

---

## Overview

JailNewsBench spans **34 regions** and **22 languages**, covering **8 evaluation sub-metrics** via LLM-as-a-Judge and **5 jailbreak attack types**, with approximately **300k instances**.

Key findings from the paper:
- Maximum attack success rate (ASR) reached **86.3%**
- Maximum harmfulness score was **3.5 / 5.0**
- LLMs showed significantly weaker defenses for English and U.S.-related topics compared to other languages and regions

| Split      | Rows    |
|------------|---------|
| Train      | 242,078 |
| Validation | 30,240  |
| Test       | 30,240  |
| **Total**  | **302,558** |

---

## Data Fields

| Field | Type | Description |
|---|---|---|
| `uid` | string | Unique instance identifier |
| `region_en` | string | Region of the source news article (e.g., `Japan`, `Mexico`) |
| `language_code` | string | Language code of the local text (e.g., `ja`, `es`) |
| `motivation_category` | string | Malicious intent category: `Financial`, `Political`, `Social`, or `Psychological` |
| `article_local` | string | News article excerpt in the local language |
| `article_en` | string | English translation of the article excerpt |
| `seed_instruction_local` | string | Jailbreak seed instruction in the local language, grounded in the news article |

---

## Motivation Categories

| Category | Description |
|---|---|
| `Financial` | Instructions intended to cause financial harm (e.g., market manipulation, fraudulent promotion) |
| `Political` | Instructions aimed at undermining public trust in governments or political figures |
| `Social` | Instructions targeting social cohesion, reputation, or community relations |
| `Psychological` | Instructions designed to induce fear, anxiety, or psychological distress |

---

## Usage
```python
from datasets import load_dataset

dataset = load_dataset("MasahiroKaneko/JailNewsBench")

# Access test split
test = dataset["test"]
print(test[0])
```

---

## Intended Use

This dataset is intended **for research purposes only**, specifically for:

- Evaluating LLM safety and robustness against jailbreak attacks
- Developing and benchmarking jailbreak defenses
- Studying multilingual and cross-cultural dimensions of LLM safety

**The seed instructions in this dataset are malicious by design and must not be used to generate harmful content.**

---

## Citation
```bibtex
@inproceedings{kaneko2026jailnewsbench,
  title     = {JailNewsBench: Multi-Lingual and Regional Benchmark for Fake News Generation under Jailbreak Attacks},
  author    = {Masahiro Kaneko and Ayana Niwa and Timothy Baldwin},
  booktitle = {The Fourteenth International Conference on Learning Representations (ICLR)},
  year      = {2026},
  url       = {https://arxiv.org/abs/2603.01291}
}
```

---

## License

This dataset is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).