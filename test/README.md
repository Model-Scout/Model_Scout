# 검색 평가와 골든셋

`test/`는 Stage 1~4 산출물의 회귀 검증, dense·sparse·hybrid 검색 비교, Stage 3 evidence 연결 검증을 보관합니다.

## 골든셋

[`retrieval_queries.jsonl`](retrieval_queries.jsonl)은 총 48개 질의를 담습니다.

- standard 33개
- adversarial 15개
- 9개 수집 task, Core/Low Popularity, parameter/context, runtime, benchmark, 빈 결과 조건을 포함
- 각 질의에는 `query_type`, `query_signals`, `routing_hint`, `relevant_model_ids`가 기록됩니다.

질의 유형은 planner의 초기 라우팅 가설을 표현합니다.

| 유형 | 의미 | 초기 라우팅 방향 |
|---|---|---|
| `semantic_capability` | 자연어로 능력과 용도를 설명 | Dense 우선 |
| `lexical_exact` | 모델명, 번역 방향, 형식명처럼 정확한 문자열이 중요 | Sparse 우선 |
| `structured_constraint` | task, parameter, context, popularity 등 구조화 조건 중심 | metadata filter + Sparse |
| `benchmark_lookup` | benchmark, dataset, metric, README 근거를 찾음 | Sparse + benchmark boost |
| `semantic_constraint` | 능력·task와 수치 조건이 함께 있음 | Dense/Sparse hybrid |
| `abstention` | 조건상 적합 후보가 없어야 함 | 빈 결과 검증 |

`routing_hint`는 정답 가중치가 아닙니다. 실제 운영 planner는 질의 분류, hard filter, 결과 품질과 사용자 feedback을 함께 사용해 가중치를 조정해야 합니다.

## 공식 평가 지표

`relevant_model_ids`가 있는 질의에는 다음 지표를 계산합니다.

- **Recall@5**: 관련 모델 중 상위 5개에 포함된 비율
- **MRR**: 첫 관련 모델의 순위 역수
- **nDCG@5**: 관련도와 순위를 함께 반영한 지표
- **Hit@5**: 상위 5개에 관련 모델이 하나라도 포함되는지

보조 지표로 `keyword_hit@5`, `hard_constraint_precision@5`, evidence completeness, invalid evidence ref, uncited claim, missing quote를 기록합니다. `keyword_hit`는 공식 relevance를 대신하지 않습니다.

## 검색 모드 비교

```bash
source ~/main/bin/activate
python test/evaluate_retrieval_modes.py
```

결과 파일:

- [`retrieval_accuracy_by_type.md`](retrieval_accuracy_by_type.md)
- [`retrieval_accuracy_by_type.json`](retrieval_accuracy_by_type.json)
- [`dense_sparse_comparison_all48.md`](dense_sparse_comparison_all48.md)
- [`dense_sparse_comparison_all48.json`](dense_sparse_comparison_all48.json)
- [`dense_sparse_comparison.md`](dense_sparse_comparison.md)
- [`dense_sparse_comparison.json`](dense_sparse_comparison.json)

세 모드는 같은 Core + Low Popularity 후보와 같은 hard filter를 사용합니다.

- Dense: Stage 4 cosine similarity
- Sparse: model ID, translation pair, task, language, benchmark, 기술 metadata를 분리한 fielded lexical/BM25 score
- Hybrid: 질의 유형의 `routing_hint`를 초기 가중치로 사용한 결합 점수

모든 모드에 task conflict penalty, benchmark boost, canonical/author diversification과 evidence 표시를 공통 적용해야 공정한 비교가 됩니다. local latency는 로컬 구현의 비교값이며 Supabase와 OpenSearch의 운영 네트워크 latency를 직접 의미하지 않습니다.

`compare_dense_sparse.py`는 기존 dense snapshot과 local BM25 proxy를 재현하는 보조 도구입니다. 공식 유형별 지표와 최신 골든셋 평가는 `evaluate_retrieval_modes.py`를 사용합니다.

## 검색·근거 검증

```bash
python 05_validate_retrieval.py --execute
python test/evaluate_retrieval_golden.py \
  --validation test/stage4_retrieval_validation.json \
  --report test/stage4_golden_set_evaluation.md
```

`05_validate_retrieval.py`는 task, 한국어 조건, parameter/context, popularity, task conflict, canonical 중복, 빈 결과를 확인합니다. Stage 2·3 상세 row를 hydrate해 README section, supporting quote, evidence level을 결과에 붙이고, invalid reference·uncited claim·missing quote를 검사합니다.

## Stage 3 청킹 평가

`stage3_chunking_comparison.md`와 JSON은 section-aware, fixed-window, packed, hierarchical, atomic-evidence 계열을 10~20개 표본으로 비교한 기록입니다. 최종 Stage 3는 atomic evidence와 Parent–Child 관계를 사용하며, claim이 원문 quote를 가리키도록 합니다.

## 해석상 주의

- 골든셋의 `relevant_model_ids`와 relevance label은 사람이 만든 provisional label입니다. 운영 전 유형별 상위 결과를 추가 검토해야 합니다.
- 질의 유형별 표본 수가 작으면 Recall·MRR·nDCG의 분산이 큽니다.
- benchmark self-reported 수치와 `keyword_hit`는 근거의 존재를 보조할 뿐 모델 품질을 보증하지 않습니다.
- 임베딩 API를 새로 호출하는 평가는 `--execute`일 때 비용이 발생할 수 있습니다.

## 실제 사례 기반 semantic 골든셋

[`golden/`](golden/README.md)은 실제 한국어 프로젝트의 모델 선정 사례 57건에서 만든 별도 골든셋입니다. 위 48개 질의와 달리 정답을 사례 원문에서 가져왔고, 원문 URL·인용·신뢰도 등급(A/B/C)을 함께 기록합니다.

- 골든셋 28개: 현재 DB(Core·Low Popularity)에 정답 모델이 있는 질의입니다. 근거 사례의 원문을 직접 열어 확인했습니다.
- 사람 판정 배치 72개: 질의를 직접 쓰고 DB 후보를 0/1/2점으로 판정해 정답을 만드는 중입니다.
- Stage 1 수집 점검용 12개: 정답 모델이 DB에 없어 골든셋에서 빼고, 수집 규칙을 바꿀 때 recall 확인에만 씁니다.

채점은 [`evaluate_semantic_golden.py`](evaluate_semantic_golden.py)로 합니다. API 키 없이 돌리는 BM25 기준선(`golden/run_bm25_golden.py`)과 라벨 점검(`golden/audit_golden.py`)도 함께 있습니다.
