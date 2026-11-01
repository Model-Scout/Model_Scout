---
license: cc-by-4.0
language:
- ko
- en
multilinguality:
- multilingual
task_categories:
- text-generation
- text-retrieval
tags:
- maplestory
- maplestory-worlds
- game-development
- documentation
- lua
- rag
size_categories:
- 1K<n<10K
pretty_name: MapleStory Worlds Creator Center Documentation
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

# MapleStory Worlds Creator Center Documentation

A curated dataset built from the official documentation of the
[MapleStory Worlds](https://maplestoryworlds-creators.nexon.com) Creator Center.
It is a parallel Korean/English documentation corpus intended for RAG, search,
embeddings, and domain language-model training.

The dataset covers **all three Creator Center content types** — guide documents
(`doc`), API Reference (`api`), and resources (`res`).

## Composition

Document counts by type and language:

| `type` | Description | KO | EN | Total |
|--------|-------------|----|----|-------|
| `doc`  | Guide documents | 218 | 215 | 433 |
| `api`  | API Reference | 571 | 571 | 1142 |
| `res`  | Resources | 102 | 50 | 152 |
| **All** | | **891** | **836** | **1727** |

## Configs

The dataset is split into per-language configs. Each config has a single `train`
split and contains all three document types.

| config | Description | Rows |
|--------|-------------|------|
| `ko`   | Korean documents  | 891 |
| `en`   | English documents | 836 |
| Total  |                   | 1727 |

```python
from datasets import load_dataset

# Korean only
ds_ko = load_dataset("msw-ai-tf/maplestory-worlds-creator-docs", "ko", split="train")

# English only
ds_en = load_dataset("msw-ai-tf/maplestory-worlds-creator-docs", "en", split="train")

# Combine both
from datasets import concatenate_datasets
ds_all = concatenate_datasets([ds_ko, ds_en])
```

## Features

| Column | Type | Description |
|--------|------|-------------|
| `id` | int64 | Unique document ID (Creator Center postId) |
| `type` | string | Document type — `api` (API Reference) / `doc` (guide document) / `res` (resource) |
| `language` | string | Language — `KO` / `EN` |
| `title` | string | Document title |
| `content` | string | Body in Markdown. Code blocks are normalized to mlua |
| `url` | string | Source URL (`https://maplestoryworlds-creators.nexon.com/{lang}/{section}?postId={id}`) |

## Source & License

- Source: MapleStory Worlds Creator Center (© NEXON Korea)
- License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to share
  and adapt, including commercially, with attribution to the source.

## Curation Process

Generated through the following pipeline: raw back-office JSON -> code-block
extraction / mlua conversion -> language ordering & stop-item removal -> HTML/table
normalization -> tokenization checks -> per-language Parquet export.
