---
license: apache-2.0
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
    num_bytes: 2774044
    num_examples: 5433
  - name: test
    num_bytes: 706918
    num_examples: 1359
  download_size: 993228
  dataset_size: 3480962
---
