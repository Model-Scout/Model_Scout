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
    num_bytes: 3691179152
    num_examples: 541633
  download_size: 651808016
  dataset_size: 3691179152
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
