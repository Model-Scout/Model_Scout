# 검색 골든셋과 Dense·Sparse 비교

이 디렉터리는 Stage 3·4 검색 품질을 검증하는 질의, 비교 결과, 회귀 테스트를 보관한다.

## 골든셋

[`retrieval_queries.jsonl`](retrieval_queries.jsonl)은 현재 48개 질의를 담고 있다.

- `standard`: 33개
- `adversarial`: 15개
- 수집 대상 9개 task 전체, Core·Low Popularity, parameter/context 조건, benchmark 질의를 포함한다.
- `query_schema_version: 2`부터 planner용 분류 필드를 함께 저장한다.

각 질의에는 다음 필드가 추가되어 있다.

```json
{
  "query_type": "semantic_constraint",
  "query_signals": ["language", "task", "numeric_constraint"],
  "routing_hint": {
    "primary": "hybrid",
    "dense_bias": "medium",
    "sparse_bias": "medium",
    "metadata_filter": "hard"
  }
}
```

`routing_hint`는 planner가 사용할 초기 가설이다. 정답 라벨이나 고정 가중치가 아니며, 사람이 relevant model ID를 라벨링한 후 유형별 성능으로 보정해야 한다.

## 질의 유형

| 유형 | 의미 | 초기 라우팅 방향 |
|---|---|---|
| `semantic_capability` | 자연어로 능력·용도를 설명하고 표현 변형을 이해해야 하는 질의 | Dense 우선 |
| `lexical_exact` | 번역 방향, 명시적 용어, 모델·형식명처럼 정확한 문자열이 중요한 질의 | BM25 우선 |
| `structured_constraint` | parameter, context, popularity, known metadata 등 구조화 조건이 중심인 질의 | metadata filter 우선 + Sparse 보조 |
| `benchmark_lookup` | MTEB·WER·dataset·metric·README 근거를 찾는 질의 | BM25와 benchmark boost 우선 |
| `semantic_constraint` | 한국어 능력·task와 수치 조건이 함께 있는 질의 | Dense·BM25 hybrid |
| `abstention` | 조건상 후보가 없어야 하는 질의 | 결과 없음 검증 |

유형은 질의의 형태를 설명한다. 특정 검색기가 항상 정답이라는 뜻은 아니다.

## Dense·Sparse 비교

비교 스크립트는 [`compare_dense_sparse.py`](compare_dense_sparse.py)다. 기존 Dense 결과는 [`stage4_retrieval_validation.json`](stage4_retrieval_validation.json)에서 재사용하고, 새 embedding API 호출은 하지 않는다.

Sparse는 OpenSearch의 `multi_match` field boost를 모사한 로컬 BM25 shadow index로 계산했다. 두 방식에 동일한 hard filter, canonical deduplication, task-conflict penalty, benchmark boost를 적용했다.

### 30개 표본

선택 기준은 표준 질의 27개(q31~q33 benchmark 포함)와 adversarial 질의 q34·q37·q39다. 9개 task, 두 pool, benchmark와 수치 조건을 모두 포함한다. q34는 조건상 후보가 없어 non-empty 질의는 29개다.

| 지표 | Dense | Sparse BM25 |
|---|---:|---:|
| Exact keyword hit@5 | 0.280 | 0.407 |
| Dense·Sparse top-5 agreement proxy | 0.227 | - |
| Sparse keyword 우세 질의 | 7/29 | - |
| Dense keyword 우세 질의 | 0/29 | - |

### 전체 48개 민감도 비교

선택 편향을 확인하기 위해 전체 골든셋도 같은 방식으로 계산했다.

| 지표 | Dense | Sparse BM25 |
|---|---:|---:|
| Exact keyword hit@5 | 0.287 | 0.412 |
| Dense·Sparse top-5 agreement proxy | 0.208 | - |
| Sparse keyword 우세 질의 | 11/46 | - |
| Dense keyword 우세 질의 | 0/46 | - |

유형별 원본 수치는 [`dense_sparse_comparison_all48.json`](dense_sparse_comparison_all48.json)의 `by_query_type`에 있다. 전체 결과에서 benchmark lookup은 Dense 0.800, Sparse 1.000, semantic constraint는 Dense 0.436, Sparse 0.636, structured constraint는 Dense 0.158, Sparse 0.305의 exact keyword hit@5를 보였다. 이 지표는 lexical 방식에 유리하므로 정확도의 단독 근거로 해석하지 않는다.

상세 결과:

- [30개 비교 Markdown](dense_sparse_comparison.md)
- [30개 비교 JSON](dense_sparse_comparison.json)
- [전체 48개 비교 Markdown](dense_sparse_comparison_all48.md)
- [전체 48개 비교 JSON](dense_sparse_comparison_all48.json)

## 공정성 및 한계

- Dense와 Sparse는 동일한 Stage 4 3,567개 후보와 동일한 hard filter를 사용했다.
- Dense top-5는 이전 vector validation 결과이고 Sparse는 같은 질의의 local BM25 ranking이다.
- OpenSearch 서버가 실행 중이지 않아 실제 OpenSearch network latency는 측정하지 않았다.
- Dense latency는 query embedding API 시간을 제외한 local vector rank 시간이며, Sparse latency는 최적화되지 않은 Python BM25 시간이다. 두 latency 수치는 production 비교가 아니다.
- 현재 골든셋에는 질의별 relevant model ID가 없다. 따라서 `agreement proxy`는 진짜 semantic Recall@5가 아니다.
- Exact keyword hit는 Sparse가 유리하도록 정의된 지표다. Sparse 도입의 근거는 keyword hit 단독이 아니라 Dense와 낮은 overlap을 보이는 보완성이다.

현재 결과는 Sparse를 Dense의 대체로 확정하는 근거가 아니라, planner가 질의 유형에 따라 Dense와 BM25의 가중치를 조절하는 hybrid 도입을 검토할 근거다. 최종 가중치는 질의별 relevant model ID를 사람이 라벨링한 relevance golden set으로 Recall@5, MRR, nDCG를 측정한 뒤 결정한다.

## Dense 점수가 낮아 보이는 이유

현재 `0.287`은 Dense의 semantic Recall@5가 아니라 결과 문서에 질의 keyword가 그대로 포함되는 비율이다. Dense가 표현이 다른 문서를 찾으면 이 지표에서는 정답이어도 hit로 세지지 않는다. 반대로 Sparse는 같은 keyword를 직접 점수화하므로 이 지표에서 유리하다.

Stage 3 청킹은 README에서 evidence span과 semantic claim을 만드는 단계다. Stage 4는 그 결과를 하나의 `embedding_text`로 합쳐 모델별 벡터 하나를 만들기 때문에 청킹 방식이 벡터 검색에 직접 적용되는 것은 아니다. 청킹은 semantic summary가 달라질 때만 간접적으로 영향을 준다.

현재 Dense 문서에는 model ID, task, language, architecture, parameter/context, runtime, popularity, Stage 3 summary와 claims가 함께 들어간다. 이 단일 텍스트 표현은 서로 다른 신호의 가중치가 없어서 generic claim이 query signal을 희석할 수 있다. 또한 Stage 1의 language metadata 오탐 후보가 있으면 Dense와 Sparse 모두 잘못된 후보를 검색할 수 있다. 예를 들어 sentence embedding 질의에서 Yoruba 특화 후보가 `korean_verified` metadata 때문에 통과한 사례가 확인됐다.

따라서 현재 우선순위는 embedding을 즉시 교체하는 것이 아니다.

1. relevance label이 있는 골든셋으로 semantic Recall@5를 먼저 측정한다.
2. 질의 유형별 Dense·BM25 hybrid와 metadata rerank를 비교한다.
3. 그래도 semantic 유형 성능이 낮을 때만 compact embedding text, semantic·metadata late fusion, `text-embedding-3-large` 또는 한국어 특화 embedding을 A/B 테스트한다.

## Dense DB 상태

마지막 Supabase 확인 기준으로 Core 1,451개와 Low Popularity 2,116개가 모두 적재되어 있으며, 각 행의 embedding dimension은 1,536이고 중복·비활성 행은 없었다. 비교 작업은 DB에 쓰지 않고 기존 Stage 4와 validation 결과만 읽었다.
