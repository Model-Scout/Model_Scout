---
dataset_info:
  features:
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: transcripts
    dtype: string
  splits:
  - name: train
    num_bytes: 9302913443.561954
    num_examples: 111200
  - name: test
    num_bytes: 1119354595.6598015
    num_examples: 13901
  - name: valid
    num_bytes: 1125525152.5452442
    num_examples: 13900
  download_size: 9232284149
  dataset_size: 11547793191.767
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
  - split: valid
    path: data/valid-*
---
# Dataset Card for "low_quality_call_voice"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)