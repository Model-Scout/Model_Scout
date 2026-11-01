---
license: cc-by-4.0
language:
- ko
- en
multilinguality:
- multilingual
task_categories:
- question-answering
- text-generation
tags:
- maplestory
- maplestory-worlds
- game-development
- qa
- synthetic
- instruction
size_categories:
- 100K<n<1M
pretty_name: MapleStory Worlds Creator QA
configs:
- config_name: ko
  data_files:
  - split: train
    path: data/ko/train-*.parquet
- config_name: en
  data_files:
  - split: train
    path: data/en/train-*.parquet
---

# MapleStory Worlds Creator QA

Synthetic question-answer dataset built from the official
[MapleStory Worlds](https://maplestoryworlds-creators.nexon.com) Creator Center
documentation. Questions are generated to be self-contained and grounded in the
source docs; answers avoid source/meta references so they read like an expert
explanation. Some QA pairs are **composed from multiple related documents**
(see `combo_sources`).

Parallel Korean/English. Intended for instruction tuning, QA, and retrieval.

## Composition

| config | Rows |
|--------|------|
| `ko`   | 61908 |
| `en`   | 38194 |
| Total  | 100102 |

Multi-document (composite) QA: 69256. Question types: {'how_to': 32407, 'property': 21504, 'constraint': 12865, 'comparison': 11961, 'definition': 11868, 'usage': 9497}.

## Usage

```python
from datasets import load_dataset

# Korean only
ds_ko = load_dataset("msw-ai-tf/maplestory-worlds-creator-qa", "ko", split="train")

# English only
ds_en = load_dataset("msw-ai-tf/maplestory-worlds-creator-qa", "en", split="train")

# Combine both
from datasets import concatenate_datasets
ds_all = concatenate_datasets([ds_ko, ds_en])
```

## Features

| Column | Description |
|--------|-------------|
| `id` | Unique QA id |
| `language` | `KO` / `EN` |
| `question_type` | definition / how_to / property / comparison / constraint / usage |
| `variant_type` | platform_alias / paraphrase / typo / colloquial (surface form) |
| `platform_alias` | platform name used in the question (MSW / 메월드 / ...) |
| `question` | user question |
| `thinking` | reasoning toward the answer |
| `answer` | self-contained explanatory answer |
| `intent` | normalized question intent |
| `source_type` / `source_id` / `source_url` / `source_title` | seed source doc |
| `combo_sources` | JSON list of docs when composed from multiple (else empty) |
| `gen_model` | model used to generate the answer |

## Generation

Documents → embedding-based related-doc combination → question synthesis
(diverse types, platform aliases, paraphrases, typos) → embedding-based
near-duplicate removal (Qdrant) → grounded self-contained answers.

## Source & License

- Source: MapleStory Worlds Creator Center (© NEXON Korea)
- License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
