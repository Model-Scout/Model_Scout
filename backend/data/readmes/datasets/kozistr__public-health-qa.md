---
language:
- ko
dataset_info:
  features:
  - name: question
    dtype: string
  - name: context
    dtype: string
  splits:
  - name: test
    num_bytes: 67554
    num_examples: 77
  download_size: 41626
  dataset_size: 67554
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
---
