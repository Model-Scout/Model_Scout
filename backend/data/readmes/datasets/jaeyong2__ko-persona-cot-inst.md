---
dataset_info:
  features:
  - name: content
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 884148898
    num_examples: 240000
  download_size: 334176138
  dataset_size: 884148898
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---

## How to use

```python
>>> from datasets import load_dataset

>>> ds = load_dataset("jaeyong2/ko-persona-cot-inst", split="train")
>>> ds
Dataset({
    features: ['content', 'text'],
    num_rows: 240000
})
```


### Development Process

1. load Question dataset from [jaeyong2/persona-inst](https://huggingface.co/datasets/jaeyong2/persona-inst)
2. We used [Qwen/Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) model to generate answer with COT.




## License
- Qwen/Qwen2.5-72B-Instruct : https://huggingface.co/Qwen/Qwen2-72B-Instruct/blob/main/LICENSE
- proj-persona/PersonaHub : https://spdx.org/licenses/CC-BY-NC-SA-4.0


## Acknowledgement
This research is supported by **TPU Research Cloud program**.