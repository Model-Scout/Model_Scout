---
language:
- ko
size_categories:
- 100K<n<1M
task_categories:
- feature-extraction
pretty_name: Korea_address
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
  - split: valid
    path: data/valid-*
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
    num_bytes: 2581554.5517241377
    num_examples: 23
  - name: test
    num_bytes: 544091.448275862
    num_examples: 6
  - name: valid
    num_bytes: 2581554.5517241377
    num_examples: 23
  download_size: 4642711
  dataset_size: 5707200.551724138
---
