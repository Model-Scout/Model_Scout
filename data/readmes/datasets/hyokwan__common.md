---
license: apache-2.0
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
    num_bytes: 7230
    num_examples: 32
  download_size: 4119
  dataset_size: 7230
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
