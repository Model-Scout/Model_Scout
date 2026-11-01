---
language:
- ko
license: apache-2.0
task_categories:
- question-answering
tags:
- finance
- korean
- bc-card
- golden-set
- regression-testing
- llm-evaluation
pretty_name: BC Card Finance LLM Golden Set
size_categories:
- n<1K
---

# BC Card Finance LLM Golden Set

LLM 배포 전 Regression 품질 검증을 위한 골든셋 데이터셋입니다.  
BC카드-연세대 DSL 산학협력(S2026 LLMOps 프로젝트)의 산출물입니다.

## 데이터셋 개요

| 파일 | 설명 | 행 수 |
|------|------|------|
| `data/regression_golden_set.csv` | Regression Gate용 핵심 골든셋 | 300 |
| `data/financial_edge_cases_200.csv` | 금융 LLM 엣지 케이스 (할루시네이션 검출용) | 200 |
| `data/hard_negatives_qa_50.csv` | Hard Negative 샘플 | 50 |

## 활용 방법

모델 업데이트 또는 프롬프트 변경 후 배포 전 회귀 테스트(Regression Gate)에 활용합니다.  
점수가 임계값 아래로 떨어지면 배포를 차단합니다.

## 라이선스

Apache 2.0
