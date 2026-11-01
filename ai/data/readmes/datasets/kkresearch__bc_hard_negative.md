---
dataset_info:
  features:
  - name: query
    dtype: string
  - name: pos
    list: string
  - name: neg
    list: string
  splits:
  - name: train
    num_bytes: 142812768
    num_examples: 58130
  download_size: 64690453
  dataset_size: 142812768
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- ko
---

Base dataset: [BCCard/BCCard-Finance-Kor-QnA](https://huggingface.co/datasets/BCCard/BCCard-Finance-Kor-QnA)

Method: [NV-Retriever](https://arxiv.org/abs/2407.15831)
