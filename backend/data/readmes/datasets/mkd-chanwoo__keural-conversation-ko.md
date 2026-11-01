---
language:
- ko
license: cc-by-4.0
task_categories:
- text-generation
tags:
- korean
- daily-chat
- synthetic
- multi-turn
- conversation
size_categories:
- 100K<n<1M
---

# keural-conversation

한국어 일상 대화 AI 학습용 합성 데이터셋입니다.  
9개 주제, 1,350개 시나리오를 기반으로 **191,093개**의 멀티턴 대화 쌍을 생성했습니다.

---

## 데이터셋 개요

| 항목 | 내용 |
|------|------|
| 언어 | 한국어 (ko) |
| 총 샘플 수 | 191,093개 |
| 시나리오 수 | 1,350개 |
| 대화 구조 | 2-turn (user → assistant → user → assistant) |
| 생성 모델 | google/gemma-4-26B-A4B-it |
| 원본 생성 수 | 202,435개 |
| 수락률 | 99.97% |
| 중복 제거율 | 5.60% |
| 라이선스 | CC BY 4.0 |

---

## 주제별 분포

| 주제 | 시나리오 수 | 샘플 수 |
|------|------------|--------|
| 자기소개 및 인사 | 150개 | 20,815 |
| 감정 표현과 공감 | 150개 | 21,411 |
| 날씨, 계절, 일상 근황 | 150개 | 20,855 |
| 취미, 관심사, 좋아하는 것 | 150개 | 20,890 |
| 창의적 글쓰기 | 150개 | 21,246 |
| 의견 및 토론 | 150개 | 21,934 |
| 유머 및 개그 | 150개 | 21,300 |
| 번역 및 교정 | 150개 | 20,972 |
| 직장 예절 | 150개 | 21,670 |
| **합계** | **1,350개** | **191,093** |

---

## 데이터 구조

```json
{
  "id": "creative_083_0000",
  "topic": "창의적 글쓰기",
  "situation": "퇴근길 버스 창가에 머리를 기대고 멍하니 있는 시나리오",
  "task_type": "daily_chat",
  "domain": "창의적 글쓰기",
  "model_name": "google/gemma-4-26B-A4B-it",
  "turns": 2,
  "conversation": "[{\"role\": \"user\", \"content\": \"...\"}, {\"role\": \"assistant\", \"content\": \"...\"}]"
}
```

> `conversation` 필드는 HuggingFace datasets 호환을 위해 JSON 문자열로 직렬화되어 있습니다.  
> `json.loads(record["conversation"])`으로 파싱하세요.

---

## 필드 설명

| 필드 | 타입 | 설명 |
|------|------|------|
| `id` | string | `{시나리오ID}_{변형번호}` 형식 고유 ID |
| `topic` | string | 대화 주제 (9개 카테고리) |
| `situation` | string | 구체적인 대화 상황 설명 |
| `task_type` | string | 항상 `"daily_chat"` |
| `domain` | string | `topic`과 동일 |
| `model_name` | string | 생성에 사용된 모델명 |
| `turns` | int | 항상 `2` (2-turn 대화) |
| `conversation` | string | JSON 직렬화된 대화 리스트 |

---

## 생성 방식

각 시나리오에 대해 4단계 API 호출로 대화를 생성했습니다:

1. **Stage 1** — 사용자 첫 발화 생성 (동일 시나리오 내 이전 발화 목록을 프롬프트에 포함하여 중복 방지)
2. **Stage 2** — AI 첫 응답 생성
3. **Followup User** — 사용자 두 번째 발화 생성
4. **Followup Assistant** — AI 두 번째 응답 생성

각 시나리오당 최대 150개 변형을 생성하여 다양성을 확보했습니다.

---

## 품질 필터링

### 생성 단계 필터

| 거절 사유 | 건수 |
|----------|------|
| turn_too_short | 60 |
| repetition | 5 |
| **총 거절** | **65** |

### 중복 제거 단계

| 항목 | 수치 |
|------|------|
| 원본 생성 수 | 202,435개 |
| 중복 제거 수 | 11,342개 (5.60%) |
| 최종 샘플 수 | 191,093개 |

---

## 사용 예시

```python
from datasets import load_dataset
import json

ds = load_dataset("mkd-chanwoo/keural-conversation")

for record in ds["train"]:
    conversation = json.loads(record["conversation"])
    for turn in conversation:
        print(f"[{turn['role']}] {turn['content']}")
    break
```

---

## 주의사항

- 본 데이터셋은 AI 모델(`google/gemma-4-26B-A4B-it`)이 생성한 합성 데이터입니다.
- 실제 인간 대화가 아니며, 학습 데이터 보강 용도로 제작되었습니다.
- `conversation` 필드는 HuggingFace datasets 호환을 위해 JSON 문자열로 직렬화되어 있습니다.