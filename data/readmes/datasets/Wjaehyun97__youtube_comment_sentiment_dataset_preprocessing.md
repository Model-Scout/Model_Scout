---
dataset_info:
  features:
  - name: comment
    dtype: string
  - name: labels
    dtype:
      class_label:
        names:
          '0': 긍정
          '1': 부정
          '2': 중립
  splits:
  - name: train
    num_bytes: 572859
    num_examples: 4735
  - name: test
    num_bytes: 101142
    num_examples: 836
  download_size: 438560
  dataset_size: 674001
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
task_categories:
- text-classification
language:
- ko
tags:
- comment
- youtube
- sentiment
size_categories:
- 1K<n<10K
---

# 유튜브 댓글 긍정, 부정, 중립 분류 데이터 셋

0: 긍정, 1: 부정, 2: 중립