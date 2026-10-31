---
language:
- ko
multilinguality:
- monolingual
task_categories:
- text-retrieval
task_ids:
- document-retrieval
configs:
  - config_name: AIR-Bench_24.05
    data_files:
      - split: corpus_default
        path: "AIR-Bench_24.05/default/corpus.jsonl"
      - split: queries_default_dev
        path: "AIR-Bench_24.05/default/dev_queries.jsonl"
      - split: queries_default_test
        path: "AIR-Bench_24.05/default/test_queries.jsonl"
---

Available Versions:
- AIR-Bench_24.05
    - Task / Domain / Language: qa / web / ko
    - Available Datasets (Dataset Name: Splits):
        - default: dev, test
