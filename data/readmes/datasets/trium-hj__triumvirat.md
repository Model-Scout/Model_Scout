---
license: apache-2.0
dataset_info:
  features:
  - name: name
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: train
    num_bytes: 1003054
    num_examples: 5
  - name: valid
    num_bytes: 646387
    num_examples: 5
  - name: test
    num_bytes: 1306494
    num_examples: 7
  download_size: 2947993
  dataset_size: 2955935
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: valid
    path: data/valid-*
  - split: test
    path: data/test-*
language:
- ko
---