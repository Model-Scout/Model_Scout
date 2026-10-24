# lexical_exact · structured_constraint 작업 노트

담당 희원 · 최종 수정 2026-10-25 · 상세 수치는 같은 폴더의 `reports/lexical_exact.md|json`, `reports/structured_constraint.md|json`

이 문서는 세션이 바뀌어도 작업을 이어갈 수 있도록 **지금까지 확인한 사실과 다음에 할 일**을 남긴 것이다. 추측과 측정값을 구분해서 적는다.

## 1. 맡은 범위

| 유형 | 의미 | 채점 질의 |
|---|---|---:|
| `lexical_exact` | 모델명, 번역 방향, 형식명 등 정확한 문자열 중심 | 21 (전체 22) |
| `structured_constraint` | Task, Parameter, Context 등 구조화 조건 중심 | 24 |

유형 필드는 **`plan_query_type`** 이다. 골든셋 원본 스키마의 `query_type`과 다르므로 주의한다.
매핑은 [`test/golden/labels/plan_query_types.json`](../test/golden/labels/plan_query_types.json)에 있고,
`identifier_match` → `lexical_exact`, `reference_anchored` → `semantic_constraint`로 이미 옮겨졌다.

실행:

```bash
python -m retrieval_lab.experiment --types lexical_exact,structured_constraint
```

## 2. 팀 작업과의 관계 (확인 완료)

main에 예주님의 `model_comparison`·`semantic_capability` 실험이 머지돼 있다. **내 실험에 오염은 없다.**

| 항목 | 확인 결과 |
|---|---|
| `planner_config.json` | 내 두 유형 칸이 비어 있음 → 계획서 Baseline(dense 0.5 / sparse 0.5, Pre-Retrieval OFF, top_k 30) 자동 적용 |
| `supplemental_judgments.jsonl` (Claude 1차 판정 1,358쌍, 기본값 ON) | 덮는 질의 37개가 **전부 `semantic_capability`**. 내 유형 영향 **0개** |
| 공유 코드 변경 | 전부 가산적 (`--types` 플래그, `nRecall` 지표, BGE-M3 벡터 재사용). 기존 동작 변경 없음 |

따라서 `--no-supplement` 여부는 내 결과를 바꾸지 않는다.

## 3. Baseline 측정 결과 (2026-10-14 실행)

| 유형 | Recall@5 | Recall@10 | Hit@10 | **Judged@10** | **제외 위반@10** | p95 |
|---|---:|---:|---:|---:|---:|---:|
| `lexical_exact` | 0.231 | 0.329 | 0.619 | **0.177** | **0.500** | 509ms |
| `structured_constraint` | 0.064 | 0.109 | 0.292 | **0.137** | **0.474** | 413ms |

## 4. 가장 먼저 해결할 것 — 라벨 공백

**이 수치는 검색 성능이 아니라 라벨 공백을 재고 있을 가능성이 높다.**

```
lexical_exact         Judged@10 0.177 · 미판정 후보 181개 (질의 22개)
structured_constraint Judged@10 0.137 · 미판정 후보 207개 (질의 24개)
```

top-10 중 **83~86%가 "아무도 판정하지 않은 모델"** 이고, 미판정은 오답으로 계산된다. 맞는 모델을 찾아도 0점이 된다.

예주님이 같은 문제를 겪었고 수치로 남겼다 (`reports/yj_summary.md` 2장):

| `semantic_capability` Baseline | 보완 전 | 보완 후 |
|---|---:|---:|
| Judged@10 | 0.14 | 1.00 |
| Precision@10 | 0.09 | 0.59 |
| Hit@10 | 0.46 | 0.95 |
| Recall@10 | 0.24 | 0.32 |

그리고 **결론이 뒤집혔다**: 보완 전에는 Rewrite + dense 0.4가 최적이었으나, 보완 후에는 Rewrite가 Baseline보다 낮았다.

→ **라벨을 먼저 채우지 않으면, A/B 테스트에서 "개선"으로 보이는 것이 라벨 공백의 그림자일 수 있다.**
현재 내 Judged@10(0.14~0.18)은 예주님의 보완 전(0.14)과 같은 수준이다.

### 할 일

1. `reports/*.json`의 `unjudged_pool`에서 미판정 후보를 꺼낸다 (총 388개)
2. 판정실 기준(2=정답 / 1=허용 / 0=무관 + 이유)으로 판정한다
3. 별도 파일로 저장하고 출처를 남긴다 (예주님 방식: `judge` 필드로 사람/AI 구분, 기존 라벨이 항상 우선)
4. 재측정해서 보완 전/후를 **둘 다 기록**한다

판정 주체(사람/AI)는 팀 합의가 필요하다. 예주님은 Claude 1차 판정 후 "사람 검수 전"으로 명시했다.

## 5. 두 번째 문제 — 제외 위반 50%

```
lexical_exact         제외 위반@10 0.500
structured_constraint 제외 위반@10 0.474
```

**질의 절반에서 `must_exclude` 모델이 top-10에 나온다.** README의 성공 기준 1번("필수 조건을 위반한 모델을 추천하지 않는다")에 직접 걸린다.

Hard Filter가 걸러야 할 것을 못 걸러내고 있다는 뜻이므로, 원인을 질의별로 확인해야 한다. 라벨 공백과 달리 이건 **측정 문제가 아니라 실제 결함**일 가능성이 높다.

관련된 데이터 공백 (Stage 2 실측, 2026-10-02 기준):

| 필드 | 확보율 |
|---|---:|
| `parameter_count` | 61% (1,424건 미상) |
| `context_length` | 62% |
| `license` | 92% (단 `other` 23%, 미기재 8%) |

`structured_constraint`는 Task·Parameter·Context 조건이 핵심인데, **후보의 약 39%가 파라미터 미상**이다.
`require_known_parameters` 플래그에 따라:
- `false` → unknown 통과 → "8B 이하" 결과에 큰 모델이 섞임 (제외 위반의 원인일 수 있음)
- `true` → unknown 탈락 → 후보 39% 소실

**이 플래그를 실험 변수로 넣어볼 가치가 있다.** 계획서에는 없지만 이 유형의 핵심 질문이다.

## 6. 실험 순서 제안

예주님은 Baseline → LLM 기법 → 가중치 순으로 갔고, 결론은 **"LLM 없이 가중치만 바꿔도 같은 값"** 이었다.

| 실험 | Recall@10 | p95 |
|---|---:|---:|
| Baseline | 0.714 | 179ms |
| HyDE | 0.738 | 4,699ms (26배) |
| Decomposition | 0.786 | 3,446ms |
| **Baseline + dense 0.85** | **0.786** | **179ms** |

→ 싼 것부터 보는 순서로 바꾼다.

```
0. 라벨 보완 (4장)          ← 이게 선행되지 않으면 이후 비교가 무의미
1. Baseline 재측정
2. 채널 비교 (Dense only / Sparse only / Hybrid)
3. 가중치 탐색 (grid + Optuna)
4. require_known_parameters A/B   ← structured_constraint 전용
5. LLM 기법 (Rewrite / Decomposition / Multi-Query / HyDE)
6. 개선된 것만 조합
7. --write-planner 로 최적값 기록
```

## 7. 유형별 가설 (미검증)

**`lexical_exact`** — 정확한 문자열이 핵심이라 LLM 변환이 **해로울 수 있다.** Rewrite가 `opus-mt-en-ko`를 "영한 번역 모델"로 바꾸면 매칭이 깨진다. 예주님 실험에서도 Rewrite가 Recall@5를 0.667 → 0.571로 낮췄다.

- **Name Lookup**이 유력하다. 예주님이 계획서에 없던 이 기법을 추가해 `model_comparison`을 0.714 → **1.000**으로 올렸다. LLM을 쓰지 않는다. 계획서에 없는 기법을 추가하는 것은 이미 팀 선례가 있다.
- 놓친 모델 목록을 보면 `facebook/nllb-200-*` 계열이 반복적으로 빠진다. 계열명(`nllb-200`)으로 묶인 모델을 한꺼번에 끌어오는 방식이 효과적일 수 있다.
- **sparse 가중치를 높이는 방향**을 먼저 본다 (예주님은 dense 0.85가 좋았으나 lexical은 반대일 수 있다).

**`structured_constraint`** — Hard Filter가 이미 조건을 거르므로 Pre-Retrieval이 할 일이 적다. 가중치 탐색과 메타데이터 공백 처리가 더 중요할 가능성이 높다. Baseline Recall@10이 0.109로 매우 낮은데, 라벨 공백(Judged@10 0.137)을 먼저 걷어내야 실제 성능을 알 수 있다.

## 8. 해석 시 주의 (리포트에 이미 적힌 것)

- 질의가 20개 안팎이라 **Recall 차이 0.05 이하는 질의 1개 차이**일 수 있다. 개선 판단 전에 질의별 결과(JSON)를 확인한다.
- 가중치 탐색과 평가에 같은 질의를 쓴다. 고른 가중치는 다른 질의에서 다시 확인해야 한다.
- `Judged@10`이 낮은 설정(특히 dense 비중이 큰 설정)은 미판정 모델 때문에 Recall이 낮게 나온다. 판정 후보 풀이 BM25·다운로드 상위에서 뽑혔기 때문이다.
- p95/p99는 노트북 CPU 기준이다. **같은 실행 안의 값끼리만 비교**한다. 실험은 한 환경에서 돌린다.

## 9. 코드 변경 (WIP)

`experiment.py`에 인코더 워밍업을 추가했다. 없으면 첫 질의의 지연에 모델 로드 시간이 섞인다.

```python
retriever = Retriever()
# Load the encoder before timing, or the first query's latency includes the model load.
dense.encode(["warmup"])
```

## 10. 환경

```
필요한 키   OPENAI_API_KEY (Pre-Retrieval LLM), SUPABASE_DB_* (코퍼스)
.env        git에 없음. 환경변수로 주입
Dense       BAAI/bge-m3 (최초 실행 시 수 GB 다운로드)
```

데이터(`data/*.jsonl`, 골든셋 라벨)는 전부 git에 커밋돼 있어 분석·리뷰는 어느 환경에서나 가능하다.
실험 실행은 지연 측정 때문에 한 환경에서 하는 것이 좋다.
