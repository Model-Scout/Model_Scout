---
license: apache-2.0
language:
  - ko
  - en
task_categories:
  - text-generation
  - question-answering
tags:
  - lora
  - sft
  - rag
  - grounded-generation
  - abstention
  - korean
size_categories:
  - 100K<n<1M
pretty_name: algocean-executor
---

# algocean-executor

질의와 근거를 받아 **답을 쓰거나, 근거가 부족하면 기권**하도록 가르치는 LoRA SFT 데이터셋입니다.  
파이프라인에서 **최종 답변을 쓰는 노드**입니다.

## 규모

| 파일 | 행 수 |
|------|------:|
| `executor.jsonl` | 150,000 |
| `executor.eval.jsonl` | 2,000 |

- 형식: JSONL, `messages` 3턴
- 언어: 한국어 약 70% · 영어 약 30%

## 어디에 쓰나요

- 주어진 근거만으로 답하는 grounded generation
- 근거 없음 / 충돌 / 개인 메모뿐일 때 **기권·조건부 답변**
- 사내 QA에서 “근거 없이 단정하지 않기”

## 어떤 모델에 LoRA 하나요

- 베이스: **1B ~ 9B** 인스트럭트 모델
- rank 8~16, alpha 16~32, lr 1e-4~2e-4, epochs 2~3
- loss: assistant 턴만
- 장문 tier는 컨텍스트에 맞게 필터

## 사용

```python
from datasets import load_dataset

ds = load_dataset("Algocean/algocean-executor", data_files="executor.jsonl", split="train")
ev = load_dataset("Algocean/algocean-executor", data_files="executor.eval.jsonl", split="train")
```

- 학습: `messages` 만
- 메타는 필터용

### assistant 출력 (요약)

```json
{
  "answer": "...",
  "evidence_refs": [{"document_id": "...", "span": "..."}],
  "abstain": false,
  "conditional": false,
  "reason_code": "SUPPORTED"
}
```

`reason_code`: `SUPPORTED` / `NO_EVIDENCE` / `PERSONAL_ONLY` / `CONFLICTING`  
`conditional=true`이면 답은 쓰되 성립 조건을 밝힙니다.


식별자·문서 id는 중립 코드(`mNN`, `doc-NNNN`, `Brand-*` 등)로 정규화되어 있다. 학습에는 `messages`만 쓴다.

## 라이선스

Apache-2.0
