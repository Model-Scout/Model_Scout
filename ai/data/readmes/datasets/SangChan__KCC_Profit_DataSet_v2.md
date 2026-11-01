---
task_categories:
- text-generation
language:
- ko
pretty_name: ' KCC_Profit_DataSet_v2'
tags:
- chemistry
---

# Dataset Card for "SangChan/KCC_Profit_DataSet_v2"

## Project Repo

- Github Repo: [Beomi/KoAlpaca](https://github.com/Beomi/KoAlpaca)

## How to use

```python
>>> from datasets import load_dataset

>>> ds = load_dataset("SangChan/KCC_Profit_DataSet_v2", split="train")
>>> ds
Dataset({
    features: ['instruction', 'input', 'output'],
    num_rows: 21155
})
```


```python
>>> ds[0]
{'instruction': 'KCC 담당자의 이름을 알려줘',
 'input': 'KCC 담당자',
 'output': '담당자는 박상찬 책임입니다.',
```