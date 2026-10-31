---
license: apache-2.0
language:
- en
- tr
- zh
- ru
- de
- ar
- fr
- hi
- id
- pt
- ko
- es
task_categories:
- text-generation
tags:
- creative-writing
- storytelling
- long-form-generation
- chain-of-thought
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
pretty_name: Novelist Chain Of Thought
dataset_info:
  features:
  - name: hash
    dtype: string
  - name: type
    dtype: string
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: metadata
    struct:
    - name: record_type
      dtype: string
    - name: source_bucket
      dtype: string
    - name: source_category
      dtype: string
    - name: source_file
      dtype: string
    - name: row_index
      dtype: int64
    - name: chapter
      dtype: int64
    - name: chapter_number
      dtype: int64
    - name: generation_mode
      dtype: string
    - name: instruction_template_id
      dtype: string
    - name: system_prompt_id
      dtype: string
    - name: system_prompt_version
      dtype: string
    - name: has_think_tag
      dtype: bool
    - name: has_answer_tag
      dtype: bool
    - name: rating
      dtype: string
    - name: average_rating
      dtype: string
    - name: models_used
      dtype: string
    - name: quality_score
      dtype: int64
    - name: meta
      dtype: string
  splits:
  - name: train
    num_bytes: 168887490
    num_examples: 8163
  download_size: 94071338
  dataset_size: 168887490
---

# Novelist Announcement.

Check out the new and biggest Novelist project [https://huggingface.co/datasets/Dxniz/Novelist]. With 5 thinking modes, agentic writing and long book support. Now only limitation is your imagination. 

# Novelist-CoT Creative Writing Dataset

## Overview

Novelist-CoT is a long-form creative writing dataset designed for supervised fine-tuning and style-focused narrative generation.  
The dataset consolidates multiple generation pipelines into a single unified structure and preserves planning traces (`<think>`) alongside final prose (`<answer>`) in accepted samples.

The dataset emphasizes:

- long-form story continuation and expansion
- style-conditioned writing
- narrative planning quality
- multilingual translation variants
- structured subtype tagging for downstream filtering

## Dataset Snapshot

- Total rows: `8,163`
- Total tokens (`instruction + input + output`, `cl100k_base`): `38,322,752`
- Average tokens per row: `4,694.69`
- Total output tokens (`output` only, `cl100k_base`): `25,204,062`
- Average output tokens per row: `3,087.60`
- Total words (`instruction + input + output`): `25,972,781`
- Average words per row: `3,181.77`
- Total output words (`output` only): `17,199,037`
- Average output words per row: `2,106.95`
- Rows with `<think>` tag present: `8,163 / 8,163` (`100%`)
- Rows with `<answer>` tag present: `8,163 / 8,163` (`100%`)

Word counts are computed with a Unicode-aware regex tokenizer. Token counts use `cl100k_base`.

## Type Composition

Each row includes a `type` field so the same dataset can be filtered into specialized training slices without changing schema.

- `extension`: `2,741` rows (`33.58%`)
- `story`: `2,525` rows (`30.93%`)
- `uncensored`: `757` rows (`9.27%`)
- `character`: `742` rows (`9.09%`)
- `long`: `625` rows (`7.66%`)
- `era`: `475` rows (`5.82%`)
- `chapter`: `251` rows (`3.07%`)
- `translation`: `36` rows (`0.44%`)
- `cot`: `11` rows (`0.13%`)

## Translation Coverage

Translation rows in the accepted combined snapshot (`n=36`) cover these target languages:

- Arabic: `3`
- Chinese (Simplified): `3`
- French: `3`
- German: `3`
- Hindi: `1`
- Indonesian: `4`
- Japanese: `2`
- Korean: `4`
- Portuguese: `4`
- Russian: `4`
- Spanish: `2`
- Turkish: `3`

## Unified Row Schema

All records use a single consistent schema:

```json
{
  "hash": "string",
  "type": "string",
  "instruction": "string",
  "input": "string",
  "output": "string",
  "metadata": {
    "record_type": "string",
    "source_bucket": "string",
    "source_category": "string",
    "source_file": "string",
    "row_index": "int",
    "chapter": "int",
    "chapter_number": "int",
    "generation_mode": "string",
    "instruction_template_id": "string",
    "system_prompt_id": "string",
    "system_prompt_version": "string",
    "has_think_tag": "bool",
    "has_answer_tag": "bool",
    "rating": "string (json-or-empty)",
    "average_rating": "string",
    "models_used": "string (json-or-empty)",
    "quality_score": "int",
    "meta": "string (json)"
  }
}
```

### Field Intent

- `hash`: Story-level linkage key for grouping related generations.
- `type`: dataset slice indicator.
- `instruction`, `input`, `output`: Direct SFT training triplet.
- `metadata.has_think_tag` / `metadata.has_answer_tag`: Tag integrity indicators.
- `metadata.rating`, `metadata.average_rating`, `metadata.models_used`: Optional rating traces where available.
- `metadata.quality_score`: Internal acceptance score from filtering stage.

## Source Consolidation

This dataset is built by consolidating:

- v3 formatted story, extension, translation, and chapter files
- v1/v2 formatted base, extension, long, and uncensored files
- v2 specialized sets for `character`, `cot`, and `era`

All of these are merged into the same unified dataset format rather than published as separate schema variants.

## Quality and Curation Policy

The acceptance pipeline enforces minimum structural quality before rows enter the combined snapshot:

- required planning/output tag checks
- minimum answer-length thresholds
- repetition and degeneration heuristics
- deterministic normalization for stable downstream ingestion

The resulting set is intentionally quality-biased toward coherent long-form narrative behavior.

## Ratings Metadata Availability

Ratings are sparse and partial, not universal.  
In the current snapshot:

- explicit per-row `rating` payloads are mostly empty
- `average_rating` / `models_used` appear where upstream ratings exist

Consumers should treat rating fields as optional metadata, not guaranteed supervision labels.

## Recommended Use Cases

- supervised fine-tuning for narrative generation
- continuation and chapter-expansion training
- chain-of-thought-aware writing systems
- stylistic adaptation experiments (author/era/persona prompts)
- multilingual style transfer experiments using translation subset
