# 검색 평가와 골든셋

`test/`는 Stage 3 evidence, Stage 4 dense vector, sparse metadata 검색, planner-weighted hybrid 검색을 검증하는 질의와 평가 결과를 보관합니다.

## 골든셋

[`retrieval_queries.jsonl`](retrieval_queries.jsonl)은 48개 질의를 담고 있습니다.

- standard 질의 33개
- adversarial 질의 15개
- 9개 수집 task, Core/Low Popularity, parameter/context, runtime, benchmark, 빈 결과 조건을 포함
- 각 질의에 `query_type`, `query_signals`, `routing_hint`, `relevant_model_ids`가 기록됨

질의 유형은 다음처럼 분류합니다.

| 유형 | 의미 | 초기 라우팅 방향 |
|---|---|---|
| `semantic_capability` | 자연어로 능력과 용도를 설명하는 질의 | Dense 우선 |
| `lexical_exact` | 모델명, 번역 방향, 형식명처럼 정확한 문자열이 중요한 질의 | Sparse 우선 |
| `structured_constraint` | task, parameter, context, popularity 등 구조화 조건 중심 | metadata filter + Sparse |
| `benchmark_lookup` | benchmark, dataset, metric, README 근거를 찾는 질의 | Sparse + benchmark boost |
| `semantic_constraint` | 한국어 능력·task와 수치 조건이 함께 있는 질의 | Dense/Sparse hybrid |
| `abstention` | 조건상 적합 후보가 없어야 하는 질의 | 빈 결과 검증 |

`routing_hint`는 planner의 초기 가설입니다. 정답 가중치가 아니며, 사람의 relevance label과 유형별 평가 결과로 조정해야 합니다.

## 평가 지표

사람이 `relevant_model_ids`를 지정한 질의에는 다음 공식 지표를 사용합니다.

- `Recall@5`: 관련 모델 중 상위 5개에 포함된 비율
- `MRR`: 첫 관련 모델의 역순위
- `nDCG@5`: 순위와 relevance를 함께 반영한 점수
- `Hit@5`: 상위 5개 안에 관련 모델이 하나라도 있는지

`keyword_hit@5`와 `hard_constraint_precision@5`는 relevance label이 없는 질의의 회귀용 proxy입니다. 이 값을 semantic Recall로 해석하지 않습니다.

최근 저장된 유형별 결과는 [`retrieval_accuracy_by_type.md`](retrieval_accuracy_by_type.md)와 JSON 파일에 있습니다. 평가 report는 생성 시점의 local corpus를 기록하므로, corpus가 변경되면 다음 명령으로 다시 생성해야 합니다.

```bash
source ~/main/bin/activate
python test/evaluate_retrieval_modes.py
```

Dense·Sparse 비교 원본은 다음 파일입니다.

- [`dense_sparse_comparison_all48.md`](dense_sparse_comparison_all48.md)
- [`dense_sparse_comparison_all48.json`](dense_sparse_comparison_all48.json)
- [`dense_sparse_comparison.md`](dense_sparse_comparison.md)
- [`dense_sparse_comparison.json`](dense_sparse_comparison.json)

## 검색 공정성

모든 모드는 같은 Core + Low Popularity 후보와 같은 hard filter를 사용합니다.

- Dense: Stage 4 vector cosine similarity
- Sparse: model ID, translation pair, task, language, benchmark, technical metadata를 분리한 fielded BM25/lexical score
- Hybrid: 질의 유형의 `routing_hint`를 초기 가중치로 사용하는 결합 점수

세 모드 모두 task conflict penalty, benchmark boost, canonical/author diversification, evidence reranking을 공통 적용합니다. local latency는 구현별 측정값일 뿐 네트워크가 있는 OpenSearch와 Supabase의 운영 지연을 직접 비교한 값이 아닙니다.

## 근거 검증

`05_validate_retrieval.py`는 검색 결과마다 다음을 검사합니다.

- task, 한국어, parameter/context, popularity hard constraint
- task conflict와 canonical 중복
- Stage 3 evidence reference와 supporting quote
- Parent section과 Child claim 연결
- 빈 결과가 필요한 abstention 질의

상세 결과는 `stage4_retrieval_validation.md`와 `stage4_golden_set_evaluation.md`에 저장합니다. 검색 결과를 사용자에게 표시할 때는 Stage 2·3 상세 row를 hydrate해 README section, supporting quote, evidence level을 함께 보여줍니다.

## 재현 시 주의

- Stage 4 임베딩 API를 새로 호출하는 평가는 비용이 발생할 수 있습니다.
- `OPENAI_API_KEY`가 없으면 질의 embedding을 만들 수 없습니다.
- 기존 결과를 재사용하는 옵션은 오프라인 점검용이며, 변경된 corpus에 대한 완전한 재평가를 대신하지 않습니다.
- 골든셋의 relevance label은 사람이 만든 provisional label입니다. 운영 전 유형별 상위 결과를 추가 검토해야 합니다.
