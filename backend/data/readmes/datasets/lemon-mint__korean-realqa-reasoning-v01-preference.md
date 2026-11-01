---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 33537562
    num_examples: 7768
  download_size: 18977985
  dataset_size: 33537562
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-sa-4.0
language:
- ko
---

https://huggingface.co/datasets/beomi/KoAlpaca-RealQA
