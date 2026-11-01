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
    num_bytes: 234444
    num_examples: 1
  download_size: 178953
  dataset_size: 234444
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
tags:
- finance
pretty_name: HeadlineAC-PairCLS-ko
size_categories:
- 1K<n<10K
license: cc-by-nc-sa-4.0
---

## HeadlineAC-PairCLS-ko
- A **Pair Classification** task built based on **Korean financial news headlines**.