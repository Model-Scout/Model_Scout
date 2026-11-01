---
license: apache-2.0
dataset_info:
  features:
  - name: image
    dtype: image
  - name: queries
    struct:
    - name: broad_topical_explanation
      dtype: string
    - name: broad_topical_query
      dtype: string
    - name: parsed_into_json
      dtype: bool
    - name: specific_detail_explanation
      dtype: string
    - name: specific_detail_query
      dtype: string
    - name: visual_element_explanation
      dtype: string
    - name: visual_element_query
      dtype: string
  - name: broad_topical_explanation
    dtype: string
  - name: broad_topical_query
    dtype: string
  - name: specific_detail_explanation
    dtype: string
  - name: specific_detail_query
    dtype: string
  - name: visual_element_explanation
    dtype: string
  - name: visual_element_query
    dtype: string
  - name: parsed_into_json
    dtype: bool
  splits:
  - name: train
    num_bytes: 59707808.0
    num_examples: 98
  download_size: 58864918
  dataset_size: 59707808.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- question-answering
language:
- ko
---
