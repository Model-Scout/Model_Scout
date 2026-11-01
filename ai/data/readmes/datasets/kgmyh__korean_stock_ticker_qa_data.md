---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 1082966
    num_examples: 13815
  - name: test
    num_bytes: 3797
    num_examples: 50
  download_size: 300370
  dataset_size: 1086763
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
license: apache-2.0
task_categories:
- text-classification
language:
- ko
tags:
- finance
- korean
- stock_ticker
- ticker
---


# 개요

- 한국 증시에 상장된 회사이름으로 종목코드 물어보는 QA 데이터셋
- 데이터 출처
  - https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage
  - 2025년 05월 15일 데이터