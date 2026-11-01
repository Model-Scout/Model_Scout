---
dataset_info:
  features:
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: tools
    dtype: string
  splits:
  - name: train
    num_bytes: 1900345
    num_examples: 1000
  download_size: 902936
  dataset_size: 1900345
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
