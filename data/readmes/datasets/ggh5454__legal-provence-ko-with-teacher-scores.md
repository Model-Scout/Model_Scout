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
- teacher-scores
- knowledge-distillation
task_categories:
- text-classification
size_categories:
- 10K<n<100K
---

# legal-provence-ko-with-teacher-scores

`legal-provence-ko-with-relevance`에 teacher model의 reranking score를 추가한 최종 훈련용 데이터셋입니다.  
`ggh5454/open-provence-koen-legal` 모델 학습에 직접 사용된 데이터셋입니다.

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
| `context_spans_relevance` | list[list[int]] | span별 relevance 레이블 |
| `teacher_scores.bge-reranker-v2-m3` | list[float] | Teacher 모델의 reranking score |

## Teacher Model

- **Teacher**: `BAAI/bge-reranker-v2-m3`
- Score distillation을 통해 문서별 relevance score를 제공
- 훈련 시 `teacher_column: teacher_scores.bge-reranker-v2-m3` 로 참조

## Related

- [`ggh5454/legal-provence-ko-with-relevance`](https://huggingface.co/datasets/ggh5454/legal-provence-ko-with-relevance): teacher score 없는 버전
- [`ggh5454/open-provence-koen-legal`](https://huggingface.co/ggh5454/open-provence-koen-legal): 이 데이터로 학습된 모델
