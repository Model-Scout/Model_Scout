---
license: apache-2.0
task_categories:
- text-classification
language:
- ko
tags:
- security
- tool-call
- guardrail
- korean
---

# Guardrail4Agent SFT Dataset

AI 에이전트 Tool Call 데이터 유출 탐지를 위한 한국어 학습 데이터셋입니다.

## 카테고리
| 레이블 | 설명 | 건수 |
|--------|------|------|
| safe | 정상 Tool Call | 2,380 |
| S1 | PII 유출 | 1,190 |
| S2 | Credential 유출 | 1,190 |
| S3 | Prompt Injection | 1,190 |
| S4 | 내부 데이터 외부 전달 | 630 |
| S5 | 시스템 프롬프트 추출 | 420 |

## 분할
- `data/sft_train.jsonl` — 4,900건 (70%)
- `data/sft_val.jsonl` — 1,050건 (15%)
- `data/sft_test.jsonl` — 1,050건 (15%)
