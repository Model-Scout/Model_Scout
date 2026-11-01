---
task_categories:
- text2text-generation
language:
- ko
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: gen_regen
    dtype: string
  - name: meta
    dtype: string
  - name: input
    dtype: string
  - name: prompt
    dtype: string
  - name: output
    dtype: string
  - name: difficultyLevel
    dtype: string
  splits:
  - name: train
    num_bytes: 58821065
    num_examples: 7241
  - name: test
    num_bytes: 14529832
    num_examples: 1800
  download_size: 20653283
  dataset_size: 73350897
---
