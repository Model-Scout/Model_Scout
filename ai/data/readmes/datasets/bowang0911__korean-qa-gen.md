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
    num_bytes: 762000
    num_examples: 751
  download_size: 373572
  dataset_size: 762000
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
    num_bytes: 17856
    num_examples: 744
  download_size: 9580
  dataset_size: 17856
- config_name: queries
  features:
  - name: _id
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 107706
    num_examples: 744
  download_size: 53852
  dataset_size: 107706
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
task_categories:
- text-retrieval
language:
- ko
---


## Attribution

MTEB-format derivative of [`ziozzang/Korean_QA_gen_datasets`](https://huggingface.co/datasets/ziozzang/Korean_QA_gen_datasets) (Korean QA). Query = question; corpus = answer.
