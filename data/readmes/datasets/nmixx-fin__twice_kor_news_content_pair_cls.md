---
dataset_info:
  features:
  - name: sent1
    dtype: string
  - name: sent2
    dtype: string
  - name: labels
    dtype: string
  splits:
  - name: train
    num_bytes: 627230
    num_examples: 1
  download_size: 364744
  dataset_size: 627230
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
tags:
- finance
pretty_name: NewsContent-PairCLS-ko
size_categories:
- 1K<n<10K
license: cc-by-nc-sa-4.0
---

## NewsContent-PairCLS-ko
- A **Pair Classification task** built based on **Korean financial news articles**.
