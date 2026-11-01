---
language:
- en
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
    num_bytes: 141793.6072723102
    num_examples: 320
  download_size: 108811
  dataset_size: 141793.6072723102
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
