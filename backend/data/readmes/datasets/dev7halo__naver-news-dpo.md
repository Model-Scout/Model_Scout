---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 14933143
    num_examples: 1638
  download_size: 8272918
  dataset_size: 14933143
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---