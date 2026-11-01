# Dense·Sparse·Hybrid 공식 검색 평가

- 골든셋: `test/retrieval_queries.jsonl` (48개 질의)
- 후보 corpus: 3,604개 (Core + Low Popularity)
- 임베딩: `text-embedding-3-small`
- 정답 라벨: metadata qrels 274개 / 라벨 질의 46개
- 라벨 버전: `assistant_curated_metadata_v2`
- `q34`는 hard constraint상 적합 후보 없음, `q48`은 의도적인 abstention으로 ranking 평균에서 제외했다.

## 전체 공식 지표

| 방식 | 라벨 질의 | Recall@5 | MRR | nDCG@5 | Hit@5 | Hard precision@5 | Keyword hit@5 proxy | 평균 latency(ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| dense | 46 | 0.3291 | 0.4924 | 0.3552 | 0.7826 | 100.0% | 65.6% | 113.01 |
| sparse | 46 | 0.4954 | 0.7337 | 0.5736 | 0.8696 | 100.0% | 79.0% | 74.56 |
| hybrid | 46 | 0.5326 | 0.7091 | 0.5995 | 0.9130 | 100.0% | 79.0% | 73.89 |

## 질의 유형별 Hit@5

| 유형 | 질의 | 라벨 | Dense | Sparse | Hybrid |
|---|---:|---:|---:|---:|---:|
| `abstention` | 1 | 0 | — | — | — |
| `benchmark_lookup` | 5 | 5 | 0.8000 | 0.6000 | 0.6000 |
| `lexical_exact` | 5 | 5 | 0.8000 | 0.8000 | 0.8000 |
| `semantic_capability` | 7 | 7 | 1.0000 | 0.8571 | 1.0000 |
| `semantic_constraint` | 11 | 10 | 0.8000 | 1.0000 | 1.0000 |
| `structured_constraint` | 19 | 19 | 0.6842 | 0.8947 | 0.9474 |

## 질의 유형별 Recall@5 / MRR / nDCG@5

| 유형 | Dense R@5 | Sparse R@5 | Hybrid R@5 | Dense MRR | Sparse MRR | Hybrid MRR | Dense nDCG@5 | Sparse nDCG@5 | Hybrid nDCG@5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `abstention` | — | — | — | — | — | — | — | — | — |
| `benchmark_lookup` | 0.1900 | 0.2300 | 0.2800 | 0.4333 | 0.3167 | 0.3167 | 0.1952 | 0.2033 | 0.2271 |
| `lexical_exact` | 0.3500 | 0.6600 | 0.6100 | 0.4333 | 0.8000 | 0.8000 | 0.3253 | 0.6709 | 0.6484 |
| `semantic_capability` | 0.2801 | 0.3407 | 0.3915 | 0.5095 | 0.7857 | 0.8143 | 0.3717 | 0.5679 | 0.6623 |
| `semantic_constraint` | 0.4966 | 0.5981 | 0.5952 | 0.5417 | 0.9000 | 0.7750 | 0.5014 | 0.7335 | 0.6675 |
| `structured_constraint` | 0.2902 | 0.5249 | 0.5978 | 0.4912 | 0.7193 | 0.7149 | 0.3223 | 0.5633 | 0.6257 |

## 정답 모델 라벨 보완

- hard filter 통과 여부, task 적합성, Korean evidence, parameter/context 조건, 모델 capability와 canonical 대안을 기준으로 검토했다.
- 기존 검색 결과 순위는 라벨 선정에 사용하지 않았다.
- 동일 query의 여러 모델은 모두 사용 가능한 정답 대안으로 취급했다.
- 기존 201개에서 274개로 73개 정답 ID를 보완했으며, 17개 질의를 확장했다.
- 모든 라벨 ID가 현재 3,604개 corpus에 존재하고 hard filter를 통과한다.
- qrels는 독립적인 사람 평가가 아닌 provisional expert qrels이므로 최종 품질 고정 전 일부 수동 검토가 필요하다.

## 지표 해석

- Recall@5: 정답 후보 중 상위 5개에 포함된 비율
- MRR: 첫 번째 정답 순위의 역수 평균
- nDCG@5: 정답을 상위 순위에 배치한 정도
- Hit@5: 상위 5개 안에 정답이 하나 이상 포함된 질의 비율
- Keyword hit@5는 보조 proxy이며 공식 ranking 지표가 아니다.
