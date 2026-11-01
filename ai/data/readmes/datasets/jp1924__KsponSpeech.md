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
  splits:
  - name: dev
    num_bytes: 453996265.875
    num_examples: 2545
  - name: eval_clean
    num_bytes: 304987608
    num_examples: 3000
  - name: eval_other
    num_bytes: 438544274
    num_examples: 3000
  - name: train
    num_bytes: 111286133042
    num_examples: 620000
  download_size: 105060754027
  dataset_size: 112483661189.875
configs:
- config_name: default
  data_files:
  - split: dev
    path: data/dev-*
  - split: eval_clean
    path: data/eval_clean-*
  - split: eval_other
    path: data/eval_other-*
  - split: train
    path: data/train-*
task_categories:
- automatic-speech-recognition
language:
- ko
size_categories:
- 100B<n<1T
---