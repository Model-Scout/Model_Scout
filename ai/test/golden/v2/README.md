# 골든셋 v2

7개 질의 유형 × 10개 = 70개. 정답은 사람이 직접 판정한다.

기존 골든셋(`../labels/`)은 그대로 둔다. v2가 완성되고 전 유형 재측정을 마친 뒤에
무엇을 대체하고 무엇을 남길지 정한다.

## 왜 다시 만드나

기존 골든셋의 문제 다섯 가지는 뿌리가 하나다. **정답 집합이 불완전하다.**

| | 문제 | v2에서 어떻게 막나 |
|---|---|---|
① | 판정 풀을 BM25로 만들어, dense가 찾은 모델은 라벨이 없다 | 하드 필터가 돌려준 후보 **전수**를 규칙으로 스캔한다. 검색기를 판정에 쓰지 않는다 |
② | 보완도 Baseline 상위 10개만 채워, Baseline에서 멀어질수록 불리하다 | 같음 — 순위를 만들지 않고 전수를 본다 |
③ | LLM 판정 2,070건에 사람 검수 0건 | 70개 전부 사람이 최종 확정한다 |
④ | 유형마다 2점/1점 기준이 달라 라벨 밀도가 다르다 | `relevance_rule`을 판정 **전에** 글로 고정한다 |
⑤ | held-out 분할이 없다 | 10개 규모에서 분할은 무의미하므로, 대신 `--min-delta`로 작은 차이를 쫓지 않는다 |

①②④는 정답 집합을 완전하게 만들면 구조적으로 사라진다. ③은 사람이 판정하므로
해소된다. ⑤는 완전히 풀리지 않는 한계이므로 명시한다.

## 판정 기준 코퍼스

GitHub Actions를 멈춘 시점의 Supabase `model_scout_models` **active 3,872행**이
확정 후보 집합이다. 더 이상 변하지 않으므로 판정 중에 기준이 흔들리지 않는다.

```bash
python test/golden/v2/tools/dump_corpus.py          # 떠오기
python test/golden/v2/tools/dump_corpus.py --check   # 검증
```

`corpus_snapshot.jsonl`은 128MB(benchmark 결과 33MB + evidence span 47MB)라
커밋하지 않는다. Supabase가 고정돼 있어 언제 떠도 같은 결과가 나오고, 출처와
행 수는 `corpus_snapshot.meta.json`에 기록해 커밋한다.

### 세 숫자가 어긋나 있다

| 출처 | 행 수 | 갱신 주체 |
|---|---:|---|
Supabase active | **3,872** | Actions (중단됨) — **확정 기준** |
`ai/data/hf_models_stage4_*.jsonl` | 3,853 | 수동 커밋만 |
`ai/data/retrieval_lab/bge_m3_*` | 3,606 | 수동 생성만 |

`retrieval_lab.corpus`는 stage4 jsonl을 읽으므로 그대로 쓰면 19행이 빠진다.
그래서 v2는 `tools/corpus_v2.py`로 스냅샷을 읽는다. 하드 필터는
`05_validate_retrieval.hard_filter`를 그대로 재사용한다 — 판정 기준이 운영 검색의
후보 결정 로직과 달라지면 안 되기 때문이다.

공유 파일은 건드리지 않는다. 골든셋이 완성되고 재측정할 때 팀과 합의해 맞춘다.

## 골든셋 생성 원칙

### 1층 — eligible: 논리적 완전성

`eligible`은 질의의 `conditions`가 하드 필터를 통과시킨 후보다. 조건 밖의 모델은
**정의상 정답일 수 없다**. 따라서 `eligible ⊇ 정답 전체`가 수학적으로 성립한다.

단, 조건이 질의문보다 엄격하면 이 보장이 깨진다. 그래서 불변식을 하나 둔다.

> `conditions`의 모든 키는 질의 문장에서 근거를 찾을 수 있어야 한다.

각 질의의 `conditions_fidelity`에 키마다 근거가 되는 질의문의 말을 적는다. 근거를
못 적는 조건은 빼야 한다. 사람이 검증할 때 이 표만 보면 1층이 뚫렸는지 알 수 있다.

#### ⚠️ `require_known_*` 는 후보를 줄이는 용도로 쓰지 않는다

`numeric_ok`는 값이 없으면 `not required`를 돌려준다. 코퍼스의 파라미터 **39.4%**,
컨텍스트 **37.7%** 가 미공개이므로, 이 플래그를 켜면 조건을 만족할 수도 있는 모델이
통째로 탈락한다.

| 질의 | known=False | known=True | 숨은 탈락 |
|---|---:|---:|---:|
translation ≤1.0B | 180 | 20 | **160** |
automatic-speech-recognition ≤1.0B | 211 | 63 | **148** |
image-text-to-text ≤0.3B | 227 | 0 | **227** |
text-generation ≤1.0B | 1,082 | 180 | **902** |

기본값은 `False`다. 질의가 "파라미터 수가 명시된"처럼 공개를 요구할 때만 켠다.
그때는 미공개 모델 탈락이 질의의 요구사항이므로 정당하다.

> 참고: `planner_config.json`의 `structured_constraint`에 `hard_filter_defaults`로
> `require_known_parameters/context: true`가 들어 있다. 그 유형의 **모든** 질의에
> 적용되므로, 공개를 요구하지 않은 질의에서도 후보가 잘린다. 팀과 논의할 사안이다.

### 2층 — 규칙 스캔: 사람의 읽을 양 줄이기

`eligible` 전수를 5단계로 스캔한다. **확실하지 않으므로 느슨하게** 한다. 조금이라도
걸리면 사람에게 올린다.

| 단계 | 보는 곳 | 난이도 기여 |
|---|---|---|
① | `model_id` 문자열 — 동의어·영문/한글 변형 | 쉬움 |
② | `filter_metadata` — task, license, runtime, context, params | 쉬움 |
③ | `semantic_metadata` — summary, use_cases, documented_strengths | **어려움** |
④ | `benchmark_metadata.results` | 중간 |
⑤ | `evidence_spans.parents` — README 원문 span. 최후 근거 | **어려움** |

결과를 세 더미로 낸다.

```
🚩 플래그   조건에 걸리는 근거를 찾음        → 정답 맞나?   (정밀도)
⚠️ 애매     걸러냈지만 근거가 약함           → 진짜 아닌가? (재현율)
✅ 명백     task부터 다름 / 언급 전혀 없음    → 분류 이유만 읽고 넘김
```

**⚠️ 더미가 재현율 방어선이다.** 빠진 정답은 당연히 "걸러낸 쪽"에 숨어 있으므로,
플래그만 보면 영원히 못 찾는다.

### 3층 — 사람 확정

`🚩 + ⚠️ ≤ 25개`를 목표로 한다. 이를 넘으면 `eligible`을 줄이는 대신 **질의의 용도를
더 구체적으로 다시 쓴다**. 조건을 몰래 추가하면 1층이 뚫린다.

## 난이도

`eligible`과 난이도는 서로 다른 것이 결정하므로 따로 조절한다.

```
eligible  ←  하드 필터가 읽는 것 (task · 파라미터 · 컨텍스트 · pool · 한국어)
난이도    ←  규칙 스캔이 몇 단계까지 가야 판정되는가
```

| | 쉬움 | 어려움 |
|---|---|---|
정의 | ①~② 단계에서 판정됨 | ③ 또는 ⑤ 단계까지 가야 판정됨 |
예 | "3B 이하 한국어 요약 모델" | "3B 이하, 회의록에서 할 일 뽑는 모델" |
eligible | 14 | **14 (동일)** |

목표는 유형당 쉬움 5 / 어려움 5. `semantic_capability`는 정답 범위가 넓어지기 쉬워
7 : 3을 권한다.

### abstention은 난이도 정의가 다르다

정답이 없으므로 "판정 단계"가 없다. 대신 검색이 틀리는 방식 —
**조건을 만족하지 않는 비슷한 모델을 끌어다 답하는 것** — 의 여지로 정한다.

```
유혹 후보 = max(수치 완화 시 후보 수, require_known_* 제거 시 후보 수)
난이도    = 유혹 후보 ≥ top_k(30) 이면 hard
```

두 경로를 다 재야 한다. `image-text-to-text ≤0.1B`는 수치를 0.3B로 완화해도 0이지만
미공개를 허용하면 227개가 나온다. 검색이 끌어올 유혹은 거기서 생긴다.

## 라벨 등급

| 등급 | 의미 | 기록 |
|---:|---|---|
**2** | 확실한 정답 — 모든 조건을 데이터로 확인, 용도 정확히 일치 | `expected_any` |
**1** | 애매한 정답 — 도메인이 넓거나 좁음 / 근거 미확인 / 변환본·재업로드 | `acceptable` |
**0** | 오답 | **기록하지 않음** |

0점을 적지 않는 근거는 `retrieval_lab/metrics.py`다.

```python
relevant = {id for id, grade in grades.items() if grade >= min_grade}   # 이진 지표
dcg = sum(grades.get(id, 0) / log2(rank + 1) ...)                       # nDCG는 값 사용
```

0점은 `relevant`에서 제외되고 nDCG 이득도 0이므로, "관련 없음"과 "완전 무관"을
나눠 적어도 모든 지표에서 똑같이 취급된다. 판정 노동만 두 배가 된다.

대신 `eligible_count`를 적는다. "후보 24개를 전수 검토해 7개가 정답"이면 나머지
17개가 오답임이 자동으로 증명된다. 이것이 완전성의 증명이고 0점 목록보다 간결하다.

## 한계

- **막연한 질의는 넣을 수 없다.** "한국어 모델 추천해줘"는 정답이 수백 개라 완전성을
  보장할 수 없다. 70개는 "채점이 가능한 질의"로 구성되며, 실제 사용자의 막연한 질문은
  측정 범위 밖이다.
- **held-out 분할이 없다.** 유형당 10개를 쪼개면 양쪽 다 노이즈가 된다. 대신
  `--min-delta 0.15` 이상만 개선으로 인정한다 (질의 1개 = 0.1).
- **2층 규칙 스캔은 휴리스틱이다.** 놓칠 수 있으므로 `⚠️ 애매` 더미를 사람이 본다.

## 파일

```
v2/
├── README.md                     이 문서
├── corpus_snapshot.jsonl         판정 기준 3,872행 (gitignore — 재생성 가능)
├── corpus_snapshot.meta.json     출처·행 수·sync_run_id
├── index/                        v2 전용 BGE-M3 인덱스 (공유 인덱스와 분리)
├── judged/<유형>.jsonl           판정 결과
├── worksheets/<유형>.md          사람이 확인할 것
├── reports/                      후보 수 지도, 탐색 결과
└── tools/
    ├── dump_corpus.py            Supabase → 스냅샷
    ├── corpus_v2.py              스냅샷 로더 + 하드 필터
    ├── candidate_map.py          조건별 후보 수 지도
    ├── build_index.py            v2 전용 BGE 인덱스
    ├── find_abstention.py        eligible == 0 조합 탐색
    ├── make_abstention.py        abstention 질의 10개
    └── make_worksheet.py         판정 워크시트 생성
```

## 진행

| 유형 | 상태 |
|---|---|
`abstention` | 질의 10개 작성, `eligible == 0` 실측 완료 — 사람 확인 대기 |
`structured_constraint` | |
`model_comparison` | |
`benchmark_lookup` | |
`lexical_exact` | |
`semantic_capability` | |
`semantic_constraint` | |
