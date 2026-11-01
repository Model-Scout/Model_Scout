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
    num_bytes: 27364102
    num_examples: 1294
  download_size: 15623257
  dataset_size: 27364102
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
