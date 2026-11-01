---
dataset_info:
  features:
  - name: title
    dtype: string
  - name: url
    dtype: string
  - name: context
    dtype: string
  - name: answer
    struct:
    - name: text
      dtype: string
    - name: html_answer_start
      dtype: int64
    - name: html_answer_text
      dtype: string
    - name: answer_start
      dtype: int64
  - name: question
    dtype: string
  - name: id
    dtype: string
  splits:
  - name: train
    num_bytes: 4252605635
    num_examples: 83486
  - name: validation
    num_bytes: 529418488
    num_examples: 10165
  download_size: 679872503
  dataset_size: 4782024123
task_categories:
- question-answering
language:
- ko
---
# Dataset Card for "korsquadv2_1"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)