---
dataset_info:
  features:
  - name: Question
    dtype: string
  - name: RAW Ground Truth
    sequence: string
  - name: Thinking
    dtype: string
  - name: Final Answer
    dtype: string
  - name: context
    dtype: string
  splits:
  - name: train
    num_bytes: 2763874173
    num_examples: 754459
  download_size: 1526868785
  dataset_size: 2763874173
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
license: cdla-sharing-1.0
---


### Development Process

1. source dataset from [ohsuz/fineweb-edu-2024-10-1M](https://huggingface.co/datasets/ohsuz/fineweb-edu-2024-10-1M) and [roneneldan/TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories)
2. We used [Qwen/Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) model to generate answer with COT.


## License
- Qwen/Qwen2.5-72B-Instruct : https://huggingface.co/Qwen/Qwen2-72B-Instruct/blob/main/LICENSE
- roneneldan/TinyStories : Community Data License Agreement – Sharing, Version 1.0

## Acknowledgement
This research is supported by **TPU Research Cloud program**.