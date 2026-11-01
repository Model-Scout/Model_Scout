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
  - rag
  - verification
  - korean
size_categories:
  - 100K<n<1M
pretty_name: algocean-verifier
---

# algocean-verifier

주장과 근거를 받아 **주장이 근거로 뒷받침되는지 판정**하도록 가르치는 LoRA SFT 데이터셋입니다.  
어긋나면 실패 유형까지 말합니다.

RAG 파이프라인의 **검증 노드**용입니다. 근거를 인용하지 않고 판정만 합니다.

## 규모

| 파일 | 행 수 |
|------|------:|
| `verifier.jsonl` | 150,000 |
| `verifier.eval.jsonl` | 2,000 |

- 형식: JSONL, `messages` 3턴
- 언어: 한국어 약 70% · 영어 약 30%
- think 비율이 높아 대조 추론에 적합

## 어디에 쓰나요

- 추출된 근거가 주장을 실제로 지지하는지 검사
- 숫자·날짜 왜곡, 근거 부재 등 **실패 유형 분류**
- 경량 모델로 프론티어 답변 검증 필터

## 어떤 모델에 LoRA 하나요

- 베이스: **1B ~ 9B** 인스트럭트 모델
- rank 8~16, alpha 16~32, lr 1e-4~2e-4, epochs 2~3
- loss: assistant 턴만

## 사용

```python
from datasets import load_dataset

ds = load_dataset("Algocean/algocean-verifier", data_files="verifier.jsonl", split="train")
ev = load_dataset("Algocean/algocean-verifier", data_files="verifier.eval.jsonl", split="train")
```

- 학습: `messages` 만
- 메타는 필터용

### assistant 출력 (요약)

```json
{"verdict": "FAIL", "failure_type": "NUMERIC_DISTORTION"}
```

- `verdict`: `PASS` / `FAIL` / `UNSURE`
- `failure_type`: FAIL일 때 — `NO_EVIDENCE` / `NUMERIC_DISTORTION` / `DATE_DISTORTION` / `TRUST_IGNORED` / `CLAIM_MISMATCH` / `OVERGENERALIZATION` 등


식별자·문서 id는 중립 코드(`mNN`, `doc-NNNN`, `Brand-*` 등)로 정규화되어 있다. 학습에는 `messages`만 쓴다.

## 라이선스

Apache-2.0
