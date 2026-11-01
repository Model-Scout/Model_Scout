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
    num_bytes: 3912658979
    num_examples: 376074
  download_size: 2214976541
  dataset_size: 3912658979
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---


### Development Process

1. source dataset from [HAERAE-HUB/KOREAN-WEBTEXT](https://huggingface.co/datasets/HAERAE-HUB/KOREAN-WEBTEXT) and [HAERAE-HUB/KOREAN-SyntheticText-1.5B](https://huggingface.co/datasets/HAERAE-HUB/KOREAN-SyntheticText-1.5B)
2. We used [Qwen/Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) model to generate answer with COT.



## License
- Qwen/Qwen2.5-72B-Instruct : https://huggingface.co/Qwen/Qwen2-72B-Instruct/blob/main/LICENSE

## Acknowledgement
This research is supported by **TPU Research Cloud program**.