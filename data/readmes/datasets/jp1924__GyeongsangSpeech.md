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
    num_bytes: 295188715803.664
    num_examples: 2088487
  - name: validation
    num_bytes: 30104901343.384
    num_examples: 229497
  download_size: 297290180997
  dataset_size: 325293617147.048
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
size_categories:
- 100B<n<1T
---