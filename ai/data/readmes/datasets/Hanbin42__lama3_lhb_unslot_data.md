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
    num_bytes: 42930
    num_examples: 200
  download_size: 5512
  dataset_size: 42930
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
