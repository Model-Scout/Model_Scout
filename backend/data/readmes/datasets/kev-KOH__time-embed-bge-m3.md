---
license: mit
language:
  - ko
task_categories:
  - sentence-similarity
  - feature-extraction
pretty_name: Korean Temporal Query Embedding Data for BGE-M3 - v1.9 Semantic Retention
size_categories:
  - 100K<n<1M
configs:
  - config_name: default
    data_files:
      - split: train
        path: train.jsonl
      - split: validation
        path: dev.jsonl
      - split: test
        path: test.jsonl
  - config_name: bge_m3_temporal_llm_v1_9
    data_files:
      - split: train
        path: bge_m3_temporal_llm_v1_9/train.jsonl
      - split: validation
        path: bge_m3_temporal_llm_v1_9/dev.jsonl
      - split: test
        path: bge_m3_temporal_llm_v1_9/test.jsonl
  - config_name: bge_m3_temporal_llm_v1_9_metadata
    data_files:
      - split: train
        path: bge_m3_temporal_llm_v1_9_metadata/train.jsonl
      - split: validation
        path: bge_m3_temporal_llm_v1_9_metadata/dev.jsonl
      - split: test
        path: bge_m3_temporal_llm_v1_9_metadata/test.jsonl
---

# Korean Temporal Query Embedding Data for BGE-M3 - v1.9 Semantic Retention

This dataset is a FlagEmbedding/BGE-M3 fine-tuning dataset for Korean LMS temporal retrieval.

The objective is to keep semantically equivalent Korean temporal expressions close in embedding space while separating Korean expressions that look similar but mean different time ranges. The root files now point to the v1.9 training dataset.

## What v1.9 Adds

v1.9 keeps the v1.7 calendar-focused temporal data and adds a semantic-retention layer for LMS retrieval. The additional hard negatives are designed to prevent the model from solving the task only by memorizing temporal surface patterns.

Key v1.9 rules:

- Positive: `일주일 전` = `7일 전` = `1주 전`
- Positive: `1년 전` = `일 년 전` = `한 해 전`
- Hard negative: `일주일 전` != `지난주`
- Hard negative: `7일 전` != `최근 7일`
- Hard negative: `지난달` != `한 달 전`
- Hard negative: `작년` != `1년 전`
- Hard negative: `1년 전` != `365일 전` unless a reference-date-specific coincidence case is explicitly modeled
- Hard negative: same time expression but different LMS intent, item type, topic, or course

The dataset intentionally excludes fuzzy temporal labels and translationese Korean query surfaces such as `기준으로`, `시점에`, and unnatural future material questions like `내일 업로드된 자료`.

## Format

The default files use the FlagEmbedding retrieval training format:

```json
{
  "query": "1년 전 업로드된 경제 강의자료 보여줘",
  "pos": ["한 해 전 업로드된 경제 강의자료 보여줘"],
  "neg": ["1년 뒤 업로드된 경제 강의자료 보여줘", "작년 업로드된 경제 강의자료 보여줘"]
}
```

`dev.jsonl` is the validation split. It is named `dev` to match the local training pipeline, and is exposed as the Hugging Face `validation` split in the dataset card config.

## Files

```text
train.jsonl
dev.jsonl
test.jsonl
bge_m3_training_stats.json
data_quality_report.json

bge_m3_temporal_llm_v1_9/           # version-pinned no-metadata training data
bge_m3_temporal_llm_v1_9_metadata/  # same rows with audit metadata
```

## Counts

| Split | Rows |
|---|---:|
| train | 123,088 |
| validation (`dev.jsonl`) | 37,365 |
| test | 37,584 |
| total | 198,037 |

Quality audit: `True`.

## Intended Use

This dataset is intended for fine-tuning `BAAI/bge-m3` or a previous Time-Embed BGE-M3 checkpoint with `FlagEmbedding.finetune.embedder.encoder_only.m3`.

Recommended loading examples:

```python
from datasets import load_dataset

# latest default, currently v1.9
ds = load_dataset("kev-KOH/time-embed-bge-m3")

# version-pinned v1.9
v19 = load_dataset("kev-KOH/time-embed-bge-m3", "bge_m3_temporal_llm_v1_9")
```

## Notes

The metadata config is for inspection and auditing. For training, use the default config or `bge_m3_temporal_llm_v1_9`.
