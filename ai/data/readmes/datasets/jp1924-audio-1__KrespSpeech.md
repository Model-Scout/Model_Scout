---
dataset_info:
  features:
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: sentence
    dtype: string
  - name: id
    dtype: string
  - name: dataSet
    struct:
    - name: version
      dtype: string
    - name: date
      dtype: string
    - name: typeInfo
      struct:
      - name: category
        dtype: string
      - name: subcategory
        dtype: string
      - name: place
        dtype: string
      - name: speakers
        list:
        - name: id
          dtype: string
        - name: gender
          dtype: string
        - name: type
          dtype: string
        - name: age
          dtype: string
        - name: residence
          dtype: string
      - name: inputType
        dtype: string
    - name: dialogs
      list:
      - name: speaker
        dtype: string
      - name: audioPath
        dtype: string
      - name: textPath
        dtype: string
  splits:
  - name: train
    num_bytes: 335639155312.5
    num_examples: 2067668
  - name: validation
    num_bytes: 3382855559.25
    num_examples: 20830
  download_size: 324002692624
  dataset_size: 339022010871.75
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