---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: input
    dtype: string
  - name: company
    dtype: string
  splits:
  - name: train
    num_bytes: 15173129
    num_examples: 16827
  download_size: 7461806
  dataset_size: 15173129
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