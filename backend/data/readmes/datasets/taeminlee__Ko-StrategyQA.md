---
language:
- ko
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- Ko-StrategyQA
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
        num_bytes: 236940
        num_examples: 4377
      - name: dev
        num_bytes: 61724
        num_examples: 1145
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
        num_bytes: 7021046
        num_examples: 9251
      - name: ko
        num_bytes: 7021046
        num_examples: 9251
      - name: en
        num_bytes: 7021046
        num_examples: 9251
  - config_name: queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: queries
        num_bytes: 244634
        num_examples: 2833
      - name: ko
        num_bytes: 244634
        num_examples: 2833
      - name: en
        num_bytes: 244634
        num_examples: 2833
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
      - split: ko
        path: corpus.jsonl
      - split: en
        path: corpus-en.jsonl
  - config_name: queries
    data_files:
      - split: queries
        path: queries.jsonl
      - split: ko
        path: queries.jsonl
      - split: en
        path: queries-en.jsonl


---

# Ko-StrategyQA

This dataset represents a conversion of the [Ko-StrategyQA dataset](https://huggingface.co/datasets/NomaDamas/Ko-StrategyQA) into the [BeIR](https://github.com/beir-cellar/beir) format, making it compatible for use with [mteb](https://github.com/embeddings-benchmark/mteb).

The original dataset was designed for multi-hop QA, so we processed the data accordingly. First, we grouped the evidence documents tagged by annotators into sets, and excluded unit questions containing 'no_evidence' or 'operation'.