---
dataset_info:
  config_name: BPO
  features:
  - name: id
    dtype: string
  - name: conversations
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: chosen
    dtype: string
  - name: reject
    dtype: string
  - name: prompt
    dtype: string
  - name: optimized_prompt
    dtype: string
  splits:
  - name: train
    num_bytes: 122180963
    num_examples: 40236
  - name: validation
    num_bytes: 12488759
    num_examples: 3598
  download_size: 67557974
  dataset_size: 134669722
configs:
- config_name: BPO
  data_files:
  - split: train
    path: BPO/train-*
  - split: validation
    path: BPO/validation-*
language:
- ko
---