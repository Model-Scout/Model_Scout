---
dataset_info:
  features:
  - name: sampled_text
    dtype: string
  - name: question_english
    dtype: string
  - name: response_english
    dtype: string
  - name: question_korean
    dtype: string
  - name: response_korean
    dtype: string
  - name: question_eng_kor
    dtype: string
  - name: response_eng_kor
    dtype: string
  splits:
  - name: train
    num_bytes: 171287792
    num_examples: 13867
  download_size: 86249130
  dataset_size: 171287792
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- ko
---