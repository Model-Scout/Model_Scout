---
language:
- ko
dataset_info:
  features:
  - name: context
    dtype: string
  - name: question
    dtype: string
  splits:
  - name: test
    num_bytes: 602138
    num_examples: 900
  download_size: 222990
  dataset_size: 602138
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
---
