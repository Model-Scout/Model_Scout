# abstention 판정 워크시트

- 판정 기준 코퍼스 **3872행** (Supabase active, 2026-10-31 기준, GitHub Actions 중단)
- sync_run_id `edf6aa33-9598-4ae9-819b-d234926d8d24`
- 질의 10개 — easy 4 / hard 6

## 이 유형에서 확인할 것

정답이 없는 유형이라 모델 카드를 열어볼 것이 없습니다. 두 가지만 봐주세요.

1. **조건이 질의문과 맞나** — `conditions`의 각 키가 질의 문장의 어느 말에서
   왔는지 적어뒀습니다. 질의에 없는 조건이 끼어 있으면 그 질의는 못 씁니다.
2. **후보가 정말 0개인가** — 각 질의마다 재현 명령을 적어뒀습니다.

## require_known_* 가 왜 들어가 있나

`numeric_ok`는 값이 없으면 조건을 통과시킵니다. 코퍼스의 파라미터 39.4%, 
컨텍스트 37.7%가 미공개이므로, 이 플래그를 끄면 수치 조건만으로는 후보가 
0이 될 수 없습니다. 그래서 질의문에 "명시된 / 공개된 / 확인된"을 넣어 
**검증 가능성을 질의의 요구사항으로** 만들었습니다. 숨은 필터가 아닙니다.

## 난이도 — 유혹 후보의 크기

검색이 틀리는 방식은 "조건을 만족하지 않는 비슷한 모델을 끌어다 답하는 것"입니다.
그런 모델이 몇 개인지를 두 경로로 재서 큰 쪽을 썼습니다.

| 경로 | 뜻 |
|---|---|
| 수치 완화 | 상한·하한을 한 칸 느슨하게 → 경계 바로 밖의 모델 수 |
| 미공개 허용 | `require_known_*` 제거 → 만족할 수도 있으나 확인 불가한 모델 수 |

기준값은 `planner_config.json`의 `top_k`(30)입니다. 유혹 후보가 그보다 적으면 
검색이 상위 10개를 채울 만큼 끌어올 것이 애초에 부족합니다.

## 요약표

| id | task | 조건 | eligible | 수치완화 | 미공개허용 | 유혹 | 난이도 |
|---|---|---|---:|---:|---:|---:|---|
| `ab01` | image-text-to-text | ≤0.1B | **0** | 0 | 227 | 227 | hard |
| `ab02` | summarization | ≤0.05B | **0** | 4 | 8 | 8 | easy |
| `ab03` | question-answering | ctx≥262144 | **0** | 3 | 12 | 12 | easy |
| `ab04` | question-answering | ≤0.01B | **0** | 1 | 12 | 12 | easy |
| `ab05` | translation | ctx≥1000000 | **0** | 28 | 120 | 120 | hard |
| `ab06` | translation | ≤0.1B · core만 | **0** | 1 | 85 | 85 | hard |
| `ab07` | text-classification | ctx≥524288 | **0** | 7 | 17 | 17 | easy |
| `ab08` | feature-extraction | ≤0.05B | **0** | 46 | 28 | 46 | hard |
| `ab09` | sentence-similarity | ≤0.01B | **0** | 11 | 31 | 31 | hard |
| `ab10` | automatic-speech-recognition | ≤0.01B | **0** | 7 | 148 | 148 | hard |

---

## `ab01` · image-text-to-text · hard

> 온디바이스로 돌릴 수 있게 파라미터 100M 이하인 한국어 이미지 이해 모델을 찾고 있어. 파라미터 수가 명시된 것만.

**조건이 질의문의 어디서 왔나**

| 조건 | 값 | 질의문 근거 |
|---|---|---|
| `tasks` | `["image-text-to-text"]` | 이미지 이해 → image-text-to-text |
| `korean_required` | `true` | 한국어 |
| `max_parameters_billion` | `0.1` | 파라미터 100M 이하 → 0.1B |
| `require_known_parameters` | `true` | 파라미터 수가 명시된 것만 |

**후보 수** `eligible = 0`

재현:

```bash
cd ai && ../.venv/bin/python -c "
import sys; sys.path.insert(0,'test/golden/v2/tools')
import corpus_v2
print(corpus_v2.count(**{"tasks": ["image-text-to-text"], "korean_required": true, "max_parameters_billion": 0.1, "require_known_parameters": true}))"
```

**유혹 후보** 227개 (수치완화 0 / 미공개허용 227) → 기준 30 → **hard**

판정: ☐ 조건이 질의와 맞음  ☐ eligible 0 재현됨  ☐ 질의문이 자연스러움

---

## `ab02` · summarization · easy

> 파라미터 50M 이하인 초소형 한국어 요약 모델이 필요해. 파라미터 수가 공개된 모델로.

**조건이 질의문의 어디서 왔나**

| 조건 | 값 | 질의문 근거 |
|---|---|---|
| `tasks` | `["summarization"]` | 요약 |
| `korean_required` | `true` | 한국어 |
| `max_parameters_billion` | `0.05` | 50M 이하 → 0.05B |
| `require_known_parameters` | `true` | 파라미터 수가 공개된 |

**후보 수** `eligible = 0`

재현:

```bash
cd ai && ../.venv/bin/python -c "
import sys; sys.path.insert(0,'test/golden/v2/tools')
import corpus_v2
print(corpus_v2.count(**{"tasks": ["summarization"], "korean_required": true, "max_parameters_billion": 0.05, "require_known_parameters": true}))"
```

**유혹 후보** 8개 (수치완화 4 / 미공개허용 8) → 기준 30 → **easy**

판정: ☐ 조건이 질의와 맞음  ☐ eligible 0 재현됨  ☐ 질의문이 자연스러움

---

## `ab03` · question-answering · easy

> 컨텍스트 길이가 262144 토큰 이상인 것으로 확인된 한국어 질의응답 모델 있어?

**조건이 질의문의 어디서 왔나**

| 조건 | 값 | 질의문 근거 |
|---|---|---|
| `tasks` | `["question-answering"]` | 질의응답 |
| `korean_required` | `true` | 한국어 |
| `min_context_length` | `262144` | 262144 토큰 이상 |
| `require_known_context` | `true` | 것으로 확인된 |

**후보 수** `eligible = 0`

재현:

```bash
cd ai && ../.venv/bin/python -c "
import sys; sys.path.insert(0,'test/golden/v2/tools')
import corpus_v2
print(corpus_v2.count(**{"tasks": ["question-answering"], "korean_required": true, "min_context_length": 262144, "require_known_context": true}))"
```

**유혹 후보** 12개 (수치완화 3 / 미공개허용 12) → 기준 30 → **easy**

판정: ☐ 조건이 질의와 맞음  ☐ eligible 0 재현됨  ☐ 질의문이 자연스러움

---

## `ab04` · question-answering · easy

> 파라미터 10M 이하로 명시된 한국어 질의응답 모델을 추천해줘.

**조건이 질의문의 어디서 왔나**

| 조건 | 값 | 질의문 근거 |
|---|---|---|
| `tasks` | `["question-answering"]` | 질의응답 |
| `korean_required` | `true` | 한국어 |
| `max_parameters_billion` | `0.01` | 10M 이하 → 0.01B |
| `require_known_parameters` | `true` | 로 명시된 |

**후보 수** `eligible = 0`

재현:

```bash
cd ai && ../.venv/bin/python -c "
import sys; sys.path.insert(0,'test/golden/v2/tools')
import corpus_v2
print(corpus_v2.count(**{"tasks": ["question-answering"], "korean_required": true, "max_parameters_billion": 0.01, "require_known_parameters": true}))"
```

**유혹 후보** 12개 (수치완화 1 / 미공개허용 12) → 기준 30 → **easy**

판정: ☐ 조건이 질의와 맞음  ☐ eligible 0 재현됨  ☐ 질의문이 자연스러움

---

## `ab05` · translation · hard

> 책 한 권을 통째로 번역하려고 해. 컨텍스트 100만 토큰 이상이 확인된 한국어 번역 모델을 찾아줘.

**조건이 질의문의 어디서 왔나**

| 조건 | 값 | 질의문 근거 |
|---|---|---|
| `tasks` | `["translation"]` | 번역 |
| `korean_required` | `true` | 한국어 |
| `min_context_length` | `1000000` | 100만 토큰 이상 |
| `require_known_context` | `true` | 이 확인된 |

**후보 수** `eligible = 0`

재현:

```bash
cd ai && ../.venv/bin/python -c "
import sys; sys.path.insert(0,'test/golden/v2/tools')
import corpus_v2
print(corpus_v2.count(**{"tasks": ["translation"], "korean_required": true, "min_context_length": 1000000, "require_known_context": true}))"
```

**유혹 후보** 120개 (수치완화 28 / 미공개허용 120) → 기준 30 → **hard**

판정: ☐ 조건이 질의와 맞음  ☐ eligible 0 재현됨  ☐ 질의문이 자연스러움

---

## `ab06` · translation · hard

> 많이 쓰이는 한국어 번역 모델 중에서 파라미터 100M 이하로 공개된 게 있을까?

**조건이 질의문의 어디서 왔나**

| 조건 | 값 | 질의문 근거 |
|---|---|---|
| `tasks` | `["translation"]` | 번역 |
| `korean_required` | `true` | 한국어 |
| `pools` | `["core"]` | 많이 쓰이는 → core (다운로드 500 이상) |
| `max_parameters_billion` | `0.1` | 100M 이하 → 0.1B |
| `require_known_parameters` | `true` | 로 공개된 |

**후보 수** `eligible = 0`

재현:

```bash
cd ai && ../.venv/bin/python -c "
import sys; sys.path.insert(0,'test/golden/v2/tools')
import corpus_v2
print(corpus_v2.count(**{"tasks": ["translation"], "korean_required": true, "pools": ["core"], "max_parameters_billion": 0.1, "require_known_parameters": true}))"
```

**유혹 후보** 85개 (수치완화 1 / 미공개허용 85) → 기준 30 → **hard**

판정: ☐ 조건이 질의와 맞음  ☐ eligible 0 재현됨  ☐ 질의문이 자연스러움

---

## `ab07` · text-classification · easy

> 아주 긴 문서를 분류해야 해. 컨텍스트 524288 토큰 이상으로 확인된 한국어 텍스트 분류 모델 있어?

**조건이 질의문의 어디서 왔나**

| 조건 | 값 | 질의문 근거 |
|---|---|---|
| `tasks` | `["text-classification"]` | 텍스트 분류 |
| `korean_required` | `true` | 한국어 |
| `min_context_length` | `524288` | 524288 토큰 이상 |
| `require_known_context` | `true` | 으로 확인된 |

**후보 수** `eligible = 0`

재현:

```bash
cd ai && ../.venv/bin/python -c "
import sys; sys.path.insert(0,'test/golden/v2/tools')
import corpus_v2
print(corpus_v2.count(**{"tasks": ["text-classification"], "korean_required": true, "min_context_length": 524288, "require_known_context": true}))"
```

**유혹 후보** 17개 (수치완화 7 / 미공개허용 17) → 기준 30 → **easy**

판정: ☐ 조건이 질의와 맞음  ☐ eligible 0 재현됨  ☐ 질의문이 자연스러움

---

## `ab08` · feature-extraction · hard

> 파라미터 50M 이하로 명시된 한국어 임베딩 모델을 찾고 있어.

**조건이 질의문의 어디서 왔나**

| 조건 | 값 | 질의문 근거 |
|---|---|---|
| `tasks` | `["feature-extraction"]` | 임베딩 → feature-extraction |
| `korean_required` | `true` | 한국어 |
| `max_parameters_billion` | `0.05` | 50M 이하 → 0.05B |
| `require_known_parameters` | `true` | 로 명시된 |

**후보 수** `eligible = 0`

재현:

```bash
cd ai && ../.venv/bin/python -c "
import sys; sys.path.insert(0,'test/golden/v2/tools')
import corpus_v2
print(corpus_v2.count(**{"tasks": ["feature-extraction"], "korean_required": true, "max_parameters_billion": 0.05, "require_known_parameters": true}))"
```

**유혹 후보** 46개 (수치완화 46 / 미공개허용 28) → 기준 30 → **hard**

판정: ☐ 조건이 질의와 맞음  ☐ eligible 0 재현됨  ☐ 질의문이 자연스러움

---

## `ab09` · sentence-similarity · hard

> 파라미터 10M 이하로 공개된 한국어 문장 유사도 모델이 있나?

**조건이 질의문의 어디서 왔나**

| 조건 | 값 | 질의문 근거 |
|---|---|---|
| `tasks` | `["sentence-similarity"]` | 문장 유사도 |
| `korean_required` | `true` | 한국어 |
| `max_parameters_billion` | `0.01` | 10M 이하 → 0.01B |
| `require_known_parameters` | `true` | 로 공개된 |

**후보 수** `eligible = 0`

재현:

```bash
cd ai && ../.venv/bin/python -c "
import sys; sys.path.insert(0,'test/golden/v2/tools')
import corpus_v2
print(corpus_v2.count(**{"tasks": ["sentence-similarity"], "korean_required": true, "max_parameters_billion": 0.01, "require_known_parameters": true}))"
```

**유혹 후보** 31개 (수치완화 11 / 미공개허용 31) → 기준 30 → **hard**

판정: ☐ 조건이 질의와 맞음  ☐ eligible 0 재현됨  ☐ 질의문이 자연스러움

---

## `ab10` · automatic-speech-recognition · hard

> 파라미터 10M 이하로 명시된 한국어 음성 인식 모델을 추천해줘.

**조건이 질의문의 어디서 왔나**

| 조건 | 값 | 질의문 근거 |
|---|---|---|
| `tasks` | `["automatic-speech-recognition"]` | 음성 인식 → automatic-speech-recognition |
| `korean_required` | `true` | 한국어 |
| `max_parameters_billion` | `0.01` | 10M 이하 → 0.01B |
| `require_known_parameters` | `true` | 로 명시된 |

**후보 수** `eligible = 0`

재현:

```bash
cd ai && ../.venv/bin/python -c "
import sys; sys.path.insert(0,'test/golden/v2/tools')
import corpus_v2
print(corpus_v2.count(**{"tasks": ["automatic-speech-recognition"], "korean_required": true, "max_parameters_billion": 0.01, "require_known_parameters": true}))"
```

**유혹 후보** 148개 (수치완화 7 / 미공개허용 148) → 기준 30 → **hard**

판정: ☐ 조건이 질의와 맞음  ☐ eligible 0 재현됨  ☐ 질의문이 자연스러움

---

