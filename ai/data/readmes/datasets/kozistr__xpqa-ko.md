---
language:
- ko
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 157879
    num_examples: 1277
  download_size: 47296
  dataset_size: 157879
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
