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
    num_bytes: 4075290
    num_examples: 1000
  download_size: 2412162
  dataset_size: 4075290
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
pretty_name: News-Summ-ko
size_categories:
- 1K<n<10K
license: cc-by-nc-sa-4.0
---

## News-Summ-ko
- A task to verify whether the **long-text summary** of a **fact-based Korean financial news article** is correct.
