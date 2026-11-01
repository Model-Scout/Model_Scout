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
  - name: meta
    struct:
    - name: original
      dtype: string
    - name: start
      dtype: string
    - name: end
      dtype: string
    - name: length
      dtype: string
    - name: subject
      dtype: string
    - name: topic
      dtype: string
    - name: gender
      dtype: string
    - name: generation
      dtype: string
    - name: location
      dtype: string
    - name: dialect
      dtype: string
    - name: source
      dtype: string
    - name: quality
      dtype: string
  splits:
  - name: train
    num_bytes: 426237436069.75
    num_examples: 2624874
  - name: validation
    num_bytes: 22950777291.625
    num_examples: 142683
  download_size: 427367614446
  dataset_size: 449188213361.375
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