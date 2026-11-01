---
language:
- ko
dataset_info:
  features:
  - name: question
    dtype: string
  - name: context
    dtype: string
  splits:
  - name: train
    num_bytes: 549835838
    num_examples: 988741
  download_size: 298607648
  dataset_size: 549835838
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
