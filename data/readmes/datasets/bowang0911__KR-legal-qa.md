---
dataset_info:
- config_name: corpus
  features:
  - name: _id
    dtype: int64
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5243998
    num_examples: 1828
  download_size: 2259593
  dataset_size: 5243998
- config_name: default
  features:
  - name: query-id
    dtype: int64
  - name: corpus-id
    dtype: int64
  - name: score
    dtype: int64
  splits:
  - name: train
    num_bytes: 43800
    num_examples: 1825
  download_size: 21427
  dataset_size: 43800
- config_name: queries
  features:
  - name: _id
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 965919
    num_examples: 1825
  download_size: 471673
  dataset_size: 965919
configs:
- config_name: corpus
  data_files:
  - split: train
    path: corpus/train-*
- config_name: default
  data_files:
  - split: train
    path: data/train-*
- config_name: queries
  data_files:
  - split: train
    path: queries/train-*
license: apache-2.0
task_categories:
- text-retrieval
language:
- ko
---


## License & Attribution

MTEB-format derivative of [`LDKSolutions/KR-legal-qa-1.8k-jsonl`](https://huggingface.co/datasets/LDKSolutions/KR-legal-qa-1.8k-jsonl). Licensed under **Apache-2.0** (same as source).
