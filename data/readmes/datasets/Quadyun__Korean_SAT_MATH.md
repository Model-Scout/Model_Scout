---
language:
- ko
configs:
- config_name: 2022_calculus
  data_files:
  - split: test
    path: data/2022_calculus-*
- config_name: 2023_calculus
  data_files:
  - split: test
    path: data/2023_calculus-*
- config_name: 2024_calculus
  data_files:
  - split: test
    path: data/2024_calculus-*
- config_name: 2025_calculus
  data_files:
  - split: test
    path: data/2025_calculus-*
tags:
- math
- Korean
- Exam
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: question
    dtype: string
  - name: choices
    sequence: string
  - name: score
    dtype: int64
  - name: answer
    dtype: string
  - name: has_image
    dtype: bool
---
