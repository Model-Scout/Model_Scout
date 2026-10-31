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
  - evidence
  - abstention
  - korean
size_categories:
  - 100K<n<1M
pretty_name: algocean-extractor
---

# algocean-extractor

질의와 문서 묶음을 받아 **답의 근거 span을 원문 그대로 뽑거나, 없으면 기권**하도록 가르치는 LoRA SFT 데이터셋입니다.

RAG / 사내 QA 파이프라인의 **근거 추출 노드**용입니다. 답을 쓰지 않고, 재료가 어디에 있는지만 가리킵니다.

## 규모

| 파일 | 행 수 |
|------|------:|
| `extractor.jsonl` | 150,000 |
| `extractor.eval.jsonl` | 2,000 |

- 형식: JSONL, `messages` 3턴 (system / user / assistant)
- 언어: 한국어 약 70% · 영어 약 30%
- eval은 학습셋과 별도 생성

## 어디에 쓰나요

- 문서 청크에서 **문자 단위 근거 인용**이 필요한 추출기
- “모르면 기권” 정책을 경량 모델에 LoRA로 심을 때
- 프론티어 모델 앞단의 값싼 grounding 필터

## 어떤 모델에 LoRA 하나요

지식 암기가 아니라 **형식·정책 행동**용입니다.

- 베이스: **1B ~ 9B** 인스트럭트 모델
- rank 8~16, alpha 16~32, lr 1e-4~2e-4, epochs 2~3
- **loss는 assistant 턴만** (user에 긴 문서가 있음)

장문 `tier` (T3·T4)는 컨텍스트가 충분한 모델에만 넣으세요. 잘라 넣으면 span이 잘려 틀린 라벨을 학습합니다.

## 사용

```python
from datasets import load_dataset

ds = load_dataset("Algocean/algocean-extractor", data_files="extractor.jsonl", split="train")
ev = load_dataset("Algocean/algocean-extractor", data_files="extractor.eval.jsonl", split="train")
```

- 학습 입력: `messages` 만 (chat template)
- 메타(`id`, `industry`, `tier` 등)는 필터용 — 학습에 넣지 마세요

### assistant 출력 (요약)

```json
{
  "evidence": [{"document_id": "...", "span": "원문 그대로", "trust": "official|team|personal"}],
  "abstain": false,
  "reason_code": "SUPPORTED"
}
```

`reason_code`: `SUPPORTED` / `NO_EVIDENCE` / `DISTRACTOR_ONLY` / `CONFLICTING`  
`span`은 user 메시지 안 원문과 **문자 단위로 일치**해야 합니다.


식별자·문서 id는 중립 코드(`mNN`, `doc-NNNN`, `Brand-*` 등)로 정규화되어 있다. 학습에는 `messages`만 쓴다.

## 라이선스

Apache-2.0
