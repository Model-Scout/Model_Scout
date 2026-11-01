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
    num_bytes: 40487553
    num_examples: 16045
  download_size: 22057370
  dataset_size: 40487553
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
