---
language:
- ko
size_categories:
- 10K<n<100K
dataset_info:
  features:
  - name: user_id
    dtype: int64
  - name: day
    dtype: string
  - name: order_ts
    dtype: string
  - name: positive_prod_id
    dtype: int64
  - name: negative_prod_id
    dtype: int64
  - name: negative_prod_ids
    sequence: int64
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 122282877.9602969
    num_examples: 58535
  - name: test
    num_bytes: 52690471.08509643
    num_examples: 17332
  - name: rigorous_test
    num_bytes: 24661037.47070749
    num_examples: 8112
  download_size: 33220918
  dataset_size: 199634386.51610082
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
  - split: rigorous_test
    path: data/rigorous_test-*
---
# Dataset Card for "ecommerce_purchase_history"

## Dataset Description

# Dataset Summary

이 데이터셋은 특정 이커머스 회사의 추천 시스템 연구 개발을 위한 데이터셋이다. 특정 기간에 대해 약 90일 동안의 구매 히스토리로부터 생성되었다. 구매 히스토리를 텍스트로 기술하였다.

llama2 토크나이저 기준 2,048 개의 토큰 미만의 예제 쌍만을 남기도록 수정하였다.

또한, test 스플릿의 경우 user_id, positive_prod_id 기준으로 train_split에 등장하지 않는 것만을 남겼다.

# Supported Tasks and Leaderboards

# Languages

This dataset is only made of `ko`(korean).

# Dataset Structure