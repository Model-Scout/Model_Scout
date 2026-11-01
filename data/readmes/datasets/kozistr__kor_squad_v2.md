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
    num_bytes: 84618323
    num_examples: 92641
  download_size: 13706229
  dataset_size: 84618323
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
