---
language:
- ko
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: all_generated_responses
    sequence: string
  - name: rank
    sequence: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 807831685.4365305
    num_examples: 59565
  - name: test
    num_bytes: 27124374.563469503
    num_examples: 2000
  download_size: 332663606
  dataset_size: 834956060.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---
