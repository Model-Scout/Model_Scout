---
dataset_info:
- config_name: default
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  - name: input
    dtype: string
  splits:
  - name: train
    num_bytes: 8250
    num_examples: 84
  download_size: 4284
  dataset_size: 8250
- config_name: en
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  - name: input
    dtype: string
  splits:
  - name: train
    num_bytes: 8250
    num_examples: 84
  download_size: 4284
  dataset_size: 8250
- config_name: ko
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  - name: input
    dtype: string
  splits:
  - name: train
    num_bytes: 10566
    num_examples: 84
  download_size: 4606
  dataset_size: 10566
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
- config_name: en
  data_files:
  - split: train
    path: en/train-*
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*
license: mit
language:
- en
- ko
tags:
- identity
---

# Example
```python
from datasets import load_dataset

# Default Dataset (English)
ds = load_dataset("injaeryou/llm-name-identity", split="train")
# Specific Language Dataset (en|ko)
# ds = load_dataset("injaeryou/llm-name-identity", split="train", name="ko")

my_model_name = "my_model_name"
my_team_name = "my_team_name"

my_ds = ds.map(lambda x: {"output": x["output"].replace("{{model_name}}", my_model_name).replace("{{team_name}}", my_team_name

print(ds[32])
print(my_ds[32])
```
```python
# English
{'instruction': 'Could you tell me your name?', 'output': 'I am {{model_name}} from {{team_name}}.', 'input': ''}
{'instruction': 'Could you tell me your name?', 'output': 'I am my_model_name from my_team_name.', 'input': ''}
# Korean
{'instruction': '이름을 말씀해 주시겠어요?', 'output': '저는 {{team_name}}에서 온 {{model_name}}입니다.', 'input': ''}
{'instruction': '이름을 말씀해 주시겠어요?', 'output': '저는 my_team_name에서 온 my_model_name입니다.', 'input': ''}

```

# Purpose
Train Dataset for assigning a custom model name and team identity to the AI.