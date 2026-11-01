---
language:
- ko
dataset_info:
  features:
  - name: index
    dtype: int64
  - name: modelAName
    dtype: string
  - name: modelBName
    dtype: string
  - name: instruction
    dtype: string
  - name: modelAResponse
    dtype: string
  - name: modelBResponse
    dtype: string
  - name: winner
    dtype: float64
  splits:
  - name: train
    num_bytes: 1101623
    num_examples: 432
  download_size: 542632
  dataset_size: 1101623
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
# Dataset Card for "ko_elo_arena_0207"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)