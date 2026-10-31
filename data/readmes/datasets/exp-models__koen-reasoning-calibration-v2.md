---
language:
- en
- ko
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 25989766
    num_examples: 2048
  download_size: 12104432
  dataset_size: 25989766
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
