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
    num_bytes: 30882
    num_examples: 132
  download_size: 15456
  dataset_size: 30882
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
