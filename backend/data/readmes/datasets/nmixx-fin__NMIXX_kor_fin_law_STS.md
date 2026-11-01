---
dataset_info:
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: score
    dtype: int64
  splits:
  - name: train
    num_bytes: 654232
    num_examples: 499
  download_size: 267057
  dataset_size: 654232
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
tags:
- finance
---