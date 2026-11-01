---
license: openrail
dataset_info:
  features:
  - name: Context
    dtype: string
  - name: Response
    dtype: string
  - name: Context-kor
    dtype: string
  - name: Response-kor
    dtype: string
  splits:
  - name: train
    num_bytes: 10077845
    num_examples: 3512
  download_size: 4957696
  dataset_size: 10077845
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- question-answering
- text-generation
language:
- en
- ko
tags:
- medi
- cro
size_categories:
- 1K<n<10K
---


[Amod/mental_health_counseling_conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)

GPT-4o 를 사용해 한글로 번역한 데이터셋입니다.