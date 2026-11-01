---
dataset_info:
  features:
  - name: source
    dtype: string
  - name: text
    dtype: string
  - name: category
    dtype: string
  - name: token_count
    dtype: int64
  splits:
  - name: train
    num_bytes: 532344662
    num_examples: 502831
  download_size: 118825124
  dataset_size: 532344662
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