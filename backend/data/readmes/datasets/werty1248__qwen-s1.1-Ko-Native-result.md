---
language:
- ko
dataset_info:
- config_name: AIME2024
  features:
  - name: input
    dtype: string
  - name: answer
    dtype: string
  - name: first_output
    dtype: string
  - name: second_output
    dtype: string
  splits:
  - name: train
    num_bytes: 677437
    num_examples: 30
  download_size: 255392
  dataset_size: 677437
- config_name: GSM8K
  features:
  - name: input
    dtype: string
  - name: answer
    dtype: float64
  - name: first_output
    dtype: string
  - name: second_output
    dtype: string
  splits:
  - name: train
    num_bytes: 9920864
    num_examples: 1319
  download_size: 3796852
  dataset_size: 9920864
- config_name: KSM
  features:
  - name: input
    dtype: string
  - name: answer
    dtype: string
  - name: first_output
    dtype: string
  - name: second_output
    dtype: string
  splits:
  - name: train
    num_bytes: 30270029
    num_examples: 1428
  download_size: 11574859
  dataset_size: 30270029
- config_name: MATH
  features:
  - name: input
    dtype: string
  - name: answer
    dtype: float64
  - name: first_output
    dtype: string
  - name: second_output
    dtype: string
  splits:
  - name: train
    num_bytes: 35075879
    num_examples: 2885
  download_size: 13944937
  dataset_size: 35075879
- config_name: MMMLU
  features:
  - name: input
    dtype: string
  - name: answer
    dtype: int64
  - name: first_output
    dtype: string
  - name: second_output
    dtype: string
  splits:
  - name: train
    num_bytes: 6851379
    num_examples: 470
  download_size: 2578358
  dataset_size: 6851379
- config_name: OMNI_MATH
  features:
  - name: input
    dtype: string
  - name: answer
    dtype: int64
  - name: first_output
    dtype: string
  - name: second_output
    dtype: string
  splits:
  - name: train
    num_bytes: 38953051
    num_examples: 1909
  download_size: 14320251
  dataset_size: 38953051
configs:
- config_name: AIME2024
  data_files:
  - split: train
    path: AIME2024/train-*
- config_name: GSM8K
  data_files:
  - split: train
    path: GSM8K/train-*
- config_name: KSM
  data_files:
  - split: train
    path: KSM/train-*
- config_name: MATH
  data_files:
  - split: train
    path: MATH/train-*
- config_name: MMMLU
  data_files:
  - split: train
    path: MMMLU/train-*
- config_name: OMNI_MATH
  data_files:
  - split: train
    path: OMNI_MATH/train-*
---
