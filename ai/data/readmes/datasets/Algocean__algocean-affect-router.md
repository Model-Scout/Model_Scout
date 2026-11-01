---
license: apache-2.0
language:
  - ko
  - en
task_categories:
  - text-generation
  - text-classification
tags:
  - lora
  - sft
  - routing
  - affect
  - empathy
  - korean
size_categories:
  - 10K<n<100K
pretty_name: algocean-affect-router
---

# algocean-affect-router

사용자 발화를 받아 **지금 공감이 필요한지, 해결·정보가 필요한지** 판정하도록 가르치는 LoRA SFT 데이터셋입니다.

사용자의 성격이 아니라 **이 프롬프트가 지금 요구하는 응답 방식**을 가르칩니다.

## 규모

| 파일 | 행 수 |
|------|------:|
| `affect_router.jsonl` | 41,042 |
| `affect_router.eval.jsonl` | 2,000 |

- 형식: JSONL, `messages` 3턴
- 언어: 한국어 약 70% · 영어 약 30%
- 최소쌍(`pair_id`) 포함 — train/eval 분할 시 **쌍 단위**로 나눌 것

## 어디에 쓰나요

- 챗봇 응답 전 **공감(F) vs 해결(T)** 라우팅
- 같은 주제라도 어투에 따라 답이 달라져야 하는 경우
- 경량 모델로 톤 분기만 맡길 때

## 어떤 모델에 LoRA 하나요

출력이 짧고 클래스가 적어 **가장 가벼운 노드**입니다.

- 베이스: **1B ~ 3B** 인스트럭트 모델 권장
- rank 8, alpha 16, lr 2e-4, epochs 3
- loss: assistant 턴만

## 사용

```python
from datasets import load_dataset

ds = load_dataset("Algocean/algocean-affect-router", data_files="affect_router.jsonl", split="train")
ev = load_dataset("Algocean/algocean-affect-router", data_files="affect_router.eval.jsonl", split="train")
```

- 학습: `messages` 만
- `pair_id` 등 메타는 분할·분석용 — 학습에 넣지 마세요

### assistant 출력 (요약)

```json
{
  "route": 1,
  "f_score": 0.82,
  "reason": "..."
}
```

| 필드 | 뜻 |
|------|-----|
| `route` | 1 = 공감 우선 · 0 = 해결 우선 |
| `f_score` | 0~1, 클수록 공감 쪽 (`route`는 0.5 기준) |
| `reason` | 한 줄 근거 |

호출부는 `route`만 써도 됩니다.


식별자·문서 id는 중립 코드(`mNN`, `doc-NNNN`, `Brand-*` 등)로 정규화되어 있다. 학습에는 `messages`만 쓴다.

## 라이선스

Apache-2.0
