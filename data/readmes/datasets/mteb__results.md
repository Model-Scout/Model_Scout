---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: model_name
    dtype: large_string
  - name: model_revision
    dtype: large_string
  - name: task_name
    dtype: large_string
  - name: split
    dtype: large_string
  - name: language
    large_list: large_string
  - name: subset
    dtype: large_string
  - name: score
    dtype: float64
  - name: experiments
    struct:
    - name: use_image_modality
      dtype: bool
    - name: vector_type
      dtype: large_string
    - name: model_type
      large_list: large_string
  - name: is_public
    dtype: bool
  - name: trained_on
    dtype: bool
  splits:
  - name: train
    num_bytes: 1907586597
    num_examples: 8921129
  download_size: 114122958
  dataset_size: 1907586597
license: cc0-1.0
pretty_name: MTEB Results
---
