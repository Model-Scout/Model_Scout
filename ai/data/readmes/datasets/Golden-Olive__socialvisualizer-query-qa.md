---
license: cc-by-4.0
language:
  - ko
tags:
  - graphrag
  - qa
---

# SocialVisualizer Query QA Dataset

"2026 오픈소스 개발자대회" 출품작 **SocialVisualizer**의 `query` LoRA 어댑터
([`llama-3.1-8b-socialvisualizer-query-lora`](https://huggingface.co/Golden-Olive/llama-3.1-8b-socialvisualizer-query-lora))를
만들 때 사용한 QA 세트입니다.

## 구성

| 파일 | 문항 수 | 도메인 |
|---|---|---|
| `Llama_mail_QA.xlsx` | 73 | 이메일 |
| `Llama_messenger_QA.xlsx` | 70 | 메신저 |

## ⚠️ 주의사항

이 QA 세트는 `local_search` SFT 학습 데이터의 원본입니다. 143문항 전체가 train(129)/val(14)로
분할되어 실제 학습(및 체크포인트 선택)에 사용됐습니다. 따라서 학습에 사용되지 않은 독립적인
held-out 벤치마크가 아니라는 점에 유의해 주세요.

## 데이터 성격

전량 오프라인 단계에서 생성한 합성(가상) 데이터로, 실제 개인 메일/메신저 데이터는 포함되어
있지 않습니다.

## 출처

- 학습/추론 코드: https://github.com/s0-yeon/SocialVisualizer/tree/main/llama-finetune