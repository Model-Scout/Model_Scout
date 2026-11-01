---
dataset_info:
  features:
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: id
    dtype: string
  - name: sentence
    dtype: string
  - name: original_form
    dtype: string
  - name: start
    dtype: float32
  - name: end
    dtype: float32
  - name: term
    dtype: string
  - name: environment
    dtype: string
  - name: hangeulToEnglish
    list:
    - name: id
      dtype: int16
    - name: hangeul
      dtype: string
    - name: english
      dtype: string
    - name: begin
      dtype: int16
    - name: end
      dtype: int16
  - name: hangeulToNumber
    list:
    - name: id
      dtype: int16
    - name: hangeul
      dtype: string
    - name: number
      dtype: string
    - name: begin
      dtype: int16
    - name: end
      dtype: int16
  - name: speaker
    struct:
    - name: id
      dtype: string
    - name: name
      dtype: string
    - name: age
      dtype: string
    - name: role
      dtype: string
    - name: sex
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
      dtype: int16
    - name: category
      dtype: string
    - name: sampling
      dtype: string
    - name: date
      dtype: string
    - name: topic
      dtype: string
    - name: media
      dtype: string
    - name: communication
      dtype: string
    - name: type
      dtype: string
    - name: domain
      dtype: string
    - name: speaker_num
      dtype: int16
    - name: organization
      dtype: string
    - name: annotation_level
      dtype: string
  splits:
  - name: train
    num_bytes: 924995624222.125
    num_examples: 5884143
  - name: validation
    num_bytes: 117241502315.25
    num_examples: 696158
  download_size: 1035999535129
  dataset_size: 1042237126537.375
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