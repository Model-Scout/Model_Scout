---
language:
- ko
license: mit
task_categories:
- text-generation
tags:
- math
- korean
- sft
- difficulty
pretty_name: Korean DeepMath with Difficulty
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: data_source
    dtype: string
  - name: prompt
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: ability
    dtype: string
  - name: reward_model
    struct:
    - name: ground_truth
      dtype: string
    - name: style
      dtype: string
  - name: extra_info
    struct:
    - name: index
      dtype: int64
    - name: split
      dtype: string
  - name: original_index
    dtype: int64
  - name: difficulty
    dtype: float64
  - name: topic
    dtype: string
  - name: difficulty_level
    dtype: string
  splits:
  - name: train
    num_bytes: 48547637
    num_examples: 101874
  download_size: 37030977
  dataset_size: 48547637
---

# Korean DeepMath with Difficulty

This dataset enriches `ChuGyouk/Korean-DeepMath` with difficulty and topic metadata from `zwhe99/DeepMath-103K`.

## Join procedure

Rows are matched using `Korean-DeepMath[extra_info][index]` -> original DeepMath row index.

## Added fields

- `original_index`
- `difficulty`
- `topic`

## Intended use

Prepared for controlled Korean mathematical reasoning SFT experiments, including difficulty-aware sampling such as TDCS.

No Easy / Medium / Hard labels are added here. Bucket boundaries should be selected after analyzing the difficulty distribution.
