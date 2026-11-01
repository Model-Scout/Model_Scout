---
language:
- ko
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- mrtydi
task_categories:
- text-retrieval
task_ids:
- document-retrieval
config_names:
- default
- queries
- corpus
tags:
- text-retrieval
dataset_info:
  - config_name: default
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 34828
        num_examples: 1317
      - name: dev
        num_bytes: 8121
        num_examples: 307
      - name: test
        num_bytes: 13482
        num_examples: 492
  - config_name: corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 609925549
        num_examples: 1496126
  - config_name: queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: queries
        num_bytes: 135944
        num_examples: 2019
configs:
  - config_name: default
    data_files:
      - split: train
        path: qrels/train.jsonl
      - split: dev
        path: qrels/dev.jsonl
      - split: test
        path: qrels/test.jsonl
  - config_name: corpus
    data_files:
      - split: corpus
        path: corpus.jsonl
  - config_name: queries
    data_files:
      - split: queries
        path: queries.jsonl

---

# Ko-mrtydi

This dataset represents a conversion of the Korean (Ko) section from the [Mr.TyDI dataset](https://github.com/castorini/mr.tydi) into the [BeIR](https://github.com/beir-cellar/beir) format, making it compatible for use with [mteb](https://github.com/embeddings-benchmark/mteb).