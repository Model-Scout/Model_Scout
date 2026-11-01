---
language:
- ko
dataset_info:
  features:
  - name: index
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: category
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: test
    num_bytes: 9682476.0
    num_examples: 240
  download_size: 3340015
  dataset_size: 9682476.0
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
---

[NCSOFT/K-DTCBench](https://huggingface.co/datasets/NCSOFT/K-DTCBench) 를 쓰기 좋게 바꾸어놓았습니다.  

아래 코드를 이용하였습니다. 
```python
from datasets import load_dataset, Dataset
from huggingface_hub import login; login(token="YOUR TOKEN")

dataset = load_dataset("NCSOFT/K-DTCBench")

def transform_format(example):
    formatted_question = f"{example['question']}\nOptions: A: {example['choice_a']}, B: {example['choice_b']}, C: {example['choice_c']}, D: {example['choice_d']}\n주어진 선택지 중 해당 옵션의 문자로 직접 답하세요."
    
    return {
        "question": formatted_question,
        "answer": example['answer'],
        "image": example['image'],
        "index": example['index'],
        "category": example['category'],
    }

new_test_dataset = dataset['test'].map(transform_format, remove_columns=[
    'choice_a', 'choice_b', 'choice_c', 'choice_d'
])

new_dataset = {}
new_dataset['test'] = new_test_dataset

from datasets import DatasetDict
new_dataset_dict = DatasetDict(new_dataset)

new_dataset_dict.push_to_hub('Ryoo72/K-DTCBench', private=False, max_shard_size="500MB")
```

아래 inference 문구 중 적절한 것을 선택하거나 추가하세요.
```
공식 : \n\n한 단어 또는 구를 사용하여 질문에 답하세요.
\n주어진 선택지 중 해당 옵션의 문자로 직접 답하세요.
```