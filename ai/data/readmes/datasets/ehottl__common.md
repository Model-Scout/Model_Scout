---
language:
- ko
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  - name: input
    dtype: string
  splits:
  - name: train
    num_bytes: 7274
    num_examples: 32
  download_size: 4618
  dataset_size: 7274
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
