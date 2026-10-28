# lexical_exact · structured_constraint 작업 노트

담당 희원 · 최종 수정 2026-10-29 · 상세 수치는 `reports/lexical_exact.md|json`, `reports/structured_constraint.md|json`

이 문서는 세션이 바뀌어도 작업을 이어갈 수 있도록 **확인한 사실과 다음에 할 일**을 남긴 것이다. 추측과 측정값을 구분해서 적는다.

## 1. 진행 상태

| 계획서 항목 | lexical_exact | structured_constraint |
|---|---|---|
| Query Type 선택 | 완료 | 완료 |
| Golden Set 20~25개 | 완료 (22) | 완료 (24) |
| Baseline 측정 | 완료 | 완료 |
| Pre-Retrieval 단일 A/B | 완료 | 완료 |
| 개선 요소 조합 | 완료(해당 없음) | 완료 |
| Dense/Sparse Fusion 비교 | 완료 | 완료 |
| Weight Grid + Optuna | 완료 | 완료 |
| planner_config 기록 | **완료** | **완료** |

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

## 6. structured_constraint 최종 결과 (2026-10-29)

`planner_config.json`에 기록한 설정은 **Known values only**다. Pre-Retrieval은 전부 OFF,
dense 0.5, 대신 `hard_filter_defaults`로 `require_known_parameters`와
`require_known_context`를 켠다.

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.125 | 0.268 | 0.229 | 0.312 | 0.187 | 0.182 | 283ms |
| **Known values only** | **0.222** | **0.379** | **0.255** | **0.411** | **0.294** | **0.295** | **272ms** |
| Rewrite | 0.075 | 0.205 | 0.123 | 0.140 | 0.076 | 0.049 | 2038ms |
| Decomposition | 0.121 | 0.194 | 0.143 | 0.293 | 0.168 | 0.130 | 2387ms |
| Multi-Query | 0.102 | 0.205 | 0.152 | 0.207 | 0.129 | 0.128 | 3209ms |
| HyDE | 0.136 | 0.233 | 0.129 | 0.212 | 0.127 | 0.085 | 2811ms |
| Name Lookup | 0.125 | 0.268 | 0.229 | 0.312 | 0.187 | 0.182 | 283ms |

LLM 사전 검색 4종은 lexical과 똑같이 전부 저하했다. Name Lookup은 Baseline과 완전히
같다. 이 유형 질의에는 모델명이 들어가지 않아 아무 일도 하지 않는다.

채널 비교에서 Hybrid가 단일 채널의 2배였고(Dense 0.133 · Sparse 0.137 · Hybrid 0.268),
가중치는 0.1~0.9 전 구간에서 0.5가 최적이었다. 여기까지는 lexical과 같다.

### 같은 필터가 유형에 따라 반대로 작동한다

```
lexical_exact          Known values only  0.555  <  Baseline 0.561   → 선택 안 됨
structured_constraint  Known values only  0.379  >  Baseline 0.268   → 선택됨
```

lexical은 수치 조건 질의가 적어 필터가 손해만 보고, structured는 수치 조건이 핵심이라
이득이다. 계획서의 "유형별 최적값" 전제를 뒷받침하는 결과다.

### 제외 위반이 함께 줄었다

| 실험 | Hit@10 | nRecall@10 | 제외 위반@10 | Judged@10 |
|---|---|---|---|---|
| Baseline | 0.542 | 0.328 | 0.474 | 0.362 |
| **Known values only** | **0.667** | **0.429** | **0.211** | 0.365 |

Recall이 오르면서 제외 위반이 절반 이하로 줄었다. 보통 트레이드오프인데 함께 개선됐다.

## 7. structured 커버리지와 진단

커버리지 조사([`structured_coverage.py`](structured_coverage.py))는 조건을 세 갈래로 센다.

```
strict   값을 아는 모델 중 조건 만족        7,601
lenient  값이 없는 모델도 통과 (기본값)    11,632
그중 판정 불가                             4,031  (35%)
```

`sg_h004`("파라미터 50M 이하")가 가장 극단적이다. task 풀 24개 중 strict 1개, lenient 15개,
그중 14개(93%)가 "50M 이하인지 모르는" 모델이다. 조건이 필드에 없는 것이 아니라
**비교할 숫자가 없다**. 조건 필드는 24개 질의 전부 정상이다(전수 확인).

진단([`structured_diagnose.py`](structured_diagnose.py))은 Recall 0을 세 갈래로 나눈다.

```
데이터 공백  11개   코퍼스를 채워야 함
라벨 공백     6개   판정하면 해결
정상          7개
```

lexical은 8/9가 라벨 공백이었는데 structured는 11개가 데이터 공백이다. 수치 조건
유무로 갈린다: 있는 15개는 판정 불가 0.713, 없는 9개는 0.222다.

### 제외 위반 0.474의 정체

규칙으로 잰 조건 위반은 **0.029**뿐이다. `must_exclude` 위반 0.474는 라벨러가
"이건 아니다"라고 지목한 모델이 나온 것이고, 규칙으로 보면 대부분 위반이 아니라
판정 불가다. `sg_h004`의 제외 위반 7건은 "50M 초과임이 확인된" 것이 아니라
"50M 이하인지 모르는" 모델이었다. **사람이 아는 것을 데이터가 모르는 상황**이다.

## 8. 라벨 보완과 검증 (structured)

라벨 공백 6개 질의의 미판정 54건을 판정했다. 파일은
[`test/golden/labels/supplement_structured_constraint.jsonl`](../test/golden/labels/supplement_structured_constraint.jsonl),
전부 `judge: "claude"`이며 사람 검수 전이다.

보완 효과는 Recall@10 0.109 → 0.268, Judged@10 0.138 → 0.362였다.

### 외부 검증에서 24건 불일치 (44%)

lexical(20%)보다 나빴다. **lexical에서 지적된 "README 미확인" 편향이 고쳐지지 않고
선택적 독해로 바뀌었다.** 0점·감점 대상은 읽고, 2점을 줄 모델과 "확인 불가" 판정은
메타데이터로 처리했다. 54건 중 10건의 reason이 해당 모델 카드에 반박됐다.

**가장 큰 오류: 골든의 `answer_grade`를 읽지 않았다(12건).**

```
[h002] answer_grade = acceptable_only
  notes: "상업 가능하면서 한국어 추출형 QA 근거가 강한 후보 없음
          / 후보 풀에 2점 모델이 없어 1점 모델을 정답으로 올림"
[h064] answer_grade = acceptable_only
  notes: "라이선스가 확실하면서 한국어 근거가 강한 후보 없음(2점 없음)"
```

골든의 `expected_any`가 "2점"이 아니라 **1점을 승격시킨 것**이다. "골든이 Apollo를
정답으로 인정했으니 2점"이라는 판단을 두 질의에서 6번씩 반복했다. 게다가 reason에
"의료 특화라 도메인이 다르다"고 적어 놓고 2점을 줬다 — 스스로 세운 AND 기준과 모순이다.

다른 오류 유형:

| 유형 | 건수 | 예 |
|---|---:|---|
| README에 답이 있는데 "확인 불가" | 3 | `LiteLLMs/Llama-3-Open-Ko-8B-GGUF` README의 `-c 8192` |
| 기존 골든 라벨과 충돌 | 1 | `team-lucid/hubert-large-korean`은 h067·h068에서 무관 처리됨 |
| 인기도·공식성 가점 | 9 | `FunAudioLLM`과 `yoyolaiyy3062`는 README·GGUF 해시가 동일한데 2점/1점 |
| 질의에 없는 조건 주입 | 3 | `sg_g019`는 license_requirement=unknown인데 라이선스로 감점 |

24건 전부 수용해 수정했다. 점수 분포는 0점 3·1점 25·2점 26에서 **0점 6·1점 35·2점 13**이 됐다.

### 수정해도 결론이 바뀌지 않았다

```
             수정 전    수정 후
Baseline      0.270     0.268
Known only    0.377     0.379
최적 설정     Known values only (동일)
```

라벨 44%를 고쳤는데 최적 설정이 그대로다. 채점이 `min_grade=1`이라 2점과 1점을 똑같이
"관련"으로 세기 때문이고, 수정의 대부분이 2→1이었다. `min_grade=2`로 재면 Baseline이
0.268 → 0.237로 떨어져 수정 효과가 드러난다.

예주님은 라벨 보완 후 결론이 뒤집혔는데(Rewrite 최적 → Baseline보다 낮음) 이번에는
뒤집히지 않았다. **결론이 라벨 오류에 둔감하다는 신호**로 읽는다.

### 검증이 제안한 구조 개선

골든셋은 카드가 침묵할 때 1점을 강제하지 않고 `unjudged`(판정 보류)로 뺀다.

```
[h033] unjudged: LFM2.5-8B-A1B-GGUF — "컨텍스트 128,000 — 질의의 '128K'가
                 131,072 기준이면 미달이라 판정 보류"
[h002] unjudged: koelectra-*-korquad — "라이선스 미표기 → 상업 사용 확인 필요"
```

0/1/2 척도는 "위반 확정"과 "확인 불가"를 똑같이 1점으로 뭉갠다. `LiteLLMs` 오류가
정확히 이 구조에서 나왔다. **"확인 불가" 버킷을 따로 두는 것을 팀에 제안할 만하다.**

## 9. 공유 코드 변경 (리뷰 필요)

계획서는 Planner의 역할로 Hard Filter 선택을 꼽지만 구현에는 그 자리가 없었다.

```python
# planner.py — 유형 기본값 위에 질의 값을 얹는다. 질의가 언제나 우선
filters = dict(values.get("hard_filter_defaults") or {})
filters.update(hard_filters(query))
```

`experiment.py`는 세 군데를 고쳤다. 자체 감사에서 찾은 버그들이다.

| 버그 | 증상 | 수정 |
|---|---|---|
| `evaluate()`가 plan의 hard_filters를 무시 | planner에 0.377을 적었는데 재실행하면 0.270 | 유형 기본값 위에 질의 값을 얹도록 |
| 조건 없는 질의에도 필터가 걸림 | 전부에 걸면 0.299 (멀쩡한 모델까지 탈락) | 짝이 되는 수치 조건이 있을 때만 |
| 하드 필터 실험이 최적 후보에서 빠짐 | `use_*` 플래그가 없어 0.299 > 0.270인데도 Baseline 선택 | 후보 목록에 추가 |

지금은 실험표의 Best Combination과 planner의 `evidence.value`가 일치한다.

**팀에 물어볼 것**: `Known values only` 행이 모든 유형에 적용된다. `hard_filter_defaults`가
없는 유형은 plan 동작이 바뀌지 않지만, 재실행하면 실험표에 행이 하나 늘고 그 행이 이기면
최적 설정이 바뀔 수 있다. 옵트인 플래그로 바꿀지 결정이 필요하다.

검증: 신규 self-check 5건 + `test_structured_rules.py` 8건 + `test_lexical_rules.py` 8건
+ 기존 `test_retrieval_lab.py` 17건 통과. lexical 재실행 0.574 유지(회귀 없음).

## 10. 남은 문제

### 검색 recall 실패 — 두 유형 공통

골든 정답이나 더 나은 후보가 코퍼스에 있는데 top-10에 들어오지 않는다.

| 질의 | 코퍼스에 있으나 미검색 |
|---|---|
| `sg_h033` | `KISTI-KONI/KONI-Llama3.1-8B-Instruct`(ko 단일, ctx 131072, dl 30,987), `skt/A.X-K2`(dl 135,396), `LGAI-EXAONE/EXAONE-4.0-32B` |
| `sg_h045` | `dragonkue/snowflake-arctic-embed-l-v2.0-ko`(dl 122,845), `nlpai-lab/KoE5`(dl 59,049), `nlpai-lab/KURE-v2` |
| `sg_g019` | `seastar105/whisper-small-komixv2`(242M, 평균 WER 7.36) |
| `sg_g002`(lexical) | `LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct`(dl 395,508) |
| `sg_h055`(lexical) | `LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ`(dl 613,538) |

근중복 범람도 같은 뿌리다. `sg_h081`은 top-10 전부가 `klue-roberta-base-klue-sts`
복제본(dl 85~202)이고 `snunlp/KR-SBERT`(dl 171,903)는 탈락했다.

**인기도·중복 제거 신호가 작동하지 않는다.** 가중치로도(0.5가 최적) LLM 사전 검색으로도
(전부 저하) 고칠 수 없다. 계획서의 실험 메뉴 밖이므로 범위 확장 제안이 필요하다.

### 코퍼스 자체의 공백

`sg_h002`·`sg_h064`는 검색이나 판정 문제가 아니다. 코퍼스에서
`primary_task=question-answering` + 한국어 + 상업 라이선스를 전수 조회하면 실제
추출형 한국어 QA 모델은 `timpal0l/mdeberta-v3-base-squad2` 하나뿐이고 이미 골든
정답이다. 나머지는 생성형이거나 번역 모델이다.

`parameter_count` 39% · `context_length` 38% 결측은 파이프라인에 넘길 내용이다.

```
lenient: 조건 위반 모델이 top-10의 37.5%에 등장
strict:  그걸 막는 대신 좋은 모델 3개를 잃음 (sg_h059, sg_h105, sg_h104)
→ 결측을 메우면 둘 다 해결된다
```

## 11. 재현 방법

```bash
# 커버리지 조사
.venv/Scripts/python -m retrieval_lab.lexical_coverage
.venv/Scripts/python -m retrieval_lab.structured_coverage

# 규칙 지표로 질의 분류 (검색 재실행 없음)
.venv/Scripts/python -m retrieval_lab.lexical_diagnose
.venv/Scripts/python -m retrieval_lab.structured_diagnose

# 판정 워크시트
.venv/Scripts/python -m retrieval_lab.lexical_worksheet
.venv/Scripts/python -m retrieval_lab.structured_worksheet

# 규칙 self-check
.venv/Scripts/python test/test_lexical_rules.py
.venv/Scripts/python test/test_structured_rules.py
.venv/Scripts/python test/test_planner_hard_filter_defaults.py

# 전체 실험 (LLM 필요, .env의 OPENAI_API_KEY)
.venv/Scripts/python -m retrieval_lab.experiment --types lexical_exact \
    --supplement test/golden/labels/supplement_lexical_structured.jsonl --write-planner
.venv/Scripts/python -m retrieval_lab.experiment --types structured_constraint \
    --supplement test/golden/labels/supplement_structured_constraint.jsonl --write-planner

# LLM 없이 Baseline + 채널 비교 + 가중치만
.venv/Scripts/python -m retrieval_lab.experiment --types structured_constraint --stage weight \
    --supplement test/golden/labels/supplement_structured_constraint.jsonl
```

`--supplement`는 이번에 추가한 플래그다. 공유 파일 대신 자기 판정 파일을 쓴다.
LLM 호출 결과는 `retrieval_lab/cache/pre_retrieval/`에 캐시되므로 재실행은 무료다.

**주의**: `--stage baseline`이나 `--min-grade`를 바꿔 돌리면 리포트가 그 설정으로
덮어써진다. 정식 수치를 남기려면 위의 전체 실행 명령으로 다시 생성한다.
