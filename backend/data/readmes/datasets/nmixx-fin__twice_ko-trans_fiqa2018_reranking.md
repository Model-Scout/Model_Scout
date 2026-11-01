---
dataset_info:
  features:
  - name: query
    dtype: string
  - name: positive
    sequence: string
  - name: negative
    sequence: string
  splits:
  - name: test
    num_bytes: 13983225
    num_examples: 1000
  download_size: 7651028
  dataset_size: 13983225
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
task_categories:
- question-answering
language:
- ko
tags:
- finance
size_categories:
- 10K<n<100K
---

## twice_ko-trans_fiqa2018_reranking

- The Korean translation of [FinanceMTEB/FiQA-reranking](https://huggingface.co/datasets/FinanceMTEB/FiQA-reranking) (translated using GPT-4o).
