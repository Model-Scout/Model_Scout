---
dataset_info:
  features:
  - name: jobpost
    dtype: string
  - name: resume_grade
    dtype: string
  - name: selfintro_grade
    dtype: string
  - name: resume
    dtype: string
  - name: selfintro
    dtype: string
  - name: evaluation
    dtype: string
  - name: total_score
    dtype: int64
  - name: resume_score
    dtype: int64
  - name: selfintro_score
    dtype: int64
  splits:
  - name: train
    num_bytes: 612749926
    num_examples: 69047
  - name: validation
    num_bytes: 884668
    num_examples: 100
  - name: test
    num_bytes: 44317001
    num_examples: 5000
  download_size: 276546470
  dataset_size: 657951595
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
language:
- ko
---