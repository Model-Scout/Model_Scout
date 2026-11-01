---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 23371027
    num_examples: 21155
  download_size: 12856014
  dataset_size: 23371027
task_categories:
- text-generation
language:
- ko
tags:
- KoAlpaca
pretty_name: KoAlpaca-v1.1a
---
# Dataset Card for "KoAlpaca-v1.1a"

## Project Repo

- Github Repo: [Beomi/KoAlpaca](https://github.com/Beomi/KoAlpaca)

## How to use

```python
>>> from datasets import load_dataset

>>> ds = load_dataset("beomi/KoAlpaca-v1.1a", split="train")
>>> ds
Dataset({
    features: ['instruction', 'input', 'output'],
    num_rows: 21155
})
```


```python
>>> ds[0]
{'instruction': '양파는 어떤 식물 부위인가요? 그리고 고구마는 뿌리인가요?',
 'output': '양파는 잎이 아닌 식물의 줄기 부분입니다. 고구마는 식물의 뿌리 부분입니다. \n\n식물의 부위의 구분에 대해 궁금해하는 분이라면 분명 이 질문에 대한 답을 찾고 있을 것입니다. 양파는 잎이 아닌 줄기 부분입니다. 고구마는 다른 질문과 답변에서 언급된 것과 같이 뿌리 부분입니다. 따라서, 양파는 식물의 줄기 부분이 되고, 고구마는 식물의 뿌리 부분입니다.\n\n 덧붙이는 답변: 고구마 줄기도 볶아먹을 수 있나요? \n\n고구마 줄기도 식용으로 볶아먹을 수 있습니다. 하지만 줄기 뿐만 아니라, 잎, 씨, 뿌리까지 모든 부위가 식용으로 활용되기도 합니다. 다만, 한국에서는 일반적으로 뿌리 부분인 고구마를 주로 먹습니다.',
 'url': 'https://kin.naver.com/qna/detail.naver?d1id=11&dirId=1116&docId=55320268'}
```