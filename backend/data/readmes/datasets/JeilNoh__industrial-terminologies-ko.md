---
license: unlicense
dataset_info:
  features:
  - name: terminology
    dtype: string
  - name: explanation
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 3866488
    num_examples: 15047
  - name: validation
    num_bytes: 829979
    num_examples: 3224
  - name: test
    num_bytes: 833240
    num_examples: 3225
  download_size: 3108566
  dataset_size: 5529707
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
task_categories:
- question-answering
language:
- ko
---