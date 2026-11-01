---
language:
- ko
license: apache-2.0
tags:
- legal
- reranking
- text-pruning
- open-provence
- korean
- relevance
task_categories:
- text-classification
size_categories:
- 10K<n<100K
---

# legal-provence-ko-with-relevance

`legal-provence-ko`에 span 단위 relevance score를 추가한 데이터셋입니다.  
`ggh5454/open-provence-koen-legal` 모델 학습에 사용된 데이터셋입니다.

## Dataset Details

| Split | Rows |
|-------|------|
| train | 50,000 |
| validation | 1,000 |
| test | 1,000 |

## Features

| Feature | Type | 설명 |
|---------|------|------|
| `id` | string | 샘플 고유 ID |
| `query` | string | 검색 쿼리 |
| `texts` | list[string] | 후보 문서 목록 (8개) |
| `labels` | list[int] | 문서별 관련성 레이블 |
| `context_spans` | list[list[list[int]]] | span character offsets |
| `context_spans_relevance` | list[list[int]] | **span별 relevance 레이블** (1=관련, 0=비관련) |

## `context_spans_relevance` 생성 방법

`BAAI/bge-reranker-v2-m3`를 teacher 모델로 사용하여,  
각 span을 쿼리와 독립적으로 재랭킹하고 relevance를 이진 레이블로 변환.

## Usage

```python
from datasets import load_dataset

ds = load_dataset("ggh5454/legal-provence-ko-with-relevance")
sample = ds["train"][0]

print(sample["query"])
print(sample["context_spans_relevance"])  # span별 relevance: [[0,1,0,...], ...]
```

## Related

- [`ggh5454/legal-provence-ko`](https://huggingface.co/datasets/ggh5454/legal-provence-ko): relevance 없는 원본
- [`ggh5454/open-provence-koen-legal`](https://huggingface.co/ggh5454/open-provence-koen-legal): 이 데이터로 학습된 모델
