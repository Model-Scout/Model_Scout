---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: question
    dtype: string
  - name: opa
    dtype: string
  - name: opb
    dtype: string
  - name: opc
    dtype: string
  - name: opd
    dtype: string
  - name: cop
    dtype: int64
  - name: choice_type
    dtype: string
  - name: exp
    dtype: string
  - name: subject_name
    dtype: string
  - name: topic_name
    dtype: string
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 82600392
    num_examples: 60000
  download_size: 48869664
  dataset_size: 82600392
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
task_categories:
- question-answering
- translation
- text-generation
- text2text-generation
language:
- en
- ko
tags:
- medical
---