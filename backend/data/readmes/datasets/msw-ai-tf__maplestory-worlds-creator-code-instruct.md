---
license: cc-by-4.0
language:
- ko
- en
multilinguality:
- multilingual
task_categories:
- text-generation
tags:
- maplestory
- maplestory-worlds
- game-development
- code
- mlua
- lua
- instruction
size_categories:
- 1K<n<10K
pretty_name: MapleStory Worlds Creator Code (mlua)
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

# MapleStory Worlds Creator Code (mlua)

Instruction-style code dataset for **mlua**, the scripting language of
[MapleStory Worlds](https://maplestoryworlds-creators.nexon.com). Built from the
official Creator Center example code: each example is grounded in its source
document and paired with a natural-language task, reasoning, a self-contained
explanation, and commented mlua code. Intended to teach LLMs to **write mlua game
scripts**.

The example code is preserved from the official source (a code-preservation check
rejects any record whose logic lines are not present in the source); the model only
adds comments, the task, reasoning, and explanation. Parallel Korean/English.

## Composition

| config | Rows |
|--------|------|
| `ko`   | 962 |
| `en`   | 979 |
| Total  | 1941 |

Source type: {'doc': 1514, 'api': 427}. Difficulty: {'beginner': 1000, 'intermediate': 891, 'advanced': 50}.

## Usage

```python
from datasets import load_dataset

# Korean only
ds_ko = load_dataset("msw-ai-tf/maplestory-worlds-creator-code-instruct", "ko", split="train")

# English only
ds_en = load_dataset("msw-ai-tf/maplestory-worlds-creator-code-instruct", "en", split="train")

# Combine both
from datasets import concatenate_datasets
ds_all = concatenate_datasets([ds_ko, ds_en])
```

## Features

| Column | Description |
|--------|-------------|
| `id` | Unique id |
| `language` | `KO` / `EN` |
| `source_type` | `doc` (guide) / `api` (API Reference) |
| `source_id` / `source_title` / `source_url` | source document |
| `api_refs` | JSON list of API Reference entries used (name, url) |
| `concepts` | JSON list of concepts taught |
| `tags` | JSON list of tags |
| `difficulty` | beginner / intermediate / advanced |
| `task` | natural-language request a creator would make |
| `thinking` | reasoning toward the implementation |
| `explanation` | self-contained explanation of the code |
| `code` | commented mlua code (preserved from source) |
| `gen_model` | model used for augmentation |

## Generation

Extracted example code (MSW → mlua converted) → join to source document + API
Reference for grounding → LLM augmentation (task / reasoning / explanation /
comments) with a no-hallucination prompt → code-preservation validation →
near-duplicate removal.

## Source & License

- Source: MapleStory Worlds Creator Center (© NEXON Korea)
- License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
