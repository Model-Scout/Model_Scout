---
language:
- zh
- en
- ja
- ko
- id
- vi
- th
license: apache-2.0
size_categories:
- 10K<n<100K
task_categories:
- translation
pretty_name: traverl_qa
dataset_info:
- config_name: en-zh_tw
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 385263
    num_examples: 2256
  download_size: 124124
  dataset_size: 385263
- config_name: id-zh_tw
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 407538
    num_examples: 2256
  download_size: 124778
  dataset_size: 407538
- config_name: ja-zh_tw
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 441775
    num_examples: 2256
  download_size: 135723
  dataset_size: 441775
- config_name: ko-zh_tw
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 414010
    num_examples: 2256
  download_size: 132364
  dataset_size: 414010
- config_name: th-zh_tw
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 569121
    num_examples: 2256
  download_size: 166608
  dataset_size: 569121
- config_name: vi-zh_tw
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 444668
    num_examples: 2256
  download_size: 138816
  dataset_size: 444668
configs:
- config_name: en-zh_tw
  data_files:
  - split: train
    path: en-zh_tw/train-*
- config_name: id-zh_tw
  data_files:
  - split: train
    path: id-zh_tw/train-*
- config_name: ja-zh_tw
  data_files:
  - split: train
    path: ja-zh_tw/train-*
- config_name: ko-zh_tw
  data_files:
  - split: train
    path: ko-zh_tw/train-*
- config_name: th-zh_tw
  data_files:
  - split: train
    path: th-zh_tw/train-*
- config_name: vi-zh_tw
  data_files:
  - split: train
    path: vi-zh_tw/train-*
tags:
- 台灣
- 桃園捷運
- 旅遊
---

# 桃園捷運旅遊問答翻譯資料集

本專案包含六國語言，中英日韓印越泰

全程由語言模型 (GPT4) 產生合成數據(synthesis data)，每一組語言存在 2K 資料量。