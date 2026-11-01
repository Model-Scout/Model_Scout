---
dataset_info:
  features:
  - name: en
    dtype: string
  - name: ko
    dtype: string
  splits:
  - name: train
    num_bytes: 902276183.057625
    num_examples: 76935
  download_size: 507380064
  dataset_size: 902276183.057625
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- en
- ko
---

### Development Process
1. source dataset from [m-a-p/FineFineWeb-test](https://huggingface.co/datasets/m-a-p/FineFineWeb-test)
2. We used [Qwen/Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) model to translate.

## License
- Qwen/Qwen2.5-72B-Instruct : https://huggingface.co/Qwen/Qwen2-72B-Instruct/blob/main/LICENSE
- m-a-p/FineFineWeb-test : https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md

## Acknowledgement
This research is supported by **TPU Research Cloud program**.