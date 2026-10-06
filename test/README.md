# 검색 평가와 골든셋

`test/`는 Stage 1~4 산출물의 회귀 검증, dense·sparse·hybrid 검색 비교, Stage 3 evidence 연결 검증을 보관합니다.

## 골든셋

[`retrieval_queries.jsonl`](retrieval_queries.jsonl)은 총 48개 질의를 담습니다.

- standard 33개
- adversarial 15개
- 9개 수집 task, Core/Low Popularity, parameter/context, runtime, benchmark, 빈 결과 조건을 포함
- 각 질의에는 `query_type`, `query_signals`, `routing_hint`, `relevant_model_ids`가 기록됩니다.

질의 유형은 planner의 초기 라우팅 가설을 표현합니다. 유형은 6개이고 질의 내용으로 판정합니다. 한 질의에 여러 유형이 해당하면 **번호가 작은 유형**을 붙입니다.

| 번호 | 유형 | 의미 | 초기 라우팅 방향 |
|---:|---|---|---|
| 1 | `model_comparison` | 이름이 주어진 둘 이상의 모델을 같은 기준으로 비교 ("A랑 B 비교해줘") | 각 모델 직접 조회 → 메타데이터·근거 비교 |
| 2 | `reference_anchored` | 특정 모델을 기준점으로 대안·상대 조건·실행 가능 여부를 물음 ("X보다 작은", "X를 24GB에서 돌릴 수 있어?") | 기준 모델 조회 → 상대 조건을 수치로 변환 → hybrid |
| 3 | `identifier_match` | 모델 계열·베이스 모델·포맷·양자화·번역 방향 같은 식별자가 일치해야 정답 (KoBART, GGUF, AWQ, ko→zh) | Sparse 우선 |
| 4 | `benchmark_lookup` | benchmark·dataset·metric·README 평가 근거가 있어야 정답 | Sparse + benchmark boost |
| 5 | `constrained_search` | 파라미터·컨텍스트·VRAM·상업 라이선스·인기도·메타데이터 확인 같은 hard 조건이 하나 이상 있음 | metadata hard filter + hybrid |
| 6 | `semantic_capability` | 용도·능력을 자연어로 설명하고 위 hard 조건이 없음 | Dense 우선 |

판정 기준:

- `constrained_search`와 `semantic_capability`는 문장 표현이 아니라 **파싱된 조건**으로 나눕니다. 수치 조건(파라미터·컨텍스트·VRAM), 상업 라이선스, 인기도, 메타데이터 확인 조건이 있으면 `constrained_search`입니다. CPU·로컬 같은 runtime 조건만 있으면 `runtime_constraint` 신호로만 기록합니다.
- 상업 라이선스를 hard 조건으로 둘지는 아직 정하지 않았습니다. 현재 검색은 라이선스로 거르지 않으며, 정책이 정해지면 이 기준도 함께 바꿉니다.
- `constrained_search` 안에서 용도 설명이 거의 없는 조건 나열형 질의는 `routing_hint`의 dense 비중을 낮춥니다. 이전의 `structured_constraint`와 `semantic_constraint` 구분을 유형이 아니라 가중치로 옮긴 것입니다.
- `identifier_match`는 이전 `lexical_exact`를 대체합니다. 식별자 없이 크기 조건만 있는 번역 질의는 `constrained_search`입니다.
- `reference_anchored`와 `model_comparison`은 질의에 나온 모델명을 DB의 모델로 연결하는 단계가 필요합니다. "7.8B보다 작은"처럼 숫자만 있으면 기준 모델 조회가 필요 없으므로 `constrained_search`입니다.
- **한 질의에는 한 유형의 신호만 넣습니다.** 예를 들어 식별자 질의에 VRAM·라이선스 조건을 붙이거나, 벤치마크 질의에 크기 조건을 붙이지 않습니다. 언어(한국어), task, 실행 환경(CPU·로컬)은 어느 유형에나 들어갈 수 있는 공통 신호라서 섞여도 됩니다.
- Ollama·vLLM·llama.cpp·sentence-transformers 같은 실행 라이브러리 언급은 실행 환경 신호입니다. 정답이 그 포맷과 일치해야 할 때(GGUF, AWQ, ONNX 등)만 `identifier_match`입니다.
- 예외: 골든셋의 실제 사례 질의 g002·g003·g005는 번역 방향과 VRAM·라이선스 조건이 함께 있습니다. 원문 조건을 지키려고 그대로 두고, 번호 규칙에 따라 `identifier_match`로 둡니다.
- 빈 결과(abstention)는 질의 유형이 아닙니다. 미지원 task이거나 hard 조건을 만족하는 후보가 없을 때 검색을 멈추는 **종료 조건**으로 따로 다룹니다. 빈 결과가 기대되는 질의도 내용에 따라 1~6번 유형을 붙이고(예: q34·q48은 `constrained_search`), 기대 결과는 `relevance_status`에 남깁니다.
- 실행 가능 여부를 묻고 경고를 기대하는 질의(`warn_on_oversize`)는 `reference_anchored`로 분류하고, 기대 동작은 `labels.expected_behavior`에 남깁니다.

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
- 사람 판정 150개: 질의를 직접 쓰고 DB 후보를 0/1/2점으로 판정해 정답을 만들었습니다(`labels/judged_queries.jsonl`, 144개 채점 가능).
- Stage 1 수집 점검용 12개: 정답 모델이 DB에 없어 골든셋에서 빼고, 수집 규칙을 바꿀 때 recall 확인에만 씁니다.

채점은 [`evaluate_semantic_golden.py`](evaluate_semantic_golden.py)로 합니다. API 키 없이 돌리는 BM25 기준선(`golden/run_bm25_golden.py`)과 라벨 점검(`golden/audit_golden.py`)도 함께 있습니다.

Retrieval 고도화 실험(쿼리 유형별 Pre-Retrieval·Dense/Sparse 조합)은 계획서의 7개 유형(`plan_query_type`)으로 나눠 [`retrieval_lab/`](../retrieval_lab/README.md)에서 돌립니다.
