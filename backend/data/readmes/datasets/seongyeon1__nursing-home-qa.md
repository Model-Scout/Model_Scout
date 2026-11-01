---
language:
- ko
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 43110
    num_examples: 82
  download_size: 23380
  dataset_size: 43110
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
