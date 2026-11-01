---
dataset_info:
  features:
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: functions
    dtype: string
  - name: function_call
    dtype: string
  splits:
  - name: train
    num_bytes: 2232255034
    num_examples: 267787
  download_size: 1054570875
  dataset_size: 2232255034
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- ko
---

### Development Process

1. source dataset from [daje/ko_wiki](https://huggingface.co/datasets/daje/ko_wiki) and [maywell/korean_textbooks](https://huggingface.co/datasets/maywell/korean_textbooks)
2. We used [Qwen/Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) model to generate answer with COT.



## License
- Qwen/Qwen2.5-72B-Instruct : https://huggingface.co/Qwen/Qwen2-72B-Instruct/blob/main/LICENSE
- maywell/korean_textbooks : https://choosealicense.com/licenses/apache-2.0/

## Acknowledgement
This research is supported by **TPU Research Cloud program**.