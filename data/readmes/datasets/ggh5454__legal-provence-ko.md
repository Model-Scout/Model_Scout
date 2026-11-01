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
task_categories:
- text-classification
size_categories:
- 10K<n<100K
---

# legal-provence-ko

한국 법률 문서(판례, 판결문, 법령)로 구성된 OpenProvence 형식의 데이터셋입니다.  
쿼리-문서 쌍에 대해 관련 span의 character offset을 레이블로 포함합니다.

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
| `labels` | list[int] | 문서별 관련성 레이블 (1=관련, 0=비관련) |
| `context_spans` | list[list[list[int]]] | 문서별 span의 character offset [start, end] |

## Data Source

- 한국 법원 판례 및 판결문
- 부가가치세법, 시행령, 시행규칙 등 법령 문서
- OpenProvence 형식으로 변환 (span-level annotation)

## Related

- [`ggh5454/legal-provence-ko-with-relevance`](https://huggingface.co/datasets/ggh5454/legal-provence-ko-with-relevance): span 단위 relevance score 추가 버전
- [`ggh5454/open-provence-koen-legal`](https://huggingface.co/ggh5454/open-provence-koen-legal): 이 데이터셋으로 학습된 모델
