---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 31275019
    num_examples: 10000
  download_size: 17847984
  dataset_size: 31275019
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-sa-4.0
language:
- ko
---