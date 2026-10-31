---
dataset_info:
  features:
  - name: date
    dtype: string
  - name: category
    dtype: string
  - name: press
    dtype: string
  - name: title
    dtype: string
  - name: document
    dtype: string
  - name: link
    dtype: string
  - name: summary
    dtype: string
  - name: gen_text
    dtype: string
  - name: gen_long_summary
    dtype: string
  splits:
  - name: train
    num_bytes: 20026155
    num_examples: 1638
  download_size: 10754216
  dataset_size: 20026155
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---