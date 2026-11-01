---
dataset_info:
- config_name: ASR
  features:
  - name: id
    dtype: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: sentence
    dtype: string
  - name: metadata
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
    num_bytes: 342810281979.375
    num_examples: 1824445
  - name: validation
    num_bytes: 3177352724.875
    num_examples: 16113
  download_size: 334470530019
  dataset_size: 345987634704.25
configs:
- config_name: ASR
  data_files:
  - split: train
    path: ASR/train-*
  - split: validation
    path: ASR/validation-*
task_categories:
- automatic-speech-recognition
language:
- ko
size_categories:
- 100B<n<1T
---