# model_comparison · semantic_capability 유형 실험 정리

작성 2026-10-17 · 브랜치 `bge-m3-index` · 상세 수치는 같은 폴더의 `model_comparison.md|json`, `semantic_capability.md|json`

## 한눈에 보기

| 유형 | 질의 | Planner에 넣은 설정 | Recall@10 (Baseline → 최종) | 결과 요약 |
|---|---:|---|---|---|
| model_comparison | 21 | **Name Lookup**, dense 0.5 / sparse 0.5, LLM Pre-Retrieval 없음 | 0.714 → **1.000** | 질문에 적힌 모델명을 DB에서 바로 찾아 앞에 고정하자 21개 질의 모두 비교 대상 모델을 찾음. LLM 변환은 효과가 작고 느림 |
| semantic_capability | 37 | Decomposition + Multi-Query, dense 0.75 / sparse 0.25 | 0.318 → **0.373** | P@10 0.62, Hit@10 0.97. Pre-Retrieval 효과는 작고 지연은 약 7배 |

- 두 유형 모두 Hybrid(Dense + Sparse)가 Dense 단독, Sparse 단독보다 좋았다.
- semantic_capability 수치에는 Claude가 1차 판정한 라벨이 포함돼 있다(2장).

## 1. 실험 방법 (두 유형 공통)

```text
질의 → (Pre-Retrieval) → Hard Filter → Dense(BGE-M3) + Sparse(BM25) → Weighted RRF(k=60) → (Name Lookup 고정) → Top-30
```

| 단계 | 내용 |
|---|---|
| Baseline | Dense 0.5 / Sparse 0.5, Pre-Retrieval 모두 OFF |
| 채널 비교 | Dense only(1.0), Sparse only(0.0), Hybrid(0.5) |
| 단일 A/B | Rewrite, Decomposition, Multi-Query, HyDE(LLM `gpt-4o-mini`, 결과 캐시), Name Lookup(LLM 없음)을 하나씩 ON |
| 조합 | 단일 실험에서 Recall@10이 Baseline보다 오른 요소만 조합 |
| 가중치 탐색 | dense 0.1~0.9 grid(0.1 간격) + Optuna(0.05 간격), sparse = 1 − dense. 최적 설정과 Baseline 양쪽에서 탐색 |
| 최적 선택 | Recall@10 → Recall@5 → nDCG@5 → LLM 호출 수 적은 것 → p95 낮은 것. 가중치는 성능이 같으면 0.5에 가까운 값 유지 |

- Hard Filter는 골든셋에 적힌 조건(task, 한국어 여부 등)을 그대로 쓴다.
- 질의 유형은 골든셋 라벨을 썼다(유형 분류기는 아직 없음).
- 지연(p95/p99)은 노트북 CPU 기준이다. 실행할 때마다 기기 상태에 따라 달라지므로 **같은 실행 안의 값끼리만 비교**한다. LLM 지연은 캐시에 기록된 최초 호출 시간이다.

### 지표
| 지표 | 정의 |
|---|---|
| Recall@k | 관련 모델 중 top-k에 든 비율 |
| nRecall@k | top-k 중 관련 수 / min(k, 관련 수). 관련 모델이 k개보다 많아도 최대 1.0 |
| Precision@k | top-k 중 관련 모델 비율 |
| Hit@10 | top-10에 관련 모델이 하나라도 있는 질의 비율 |
| MRR@5, nDCG@5, MAP@5 | 순위 품질 |
| Judged@10 | top-10 중 정답 여부가 판정된 모델 비율 |

## 2. 라벨 보완 (semantic_capability)

처음 실험에서 semantic_capability top-10 중 **판정된 모델이 14%뿐**이었다. 판정 안 된 모델은 오답으로 계산되므로, 맞는 모델을 찾아도 0점이 됐다. 예: "한국어 FAQ용 문장 임베딩" 질의에 `upskyy/e5-base-korean`이 나와도 0점.

- 판정 안 된 (질의, 모델) **1,358쌍**을 기존 판정실 기준에 맞춰 2(정답) / 1(허용) / 0(무관) + 이유로 판정했다.
- 파일: `test/golden/labels/supplemental_judgments.jsonl` (`judge: "claude"`, 사람 검수 전)
- 기존 라벨이 항상 우선이고, 이 파일은 비어 있는 칸만 채운다. `--no-supplement`로 끄면 기존 라벨만으로 채점한다.
- model_comparison은 정답이 "비교 대상 모델"로 정해져 있어 보완이 필요 없었다.

| semantic_capability Baseline | 보완 전 | 보완 후 |
|---|---:|---:|
| Judged@10 | 0.14 | 1.00 |
| Precision@10 | 0.09 | 0.59 |
| Hit@10 | 0.46 | 0.95 |
| Recall@10 | 0.24 | 0.32 |

보완 전에는 Rewrite + dense 0.4가 최적으로 나왔지만, 보완 후에는 Rewrite가 Baseline보다 낮았다. 보완 전 결과는 비어 있는 라벨의 영향을 크게 받았다.

보완 후 질의당 관련 모델이 평균 24.5개다(37개 중 26개 질의가 10개 초과). 그래서 Recall@10은 top-10을 모두 맞혀도 질의 평균 0.571을 넘을 수 없다. 이 유형은 nRecall@10, Precision@10, Hit@10을 함께 본다.

## 3. model_comparison

### 질의 특징
"whisper-large-v3와 whisper-large-v3-turbo 비교해 줘"처럼 **모델 이름 2~3개가 질문에 직접 들어 있다.** 정답은 그 모델들이 모두 top-k에 들어오는 것이다.

### 채널 비교 (Pre-Retrieval 없음)

| 실험 | Recall@5 | Recall@10 | MRR@5 | nDCG@5 |
|---|---:|---:|---:|---:|
| Dense only | 0.548 | 0.690 | 0.528 | 0.485 |
| Sparse only | 0.429 | 0.548 | 0.587 | 0.415 |
| **Hybrid 0.5/0.5** | **0.667** | **0.714** | **0.704** | **0.597** |

### LLM Pre-Retrieval만 썼을 때 (Name Lookup 도입 전)
| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Baseline | 0.667 | 0.714 | 0.238 | 0.704 | 0.597 | 0.504 | 179ms |
| Rewrite | 0.571 | 0.714 | 0.238 | 0.817 | 0.599 | 0.512 | 1,926ms |
| Decomposition | 0.548 | 0.786 | 0.262 | 0.575 | 0.481 | 0.394 | 3,446ms |
| Multi-Query | 0.595 | 0.714 | 0.238 | 0.730 | 0.578 | 0.494 | 3,535ms |
| HyDE | 0.667 | 0.738 | 0.246 | 0.835 | 0.655 | 0.562 | 4,699ms |
| 조합: Decomposition + HyDE | 0.548 | 0.738 | 0.246 | 0.617 | 0.496 | 0.405 | 5,735ms |
| Baseline + dense 0.85 | 0.690 | 0.786 | 0.262 | 0.674 | 0.610 | 0.531 | 179ms |

LLM 변환으로는 Recall@10이 최대 0.786에 그쳤고, 같은 값은 LLM 없이 가중치(dense 0.85)만 바꿔도 나왔다.

### 놓친 모델 분석
| 질의 | 놓친 모델 | 원인 |
|---|---|---|
| h132 | kanana-1.5-2.1b-instruct-2505 | 이름이 비슷한 `kanana-nano-2.1b-instruct`와 EXAONE 변환본이 상위를 차지, 30위 밖 |
| h136 | microsoft/Phi-4-mini-instruct | EXAONE-3.5-2.4B의 GGUF·변환본이 상위를 채움, 30위 밖 |
| h137 | jhgan/ko-sroberta-multitask | multilingual-e5-small 계열 변형이 상위를 채움, 30위 밖 |
| h142 | google/madlad400-3b-mt | Hy-MT 계열만 상위, 30위 밖 |
| h127, h133, h134, h139 | 두 번째 모델 | 11~21위 |

**질문 속 모델 하나의 변환본(GGUF, MLX, 양자화)이 top-10을 채워서 두 번째 모델이 밀려났다.** 의미가 아니라 이름이 일치하느냐의 문제라서 Name Lookup을 추가했다.

### Name Lookup (모델명 직접 조회)
LLM 없이 문자열 규칙만 쓴다.

1. 질문에서 모델명처럼 생긴 토큰을 뽑는다. 영문자로 시작하고 영문·숫자·`.`·`_`·`-`로 이어지며 4자 이상인 것. 예: `EXAONE-3.5-2.4B-Instruct`, `whisper-small`
2. DB 모델 ID의 이름 부분(`org/` 뒤)과 대소문자 무시하고 **정확히 일치**하는 모델을 찾는다. 없으면 `토큰-`으로 시작하는 이름을 찾는다. 예: `kanana-1.5-2.1b-instruct` → `kanana-1.5-2.1b-instruct-2505`
3. 같은 이름이 여러 개면(원본, 미러, GGUF 등) Hard Filter를 통과한 것 중 **다운로드가 가장 많은 것**을 고른다. 대개 원본이다.
4. 찾은 모델을 언급된 순서대로 결과 맨 앞에 고정하고, 나머지는 기존 RRF 순위를 그대로 이어 붙인다.

- 코드: `retrieval_lab/pipeline.py`의 `Retriever.name_lookup`, Planner 옵션 `use_name_lookup`
- 추가 지연은 측정 오차 수준이다(Baseline 179ms, Name Lookup 180ms).

### 최종 실험표

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Baseline | 0.667 | 0.714 | 0.238 | 0.704 | 0.597 | 0.504 | 179ms |
| Rewrite | 0.571 | 0.714 | 0.238 | 0.817 | 0.599 | 0.512 | 1,926ms |
| Decomposition | 0.548 | 0.786 | 0.262 | 0.575 | 0.481 | 0.394 | 3,446ms |
| Multi-Query | 0.595 | 0.714 | 0.238 | 0.730 | 0.578 | 0.494 | 3,535ms |
| HyDE | 0.667 | 0.738 | 0.246 | 0.835 | 0.655 | 0.562 | 4,699ms |
| Name Lookup | 1.000 | 1.000 | 0.333 | 0.976 | 0.985 | 0.980 | 180ms |
| **Best: Name Lookup, dense 0.5** | **1.000** | **1.000** | **0.333** | **0.976** | **0.985** | **0.980** | **180ms** |

- Name Lookup에 Decomposition·HyDE를 더한 조합도 모두 Recall@10 1.000이었지만 지연만 늘었다(3.4~5.7초).
- Name Lookup을 켜면 dense weight 0.1~0.9 전 구간에서 결과가 같았다. 비교 대상 모델이 항상 맨 앞에 고정되기 때문이다. 그래서 0.5를 유지했다.
- F1@10이 0.333에 머무는 것은 정답이 2~3개인데 top-10의 나머지 칸이 정답 외 모델이기 때문이다(P@10 0.200).

## 4. semantic_capability

### 질의 특징
"휴대폰으로 녹음한 한국어 회의를 GPU 없는 PC에서 전사하려고 해"처럼 **원하는 기능·용도·환경을 자연어로 설명**한다. 질의당 맞는 모델이 많다(평균 24.5개).

### 채널 비교 (Pre-Retrieval 없음)

| 실험 | Recall@5 | Recall@10 | MRR@5 | nDCG@5 |
|---|---:|---:|---:|---:|
| Dense only | 0.211 | 0.325 | 0.762 | 0.468 |
| Sparse only | 0.137 | 0.280 | 0.713 | 0.392 |
| **Hybrid 0.5/0.5** | 0.173 | 0.318 | 0.698 | **0.477** |

Dense 단독과 Hybrid가 비슷하다. 의미 설명형 질의라 Dense 비중이 클수록 유리한 경향이 있다(가중치 표 참고).

### 실험표

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Baseline | 0.173 | 0.318 | 0.346 | 0.698 | 0.477 | 0.560 | 708ms |
| Rewrite | 0.176 | 0.315 | 0.337 | 0.748 | 0.430 | 0.512 | 1,644ms |
| Decomposition | 0.186 | 0.327 | 0.354 | 0.833 | 0.477 | 0.582 | 3,656ms |
| Multi-Query | 0.173 | 0.325 | 0.361 | 0.735 | 0.481 | 0.562 | 3,741ms |
| HyDE | 0.188 | 0.314 | 0.362 | 0.818 | 0.511 | 0.640 | 3,596ms |
| Name Lookup | 0.172 | 0.318 | 0.346 | 0.694 | 0.474 | 0.553 | 708ms |
| 조합: Decomposition + Multi-Query | 0.176 | 0.331 | 0.361 | 0.789 | 0.497 | 0.597 | 5,165ms |
| **Best: Decomposition + Multi-Query, dense 0.75** | **0.192** | **0.373** | **0.379** | 0.797 | 0.475 | 0.587 | 5,165ms |

| 보조 지표 | P@10 | Hit@10 | nRecall@10 | 제외 위반@10 |
|---|---:|---:|---:|---:|
| Baseline | 0.589 | 0.946 | 0.651 | 0.400 |
| Best | 0.624 | 0.973 | 0.718 | 0.600 |

### 가중치 (Recall@10)
| dense | 0.1 | 0.3 | 0.5 | 0.7 | 0.75 | 0.85 | 0.9 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Decomposition + Multi-Query | 0.280 | 0.316 | 0.331 | 0.359 | **0.373** | 0.365 | 0.367 |
| Pre-Retrieval 없음 | 0.282 | 0.289 | 0.318 | 0.316 | 0.325 | **0.338** | 0.332 |

### 결과 해석
- Pre-Retrieval 단일 요소는 모두 Recall@10이 Baseline ±0.01 이내다. 질의 37개에서는 질의 1개 미만의 차이다.
- 최종 설정은 Baseline 대비 Recall@10 +0.055, nRecall@10 +0.067이지만 p95가 708ms에서 5,165ms로 늘었다. LLM 없이 dense 0.85만 쓰면 Recall@10 0.338이다.
- 순위 품질(MRR@5)은 Decomposition(0.833), HyDE(0.818)가 Baseline(0.698)보다 확실히 높다.
- Name Lookup은 이 유형에서 효과가 없었다. 질문에 모델명이 거의 없기 때문이다.
- 제외 위반@10(must_exclude 모델이 top-10에 나온 질의 비율)은 최종 설정이 0.6으로 Baseline 0.4보다 높다(해당 질의 5개 중 3개 vs 2개).

### 약한 질의 (Best 기준 Precision@10 하위)
| 질의 | P@10 | 원인 |
|---|---:|---|
| h065 GPU 없는 다국어 추출형 QA | 0.0 | 베트남어·일본어 번역 모델과 생성형 의료 LLM(Apollo 계열)이 상위. 정답(KorQuAD 계열)은 14~24위 |
| h007 존댓말/반말 분류 | 0.1 | 정답 `circulus/koelectra-polite-v1`이 30위 밖. task가 text-classification으로 넓어 필터가 못 좁힘 |
| h040 의도 분류 | 0.1 | 금융 문장 분류, 문서 없는 분류기, 거절 분류기 등 다른 용도 분류기가 상위 |
| h039 NLI, h041 언어 식별 | 0.2 | 같은 text-classification 안의 다른 용도 모델(금융 분류, 대화 턴 감지 등)이 상위 |
| h053 번역 품질 평가 | 0.2 | "번역"이라는 단어 때문에 번역 모델 자체가 상위. 평가 모델(COMET)은 9~10위 |
| h025 이미지 유해성 판별 | 0.2 | 검열해제(abliterated) VLM이 상위. 정답은 29위 |

**task 태그가 넓은 분류(text-classification, image-text-to-text) 안에서 세부 용도를 구분하지 못하고, 질문 속 단어(번역, 안전)와 겉으로 비슷한 모델이 올라온다.** top-30 안에는 관련 모델이 평균 11.9개, top-10에는 6.2개가 있다. 정답이 후보 안에 있지만 순위가 낮은 경우가 많다.

## 5. Planner 반영값 (`retrieval_lab/planner_config.json`)

```json
"model_comparison":    { "dense_weight": 0.5,  "sparse_weight": 0.5,  "use_name_lookup": true,  "use_rewrite": false, "use_decomposition": false, "use_multi_query": false, "use_hyde": false, "top_k": 30 },
"semantic_capability": { "dense_weight": 0.75, "sparse_weight": 0.25, "use_name_lookup": false, "use_rewrite": false, "use_decomposition": true,  "use_multi_query": true,  "use_hyde": false, "top_k": 30 }
```

## 6. 한계

- 질의가 21·37개라 Recall 0.05 차이는 질의 1~2개다.
- 가중치 탐색과 평가에 같은 질의를 썼다. 새 질의로 다시 확인해야 과적합 여부를 알 수 있다.
- Name Lookup 규칙은 model_comparison 질의를 보고 만들었다. 이름 표기가 다른 경우(예: "엑사원", 띄어쓰기가 들어간 모델명)는 아직 처리하지 못한다.
- semantic_capability 보완 판정은 LLM(Claude) 1차 판정이다. 기준은 기존 판정실 라벨에 맞췄다. 예를 들어 같은 질의에서 범용 모델이 정답이면 비슷한 범용 모델도 정답으로 채점했다.
- 지연은 노트북 CPU 기준이고 실행마다 달라진다.

## 7. 추가로 시도할 수 있는 것

- **Reranker (semantic_capability)**: top-30을 cross-encoder(예: `BAAI/bge-reranker-v2-m3`)로 다시 정렬. 관련 모델이 top-30에 약 12개, top-10에 약 6개라 개선 여지가 있다.
- **변환본 묶기**: 같은 원본의 GGUF·MLX·양자화본을 결과에서 하나로 묶어 다양성 확보
- **소프트 조건 반영**: "CPU에서 가볍게", "맥용" 같은 조건을 파라미터 수·형식(GGUF/MLX/ONNX) 가점으로 반영
- **Name Lookup 확장**: lexical_exact 유형에도 적용 가능성 확인

## 재현

```bash
# 전체 실험 (LLM 캐시가 있으면 API 키 없이 재현)
python -m retrieval_lab.experiment --types model_comparison,semantic_capability --trials 30 --write-planner
# 보완 라벨 없이 기존 라벨만으로 채점
python -m retrieval_lab.experiment --types semantic_capability --no-supplement
# LLM 없이 가중치만
python -m retrieval_lab.experiment --types model_comparison --stage weight
```
