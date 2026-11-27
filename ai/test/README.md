# 검색 실험 지도

Model Scout 의 검색 성능을 어떻게 재고 어떻게 고쳤는지 한곳에서 찾아가는 안내다. 실험 파일은 각자 폴더에 그대로 두고, 이 문서가 목차 역할을 한다. 운영 스크립트(`05_validate_retrieval.py` 등)와 실험 도구가 경로로 서로 묶여 있어서, 파일 위치는 바꾸지 않았다.

## 1. 최종 성능 (2026-11-27)

서비스 설정 그대로 골든셋으로 잰 값이다. 자세한 지표·원인 분석·재실행은 [`final_search_eval/`](final_search_eval/README.md)에 있다.

| | 모델 검색 | 공공데이터 검색 |
|---|---:|---:|
| 상위 3개 안에 정답 (Hit@3) | **90.6%** (쓸 만한 모델 기준) | **97.7%** (딱 맞는 데이터 기준) |
| 상위 5개 안에 딱 맞는 정답 (Hit@5) | 75.0% | **100%** |
| 첫 정답 순위 (MRR@10, 쓸 만한 결과 기준) | 0.841 | 0.956 |

- 모델 수치는 planner 가 검색까지 보낸 역할 32개 기준이다. 만들지 않은 역할까지 0점으로 넣으면 Hit@3 는 73.9%다.
- 모델은 프로젝트형 30문항, 공공데이터는 골든셋 v2 의 추천 질문 53개로 쟀다.

## 2. 폴더 안내

| 폴더·파일 | 무엇 | 골든셋 |
|---|---|---|
| [`final_search_eval/`](final_search_eval/README.md) | **최종 성능 측정.** 운영 라우터·planner·검색을 그대로 돌려 잰다 | 모델 프로젝트형 30문항, 공공데이터 v2 53문항 |
| [`model_retrieval/`](model_retrieval/README.md) | **모델 검색 튜닝.** sparse 진단, IDF sparse, 유형별 가중치, LLM 리랭커, pre-retrieval 실험 | 모델 240문항(6유형 × 40) |
| [`public_data/`](public_data/README.md) | **공공데이터 검색.** 골든셋 구축, 코퍼스 v2 비교, 검색 경로·결합·분해 실험([`retrieval/`](public_data/retrieval/README.md)), 별도 질문 검증([`holdout/`](public_data/holdout/README.md)) | 58문항(라벨 v9) + holdout 32문항 |
| [`golden/`](golden/README.md) | 실제 프로젝트 사례로 만든 초기 모델 골든셋 | 사례 기반 28개 + 사람 판정 150개 |
| 최상위 `stage*`·`dense_sparse_*`·`retrieval_*` | 초기 Stage 4 검증 기록([4절](#4-초기-검증-stage-4)). `05_validate_retrieval.py` 가 직접 읽고 쓰므로 옮기지 않는다 | 48문항 |
| `test_*.py`, `conftest.py` | 단위 테스트. `pytest` 로 돌린다 | — |

## 3. 실험 기록

### 모델 검색

지표는 240문항 골든셋의 recall@5(2점 정답 기준)이고, 운영이 need 마다 상위 5개를 돌려주는 것과 같은 깊이다. 모든 측정은 앞 단계를 반영한 상태에서 다음 단계를 쌓았다.

| 순서 | 바꾼 것 | 결과 | 결정 | 근거 |
|---:|---|---|---|---|
| 1 | **진단:** 운영 하이브리드 검색의 sparse 점수가 항상 0 | `plainto_tsquery` 가 모든 단어를 AND 로 묶고, 검색 컬럼이 영어 메타데이터뿐이라 한국어가 섞인 질의는 매칭 0행. 즉 검색이 사실상 100% dense 였다 | 아래 3에서 수정 | [`model_retrieval/README.md`](model_retrieval/README.md) §2, `tools/diagnose_sparse.py` |
| 2 | 분해가 내는 task 키(`language_modeling`, `vision`)를 HF 태그로 잇기 (`MODEL_TASK_FALLBACK`) | 결과 0건 질의 53 → 3개, recall@5 0.265 → 0.331 | 채택 | `tools/final_compare.py` ② |
| 3 | sparse 를 IDF 가중 매칭 비율로 교체 | 0.331 → 0.350 | 채택 (`MODEL_SPARSE_IDF_ENABLED=1`, `supabase_migration_sparse_idf.sql`) | `tools/sparse_idf.py`, `final_compare.py` ③ |
| 4 | 질문 유형 6개별 dense:sparse 비중 (`MODEL_DENSE_WEIGHTS`) | 0.350 → 0.390. 1~4 합계는 운영 대비 **+0.125 [+0.085, +0.166]**, 상대 +47% | 채택 | `tools/tune.py`, `final_compare.py` ④ |
| 5 | 벤치마크 질문은 task 필터 해제 (`TASK_FILTER_FREE_TYPES`) | benchmark_lookup 0.305 → 0.524 | 채택 | `17_recommend_graph.search_models` 주석 |
| 6 | LLM 리랭커(gpt-4.1-mini, 상위 20개)를 효과가 증명된 4유형에만 | 0.444 → **0.521 [+0.040, +0.115]**. 조건 나열형 2유형은 리랭크하면 나빠져서 제외 | 채택 | [`model_rerank.py`](../model_rerank.py) 머리말, `tools/rerank_llm.py` |
| 7 | pre-retrieval 4종: 질의 재작성, multi-query, multi-query + 원문, HyDE | 재작성 −0.013, multi-query −0.007, multi-query + 원문 −0.025, **HyDE +0.025 [+0.003, +0.048]** | 보류. HyDE 는 리랭커와 함께 다시 재야 한다 | `tools/preretrieval.py`, `runs/scores_idf_dectf_sg_nt_{rw,mq,mqb,hy}.json` |
| 8 | 프로젝트 질문 경로에 모델 리랭커 켜기 | Recall@5(1점 이상) +6.6%p [+0.8, +12.8], 그 밖의 지표는 미확정 | 보류 (project 경로는 리랭크 꺼짐 유지) | [`final_search_eval/`](final_search_eval/README.md) |

- 4번까지의 값(0.390)은 운영과 같은 방법으로 **예측한** 질문 유형으로 쟀다. 정답 유형을 넣으면 0.405 가 상한이다.
- 7번은 벤치마크 질문을 뺀 recall@5 이고, 리랭크 없이 쟀다. 벤치마크 질문은 dense 상위 300개만 다시 채점하는 측정 방식 때문에 값이 왜곡돼서 뺐다.

### 공공데이터 검색

| 바꾼 것 | 결과 | 결정 | 근거 |
|---|---|---|---|
| 코퍼스 v2 고정본(`aa1a71d35a121150`)으로 교체 | v1 과 같은 질문으로 비교 | 채택 (서버는 v2 로 운영) | [`public_data/corpus_v2/`](public_data/corpus_v2/README.md) |
| 검색 경로·dense:BM25 가중치·채널 결합·질의 분해 비교 | 파일럿과 별도 질문 검증 | 실험 결과별로 정리 | [`public_data/retrieval/README.md`](public_data/retrieval/README.md), [`public_data/holdout/README.md`](public_data/holdout/README.md) |
| LLM 재정렬(gpt-4.1-mini, 상위 20개) | nDCG@5 0.625 → 0.750 (개발셋), 0.525 → 0.670 (별도 질문) | 채택 (`dataset_rerank.py`) | [`dataset_rerank.py`](../dataset_rerank.py) 머리말 |
| 최종 측정에서 재정렬 효과 다시 확인 | Hit@3 79.1% → 97.7%, MRR@10 0.644 → 0.944 | — | [`final_search_eval/`](final_search_eval/README.md) |

### 다음에 할 것

[최종 측정](final_search_eval/README.md#모델-recall-이-공공데이터보다-낮은-이유)에서 모델 검색 성능을 가장 많이 깎은 원인은 검색이 아니라 planner 였다. 우선순위 순서대로 적는다.

1. planner 역할 분해 보강: QA 챗봇의 임베딩·LLM, 리랭커, 음성인식 역할이 빠지지 않게
2. 같은 모델의 양자화 재포장본을 한 카드로 묶기
3. HyDE 를 리랭커와 함께 다시 재기

## 4. 초기 검증 (Stage 4)

프로젝트 초기에 Stage 1~4 산출물을 검증하던 기록이다. 지금 운영 검색(Supabase RPC + IDF sparse + 유형별 가중치)과는 검색 방식이 달라서, 성능 수치는 위 3절을 본다.

- **골든셋:** [`retrieval_queries.jsonl`](retrieval_queries.jsonl) 48문항(standard 33, adversarial 15)이다. 질문마다 `query_type`, `routing_hint`, `relevant_model_ids` 가 붙어 있다.
- **검색 모드 비교:** `evaluate_retrieval_modes.py` 로 dense·sparse·hybrid 를 비교한다. 결과는 [`retrieval_accuracy_by_type.md`](retrieval_accuracy_by_type.md), [`dense_sparse_comparison_all48.md`](dense_sparse_comparison_all48.md), [`dense_sparse_comparison.md`](dense_sparse_comparison.md)에 있다.
- **검색·근거 검증:** `05_validate_retrieval.py` 가 task·한국어·크기·중복·빈 결과 조건과 근거 인용(README 구절, 인용 누락)을 검사한다. 결과는 [`stage4_retrieval_validation.md`](stage4_retrieval_validation.md), [`stage4_golden_set_evaluation.md`](stage4_golden_set_evaluation.md)에 있다.
- **청킹 비교:** [`stage3_chunking_comparison.md`](stage3_chunking_comparison.md). 최종 Stage 3 는 atomic evidence 와 Parent–Child 관계를 쓴다.

```bash
# ai/ 에서
python test/evaluate_retrieval_modes.py
python 05_validate_retrieval.py --execute
python test/evaluate_retrieval_golden.py \
  --validation test/stage4_retrieval_validation.json \
  --report test/stage4_golden_set_evaluation.md
```

48문항의 정답은 사람이 만든 잠정 라벨이고 유형별 표본이 작다. 임베딩을 새로 호출하는 평가(`--execute`)는 비용이 든다.
