---
license: mit
task_categories:
- question-answering
language:
- en
- zh
- ja
- ko
- fr
- th
- de
- es
- yo
tags:
- medical
- biology
- multilingual
- reasoning
size_categories:
- 1K<n<10K
configs:
- config_name: en
  default: true
  data_files:
  - split: test
    path: data/en/train-*.parquet
- config_name: zh
  data_files:
  - split: test
    path: data/zh/train-*.parquet
- config_name: ja
  data_files:
  - split: test
    path: data/ja/train-*.parquet
- config_name: ko
  data_files:
  - split: test
    path: data/ko/train-*.parquet
- config_name: fr
  data_files:
  - split: test
    path: data/fr/train-*.parquet
- config_name: th
  data_files:
  - split: test
    path: data/th/train-*.parquet
- config_name: de
  data_files:
  - split: test
    path: data/de/train-*.parquet
- config_name: es
  data_files:
  - split: test
    path: data/es/train-*.parquet
- config_name: yo
  data_files:
  - split: test
    path: data/yo/train-*.parquet
---

# HLE-BioMedX — Multilingual HLE Biology/Medicine

A multilingual version of the **Biology/Medicine** subset of *Humanity's Last Exam*
(HLE), released as one subset per language.

Source benchmark: [Humanity's Last Exam](https://lastexam.ai), dataset
[`cais/hle`](https://huggingface.co/datasets/cais/hle).

## Subsets

| Group | Languages | How the target-language text was produced |
|---|---|---|
| Source | `en` | Original English questions and answers. |
| **Machine-translated and expert-verified / revised** | `zh`, `ja`, `ko`, `fr`, `th` | Machine translation reviewed by a human expert, who verified and revised it. |
| **Machine-translated only** | `de`, `es`, `yo` | Machine translation, no human verification. |

Every subset contains the same **280 questions**, aligned by `id` and in the same
order, so subsets can be compared item by item.

## Fields

| column | description |
|---|---|
| `id` | original HLE question id — shared across all subsets |
| `question` | question text (original for `en`, translated otherwise) |
| `answer` | ground-truth answer (original for `en`, translated otherwise) |

Each `data/<subset>/` folder also contains a plain CSV copy of the same 280 rows
for convenience; the Hub loader below reads the parquet file.

## Loading

```python
from datasets import load_dataset

en = load_dataset("li-lab/HLE-BioMedX", "en")["test"]
zh = load_dataset("li-lab/HLE-BioMedX", "zh")["test"]
```

## Notes

- These questions were drawn from the text-only portion of the HLE
  Biology/Medicine category. A small number originally referred to an
  accompanying image; the image is not distributed here, so those items are
  answerable only from the text.
- One Japanese question (`6734b4befaf4e6eb454c1c92`) is missing and is stored as
  null; the corresponding English, Chinese, Korean, French, Thai, German,
  Spanish and Yoruba entries are present.

## Contributors

Contributors will be updated soon!
