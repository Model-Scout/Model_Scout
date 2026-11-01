---
language:
- ko
license: cc-by-4.0
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*
dataset_info:
  features:
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 46130
    num_examples: 10
---