---
license: apache-2.0
dataset_info:
  features:
  - name: question_id
    dtype: string
  - name: image
    dtype: image
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: category
    dtype: string
  - name: ko_question
    dtype: string
  - name: ko_answer
    dtype: string
  splits:
  - name: test
    num_bytes: 401197996.104
    num_examples: 2374
  download_size: 200086736
  dataset_size: 401197996.104
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
language:
- ko
- en
size_categories:
- 1K<n<10K
---
