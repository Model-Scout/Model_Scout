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
  - model-selection
  - korean
size_categories:
  - 100K<n<1M
pretty_name: algocean-router
---

# algocean-router

질의·보안 등급·사용 가능한 모델 목록을 받아 **어느 모델로 보낼지(또는 기권)** 정하도록 가르치는 LoRA SFT 데이터셋입니다.

파이프라인 **첫 관문**입니다. 답을 만들지 않고, 근거도 보지 않습니다. **누가 이 일을 할지**만 정합니다.

## 규모

| 파일 | 행 수 |
|------|------:|
| `router.jsonl` | 150,000 |
| `router.eval.jsonl` | 2,000 |

- 형식: JSONL, `messages` 3턴
- 언어: 한국어 약 70% · 영어 약 30%

## 어디에 쓰나요

- 멀티 모델 게이트웨이의 **난이도·보안 기반 라우팅**
- 후보 모델 레지스트리를 읽고 스펙(컨텍스트·등급·비용 등)으로 선택
- 조건 맞는 모델이 없으면 `ABSTAIN`

모델 id는 샘플마다 가명으로 바뀌어 있어, **이름 암기가 아니라 스펙 추론**을 배우게 됩니다.

## 어떤 모델에 LoRA 하나요

- 베이스: **1B ~ 9B** 인스트럭트 모델
- rank 8~16, alpha 16~32, lr 1e-4~2e-4, epochs 2~3
- loss: assistant 턴만

## 사용

```python
from datasets import load_dataset

ds = load_dataset("Algocean/algocean-router", data_files="router.jsonl", split="train")
ev = load_dataset("Algocean/algocean-router", data_files="router.eval.jsonl", split="train")
```

- 학습: `messages` 만
- 메타는 필터용

### assistant 출력 (요약)

```json
{
  "difficulty": 3,
  "security": "internal",
  "selection": "MDL-VERDANT-2",
  "reason_code": "...",
  "confidence": 0.9
}
```

- `selection`: user에 제시된 후보 id 중 하나를 **그대로** (없으면 `ABSTAIN`)
- `difficulty`: 1~5


식별자·문서 id는 중립 코드(`mNN`, `doc-NNNN`, `Brand-*` 등)로 정규화되어 있다. 학습에는 `messages`만 쓴다.

## 라이선스

Apache-2.0
