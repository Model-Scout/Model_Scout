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
    num_bytes: 1957372
    num_examples: 30
  download_size: 712453
  dataset_size: 1957372
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
    num_bytes: 14262431
    num_examples: 1319
  download_size: 4759101
  dataset_size: 14262431
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
    num_bytes: 71808890
    num_examples: 1428
  download_size: 25831564
  dataset_size: 71808890
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
    num_bytes: 72375980
    num_examples: 2885
  download_size: 25728675
  dataset_size: 72375980
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
    num_bytes: 16308653
    num_examples: 470
  download_size: 4954845
  dataset_size: 16308653
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
    num_bytes: 92627945
    num_examples: 1909
  download_size: 32314658
  dataset_size: 92627945
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
