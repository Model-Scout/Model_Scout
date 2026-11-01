---
language:
- ko
dataset_info:
  features:
  - name: context
    dtype: string
  - name: question
    dtype: string
  splits:
  - name: train
    num_bytes: 120003388
    num_examples: 76661
  download_size: 29186369
  dataset_size: 120003388
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
