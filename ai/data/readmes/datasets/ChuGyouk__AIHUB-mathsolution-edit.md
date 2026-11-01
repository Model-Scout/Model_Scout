---
language:
- ko
dataset_info:
  features:
  - name: question
    dtype: string
  - name: new_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 45048807.86342928
    num_examples: 28957
  download_size: 13761873
  dataset_size: 45048807.86342928
tags:
- math
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Details

This is the subset of [수학 과목 자동 풀이 데이터](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71716) from AIHUB, and do edit by [Qwen/Qwen2.5-72B-Instruct](Qwen/Qwen2.5-72B-Instruct). To see the difference of answers between original dataset and this dataset, go to the original data [here](https://huggingface.co/datasets/ChuGyouk/AIHUB-mathsolution).
