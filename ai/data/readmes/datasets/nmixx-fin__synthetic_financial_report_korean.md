---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: category
    dtype: string
  - name: source
    dtype: string
  - name: token_count
    dtype: int64
  splits:
  - name: train
    num_bytes: 21941932
    num_examples: 20846
  download_size: 11093843
  dataset_size: 21941932
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- ko
tags:
- finance
---
