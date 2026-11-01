---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label_text
    dtype: string
  - name: label
    dtype: int64
  splits:
  - name: train
    num_bytes: 283193
    num_examples: 1000
  download_size: 158119
  dataset_size: 283193
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
tags:
- finance
pretty_name: FinSent-CLS-ko
size_categories:
- 1K<n<10K
---

## FinSent-CLS-ko
- A task to classify Korean financial news sentences into **Positive/Negative/Neutral** categories.
