---
language:
- ko
license: mit
dataset_info:
  features:
  - name: query
    dtype: string
  - name: pos
    sequence: string
  - name: neg
    sequence: 'null'
  splits:
  - name: train
    num_bytes: 2432322
    num_examples: 7000
  download_size: 1250736
  dataset_size: 2432322
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
