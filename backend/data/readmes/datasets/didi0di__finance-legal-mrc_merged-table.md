---
license: cc-by-sa-4.0
dataset_info:
  features:
  - name: image
    dtype: image
  - name: table_title
    dtype: string
  - name: table_html
    dtype: string
  splits:
  - name: train
    num_bytes: 2663265389.974
    num_examples: 1457
  - name: test
    num_bytes: 1357116759
    num_examples: 743
  download_size: 314620058
  dataset_size: 4020382148.974
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
task_categories:
- table-question-answering
- text-generation
language:
- ko
tags:
- HTML
- table
- finance
- mrc
- legal
- table-mrc
size_categories:
- n<1K
---

# 데이터셋 설명
shchoice/finance-legal-mrc 데이터 중 병합된 테이블만 추출한 뒤 이미지와 함께 저장한 데이터입니다.

