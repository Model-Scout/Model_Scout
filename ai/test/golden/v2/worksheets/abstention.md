# abstention 판정 워크시트

**읽고 판단하면 됩니다. 명령을 10번 돌릴 필요 없습니다.**
숫자가 맞는지는 아래 한 줄이 전부 확인합니다.

```bash
cd ai && ../.venv/bin/python test/golden/v2/tools/verify.py abstention
```

`✅ 기계 검증 전부 통과`가 나오면 다음을 확인한 것입니다.

- 조건이 하드 필터가 실제로 읽는 키인지 (`HARD_FILTER_KEYS`)
- 조건마다 질의문 근거가 적혀 있는지
- `eligible == 0`이 지금도 재현되는지
- 정답이 잘못 기록돼 있지 않은지
- 판정 기준 코퍼스가 같은 스냅샷인지

## 정훈님이 판단할 것 — 두 가지

정답이 없는 유형이라 **모델 카드를 열어볼 것이 없습니다.**

| | 질문 | 아니라면 |
|---|---|---|
| **①** | 이 질의를 실제로 누가 물어볼까? | 질의문을 바꾼다 |
| **②** | 조건이 질의문이 요구한 것을 넘지 않나? | 조건을 뺀다 |

②가 핵심입니다. 질의에 없는 조건이 끼어 있으면 후보가 부당하게 깎이고,
정답이 있는 유형에서는 그게 바로 정답 누락이 됩니다. abstention에서는
"없어야 할 이유"가 질의문에 다 적혀 있는지를 보는 것입니다.

### `require_known_*` 가 들어간 이유

`numeric_ok`는 값이 없으면 조건을 통과시킵니다. 코퍼스의 파라미터 **39.4%**,
컨텍스트 **37.7%** 가 미공개이므로, 이 플래그 없이는 수치 조건만으로 후보가
0이 될 수 없습니다. 그래서 질의문에 "명시된 / 공개된 / 확인된"을 넣어
**검증 가능성 자체를 질의의 요구사항으로** 만들었습니다. ②를 보실 때 이 말이
질의문에 실제로 있는지 확인해 주세요. 없으면 숨은 필터입니다.

---

## 질의 10개

코퍼스 3872행 · 2026-10-31 기준 · easy 4 / hard 6

### `ab01` ≤100M · image-text-to-text · hard

> 온디바이스로 돌릴 수 있게 파라미터 100M 이하인 한국어 이미지 이해 모델을 찾고 있어. 파라미터 수가 명시된 것만.

조건 → 질의문 근거

- `tasks=["image-text-to-text"]` ← 이미지 이해 → image-text-to-text
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.1` ← 파라미터 100M 이하 → 0.1B
- `require_known_parameters=true` ← 파라미터 수가 명시된 것만

후보 **0개** · 유혹 후보 227개(수치완화 0 / 미공개허용 227)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab02` ≤50M · summarization · easy

> 파라미터 50M 이하인 초소형 한국어 요약 모델이 필요해. 파라미터 수가 공개된 모델로.

조건 → 질의문 근거

- `tasks=["summarization"]` ← 요약
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.05` ← 50M 이하 → 0.05B
- `require_known_parameters=true` ← 파라미터 수가 공개된

후보 **0개** · 유혹 후보 8개(수치완화 4 / 미공개허용 8)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab03` ctx≥262,144 · question-answering · easy

> 컨텍스트 길이가 262144 토큰 이상인 것으로 확인된 한국어 질의응답 모델 있어?

조건 → 질의문 근거

- `tasks=["question-answering"]` ← 질의응답
- `korean_required=true` ← 한국어
- `min_context_length=262144` ← 262144 토큰 이상
- `require_known_context=true` ← 것으로 확인된

후보 **0개** · 유혹 후보 12개(수치완화 3 / 미공개허용 12)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab04` ≤10M · question-answering · easy

> 파라미터 10M 이하로 명시된 한국어 질의응답 모델을 추천해줘.

조건 → 질의문 근거

- `tasks=["question-answering"]` ← 질의응답
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.01` ← 10M 이하 → 0.01B
- `require_known_parameters=true` ← 로 명시된

후보 **0개** · 유혹 후보 12개(수치완화 1 / 미공개허용 12)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab05` ctx≥1,000,000 · translation · hard

> 책 한 권을 통째로 번역하려고 해. 컨텍스트 100만 토큰 이상이 확인된 한국어 번역 모델을 찾아줘.

조건 → 질의문 근거

- `tasks=["translation"]` ← 번역
- `korean_required=true` ← 한국어
- `min_context_length=1000000` ← 100만 토큰 이상
- `require_known_context=true` ← 이 확인된

후보 **0개** · 유혹 후보 120개(수치완화 28 / 미공개허용 120)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab06` ≤100M · core만 · translation · hard

> 많이 쓰이는 한국어 번역 모델 중에서 파라미터 100M 이하로 공개된 게 있을까?

조건 → 질의문 근거

- `tasks=["translation"]` ← 번역
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)
- `max_parameters_billion=0.1` ← 100M 이하 → 0.1B
- `require_known_parameters=true` ← 로 공개된

후보 **0개** · 유혹 후보 85개(수치완화 1 / 미공개허용 85)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab07` ctx≥524,288 · text-classification · easy

> 아주 긴 문서를 분류해야 해. 컨텍스트 524288 토큰 이상으로 확인된 한국어 텍스트 분류 모델 있어?

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 텍스트 분류
- `korean_required=true` ← 한국어
- `min_context_length=524288` ← 524288 토큰 이상
- `require_known_context=true` ← 으로 확인된

후보 **0개** · 유혹 후보 17개(수치완화 7 / 미공개허용 17)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab08` ≤50M · feature-extraction · hard

> 파라미터 50M 이하로 명시된 한국어 임베딩 모델을 찾고 있어.

조건 → 질의문 근거

- `tasks=["feature-extraction"]` ← 임베딩 → feature-extraction
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.05` ← 50M 이하 → 0.05B
- `require_known_parameters=true` ← 로 명시된

후보 **0개** · 유혹 후보 46개(수치완화 46 / 미공개허용 28)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab09` ≤10M · sentence-similarity · hard

> 파라미터 10M 이하로 공개된 한국어 문장 유사도 모델이 있나?

조건 → 질의문 근거

- `tasks=["sentence-similarity"]` ← 문장 유사도
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.01` ← 10M 이하 → 0.01B
- `require_known_parameters=true` ← 로 공개된

후보 **0개** · 유혹 후보 31개(수치완화 11 / 미공개허용 31)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab10` ≤10M · automatic-speech-recognition · hard

> 파라미터 10M 이하로 명시된 한국어 음성 인식 모델을 추천해줘.

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 음성 인식 → automatic-speech-recognition
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.01` ← 10M 이하 → 0.01B
- `require_known_parameters=true` ← 로 명시된

후보 **0개** · 유혹 후보 148개(수치완화 7 / 미공개허용 148)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

---

## 제가 불확실한 것

**10M 이하 질의가 3개입니다** (`ab04`, `ab09`, `ab10`). 10M은 아주 작습니다 —
비교하면 `whisper-tiny`가 39M, `MiniLM-L6`이 22M입니다. 그래서 "실제로
물어볼 질문인가"가 의심스럽습니다. 과하다고 보시면 조건을 올리겠습니다.
다만 숫자를 올리면 후보가 0이 아니게 되는 task가 있어서, 그때는 질의를
다른 조합으로 바꿔야 합니다.

**`ab06`은 `pools: ["core"]`를 씁니다.** "많이 쓰이는"을 다운로드 500 이상으로
옮긴 것인데, 이 해석이 과한지 봐주세요. core/low 경계는 다운로드 500입니다.

## 고칠 것이 있으면

`tools/make_abstention.py`의 `SPECS`를 고치고 다시 생성합니다.

```bash
cd ai
../.venv/bin/python test/golden/v2/tools/make_abstention.py    # eligible==0 재확인
../.venv/bin/python test/golden/v2/tools/make_worksheet.py abstention
```
