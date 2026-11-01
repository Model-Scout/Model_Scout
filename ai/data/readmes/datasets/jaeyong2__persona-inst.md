---
dataset_info:
  features:
  - name: Level
    dtype: int64
  - name: English
    dtype: string
  - name: Korean
    dtype: string
  - name: Japanese
    dtype: string
  - name: Thai
    dtype: string
  - name: Vietnamese
    dtype: string
  - name: context
    dtype: string
  splits:
  - name: train
    num_bytes: 2973151280
    num_examples: 3006572
  download_size: 995697751
  dataset_size: 2973151280
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ja
- ko
- th
- vi
license: cc-by-nc-sa-4.0
---

## How to use

```python
>>> from datasets import load_dataset

>>> ds = load_dataset("jaeyong2/persona-inst", split="train")
>>> ds
Dataset({
    features: ['Level', 'English', 'Korean', 'Thai', 'Vietnamese', 'context'],
    num_rows: 3006572
})
```


### Development Process

1. Generate persona pair from [proj-persona/PersonaHub](https://huggingface.co/datasets/proj-persona/PersonaHub)
2. We used [Qwen/Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) model to generate Question.




## License
- Qwen/Qwen2.5-72B-Instruct : https://huggingface.co/Qwen/Qwen2-72B-Instruct/blob/main/LICENSE
- proj-persona/PersonaHub : https://spdx.org/licenses/CC-BY-NC-SA-4.0


## Acknowledgement
This research is supported by **TPU Research Cloud program**.