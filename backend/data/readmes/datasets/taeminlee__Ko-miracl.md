---
language:
- ko
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- miracl
task_categories:
- text-retrieval
task_ids:
- document-retrieval
config_names:
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
        num_bytes: 347785
        num_examples: 12767
      - name: dev
        num_bytes: 83188
        num_examples: 3057
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
        num_bytes: 633206834
        num_examples: 1486752
  - config_name: queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: queries
        num_bytes: 174597
        num_examples: 2761
configs:
  - config_name: default
    data_files:
      - split: train
        path: qrels/train.jsonl
      - split: dev
        path: qrels/dev.jsonl
  - config_name: corpus
    data_files:
      - split: corpus
        path: corpus.jsonl
  - config_name: queries
    data_files:
      - split: queries
        path: queries.jsonl

---

# Ko-miracl

This dataset represents a conversion of the Korean (Ko) section from the [miracl dataset](https://huggingface.co/datasets/miracl/miracl) into the [BeIR](https://github.com/beir-cellar/beir) format, making it compatible for use with [mteb](https://github.com/embeddings-benchmark/mteb).