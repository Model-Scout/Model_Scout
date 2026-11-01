---
dataset_info:
  features:
  - name: sentence
    dtype: string
  - name: summary
    dtype: string
  - name: label
    dtype: int64
  splits:
  - name: train
    num_bytes: 3660257
    num_examples: 1000
  download_size: 2235965
  dataset_size: 3660257
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- summarization
language:
- ko
tags:
- finance
pretty_name: Opinion-Summ-ko
size_categories:
- 1K<n<10K
license: cc-by-nc-sa-4.0
---

## Opinion-Summ-ko
- A task to verify whether the **long-text summary** of an **opinion-based Korean financial editorial/column** is correct.