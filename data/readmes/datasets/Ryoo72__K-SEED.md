---
language:
- ko
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: image
    dtype: image
  - name: question_id
    dtype: int64
  splits:
  - name: train
    num_bytes: 512623740.625
    num_examples: 2971
  download_size: 505037113
  dataset_size: 512623740.625
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

> [!CAUTION]
> 첫번째 이미지 부터 누가봐도 수건 2개인데, 정답이 1개로 표기되어있는 문제가 있습니다.  
> 사용에 유의하세요.

[NCSOFT/K-SEED](https://huggingface.co/datasets/NCSOFT/K-SEED) 를 쓰기 좋게 바꾸어놓았습니다.

아래 코드를 이용하였습니다.
```python
from datasets import load_dataset, DatasetDict, Dataset
from huggingface_hub import login; login(token="YOUR TOKEN")

dataset = load_dataset("NCSOFT/K-SEED")
test_dataset = dataset['test']

formatted_data = {
    'question': [],
    'answer': [],
    'image': [],
    'question_id': []
}

for item in test_dataset:
    formatted_question = f"{item['question']}\nA. {item['choice_a']}\nB. {item['choice_b']}\nC. {item['choice_c']}\nD. {item['choice_d']}\n\n주어진 선택지 중 해당 옵션의 문자로 직접 답하세요."
    
    formatted_data['question'].append(formatted_question)
    formatted_data['answer'].append(item['answer'])
    formatted_data['image'].append(item['image'])
    formatted_data['question_id'].append(item['question_id'])

new_dataset = Dataset.from_dict(formatted_data)
new_dataset_dict = DatasetDict({'test': new_dataset})

new_dataset.push_to_hub("Ryoo72/K-SEED", private=False)

```