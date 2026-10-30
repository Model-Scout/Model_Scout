# benchmark_lookup · semantic_constraint 작업 노트

담당 정훈 · 최종 수정 2026-10-31 · 상세 수치는 `reports/benchmark_lookup.md|json`

이 문서는 세션이 바뀌어도 작업을 이어갈 수 있도록 **확인한 사실과 다음에 할 일**을 남긴 것이다. 추측과 측정값을 구분해서 적는다.

## 1. 진행 상태

| 계획서 항목 | benchmark_lookup | semantic_constraint |
|---|---|---|
| Query Type 선택 | 완료 | 완료 |
| Golden Set 20~25개 | **18 (목표 미달)** | 50 (채점 47) |
| 라벨 보완 | **완료 (136건)** | 미착수 (443건 예정) |
| Baseline 측정 | 완료 | 완료 (0.168) |
| Pre-Retrieval 단일 A/B | 완료 | 미착수 |
| 개선 요소 조합 | 완료(해당 없음) | 미착수 |
| Dense/Sparse Fusion 비교 | 완료 | 미착수 |
| Weight Grid + Optuna | 완료 | 미착수 |
| planner_config 기록 | **완료** | 미착수 |

실행 환경은 프로젝트 `.venv`(Python 3.12)다. macOS에는 `python`이 없고 시스템 `python3`은 3.9.6이라
`python3.12 -m venv .venv`로 만들었다.

```bash
source .venv/bin/activate
python -m retrieval_lab.experiment --types benchmark_lookup \
    --supplement test/golden/labels/supplement_benchmark_lookup.jsonl
```

## 2. benchmark_lookup 최종 결과 (2026-10-31)

`planner_config.json`에 기록한 설정은 **Pre-Retrieval 전부 OFF, dense 0.5, LLM 호출 0회**다.
즉 Baseline이 최종 승자다.

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| **Baseline** | **0.522** | **0.733** | **0.529** | **0.861** | **0.666** | **0.616** | **3980ms** |
| Known values only | 0.522 | 0.733 | 0.529 | 0.861 | 0.666 | 0.616 | 3980ms |
| Rewrite | 0.349 | 0.474 | 0.330 | 0.620 | 0.423 | 0.366 | 4554ms |
| Decomposition | 0.388 | 0.503 | 0.372 | 0.731 | 0.507 | 0.464 | 6026ms |
| Multi-Query | 0.489 | 0.647 | 0.479 | 0.861 | 0.665 | 0.608 | 6391ms |
| HyDE | 0.352 | 0.525 | 0.355 | 0.639 | 0.425 | 0.372 | 4222ms |
| Name Lookup | 0.519 | 0.733 | 0.529 | 0.857 | 0.662 | 0.612 | 3982ms |

**Pre-Retrieval 5종 모두 Baseline을 넘지 못했다(개선 요소 0개).** 이 유형 질의의 핵심은
`KorQuAD`·`KMMLU`·`LogicKor`·`MTEB`·`FLORES-200`·`NSMC` 같은 벤치마크 고유명사이고,
LLM 변환이 그 문자열을 변형·소실시키면서 BM25 매칭이 깨지는 것으로 보인다(추측).
손실 크기가 변환 방식과 일치하는 것이 이를 뒷받침한다.

| 변환 방식 | 전략 | Recall@10 손실 |
|---|---|---|
| 원질의 **유지 + 추가** | Multi-Query | −0.086 |
| 원질의 **유지 + 추가** | Decomposition | −0.230 |
| 원질의 **대체** | HyDE (dense만) | −0.208 |
| 원질의 **대체** | Rewrite | −0.259 |

희원님 `lexical_exact`에서도 LLM 4종이 모두 Baseline보다 낮았다(`NOTES_lexical_structured.md` 2장).
정확한 문자열이 핵심인 유형에서 같은 결과가 두 번 독립적으로 나왔다.

**Name Lookup은 효과가 없었다(±0.000).** 이 유형 질의에는 모델명이 거의 없고 벤치마크 이름만 있어
고정할 대상이 없다. `model_comparison`(0.714 → 1.000), `lexical_exact`(0.561 → 0.574)와 대조된다.

**희원님의 `Known values only`도 무효였다(±0.000).** 이 유형 질의에 파라미터·context 수치 조건이
없어 `require_known_*` 필터가 자동 제거된다(`experiment.py` 60~66행).

### 채널 비교

| 채널 | Recall@10 |
|---|---|
| Dense only (BGE-M3) | 0.419 |
| Sparse only (BM25) | 0.432 |
| **Hybrid (Weighted RRF 0.5/0.5)** | **0.733** |

**하이브리드가 단독 채널의 1.7배다.** 이 유형에서 가장 큰 효과이고, Pre-Retrieval·가중치보다
훨씬 크다. 두 채널이 서로 다른 모델을 찾아온다는 뜻이다.

### 가중치 탐색

Optuna 14점(0.1~0.9 grid 9개 + TPE 0.05 간격) 결과 **dense 0.5가 최적**이다. 곡선이 단봉이고
양쪽으로 매끄럽게 떨어져 노이즈로 보기 어렵다.

| dense | 0.1 | 0.2 | 0.3 | 0.4 | 0.45 | **0.5** | 0.55 | 0.6 | 0.7 | 0.8 | 0.9 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Recall@10 | 0.477 | 0.555 | 0.619 | 0.664 | 0.700 | **0.733** | 0.693 | 0.665 | 0.583 | 0.520 | 0.445 |

5개 유형 중 4개가 dense 0.5다(`semantic_capability`만 0.75). "유형별로 가중치를 다르게"라는
가설은 현재까지 거의 지지되지 않았다.

### 보조 지표

| 지표 | 값 |
|---|---|
| Precision@5 / @10 | 0.600 / 0.456 |
| Hit@10 | 0.944 |
| nRecall@10 | 0.758 |
| Judged@10 | **1.000** |
| 제외 위반@10 | **0.000** |
| p50 / p99 | 243ms / 3980ms |

## 3. 측정 도구를 먼저 고친 이유

첫 Baseline은 Recall@10 0.530이었으나 **Judged@10이 0.244**였다. top-10의 76%가 미판정이고
미판정은 오답으로 계산되므로, 그 수치는 검색 성능이 아니라 판정 커버리지를 재고 있었다.
예주님·희원님도 같은 벽을 먼저 넘었다.

미판정 136건을 판정한 결과 **검색을 바꾸지 않고** 수치가 이렇게 움직였다.

| 지표 | 보완 전 | 보완 후 |
|---|---|---|
| Judged@10 | 0.244 | **1.000** |
| Recall@10 | 0.530 | **0.733** |
| Precision@10 | 0.172 | 0.456 |
| MRR@5 | 0.597 | 0.861 |
| Hit@10 | 0.778 | 0.944 |

보완 전에는 질의 4개가 "정답을 하나도 못 찾음"으로 집계됐으나, 실제로는 찾았고 라벨이 없었다.

### 라벨 보완

파일: [`test/golden/labels/supplement_benchmark_lookup.jsonl`](../test/golden/labels/supplement_benchmark_lookup.jsonl) 136건.
공유 파일 `supplemental_judgments.jsonl`은 건드리지 않았고 `--supplement` 플래그로 분리했다.

점수 분포는 **0점 85 · 1점 22 · 2점 29**다. 0점이 63%로 가장 많다. 점수를 올리려고 채운 것이
아니라는 근거로 남긴다. 팀 내 비교로도 가장 엄격하다.

| 담당 | 파일 | 건수 | 관련율(2+1) |
|---|---|---|---|
| 예주 | supplemental_judgments | 1358 | 54.3% |
| 희원 | lexical_structured | 79 | 63.3% |
| 희원 | structured_constraint | 54 | 88.9% |
| **정훈** | **benchmark_lookup** | **136** | **37.5%** |

`judge: "claude"`이고 **사람 검수 전**이다. 회의 자료에는 "LLM 1차 판정"으로 밝힌다.

### 판정 기준

희원님이 기존 `judged_irrelevant` 317건에서 추출한 기준 3개를 그대로 쓰고
(`NOTES_lexical_structured.md` 3장), 이 유형에 한 줄을 더했다.

1. 질의 조건은 전부 만족해야 한다(AND).
2. 제3자 변환본도 인정한다.
3. 근거 없음은 감점 사유다.
4. **(추가) 질의가 특정 벤치마크 점수의 공개를 요구하면, `benchmark_metadata` 또는 README에서
   그 수치를 확인한 경우만 2점이다. 벤치마크 이름만 등장하거나 아예 없으면 0점이다.**
   기준 3의 적용이고, 기존 라벨의 h098 "문서·표·차트 벤치 없음" 처리와 같은 방향이다.

처음에는 "task·언어·용도가 적합하면 1점"이라는 느슨한 기준으로 판정했고 그때 Recall@10이
0.818이었다. 기준 4를 적용해 44건을 재판정한 결과가 0.733이다. **판정 기준에 따라 0.733~0.818
범위이며, 팀 기준에 맞는 0.733을 채택했다.**

## 4. 이 유형의 성격 (확인된 사실)

| 항목 | 값 | 비교 |
|---|---|---|
| 채점 질의 | 18 | 목표 20~25 **미달** |
| 질의당 정답 수 | 평균 6.3 (1~13), 10개 초과 3/18 | `semantic_capability` 24.5 |
| hard filter 통과 후보 | 중앙값 317 (15~2177) | 유형 간 비슷 |
| Baseline Recall@10 | **0.733 (5개 유형 중 최고)** | 최저 `semantic_constraint` 0.168 |

Baseline이 높은 이유는 **정답 수가 적당해 top-10에 담을 수 있고**(정답 24.5개인 유형은
Recall@10 상한이 0.41), **벤치마크 고유명사의 IDF가 높아 BM25에 유리하기** 때문으로 보인다(추측).

### benchmark_metadata 커버리지 — 성능 상한은 아니었다

코퍼스 3,606개 중 benchmark 점수를 가진 모델은 **289개(8.0%)**, 이름만 있는 것이 368개(10.2%),
나머지 2,949개(81.8%)는 아무것도 없다. 정답 라벨 62개 중에서도 점수 보유가 10개(16%)뿐이다.

처음에는 이 낮은 추출률이 성능 상한을 제약한다고 보았으나, **라벨 보완만으로 Recall@10이
0.733까지 올랐으므로 그 가설은 기각됐다.** 추출률이 낮은 것은 사실이나 이 유형의 Recall을
제약하는 주된 요인은 아니었다. 희원님 진단 분류로 말하면 **"데이터 공백"이 아니라
"라벨 공백"이 지배적 원인**이었다.

### benchmark 추출기 누락 — 별건으로 확인

판정 과정에서 A군 1점 44건의 README를 직접 확인한 결과, **README에 요구 점수가 있는데
`benchmark_metadata`가 비어 있는 경우 9건**을 찾았다.

```
QuantFactory/Llama-DNA-1.0-8B-Instruct-GGUF   | Korean | KMMLU | **53.26** (1st) |
skt/A.X-4.0-VL-Light                          | K-DTCBench* | 90.0 |
INo0121/whisper-base-ko-callvoice             - Cer: 30.7538
```

`06_extract_benchmark_metadata.py`가 보수적으로 설계된 결과다(README: "확실하지 않으면
ranking signal로 쓰지 않는다"). 검색 성능 문제는 아니지만 **"점수를 보고 고르고 싶다"는
사용자 요구에는 직접 영향**이 있어, 추출기 개선을 별건으로 제안한다.

## 5. 다음에 할 일

1. **semantic_constraint 라벨 보완 443건** — Baseline 0.168, Judged@10 0.114로 7유형 최저다.
   먼저 정답 수 분포를 확인해야 한다. `semantic_capability`처럼 정답이 10개를 넘으면
   Recall@10 상한이 낮아 nRecall@10·Precision@10·Hit@10을 함께 봐야 한다.
   조건이 수치·라이선스·런타임이므로 희원님 `structured_rules.py`를 재사용할 수 있다.
2. **benchmark_lookup 질의 보강 18 → 22~25** — 계획서 목표 미달이고, 질의 18개에서는
   Recall 차이 0.056이 질의 1개 차이다. p95도 n=18에서는 최댓값과 같아 첫 질의의
   BGE-M3 로딩(약 2.2초)이 그대로 잡힌다. 지연 비교에는 p50(243ms)을 쓴다.
3. **2점 29건 사람 검수** — 2점은 Recall을 직접 올리므로 가장 위험하다. 특히 아래 3건은
   근거가 산문뿐이어서 0점 가능성이 있다.
   - `sg_h091` KIST-robot-intelligence/KONI-Llama3-8B-...-GGUF-Quantization
   - `sg_h091` QuantFactory/Llama-3-Alpha-Ko-8B-Evo-GGUF
   - `sg_h091` QuantFactory/Llama-3-Alpha-Ko-8B-Instruct-GGUF
4. **추출기 개선 제안** — 4장의 누락 9건을 근거로 팀에 공유한다.

## 6. 한계

- 실험 코퍼스는 로컬 Stage 4 스냅샷 **3,606개(2026-09-28)**다. 운영 Supabase는 3,823개로
  갱신돼 있으나, 선행 4유형 결과와의 비교 가능성을 위해 같은 스냅샷을 유지했다.
  워크플로가 Stage 4 JSONL을 커밋하지 않으므로 이 파일은 구조적으로 갱신되지 않는다.
- 지연(p95/p99)은 노트북 CPU 기준이고 실행마다 달라진다. **같은 실행 안의 값끼리만 비교한다.**
  같은 코드·같은 데이터로 p95가 2,439ms와 6,592ms로 관측된 사례가 있다.
- 가중치 탐색과 평가에 같은 질의 18개를 쓴다. 고른 dense 0.5는 다른 질의에서 재확인해야 한다.
- `judge: "claude"`, 사람 검수 전이다.
