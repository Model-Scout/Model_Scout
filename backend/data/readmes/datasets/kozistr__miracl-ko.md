---
language:
- ko
dataset_info:
  features:
  - name: query
    dtype: string
  - name: positive_passages
    sequence: string
  - name: negative_passages
    sequence: string
  splits:
  - name: train
    num_bytes: 10501940
    num_examples: 1081
  download_size: 6092289
  dataset_size: 10501940
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
