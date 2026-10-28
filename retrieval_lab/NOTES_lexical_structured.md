# lexical_exact · structured_constraint 작업 노트

담당 희원 · 최종 수정 2026-10-28 · 상세 수치는 `reports/lexical_exact.md|json`, `reports/structured_constraint.md|json`

이 문서는 세션이 바뀌어도 작업을 이어갈 수 있도록 **확인한 사실과 다음에 할 일**을 남긴 것이다. 추측과 측정값을 구분해서 적는다.

## 1. 진행 상태

| 계획서 항목 | lexical_exact | structured_constraint |
|---|---|---|
| Query Type 선택 | 완료 | 완료 |
| Golden Set 20~25개 | 완료 (22) | 완료 (24) |
| Baseline 측정 | 완료 | 완료(라벨 보완 전) |
| Pre-Retrieval 단일 A/B | 완료 | 미착수 |
| 개선 요소 조합 | 완료(해당 없음) | 미착수 |
| Dense/Sparse Fusion 비교 | 완료 | 미착수 |
| Weight Grid + Optuna | 완료 | 미착수 |
| planner_config 기록 | **완료** | 미착수 |

유형 필드는 **`plan_query_type`** 이다(`query_type`과 다름). 매핑은
[`test/golden/labels/plan_query_types.json`](../test/golden/labels/plan_query_types.json).

실행 환경은 프로젝트 `.venv`다. conda `kseb`에는 의존성이 없다.

```bash
.venv/Scripts/python -m retrieval_lab.experiment --types lexical_exact \
    --supplement test/golden/labels/supplement_lexical_structured.jsonl
```

## 2. lexical_exact 최종 결과 (2026-10-28)

`planner_config.json`에 기록한 설정은 **Name Lookup만 ON, dense 0.5, LLM 호출 0회**다.

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.349 | 0.561 | 0.397 | 0.594 | 0.414 | 0.421 | 359ms |
| Rewrite | 0.279 | 0.428 | 0.282 | 0.458 | 0.297 | 0.280 | 1843ms |
| Decomposition | 0.322 | 0.494 | 0.329 | 0.572 | 0.356 | 0.330 | 2251ms |
| Multi-Query | 0.346 | 0.517 | 0.351 | 0.594 | 0.398 | 0.407 | 2610ms |
| HyDE | 0.340 | 0.445 | 0.283 | 0.619 | 0.419 | 0.393 | 2676ms |
| **Name Lookup** | **0.378** | **0.574** | **0.405** | **0.662** | **0.449** | **0.422** | **360ms** |

**LLM 사전 검색 4종이 모두 Baseline보다 나빴다.** 질의의 정확한 문자열(`opus-mt-en-ko`,
`GGUF`, `KoELECTRA`)이 변환 과정에서 사라져 BM25 매칭이 깨지는 것으로 보인다.
보조 지표가 이를 뒷받침한다.

| 실험 | Hit@10 | 제외 위반@10 | Judged@10 | p99 |
|---|---|---|---|---|
| Baseline | 0.955 | 0.500 | 0.536 | 381ms |
| Rewrite | 0.818 | **0.625** | 0.359 | 4376ms |
| HyDE | 0.864 | **0.625** | 0.364 | 2760ms |
| **Name Lookup** | **1.000** | 0.500 | 0.545 | 381ms |

Rewrite와 HyDE는 조건 위반 모델까지 끌어온다(0.500 → 0.625).

채널 비교에서 Hybrid가 단일 채널을 크게 앞섰다. 두 채널이 서로 다른 모델을 찾아온다는 뜻이다.

| 채널 | Recall@10 |
|---|---|
| Dense only (BGE-M3) | 0.377 |
| Sparse only (BM25) | 0.392 |
| **Hybrid (0.5/0.5)** | **0.561** |

가중치 탐색(0.1~0.9 grid + Optuna 14점)은 Baseline 위에서도 Name Lookup 위에서도
**dense 0.5**가 최적이었다. "lexical이니 sparse를 높이면 좋아질 것"이라는 가설은 기각됐다.

### 해석 주의

Name Lookup의 Recall 이득은 **+0.013으로 질의 1개(약 0.045)에 못 미친다.**
채택 근거는 Recall이 아니라 순위 지표다. nDCG@5 0.414 → 0.449, MRR@5 0.594 → 0.662,
Hit@10 0.955 → **1.000**(22개 질의 전부 top-10에 정답 포함), 그리고 LLM 호출이 0회다.

## 3. 측정 도구를 먼저 고친 이유

10-14 Baseline은 Recall@10 0.329였으나 **Judged@10이 0.177**이었다. top-10의 83%가
미판정이고 미판정은 오답으로 계산되므로, 그 수치는 검색 성능이 아니라 판정 커버리지를
재고 있었다. 예주님도 같은 벽에서 라벨 보완 후 **최적 설정이 뒤집혔다**
(Rewrite 최적 → Baseline보다 낮음, `reports/yj_summary.md` 2장).

그래서 A/B에 들어가기 전에 두 가지를 했다.

**규칙 지표** — [`lexical_rules.py`](lexical_rules.py). 이 유형은 정오를 사람 판정 없이
가릴 수 있다. 질의 22개가 번역 방향 10 / 형식 7 / 계열 5로 나뉘고, 셋 다 코퍼스
메타데이터로 검증된다. [`lexical_diagnose.py`](lexical_diagnose.py)가 이를 써서
Recall 0인 질의를 "라벨 공백 8개 / 검색 실패 1개"로 분류했고, 보완 후 그 8개가
전부 올라 진단이 맞았음이 확인됐다.

**라벨 보완** — [`test/golden/labels/supplement_lexical_structured.jsonl`](../test/golden/labels/supplement_lexical_structured.jsonl) 79건.
공유 파일 `supplemental_judgments.jsonl`은 건드리지 않았고 `--supplement` 플래그로 분리했다.
결과: Recall@10 0.329 → 0.561, Judged@10 0.177 → 0.536. **검색은 바꾸지 않았다.**

점수 분포는 0점 29 · 1점 26 · 2점 24다. 0점이 가장 많다. 점수를 올리려고 채운 것이
아니라는 근거로 남긴다.

### 판정 기준 (기존 골든셋에서 추출)

기존 `judged_irrelevant` 317건을 조사해 얻은 기준이다.

1. **질의 조건은 전부 만족해야 한다(AND).** h075에서 `EXAONE-3.5-7.8B-Instruct-AWQ`는
   "EXAONE이지만 GGUF 아님", `LiquidAI/LFM2.5-2.6B-GGUF`는 "GGUF지만 EXAONE 아님"으로
   둘 다 무관이다.
2. **제3자 변환본도 인정한다.** h077의 `deepdml/faster-whisper-...-ct2`, h080의
   `NotoriousH2/kanana-...-awq`가 정답·허용이다. 공식 여부를 가리지 않는다.
3. **근거 없음은 감점 사유다.** h098 "문서·표·차트 벤치 없음", h160 "입력 길이 근거 없음"이
   무관 처리됐다.

같은 모델이 질의에 따라 0점도 2점도 된다. h049에서 `intfloat/multilingual-e5-*`는
"GGUF 아님"으로 무관인데, h078(ONNX 질의)에서는 정답이다.

### 1차 판정의 오류 (검증으로 드러남)

별도 세션이 79건을 코퍼스+README로 재검증해 **16건 불일치(오류율 20%)**를 찾았고
14건을 수용했다. **원인은 `data/readmes/`를 열지 않고 model_id와 메타데이터로만
판단한 것**이다. 다음에 판정할 때 반드시 피해야 할 패턴이다.

| 사례 | 오판 | README가 말한 것 |
|---|---|---|
| `hell0ks/ja-ko-vn-7b-v1` | 상업 질의(sg_g003)에 2점 | "비즈니스 용 등에 사용 비권장", Safety RL 미적용 |
| `LRieser/steam-ai-mention-qwen3-8b-merged` | 번역으로 보고 1점 | `task.type: text-classification`, Steam 리뷰 분류기 |
| `klue-roberta-base-klue-sts` 9건 | STS/MRC로 2점·1점 구분 | 전부 sentence-transformers **빈 템플릿**. 학습 순서 근거 없음 |
| `alphaZimuth/Hy-MT2-1.8B-SpecDraft-30B` | 경량 번역으로 1점 | 30B 타깃용 speculative draft 모델. 단독 구동 불가 |

체계적 편향 3가지: ① 이름이 그럴듯하면 후함 ② 빈 모델 카드를 "위반 없음"으로 읽어 2점
(루브릭의 "근거 불충분 → 1"을 한 번도 적용하지 않음) ③ 크기 위반엔 엄격, 용도·런타임
위반엔 관대.

검증이 제안한 2건(h049 e5 GGUF 2→1)은 **기각**했다. 위 기준 2(변환본 인정)와
h078 선례에 어긋나기 때문이다.

판정은 전부 `judge: "claude"`이며 **사람 검수 전**이다.

## 4. 남은 검색 품질 문제 (라벨과 무관)

검증이 코퍼스를 직접 조회해 찾은 것이다. **lexical_exact 개선의 다음 타깃**이다.

**골든 정답이 코퍼스에 있는데 top-10에 없는 질의 6개**

| 질의 | 미검색된 expected_any |
|---|---|
| sg_g002 | `LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct` (dl 395,508) |
| sg_h055 | `LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ` (dl 613,538) |
| sg_g005 | `NHNDQ/nllb-finetuned-en2ko` |
| sg_h054 | `trillionlabs/Tri-1.8B-Translation`, `facebook/nllb-200-distilled-600M` |
| sg_h049 | 한국어 특화 GGUF 임베딩 6종(KURE-v1 등) 전부 |

**근중복 범람**

- sg_h079: 10슬롯 중 6개가 LiquidAI LFM2.5 230M/350M 비트폭 변종
- sg_h081: 10슬롯 전부 `klue-roberta-base-klue-sts` 복제본(dl 85~202).
  같은 코퍼스의 `snunlp/KR-SBERT-V40K-klueNLI-augSTS`(dl 171,903),
  `hunkim/sentence-transformer-klue`(dl 174,487)는 탈락

**인기도·중복 제거 신호가 작동하지 않는다.** 가중치로는 고칠 수 없고(0.5가 최적),
LLM 사전 검색으로도 안 된다(전부 저하). 중복 억제나 인기도 보정이 다음 실험 후보다.
계획서에 없지만 예주님이 Name Lookup을 추가한 선례가 있다.

`sg_h166`(Midm 계열)은 코퍼스에 7개가 있는데 top-10에 1개만 들어왔다. 라벨 보완
후에도 Recall 0이라 **유일하게 확인된 순수 검색 실패**다.

## 5. 커버리지 조사 결과 ([`lexical_coverage.py`](lexical_coverage.py))

실험 전에 "정답이 코퍼스에 있는가"를 센 것이다. 0개면 어떤 설정으로도 못 찾는다.

**번역 방향** — `translation_pairs`는 코퍼스의 0.6%(23개)만 채워져 있고 이름 파싱이
커버리지를 거의 2배로 늘린다(34개). `zh-ko` 쌍 특화 모델은 **0개**이고, 정답인
NLLB·mBART는 `translation_pairs`가 비어 `languages`에 zh·ko가 있는 형태다.
그래서 방향 판정은 선언 ∪ 이름 ∪ 다국어(task가 번역일 때만)의 3경로가 필요하다.

**형식·런타임** — 7개 질의 모두 후보가 11~888개로 충분하다. 다만 `artifacts`에
`ct2`·`openvino` 칸이 없어 이름으로만 찾을 수 있고, `awq`는 `variant_types` 13개 vs
이름 35개로 Stage 1의 `detect_variant_types`가 놓치는 것이 있다.

**계열명** — 이름과 `canonical_model_id`가 거의 일치해 이름만으로 충분하다.
다만 task를 걸면 후보가 급감한다(Kanana 35 → VLM 1개, KoBART 4 → 요약 2개).

## 6. structured_constraint 착수 시 메모

Baseline은 10-14에 측정됐고 **라벨 보완 전**이다(Recall@10 0.109, Judged@10 0.137).
lexical보다 판정 커버리지가 낮으므로 같은 순서로 진행한다.

- 미판정 후보 207개. [`lexical_worksheet.py`](lexical_worksheet.py)를 재사용하되
  `REPORT` 경로와 `LABEL_GAP_QUERIES`를 structured용으로 바꿔야 한다
- 규칙 지표는 방향·형식·계열이 아니라 **수치·라이선스 조건**이 대상이다
- **제외 위반@10이 0.474**다. 질의 절반에서 금지 모델이 top-10에 나온다
- 관련 데이터 공백: `parameter_count` 미상 1,424/3,638(39%), `context_length` 38%.
  `require_known_parameters` 플래그를 실험 변수로 넣어볼 가치가 있다
- 골든셋 자체 약점: 질의문에 "50M 이하"가 있는데 `max_parameters_billion`이 None인
  질의가 많다. 조건이 필드에 없으면 하드 필터가 거를 수 없다

## 7. 골든셋 감사 (두 유형 공통)

| | lexical_exact | structured_constraint |
|---|---|---|
| 질의 | 23 | 24 |
| 사례 기반 / 팀 작성 | 2 / 20 | 4 / 20 |
| 질의당 판정 모델 (최소/중앙/최대) | 2 / 8 / 12 | 4 / 7 / 12 |
| must_exclude 없는 질의 | 15 | 5 |
| judged_irrelevant 없는 질의 | 9 | **17** |
| reliability 등급 | 없음 | 없음 |

코퍼스 3,606개에 대해 질의당 7~8개만 판정돼 있어 **Recall의 해상도가 낮다.**
정답이 2개인 질의는 0 / 0.5 / 1.0 세 값만 나온다. 절대값을 신뢰하지 말고
설정 간 상대 비교로만 쓴다.

`reliability` 등급은 사례 기반 골든셋 28개에만 매겨졌고 판정 배치(`judged`) 질의
40개에는 없다. 희원님 유형의 87%가 여기 속한다.

## 8. 재현 방법

```bash
# 커버리지 조사
.venv/Scripts/python -m retrieval_lab.lexical_coverage

# 규칙 지표로 질의 분류 (검색 재실행 없음)
.venv/Scripts/python -m retrieval_lab.lexical_diagnose

# 판정 워크시트 생성
.venv/Scripts/python -m retrieval_lab.lexical_worksheet

# 규칙 자체 검증
.venv/Scripts/python test/test_lexical_rules.py

# 전체 실험 (LLM 필요, .env의 OPENAI_API_KEY)
.venv/Scripts/python -m retrieval_lab.experiment --types lexical_exact \
    --supplement test/golden/labels/supplement_lexical_structured.jsonl --write-planner

# LLM 없이 Baseline + 채널 비교 + 가중치만
.venv/Scripts/python -m retrieval_lab.experiment --types lexical_exact --stage weight \
    --supplement test/golden/labels/supplement_lexical_structured.jsonl
```

`--supplement`는 이번에 추가한 플래그다. 공유 파일 대신 자기 판정 파일을 쓴다.
LLM 호출 결과는 `retrieval_lab/cache/pre_retrieval/`에 캐시되므로 재실행은 무료다.
