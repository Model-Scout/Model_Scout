---
dataset_info:
  config_name: ASR
  features:
  - name: id
    dtype: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: sentence
    dtype: string
  splits:
  - name: train
    num_bytes: 475929597909.875
    num_examples: 2385457
  - name: validation
    num_bytes: 6459745246.625
    num_examples: 32971
  download_size: 466422692090
  dataset_size: 482389343156.5
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
---