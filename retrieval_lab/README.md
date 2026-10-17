# Retrieval 실험 환경 (retrieval_lab)

쿼리 유형별로 가장 좋은 Pre-Retrieval·Retrieval 조합을 골든셋으로 찾고, 그 결과를 Retrieval Planner(`planner_config.json`)에 기록하는 실험 코드다.

```text
User Query
→ Query Type (골든셋의 plan_query_type 사용, 분류기는 아직 없음)
→ Pre-Retrieval: Rewrite / Decomposition / Multi-Query / HyDE   pre_retrieval.py
→ Retrieval Planner: hard filter, dense/sparse weight, top_k   planner.py
→ Dense: BGE-M3 (BAAI/bge-m3)                                   dense.py
→ Sparse: fielded BM25 (05_validate_retrieval.py와 같은 점수)    corpus.py
→ Weighted RRF (k=60)                                           fusion.py
→ Top-K 후보 (기본 30)                                           pipeline.py
```

## 담당

| 유형 | 의미 | 담당 | 채점 질의 |
|---|---|---|---:|
| `model_comparison` | 이름이 명시된 모델 간 비교 | 예주 | 21 |
| `semantic_capability` | 자연어로 원하는 능력과 용도를 설명 | 예주 | 37 |
| `lexical_exact` | 모델명, 번역 방향, 형식명 등 정확한 문자열 중심 | 희원 | 21 |
| `structured_constraint` | Task, Parameter, Context 등 구조화 조건 중심 | 희원 | 24 |
| `benchmark_lookup` | Benchmark, Dataset, Metric, README 근거 탐색 | 정훈 | 18 |
| `semantic_constraint` | 의미적 요구와 수치 조건이 함께 존재 | 정훈 | 47 |
| `abstention` | 조건에 맞는 후보가 없어야 함 | 공통 | 0 (작성 필요) |

채점 질의는 `evaluable_now`이면서 정답 라벨이 있는 질의 수다(골든셋 28 + 판정 150 기준). 유형 매핑은 [`test/golden/labels/plan_query_types.json`](../test/golden/labels/plan_query_types.json)에 있다.

- 라벨의 6개 유형 중 `identifier_match`는 `lexical_exact`, `reference_anchored`는 `semantic_constraint`로 옮겼다.
- `constrained_search` 53개는 문장을 읽고 나눴다. task 이름 외에 용도·도메인·능력(회의록, RAG, 리랭커, OCR, 감성분석, 코딩, 잡음 음성 등)을 설명하면 `semantic_constraint`(29개), task와 수치·라이선스·실행 환경 조건만 나열하면 `structured_constraint`(24개)다. 경계가 애매하면 이 파일을 고치고 `convert_golden.py`를 다시 실행한다.
- `benchmark_lookup`은 18개로 목표(20~25)보다 적고, `semantic_constraint`는 47개로 많다. `abstention` 질의는 아직 없다(아래 참고).

## 설치

```bash
python -m venv .venv
.venv\Scripts\activate            # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pip install torch --index-url https://download.pytorch.org/whl/cpu   # GPU가 있으면 생략
pip install -r requirements_retrieval.txt
```

`.env`에 `OPENAI_API_KEY`가 있어야 Pre-Retrieval LLM을 새로 호출할 수 있다. 모델은 `PRE_RETRIEVAL_LLM_MODEL`(기본 `gpt-4o-mini`, Stage 3와 같음)로 바꾼다.

## 준비물: BGE-M3 문서 인덱스

`data/retrieval_lab/bge_m3_doc_embeddings.npy`(3,606 × 1,024, float16)와 manifest가 커밋돼 있으면 바로 실험할 수 있다. 없거나 corpus가 바뀌었으면 다시 만든다.

```bash
python -m retrieval_lab.dense --build
```

- 문서는 Stage 4의 `embedding_text`(운영 OpenAI 임베딩과 같은 텍스트), 최대 1,024 토큰이다.
- 노트북 CPU에서는 문서당 5~8초라 수 시간이 걸린다. GPU(Colab T4 등)에서는 수 분이다. 64개 단위로 `data/retrieval_lab/.bge_m3_build/`에 저장하므로 중단돼도 다시 실행하면 이어서 만든다.
- manifest에 문서별 해시가 있어서, corpus가 바뀌었는데 인덱스가 옛것이면 실험이 에러로 멈춘다.

## 실험 실행

```bash
# 내 유형만: Baseline → 단일 A/B 4개 → 개선 요소 조합 → dense weight 탐색(Optuna)
python -m retrieval_lab.experiment --types semantic_capability,model_comparison

# 단계별로 끊어서
python -m retrieval_lab.experiment --types lexical_exact --stage baseline   # LLM 불필요
python -m retrieval_lab.experiment --types lexical_exact --stage single
python -m retrieval_lab.experiment --types lexical_exact --stage weight     # Pre-Retrieval 없이 가중치만, LLM 불필요

# 결과를 planner에 반영
python -m retrieval_lab.experiment --types benchmark_lookup --write-planner
```

| 옵션 | 기본 | 뜻 |
|---|---|---|
| `--metric` | `recall@10` | 개선 판단과 최적 선택 기준 |
| `--min-grade` | 1 | 1이면 정답(2점)+허용(1점)을 관련으로 본다. 2면 정답만 |
| `--min-delta` | 0 | 단일 요소가 Baseline보다 이만큼 넘게 좋아야 "개선" |
| `--weight-search` | `optuna` | `optuna` · `grid`(0.1~0.9, 0.1 간격) · `none` |
| `--trials` | 20 | Optuna 시행 수. 앞의 9회는 0.1~0.9 grid(0.1 간격), 나머지는 TPE가 0.05 간격으로 탐색 |

결과는 `retrieval_lab/reports/<유형>.md`(계획서 형식의 실험표, 조합표, 가중치표, top-10에서 놓친 모델)와 `.json`(질의별 순위·지표·지연)에 저장된다.

### 실험 규칙

1. **Baseline**: BGE-M3 + BM25, Weighted RRF, dense 0.5 / sparse 0.5, Pre-Retrieval 모두 OFF.
2. **채널 비교**: Pre-Retrieval 없이 Dense only(weight 1.0), Sparse only(0.0), Hybrid(0.5)를 비교한다.
3. **단일 A/B**: Rewrite, Decomposition, Multi-Query, HyDE를 하나씩 켠다.
4. **조합**: 단일 실험에서 `--metric`이 Baseline보다 오른 요소만 2개 이상씩 모든 조합을 돌린다.
5. **가중치 탐색**: 가장 좋은 설정에서 dense weight를 0.1~0.9로 바꾸고 sparse = 1 − dense로 둔다. 가장 좋은 설정이 Pre-Retrieval을 쓰면 Baseline에서도 탐색해, LLM 없이 가중치만으로 같은 성능이 나오는지 확인한다.
6. 최적 설정은 `--metric` → Recall@5 → nDCG@5 → 사전 검색 호출 수가 적은 것 → p95가 낮은 것 순으로 고른다.
7. **추가 판정**: 리포트의 "추가 판정이 필요한 후보"(JSON `unjudged_pool`)를 판정실에서 판정하고 라벨을 다시 만든 뒤(`import_judgments.py` → `convert_golden.py`) 실험을 다시 돌린다. BM25 단독으로 재 보면 top-10 중 판정된 모델이 유형별 10~20%뿐이라(2026-10-04), 이 단계 없이 고른 최적값은 믿기 어렵다.
   - 판정실 밖에서 한 추가 판정은 [`test/golden/labels/supplemental_judgments.jsonl`](../test/golden/labels/supplemental_judgments.jsonl)에 둔다(질의 ID·모델·점수 2/1/0·이유·판정자). 실험은 기존 라벨에 없는 모델에만 이 점수를 더한다. 기존 라벨이 항상 우선이다. `--no-supplement`를 주면 기존 라벨만으로 채점한다.
   - 2026-10-17 semantic_capability 후보 1,358쌍은 Claude가 1차 판정했다(`judge: "claude"`). 사람 검수 전이므로 회의 자료에는 "LLM 1차 판정"으로 밝힌다.

### 각 Pre-Retrieval이 하는 일

| 전략 | LLM 출력 | 검색에 쓰는 방식 |
|---|---|---|
| Rewrite | 영어 기술 용어를 덧붙인 검색 질의 1개 | 두 채널의 기본 질의를 대체 |
| Decomposition | 요구 측면별 하위 질의 2~4개 | 두 채널에 질의로 추가 |
| Multi-Query | 한국어·영어·키워드형 질의 3개 | 두 채널에 질의로 추가 |
| HyDE | 가상의 영어 모델 카드 요약 | dense 채널의 기본 질의를 대체 (sparse는 텍스트 질의 유지) |

- 모든 변환은 **원래 질의**를 입력으로 받아 병렬 실행을 가정한다. 지연은 가장 느린 변환 하나만 더한다.
- 질의가 여러 개면 채널마다 질의별 순위 리스트를 만들고, 채널 가중치를 리스트 수로 나눠 RRF에 넣는다. 그래서 dense/sparse weight의 뜻이 실험마다 같다.
- Hard filter는 골든셋에 적힌 조건(정답 조건)을 그대로 쓴다. 조건 파싱 오류는 이 실험에서 측정하지 않는다.
- 프롬프트는 [`pre_retrieval.py`](pre_retrieval.py)의 `PROMPTS`에 있다. 고치면 `PROMPT_VERSION`을 올린다(옛 캐시는 무시된다).

### LLM 캐시

LLM 출력은 `retrieval_lab/cache/pre_retrieval/<전략>/<해시>.json`에 질의 하나당 파일 하나로 저장된다. 캐시를 커밋하면 다른 사람은 API 키 없이 같은 결과를 재현할 수 있다. 파일이 질의별로 나뉘어 있어 서로 다른 유형을 맡은 팀원이 동시에 커밋해도 충돌하지 않는다. 캐시가 없고 API 키도 없으면 해당 실험은 "건너뜀"으로 표시된다.

## 지표

관련도는 골든셋 라벨에서 온다. `expected_any`(판정 2점, 비교 질의는 `expected_all`)는 2, `acceptable`(1점)은 1이다. DB에 없는 원본 모델 ID(예: 변환본과 함께 적힌 `Qwen/Qwen2.5-7B-Instruct`)는 어떤 검색기도 찾을 수 없으므로 관련 집합에서 뺀다.

| 구분 | 지표 | 정의 |
|---|---|---|
| 핵심 | Recall@5, Recall@10 | 관련 모델 중 top-k에 든 비율 |
| 검색 품질 | Precision@5/10, F1@5/10, Hit@10 | Precision은 k로 나눈다(결과가 k개보다 적어도) |
| 순위 품질 | MRR@5, nDCG@5, MAP@5 | nDCG는 등급(2/1)을 gain으로 쓴다. MAP@5는 min(관련 수, 5)로 나눈다 |
| 운영 | p95, p99 latency | 질의별 Pre-Retrieval + dense(질의 인코딩 포함) + sparse + fusion 시간 |
| 안전 | 제외 위반@10 | `must_exclude`가 있는 질의 중 그 모델이 top-10에 나온 비율 |
| 라벨 신뢰도 | Judged@10 | top-10 중 판정된 모델 비율. 낮으면 미판정 모델 때문에 Recall이 과소평가됐을 수 있다. 질의별 `unjudged@10`을 추가 판정한다 |
| abstention | abstention accuracy | `expected_behavior: "abstain"` 질의 중 후보가 0개인 비율 |

지연 시간 주의: 같은 실행 안에서 질의 인코딩·BM25 결과는 재사용하되, 처음 측정한 시간을 계속 쓴다. LLM은 캐시에 기록된 최초 호출 시간을 쓴다. CPU·네트워크에 따라 달라지므로 같은 기기에서 잰 값끼리만 비교한다.

## abstention 질의 추가하기

조건에 맞는 모델이 DB에 없어서 **후보가 0개여야 하는** 질의다. 라벨 원본(`test/golden/labels/`의 jsonl)에 `expected_behavior: "abstain"`으로 넣으면 `convert_golden.py`가 `plan_query_type`을 `abstention`으로 붙인다. (어느 질의든 라벨에 `plan_query_type`을 직접 적으면 그 값이 매핑보다 우선한다.)

```json
{"query_id": "x001", "label_type": "judged", "query_type": "constrained_search", "evaluable_now": true,
 "query": "...", "conditions": {...}, "expected_behavior": "abstain",
 "expected_any": [], "acceptable": [], "must_exclude": [], "needs_review": []}
```

현재 hard filter는 task·한국어·파라미터·컨텍스트·인기도만 거른다. 라이선스·VRAM 조건만으로는 후보가 0개가 되지 않으므로, 그런 질의는 abstention으로 채점할 수 없다.

## 서비스에서 쓰기

```python
from retrieval_lab.pipeline import Retriever
from retrieval_lab.planner import plan_for

retriever = Retriever()                       # 시작할 때 한 번 (BM25·인덱스 로드 수 초)
plan = plan_for("semantic_capability", parsed_query)   # parsed_query: tasks, korean_required, max_parameters_billion …
result = retriever.run(user_text, plan)
result.ranked      # top_k model_id
```

## 테스트

```bash
python -m pytest -q test/test_retrieval_lab.py
```

모델 다운로드나 LLM 호출 없이 RRF, 지표 계산(손으로 계산한 값과 비교), planner, 골든 라벨 변환, HyDE 처리, LLM 캐시, BM25 점수 동치성을 확인한다.

## 해석상 주의

- 유형당 질의가 20개 안팎이다. Recall 0.05 차이는 질의 1개일 수 있으므로 JSON의 질의별 결과를 함께 본다.
- 가중치 탐색과 평가에 같은 질의를 쓴다. 고른 값은 새 질의로 다시 확인해야 과적합인지 알 수 있다.
- **판정 풀 편향**: 판정 150개의 후보는 BM25 상위와 다운로드 상위에서 뽑았다. dense가 풀 밖의 좋은 모델을 찾아도 정답에 없으므로, 그대로 두면 sparse 비중이 큰 설정이 유리하게 나온다. 유형별 최적 설정을 확정하기 전에 상위 설정들의 `unjudged@10` 모델을 판정해 라벨에 추가한다.
- 골든셋 28개는 실제 사례가 고른 모델이 정답이라 정답이 1~2개뿐인 질의가 많다. 판정 150개는 후보 풀(8~12개) 안에서만 판정했으므로, 풀 밖의 좋은 모델을 찾으면 오답으로 집계된다.
