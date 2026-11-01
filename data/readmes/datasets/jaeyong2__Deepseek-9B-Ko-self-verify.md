---
dataset_info:
  features:
  - name: content
    dtype: string
  - name: response
    sequence: string
  - name: parsing_success
    sequence: string
  - name: parsing_failed
    sequence: string
  - name: success_results
    sequence: string
  splits:
  - name: train
    num_bytes: 1650985347
    num_examples: 16071
  download_size: 699386043
  dataset_size: 1650985347
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---

## Verification Rules
1. Whether the generated function is parsed
2. Whether the parsed function is executed
3. Whether the result of the executed function and the result predicted by LLM are the same
