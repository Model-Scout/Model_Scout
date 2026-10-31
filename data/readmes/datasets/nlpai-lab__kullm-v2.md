---
license: apache-2.0
task_categories:
- text-generation
language:
- ko
pretty_name: kullm
size_categories:
- 10K<n<100K
---

# Dataset Card for "KULLM-v2"

## Dataset Summary

Korean translation of GPT4ALL, Dolly, and Vicuna data.


repository: [nlpai-lab/KULLM](https://github.com/nlpai-lab/KULLM)

huggingface: [nlpai-lab/kullm-v2](https://huggingface.co/nlpai-lab/kullm-polyglot-12.8b-v2)

#### Translate dataset

Translated 'instruction', 'input', and 'output' in the dataset via the DeepL API

## Lisence
Apache-2.0


```python
>>> from datasets import load_dataset

>>> ds = load_dataset("nlpai-lab/kullm-v2", split="train")
>>> ds
DatasetDict({
    train: Dataset({
        features: ['id', 'instruction', 'input', 'output'],
        num_rows: 152630
    })
})
```

```python
>>> ds[0]
{'id': 'alpaca_{idx}',
 'instruction': '3원색이란 무엇인가요?',
 'input': '',
 'output': '세 가지 기본 색은 빨강, 파랑, 노랑입니다. 이 색은 다른 색을 혼합하여 만들 수 없고 다른 모든 색은 다양한 비율로 조합하여 만들 수 있기 때문에 원색이라고 부릅니다. 빛에 사용되는 첨가제 색상 시스템에서 원색은 빨강, 녹색, 파랑(RGB)입니다.'}
```