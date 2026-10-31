---
license: mit
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 1540988
    num_examples: 2271
  - name: test
    num_bytes: 496016
    num_examples: 757
  download_size: 660904
  dataset_size: 2037004
---
