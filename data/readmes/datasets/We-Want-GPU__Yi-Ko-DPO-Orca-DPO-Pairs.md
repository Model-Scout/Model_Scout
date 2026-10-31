---
dataset_info:
  features:
  - name: system
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 29496437
    num_examples: 12727
  download_size: 15882568
  dataset_size: 29496437
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
