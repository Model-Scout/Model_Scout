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
    num_bytes: 150779
    num_examples: 30
  download_size: 74913
  dataset_size: 150779
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
    num_bytes: 2197065
    num_examples: 1319
  download_size: 972014
  dataset_size: 2197065
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
    num_bytes: 6698789
    num_examples: 1428
  download_size: 2672655
  dataset_size: 6698789
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
    num_bytes: 7525002
    num_examples: 2885
  download_size: 3176994
  dataset_size: 7525002
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
    num_bytes: 1292000
    num_examples: 470
  download_size: 554258
  dataset_size: 1292000
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
    num_bytes: 7336719
    num_examples: 1909
  download_size: 3073854
  dataset_size: 7336719
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
