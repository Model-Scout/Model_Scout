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
    num_bytes: 94759
    num_examples: 447
  download_size: 42401
  dataset_size: 94759
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
