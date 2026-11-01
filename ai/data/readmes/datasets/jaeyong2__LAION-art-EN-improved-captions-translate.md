---
dataset_info:
  features:
  - name: Korean
    dtype: string
  - name: Japanese
    dtype: string
  - name: Thai
    dtype: string
  - name: Vietnamese
    dtype: string
  - name: Hindi
    dtype: string
  - name: Indonesian
    dtype: string
  - name: generated_caption
    dtype: string
  - name: orig_caption
    dtype: string
  - name: key
    dtype: string
  - name: url
    dtype: string
  - name: index
    dtype: int64
  splits:
  - name: train
    num_bytes: 447028367
    num_examples: 605578
  download_size: 229642782
  dataset_size: 447028367
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-4.0
language:
- ko
- ja
- th
- vi
- hi
- id
---
### Development Process
1. source dataset from [recastai/LAION-art-EN-improved-captions](https://huggingface.co/datasets/recastai/LAION-art-EN-improved-captions)
2. We used [Qwen/Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) model to translate.

## License
- Qwen/Qwen2.5-72B-Instruct : https://huggingface.co/Qwen/Qwen2-72B-Instruct/blob/main/LICENSE
- recastai/LAION-art-EN-improved-captions : https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/cc-by-4.0.md

## Acknowledgement
This research is supported by **TPU Research Cloud program**.