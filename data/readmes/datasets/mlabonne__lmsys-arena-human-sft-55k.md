---
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
    num_bytes: 104743494.03361344
    num_examples: 57362
  download_size: 56640562
  dataset_size: 104743494.03361344
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
