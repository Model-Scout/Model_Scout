---
license: apache-2.0
task_categories:
- question-answering
language:
- ko
size_categories:
- 1M<n<10M

configs:
- config_name: default
  data_files:
  - path: test.json
    split: test

dataset_info:
  features:
    - name: category
      dtype: string
    - name: category_detail
      dtype: string
    - name: question
      dtype: string
    - name: answer
      dtype: string
---