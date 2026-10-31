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
    num_bytes: 203421
    num_examples: 1
  download_size: 139876
  dataset_size: 203421
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
tags:
- finance
size_categories:
- 1K<n<10K
license: cc-by-nc-sa-4.0
---

## HeadlineOpinion-PairCLS-ko
- A **PairClassification** task built based on **Korean financial editorial/column titles**.