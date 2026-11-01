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
- debug
task_categories:
- text-classification
size_categories:
- n<1K
---

# legal-provence-ko-debug

`legal-provence-ko`의 소규모 디버그용 서브셋입니다.  
파이프라인 개발 및 빠른 실험에 사용합니다.

## Dataset Details

| Split | Rows |
|-------|------|
| train | 소규모 |
| validation | 소규모 |
| test | 소규모 |

## Features

`legal-provence-ko`와 동일한 구조입니다.

| Feature | Type | 설명 |
|---------|------|------|
| `id` | string | 샘플 고유 ID |
| `query` | string | 검색 쿼리 |
| `texts` | list[string] | 후보 문서 목록 |
| `labels` | list[int] | 문서별 관련성 레이블 |
| `context_spans` | list[list[list[int]]] | span character offsets |

## Related

- [`ggh5454/legal-provence-ko`](https://huggingface.co/datasets/ggh5454/legal-provence-ko): 전체 데이터셋
