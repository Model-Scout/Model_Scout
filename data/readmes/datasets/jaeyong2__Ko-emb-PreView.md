---
dataset_info:
  features:
  - name: context
    dtype: string
  - name: Title
    dtype: string
  - name: Fake Title
    dtype: string
  splits:
  - name: train
    num_bytes: 1034566733.5263829
    num_examples: 223849
  - name: test
    num_bytes: 114955967.47361714
    num_examples: 24873
  download_size: 496958568
  dataset_size: 1149522701
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
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