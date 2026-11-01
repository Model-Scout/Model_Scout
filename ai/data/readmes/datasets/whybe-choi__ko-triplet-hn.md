---
language:
- ko
tags:
- text
- retrieval
- korean
- hard-negative-mining
- qwen3-embedding
- sentence-transformers
task_categories:
- sentence-similarity
- text-retrieval
pretty_name: Korean Triplet Hard Negatives
configs:
- config_name: percpos
  data_files:
  - split: train
    path: percpos/train-*
  default: true
dataset_info:
  config_name: percpos
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  splits:
  - name: train
    num_bytes: 2301400746
    num_examples: 370106
  download_size: 1165794308
  dataset_size: 2301400746
---

## Overview

This dataset extends [nlpai-lab/ko-triplet-v1.0](https://huggingface.co/datasets/nlpai-lab/ko-triplet-v1.0) with freshly mined hard negatives for each (anchor, positive) pair, intended for fine-tuning Korean text embedding models.

The hard negatives were identified using `Qwen/Qwen3-Embedding-8B`, retrieving candidates from a corpus built from the deduplicated union of the original dataset's `document` and `hard_negative` columns.

## Dataset Structure

- **anchor** (string): Query
- **positive** (string): Document relevant to the anchor
- **negative_1** ... **negative_7** (string): Mined hard negative documents (descending similarity)

- Total rows: 370,106

## Mining Methodology

Hard negatives were mined with sentence-transformers' [`mine_hard_negatives`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.mine_hard_negatives) utility using the TopK-PercPos strategy (`sampling_strategy="top"`, `relative_margin=0.05`): for each anchor, candidates are retrieved from the corpus and only those scoring within the top 95% of the positive's similarity score are kept, up to 7 negatives per anchor.

## Filtering

Some queries in the source dataset are bare comma-separated keyword lists rather than natural-language questions (e.g. `"대통령, 경제, 회복, 고용, 안정, 대책, 발표하다"`). To keep training focused on natural-language questions, rows with this kind of `anchor` were filtered out, removing 341,707 of the original 711,813 rows (~48%) and leaving 370,106 rows.

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("whybe-choi/ko-triplet-hn", name="percpos", split="train")
```

