---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: rejected
    dtype: string
  - name: chosen
    dtype: string
  splits:
  - name: train
    num_bytes: 313673
    num_examples: 611
  download_size: 158374
  dataset_size: 313673
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---