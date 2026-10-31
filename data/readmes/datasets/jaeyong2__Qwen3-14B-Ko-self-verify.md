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
    num_bytes: 881076591
    num_examples: 18000
  download_size: 298583642
  dataset_size: 881076591
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