---
license: mit
language:
- ko
task_categories:
- question-answering
- text-generation
tags:
- gsm8k
- math
- korean
configs:
- config_name: full
  data_files:
  - split: train
    path: full/train.jsonl
  - split: test
    path: full/test.jsonl
- config_name: sft
  data_files:
  - split: train
    path: sft/train.jsonl
- config_name: eval
  data_files:
  - split: test
    path: eval/test.jsonl
---

# GSM8K Korean

Korean GSM8K-style dataset generated from GSM8K. Failed rows from the source generation outputs were excluded.

## Configs

- `full`: full translation/generation metadata for ok rows only.
- `sft`: train split with `question`, `answer`, `parsed_answer`, and original GSM8K fields.
- `eval`: test split with `question`, short `answer`, and original GSM8K fields.

## Row counts

- full train: 7,309
- full test: 1,296
- sft train: 7,309
- eval test: 1,296

Excluded failed rows: 1,184 train and 187 test.
