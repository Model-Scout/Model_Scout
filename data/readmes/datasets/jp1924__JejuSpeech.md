---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: sentence
    dtype: string
  - name: standard_form
    dtype: string
  - name: dialect_form
    dtype: string
  - name: start
    dtype: float32
  - name: end
    dtype: float32
  - name: note
    dtype: string
  - name: eojeolList
    list:
    - name: id
      dtype: int8
    - name: eojeol
      dtype: string
    - name: standard
      dtype: string
    - name: isDialect
      dtype: bool
  - name: speaker
    struct:
    - name: id
      dtype: string
    - name: name
      dtype: string
    - name: age
      dtype: string
    - name: occupation
      dtype: string
    - name: sex
      dtype: string
    - name: birthplace
      dtype: string
    - name: principal_residence
      dtype: string
    - name: current_residence
      dtype: string
    - name: education
      dtype: string
  - name: metadata
    struct:
    - name: title
      dtype: string
    - name: creator
      dtype: string
    - name: distributor
      dtype: string
    - name: year
      dtype: string
    - name: category
      dtype: string
    - name: annotation_level
      list: string
    - name: sampling
      dtype: string
    - name: author
      dtype: string
    - name: publisher
      dtype: string
    - name: date
      dtype: string
    - name: topic
      dtype: string
  splits:
  - name: train
    num_bytes: 730867084925.104
    num_examples: 2774257
  - name: validation
    num_bytes: 90310808652.344
    num_examples: 333802
  download_size: 786625196812
  dataset_size: 821177893577.448
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
task_categories:
- automatic-speech-recognition
language:
- ko
---