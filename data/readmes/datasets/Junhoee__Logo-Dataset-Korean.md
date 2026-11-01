---
language:
- ko
dataset_info:
  features:
  - name: image
    dtype: image
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 42812224
    num_examples: 3228
  - name: train
    num_bytes: 486233574.472
    num_examples: 17942
  download_size: 1572400998
  dataset_size: 529045798.47200006
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
tags:
- logo
---
