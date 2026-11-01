---
language:
- ko
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: output_edit
    dtype: string
  - name: instruction_edit
    dtype: string
  splits:
  - name: train
    num_bytes: 329314302
    num_examples: 100000
  download_size: 177083172
  dataset_size: 329314302
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
