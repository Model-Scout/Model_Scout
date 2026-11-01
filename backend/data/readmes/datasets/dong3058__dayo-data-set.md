---
language:
- ko
dataset_info:
  features:
  - name: query
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 102342
    num_examples: 333
  download_size: 58415
  dataset_size: 102342
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
