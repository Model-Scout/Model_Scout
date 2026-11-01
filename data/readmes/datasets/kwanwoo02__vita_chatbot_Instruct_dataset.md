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
    num_bytes: 58265
    num_examples: 223
  download_size: 27887
  dataset_size: 58265
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
