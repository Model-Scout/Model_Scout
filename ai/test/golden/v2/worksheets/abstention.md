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

### 수치값이 없는 모델의 처리

실제 Supabase 검색과 같은 규칙을 씁니다. 파라미터·컨텍스트의 상한 또는 하한을
요구하면, 값이 없는 모델은 그 수치를 만족한다고 **검증할 수 없으므로 후보에서
제외**됩니다. 따라서 질문에 "공개된 / 확인된 모델만" 같은 말을 인위적으로
넣지 않습니다. 이 처리 자체가 데이터 품질의 한계이므로, 미기재 모델을 더
채우는 일은 별도 백필 작업으로 계속 추적합니다.

---

## 질의 10개

코퍼스 3872행 · 2026-10-31 기준 · easy 3 / hard 7

### `ab01` ≤100M · image-text-to-text · hard

> 파라미터 100M 이하인 한국어 이미지 이해 모델을 찾고 있어.

조건 → 질의문 근거

- `tasks=["image-text-to-text"]` ← 이미지 이해 → image-text-to-text
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.1` ← 파라미터 100M 이하 → 0.1B

후보 **0개** · 유혹 후보 444개(조건완화 0 / 수치제거 444)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab02` ≤50M · summarization · easy

> 파라미터 50M 이하인 초소형 한국어 요약 모델이 필요해.

조건 → 질의문 근거

- `tasks=["summarization"]` ← 요약
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.05` ← 50M 이하 → 0.05B

후보 **0개** · 유혹 후보 14개(조건완화 4 / 수치제거 14)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab03` ctx≥250,000 · question-answering · easy

> 컨텍스트 길이가 25만 토큰 이상인 한국어 질의응답 모델 있어?

조건 → 질의문 근거

- `tasks=["question-answering"]` ← 질의응답
- `korean_required=true` ← 한국어
- `min_context_length=250000` ← 25만 토큰 이상

후보 **0개** · 유혹 후보 21개(조건완화 9 / 수치제거 21)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab04` ctx≥500,000 · core만 · summarization · easy

> 긴 회의록을 한 번에 요약하려고 해. 컨텍스트 50만 토큰 이상이고 많이 쓰이는 한국어 요약 모델이 있어?

조건 → 질의문 근거

- `tasks=["summarization"]` ← 요약
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)
- `min_context_length=500000` ← 50만 토큰 이상

후보 **0개** · 유혹 후보 3개(조건완화 0 / 수치제거 3)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab05` ctx≥1,000,000 · translation · hard

> 책 한 권을 통째로 번역하려고 해. 컨텍스트 100만 토큰 이상인 한국어 번역 모델을 찾아줘.

조건 → 질의문 근거

- `tasks=["translation"]` ← 번역
- `korean_required=true` ← 한국어
- `min_context_length=1000000` ← 100만 토큰 이상

후보 **0개** · 유혹 후보 245개(조건완화 71 / 수치제거 245)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab06` ≤100M · core만 · translation · hard

> 많이 쓰이는 한국어 번역 모델 중에서 파라미터 100M 이하인 게 있을까?

조건 → 질의문 근거

- `tasks=["translation"]` ← 번역
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)
- `max_parameters_billion=0.1` ← 100M 이하 → 0.1B

후보 **0개** · 유혹 후보 117개(조건완화 1 / 수치제거 117)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab07` ctx≥500,000 · text-classification · hard

> 아주 긴 문서를 분류해야 해. 컨텍스트 50만 토큰 이상인 한국어 텍스트 분류 모델 있어?

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 텍스트 분류
- `korean_required=true` ← 한국어
- `min_context_length=500000` ← 50만 토큰 이상

후보 **0개** · 유혹 후보 105개(조건완화 9 / 수치제거 105)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab08` ≤50M · feature-extraction · hard

> 파라미터 50M 이하인 한국어 임베딩 모델을 찾고 있어.

조건 → 질의문 근거

- `tasks=["feature-extraction"]` ← 임베딩 → feature-extraction
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.05` ← 50M 이하 → 0.05B

후보 **0개** · 유혹 후보 146개(조건완화 50 / 수치제거 146)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab09` ctx≥500,000 · core만 · sentence-similarity · hard

> 장문의 판례·보고서를 통째로 비교하려고 해. 컨텍스트 50만 토큰 이상이고 많이 쓰이는 한국어 문장 유사도 모델이 있을까?

조건 → 질의문 근거

- `tasks=["sentence-similarity"]` ← 문장 유사도
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)
- `min_context_length=500000` ← 50만 토큰 이상

후보 **0개** · 유혹 후보 71개(조건완화 1 / 수치제거 71)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

### `ab10` ≤20M · core만 · automatic-speech-recognition · hard

> 널리 쓰이는 한국어 음성 인식 모델 중, 파라미터 20M 이하인 게 있을까?

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 음성 인식 → automatic-speech-recognition
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 널리 쓰이는 → core (다운로드 500 이상)
- `max_parameters_billion=0.02` ← 파라미터 20M 이하 → 0.02B

후보 **0개** · 유혹 후보 136개(조건완화 4 / 수치제거 136)

**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → 

**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → 

---

## 제가 불확실한 것

**`ab06`은 `pools: ["core"]`를 씁니다.** "많이 쓰이는"을 다운로드 500 이상으로
옮긴 것인데, 이 해석이 과한지 봐주세요. core/low 경계는 다운로드 500입니다.

## 고칠 것이 있으면

`tools/make_abstention.py`의 `SPECS`를 고치고 다시 생성합니다.

```bash
cd ai
../.venv/bin/python test/golden/v2/tools/make_abstention.py    # eligible==0 재확인
../.venv/bin/python test/golden/v2/tools/make_worksheet.py abstention
```
