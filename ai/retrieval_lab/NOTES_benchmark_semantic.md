# benchmark_lookup · semantic_constraint 작업 노트

담당 정훈 · 최종 수정 2026-11-01 · 상세 수치는 `reports/benchmark_lookup.md|json`, `reports/semantic_constraint.md|json`

이 문서는 세션이 바뀌어도 작업을 이어갈 수 있도록 **확인한 사실과 다음에 할 일**을 남긴 것이다. 추측과 측정값을 구분해서 적는다.

## 1. 진행 상태

| 계획서 항목 | benchmark_lookup | semantic_constraint |
|---|---|---|
| Query Type 선택 | 완료 | 완료 |
| Golden Set 20~25개 | **18 (목표 미달)** | 50 (채점 50) |
| 라벨 보완 | **완료 (136건)** | **완료 (443건)** |
| Baseline 측정 | 완료 | 완료 |
| Pre-Retrieval 단일 A/B | 완료 | 완료 |
| 개선 요소 조합 | 완료(해당 없음) | 완료(해당 없음) |
| Dense/Sparse Fusion 비교 | 완료 | 완료 |
| Weight Grid + Optuna | 완료 | 완료 |
| planner_config 기록 | **완료** | **완료** |

실행 환경은 프로젝트 `.venv`(Python 3.12)다. macOS에는 `python`이 없고 시스템 `python3`은 3.9.6이라
`python3.12 -m venv .venv`로 만들었다.

```bash
source .venv/bin/activate
python -m retrieval_lab.experiment --types benchmark_lookup \
    --supplement test/golden/labels/supplement_benchmark_lookup.jsonl
python -m retrieval_lab.experiment --types semantic_constraint \
    --supplement test/golden/labels/supplement_semantic_constraint.jsonl
```

## 2. 결론 — 두 유형 모두 Baseline이 최적

`planner_config.json`에 기록한 설정은 둘 다 **Pre-Retrieval 전부 OFF, dense 0.5, LLM 호출 0회**다.

| 유형 | 질의 | Baseline | 최종 | Recall@5 | nDCG@5 | MRR@5 | p50 |
|---|---:|---:|---:|---:|---:|---:|---:|
| benchmark_lookup | 18 | 0.733 | **0.733** | 0.522 | 0.666 | 0.861 | 243ms |
| semantic_constraint | 50 | 0.652 | **0.652** | 0.346 | 0.512 | 0.775 | 182ms |

두 유형의 Baseline이 7유형 중 1·2위다.

### benchmark_lookup 실험표

| 실험 | Recall@10 | nDCG@5 | p95 | LLM |
|---|---|---|---|---|
| **Baseline** | **0.733** | **0.666** | 2438ms | 0회 |
| Known values only | 0.733 | 0.666 | 2437ms | 0회 |
| Name Lookup | 0.733 | 0.662 | 2441ms | 0회 |
| Multi-Query | 0.647 | 0.665 | 7214ms | 18회 |
| HyDE | 0.525 | 0.425 | 7688ms | 18회 |
| Decomposition | 0.503 | 0.507 | 17442ms | 18회 |
| Rewrite | 0.474 | 0.423 | 8430ms | 18회 |

### semantic_constraint 실험표

| 실험 | Recall@10 | nDCG@5 | p95 | LLM |
|---|---|---|---|---|
| **Baseline** | **0.652** | **0.512** | 854ms | 0회 |
| Name Lookup | 0.646 | 0.492 | 854ms | 0회 |
| Known values only | 0.556 | 0.510 | 854ms | 0회 |
| Multi-Query | 0.491 | 0.505 | 3078ms | 50회 |
| Decomposition | 0.424 | 0.409 | 2816ms | 50회 |
| HyDE | 0.376 | 0.374 | 2236ms | 50회 |
| Rewrite | 0.352 | 0.337 | 1925ms | 50회 |

### 채널 비교 — 하이브리드가 가장 큰 효과

| 유형 | Dense only | Sparse only | **Hybrid 0.5/0.5** | 배수 |
|---|---|---|---|---|
| benchmark_lookup | 0.419 | 0.432 | **0.733** | 1.7배 |
| semantic_constraint | 0.316 | 0.252 | **0.652** | **2.1배** |

`semantic_constraint`의 2.1배는 6유형 중 최대다. Pre-Retrieval·가중치·필터를 통틀어 **이 프로젝트에서
가장 일관되고 큰 효과는 Dense/Sparse 하이브리드**다.

### 가중치 탐색

Optuna 14점(0.1~0.9 grid 9개 + TPE 0.05 간격) 결과 두 유형 모두 **dense 0.5가 최적**이다.
`benchmark_lookup` 곡선은 단봉이고 양쪽으로 매끄럽게 떨어져 노이즈로 보기 어렵다.

| dense | 0.1 | 0.2 | 0.3 | 0.4 | 0.45 | **0.5** | 0.55 | 0.6 | 0.7 | 0.9 |
|---|---|---|---|---|---|---|---|---|---|---|
| Recall@10 | 0.477 | 0.555 | 0.619 | 0.664 | 0.700 | **0.733** | 0.693 | 0.665 | 0.583 | 0.445 |

6유형 중 5개가 dense 0.5다(`semantic_capability`만 0.75). "유형별로 가중치를 다르게"라는 가설은
현재까지 거의 지지되지 않았다.

## 3. 두 유형의 특징과 Pre-Retrieval 실패 원인

### 유형 특징 (측정값)

| | benchmark_lookup | semantic_constraint |
|---|---|---|
| 질의 평균 길이 | **52자** (최단) | 65자 |
| 핵심 신호 | 벤치마크 고유명사(`KorQuAD`·`KMMLU`·`MTEB`·`LogicKor`·`FLORES-200`·`CER`) | 도메인 용어 + 제약 조건의 AND |
| 정답 평균 | 6.3개 | 10.1개 |
| 후보 중앙값 | 317 | 357 |
| 질의 구성 | 점수 공개 요구 12 / 수준 언급 6 | 도메인 28 / 참조모델 15 / 라이선스 7 |

`semantic_constraint`는 질의 50개 중 `runtime` 32개, `gpu_vram_gb` 22개, `license_requirement` 17개를
명시하지만 **`planner.HARD_FILTER_KEYS`에 이 세 키가 없어 하드 필터에서 버려진다**. 그래서 MLX(Apple
전용)·LiteRT(Android)·CoreML 배포본과 비상업 라이선스 모델이 후보에 남는다.

### 공통 원인 — RRF 가중치 희석

전략을 켜면 질의가 늘어나고 채널 가중치가 질의 수로 나뉜다(lab README 규칙). 원질의의 기여가
1/N로 줄어든다. 손해 순서가 이를 뒷받침한다.

| 전략 | 원질의 처리 | benchmark_lookup | semantic_constraint |
|---|---|---|---|
| Multi-Query | 유지 + 3개 추가 | −0.085 | −0.160 |
| Decomposition | 유지 + 2~4개 추가 | −0.229 | −0.227 |
| HyDE | dense만 대체 | −0.208 | −0.276 |
| **Rewrite** | **완전 대체** | **−0.258** | **−0.300** |

**원질의를 보존하는 전략의 손해가 작고 대체하는 전략의 손해가 크다.** 두 유형에서 동일하게 재현됐다.

### 전략별 실패 원인 (캐시된 LLM 출력 근거)

**Rewrite** — 6유형 전부에서 악화(0승 6패). 원인이 유형별로 다르다.

`benchmark_lookup`에서는 고유명사를 **잘 보존했다.**
```
원질의:  "KorQuAD에서 EM·F1 점수가 공개된 한국어 기계독해 모델이 필요해. 점수를 보고 고르고 싶어."
Rewrite: "Korean machine reading comprehension model with EM and F1 scores in KorQuAD benchmark."
```
고유명사 소실이 아니라 **한국어 토큰("한국어"·"기계독해"·"모델")이 전부 영어로 치환된 것**이 원인으로
보인다(추측). `embedding_text`는 영어 위주지만 모델명과 Stage 3 claim에 `한국어`·`koelectra`·`klue`가
섞여 있어 원질의의 한국어 토큰이 BM25 매칭 기회를 제공한다. 질의가 52자로 짧아 버릴 여유가 없다.

`semantic_constraint`에서는 **핵심 용어 번역에 실패했다.**
```
원질의:  "한국어 RAG에서 검색된 문서 후보를 다시 정렬할 리랭커가 필요해. 상업 서비스에 넣을 거야."
Rewrite: "리랭커 for Korean RAG, commercial service, document ranking"
```
프롬프트가 영어 기술 용어 추가를 지시했는데 가장 중요한 `리랭커`를 한국어로 남겼다. 모델 카드에는
`reranker`·`cross-encoder`로 적혀 있어 매칭되지 않는다. 동시에 `"다시 정렬할"`·`"검색된 문서 후보"`
같은 용도 설명이 압축돼 dense 단서도 줄었다. **양쪽 채널에서 모두 잃어 −0.300으로 최대 손해다.**

**HyDE** — 가상 문서가 질의 조건을 반영하지 못한다.
```
원질의: "KMMLU 점수가 공개된 한국어 LLM을 비교하고 싶어."
HyDE:   "The Korean Language Model (KLM) is a state-of-the-art large language model designed
         specifically for Korean text processing. With 1.5 billion parameters and a context
         length of 2048 tokens, ..."
```
질의의 핵심인 `"KMMLU 점수가 공개된"`이 가상 문서에 없다. 프롬프트가 요구하는 항목이
`task, languages, size, intended use cases, strengths`로 **벤치마크 공개 여부가 들어 있지 않다.**
게다가 `1.5 billion parameters`·`2048 tokens` 같이 질의에 없던 수치를 지어내 실제 정답 모델과의
유사도를 떨어뜨린다. dense만 대체하므로 Rewrite보다는 손해가 작다.

**Decomposition** — AND 조건을 OR로 분해한다.
```
원질의: "한국어 RAG에서 검색된 문서 후보를 다시 정렬할 리랭커가 필요해. 상업 서비스에 넣을 거야."
→ "리랭커 모델을 찾고 있습니다."
→ "상업 서비스에 적합한 모델을 찾고 있습니다."
→ "한국어 RAG에 적합한 모델을 찾고 있습니다."
```
`"모델을 찾고 있습니다"`가 3번 반복된다. 모든 질의에 공통인 표현이라 IDF가 낮아 변별력이 없다.
그리고 쪼갠 조건이 개별적으로는 범위가 너무 넓다(`"상업 서비스에 적합한 모델"` → 상업 가능 2,084개).
**`semantic_constraint`는 AND 조건이 핵심인데 Decomposition은 그걸 OR로 분해한다.**
`model_comparison`에서 Decomposition이 +0.071로 도움이 된 것은 그 유형이 "A와 B를 비교"라는
실제로 분해 가능한 구조이기 때문으로 보인다(추측).

**Multi-Query** — 품질은 가장 좋으나 희석을 못 넘는다.
```
→ "상업 서비스에 사용할 한국어 RAG 리랭커를 찾고 있어요."
→ "I need a reranker for documents retrieved in Korean RAG for commercial services."   ← reranker 정상
→ "리랭커, 한국어, RAG, 상업 서비스, 모델"
```
영어판에서 `reranker`를 제대로 쓴다. 그런데도 음수인 것은 질의 4개로 dense 0.5가 각 0.125로
쪼개져 **좋은 질의 1개를 추가하는 이득이 원질의를 1/4로 깎는 손해보다 작기** 때문으로 보인다.

**Name Lookup** — `semantic_constraint`에서만 음수(6유형 중 유일).

| 유형 | 효과 |
|---|---|
| model_comparison | **+0.286** |
| lexical_exact | +0.013 |
| benchmark_lookup | 0.000 (질의에 모델명이 없어 미작동) |
| structured_constraint | 0.000 |
| **semantic_constraint** | **−0.006** (nDCG@5 −0.020) |

`semantic_constraint`의 참조모델 질의 15개는 **질의가 언급한 모델이 정답이 아닌 구조**다.

```
sg_h147  "EXAONE-3.5-7.8B-Instruct가 느려. 이것보다 작고 빠른 것"
         top-10의 6개가 그 7.8B 변환본(1·3·4·6·7·8·10위) → 전부 무관 판정
         정답은 LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct(5위)와 -AWQ(9위)
sg_h123  "Qwen2.5-72B를 8GB에서?"       72B 변환본이 2·10위 → 0점
sg_h125  "whisper-large-v3를 1GB에서?"  large-v3-turbo가 1·3·7위 → 0점
sg_h150  "whisper-medium보다 빠른 것"    medium 자체가 1·6위 → 0점
sg_h157  "EXAONE-4.5-33B를 16GB 맥에서?" 33B 변환본이 2·4·5위 → 0점
```

Name Lookup은 질의의 모델명을 top-1에 고정하므로 오답을 1위로 올린다. 15/50(30%)에서만 작동해
전체 수치가 −0.006으로 희석됐고, 질의 1개 차이(0.020)보다 작아 **통계적으로는 "차이 없음"과
구분되지 않는다.** nDCG@5가 −0.020으로 더 크게 떨어진 것이 순위 악화의 신호다.

**→ 같은 전략이 유형에 따라 +0.286과 −0.006으로 갈린다. "유형별로 전략을 다르게 한다"는 계획서
전제를 가장 잘 보여주는 사례다.**

**Known values only** — `semantic_constraint`에서 −0.096으로 희원님 결과와 정반대다.

| 유형 | 효과 | 수치 조건 질의 비율 |
|---|---|---|
| structured_constraint (희원) | **+0.111** | 15/24 (63%) |
| **semantic_constraint** | **−0.096** | **18/50 (36%)** |
| benchmark_lookup | 0.000 | 0/18 (수치 조건 없어 필터 자동 제거) |

코퍼스의 `parameter_count` 커버리지가 60.8%, `context_length`가 62.3%다. 수치 조건 질의 비율이
낮은 유형에서는 필터가 노이즈보다 **정답을 더 많이 제거한다.**

### Baseline이 높을수록 손해가 크다

| Rewrite 손해 | Baseline | 유형 |
|---|---|---|
| −0.300 | 0.652 | semantic_constraint |
| −0.258 | 0.733 | benchmark_lookup |
| −0.133 | 0.561 | lexical_exact |
| −0.062 | 0.268 | structured_constraint |
| −0.003 | 0.318 | semantic_capability |

Baseline이 높으면 원질의가 이미 거의 최적이라 바꿀 이득이 없고 떨어질 여지만 크다(추측).
두 유형의 Baseline이 1·2위라는 점이 손해폭이 가장 큰 이유로 보인다.

## 4. 측정 도구를 먼저 고친 이유

두 유형 모두 첫 Baseline의 `Judged@10`이 낮았다. 미판정은 오답으로 계산되므로 그 수치는 검색
성능이 아니라 판정 커버리지를 재고 있었다. 예주님·희원님도 같은 벽을 먼저 넘었다.

| | benchmark_lookup | | semantic_constraint | |
|---|---|---|---|---|
| | 보완 전 | 보완 후 | 보완 전 | 보완 후 |
| Judged@10 | 0.244 | **1.000** | 0.114 | **1.000** |
| Recall@10 | 0.530 | **0.733** | 0.168 | **0.652** |
| Precision@10 | 0.172 | 0.456 | 0.070 | 0.630 |
| MRR@5 | 0.597 | 0.861 | 0.243 | 0.775 |
| Hit@10 | 0.778 | 0.944 | 0.426 | **1.000** |
| 채점 질의 | 18/18 | 18/18 | 47/50 | **50/50** |

**검색은 바꾸지 않았다.** `semantic_constraint`의 +0.484는 6유형 중 최대 상승폭이다. 보완 전에는
29개 질의가 "정답을 하나도 못 찾음"으로 집계됐으나 실제로는 찾았고 라벨이 없었다.
정답이 전부 코퍼스 밖이던 3개 질의(`sg_a001`·`sg_g016`·`sg_g030`)도 판정으로 채점 가능해졌다.

### 라벨 보완

| 파일 | 건수 | 2점 | 1점 | 0점 | 관련율 |
|---|---|---|---|---|---|
| [`supplement_benchmark_lookup.jsonl`](../test/golden/labels/supplement_benchmark_lookup.jsonl) | 136 | 29 | 22 | 85 | 37.5% |
| [`supplement_semantic_constraint.jsonl`](../test/golden/labels/supplement_semantic_constraint.jsonl) | 443 | 87 | 195 | 161 | 63.7% |

공유 파일 `supplemental_judgments.jsonl`은 건드리지 않았고 `--supplement` 플래그로 분리했다.
`benchmark_lookup`의 0점 비율 63%는 팀 내 최고다. 점수를 올리려고 채운 것이 아니라는 근거로 남긴다.

| 담당 | 파일 | 건수 | 관련율(2+1) |
|---|---|---|---|
| 예주 | supplemental_judgments | 1358 | 54.3% |
| 희원 | lexical_structured | 79 | 63.3% |
| 희원 | structured_constraint | 54 | 88.9% |
| **정훈** | **benchmark_lookup** | **136** | **37.5%** |
| **정훈** | **semantic_constraint** | **443** | 63.7% |

`judge: "claude"`이고 **사람 검수 전**이다. 회의 자료에는 "LLM 1차 판정"으로 밝힌다.

### 판정 기준

희원님이 기존 `judged_irrelevant` 317건에서 추출한 기준 3개를 그대로 쓰고
(`NOTES_lexical_structured.md` 3장), 두 유형에 한 줄씩 더했다.

1. 질의 조건은 전부 만족해야 한다(AND).
2. 제3자 변환본도 인정한다.
3. 근거 없음은 감점 사유다.
4. **(benchmark_lookup) 질의가 특정 벤치마크 점수의 공개를 요구하면, `benchmark_metadata` 또는
   README에서 그 수치를 확인한 경우만 2점이다. 이름만 등장하거나 아예 없으면 0점이다.**
5. **(semantic_constraint) 실행 환경이 데이터로 불가능하면 0점이다.** MLX는 Apple Silicon 전용,
   LiteRT/TFLite는 Android 엣지, CoreML은 Apple 전용, OpenVINO는 Intel 가속이다. 질의가 CUDA GPU나
   리눅스 서버를 명시하면 이들은 조건 위반이다. 참조모델 질의에서 질의가 명시적으로 배제한
   크기대(예: "7.8B가 느려서")에 해당하는 모델도 0점이다.

`benchmark_lookup`은 처음에 "task·언어·용도가 적합하면 1점"이라는 느슨한 기준으로 판정해
Recall@10이 0.818이었다. 기준 4를 적용해 44건을 재판정한 결과가 0.733이다. **판정 기준에 따라
0.733~0.818 범위이며, 팀 기준(희원님 기준 3)에 맞는 0.733을 채택했다.**

### 규칙 기반 선별이 전이되지 않은 이유

희원님의 `structured_rules.py` 접근을 재사용하려 했으나 효과가 없었다.

| 규칙 | 자동 0점 처리 | 이유 |
|---|---|---|
| 라이선스 (상업 질의 17개 / 150쌍) | **12쌍 (8%)** | 하드 필터에 `license`가 없어 위반 모델이 통과 |
| 크기·context (수치 질의 18개 / 154쌍) | **0쌍 (0%)** | 하드 필터가 이미 제거해 걸러낼 것이 없음 |

두 규칙 모두 기존 사람 라벨과 한 건도 어긋나지 않아 규칙 자체는 맞았다. 그래도 443쌍 중
431쌍은 수동 판정이 필요했다. `semantic_constraint`는 수치 조건 질의가 36%뿐이고 나머지 64%가
"리랭커인가, 코딩 특화인가" 같은 **의미 판단**을 요구해 메타데이터 규칙으로 가릴 수 없다.
판정에는 `filter_metadata`만으로 부족하고 **Stage 3 claim이 결정적이었다.**

```
LLM-OS-Models/LFM2.5-8B-A1B-Terminal-ToolBench-...
   claim: "터미널 상태를 읽어 다음 터미널 액션 JSON을 출력하는 자동화 SFT 모델"  → 회의록 요약 질의에서 0점
INo0121/whisper-base-ko-callvoice
   limitations: "can only be used for learning purposes"               → 상업 서비스 질의에서 0점
```

## 5. 별건으로 제안할 사항

**(1) 하드 필터에 `license_requirement` 추가** — 질의 17개가 상업 이용을 명시하는데 필터가 이를
버린다. `semantic_constraint`의 `must_exclude_violation_rate@10`이 **0.424**로 높다(benchmark_lookup은
0.000). 희원님이 `require_known_*`로 +0.111을 얻은 것과 같은 종류의 개선 여지다. 코퍼스의 license
커버리지는 92.3%이나 상업 가능 여부를 판정할 수 있는 것은 57%다(`other` 850 · 미표기 277 ·
`gemma`/`llama*` 132 등).

**(2) `runtime`·`gpu_vram_gb` 필터는 권하지 않음** — 질의 32개·22개가 명시하지만 코퍼스
`runtime_compatibility` 커버리지가 cpu 12.1% · cuda 8.0% · onnx 5.2% · mps 4.3%다. 필터를 켜면
87~96%가 "미확인"으로 탈락해 희원님의 "데이터 공백"과 같은 역효과가 난다.

**(3) Pre-Retrieval 프롬프트 개선** — 3장의 분석 근거. `Rewrite`가 핵심 용어를 번역하지 못하고
(`리랭커` 그대로), `Decomposition`이 무정보 표현(`"모델을 찾고 있습니다"`)을 반복하며, `HyDE`
프롬프트 항목에 벤치마크 공개 여부가 없다. `PROMPT_VERSION`을 올리면 기존 캐시 232건이 무효가
되고 선행 4유형 결과와 비교가 깨지므로 **팀 합의가 필요하다.**

**(4) benchmark 추출기 누락 9건** — A군 1점 44건의 README를 확인한 결과, README에 요구 점수가
있는데 `benchmark_metadata`가 비어 있는 경우를 찾았다.
```
QuantFactory/Llama-DNA-1.0-8B-Instruct-GGUF   | Korean | KMMLU | **53.26** (1st) |
skt/A.X-4.0-VL-Light                          | K-DTCBench* | 90.0 |
INo0121/whisper-base-ko-callvoice             - Cer: 30.7538
```
코퍼스 전체로는 benchmark 점수 보유가 289개(8.0%)뿐이다. 다만 **라벨 보완만으로 Recall@10이
0.733까지 올랐으므로 "추출률이 성능 상한을 제약한다"는 초기 가설은 기각됐다.** 검색 성능 문제는
아니지만 "점수를 보고 고르고 싶다"는 사용자 요구에는 직접 영향이 있다.

**(5) benchmark_lookup 질의 보강 18 → 22~25** — 계획서 목표 미달. 질의 18개에서는 Recall 차이
0.056이 질의 1개 차이다. p95도 n=18에서는 최댓값과 같아 첫 질의의 BGE-M3 로딩(약 2.2초)이 그대로
잡히므로 지연 비교에는 p50(243ms)을 쓴다.

## 6. 다음에 할 일

1. **2점 판정 검수** — 2점은 Recall을 직접 올리므로 가장 위험하다. `benchmark_lookup`의 아래 3건은
   근거가 산문뿐이어서 0점 가능성이 있다.
   - `sg_h091` KIST-robot-intelligence/KONI-Llama3-8B-...-GGUF-Quantization
   - `sg_h091` QuantFactory/Llama-3-Alpha-Ko-8B-Evo-GGUF
   - `sg_h091` QuantFactory/Llama-3-Alpha-Ko-8B-Instruct-GGUF
2. **abstention 유형** — 질의 0개로 공통 담당. 작성이 필요하다.
3. 위 5장의 제안을 팀에 공유한다.

## 7. 한계

- 실험 코퍼스는 로컬 Stage 4 스냅샷 **3,606개(2026-09-28)**다. 운영 Supabase는 3,823개로
  갱신돼 있으나, 선행 4유형 결과와의 비교 가능성을 위해 같은 스냅샷을 유지했다.
  워크플로가 Stage 4 JSONL을 `git add` 목록에 넣지 않으므로 이 파일은 구조적으로 갱신되지 않는다.
- 지연(p95/p99)은 노트북 CPU 기준이고 실행마다 달라진다. **같은 실행 안의 값끼리만 비교한다.**
  같은 코드·같은 데이터로 `benchmark_lookup` p95가 2,439ms와 6,592ms로 관측된 사례가 있다.
- 가중치 탐색과 평가에 같은 질의를 쓴다. `benchmark_lookup`은 18개 질의로 설정 23개를, 
  `semantic_constraint`는 50개로 37개를 평가해 최댓값을 골랐다. held-out 분할 옵션이 없어
  고른 dense 0.5는 다른 질의에서 재확인해야 한다. 질의 1개 차이가 `benchmark_lookup` 0.056,
  `semantic_constraint` 0.020이므로 그 미만의 차이는 "차이 없음"으로 읽는다.
- 질의를 성격별로 분류해(도메인 28 / 참조모델 15 / 라이선스 7) 판정 효율화와 결과 해석에 썼으나,
  **군별로 다른 설정을 고르지는 않았다.** `planner_config.json`이 7유형 단위로만 저장하고 운영
  분류기도 7유형만 다루므로 하위 군별 최적값은 기록할 곳도 적용할 방법도 없다.
- `judge: "claude"`, 사람 검수 전이다.
