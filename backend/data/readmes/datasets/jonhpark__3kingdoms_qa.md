---
language:
- ko
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: level
    dtype: string
  splits:
  - name: train
    num_bytes: 3745192
    num_examples: 18314
  download_size: 1942926
  dataset_size: 3745192
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
