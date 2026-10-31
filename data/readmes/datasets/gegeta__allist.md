---
language:
- ko
- en
license: apache-2.0
size_categories:
- 10M<n<100M
pretty_name: gegeta
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
    num_bytes: 9114
    num_examples: 39
  download_size: 9258
  dataset_size: 9114
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
