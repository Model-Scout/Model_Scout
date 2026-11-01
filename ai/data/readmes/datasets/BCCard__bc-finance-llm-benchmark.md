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
- benchmark
- llm-evaluation
pretty_name: BC Card Finance LLM Benchmark
size_categories:
- 100K<n<1M
---

# BC Card Finance LLM Benchmark

한국 금융 도메인 특화 LLM 성능 평가를 위한 벤치마크 데이터셋입니다.  
BC카드-연세대 DSL 산학협력(S2026 LLMOps 프로젝트)의 산출물입니다.

## 데이터셋 개요

| 항목 | 내용 |
|------|------|
| 총 문항 수 | 800 |
| 언어 | 한국어 |
| 도메인 | 금융 (BC카드 FAQ, 금융 일반) |
| 형식 | Question / Ground Truth |

## 컬럼 설명

| 컬럼 | 설명 |
|------|------|
| `no` | 순번 |
| `id` | 문항 ID |
| `대분류` | 데이터 출처 대분류 (BC카드FAQ, general 등) |
| `금융토픽` | 세부 금융 토픽 |
| `문제유형` | 문제 유형 (단일추론, 다중추론 등) |
| `question` | 평가 질문 |
| `ground_truth` | 정답 (참조 답변) |
| `source_tag` | 원본 출처 문서 태그 |

## 활용 방법

LLM-as-Judge 방식의 자동 평가 파이프라인에서 모델 응답과 `ground_truth`를 비교하는 용도로 활용합니다.

## 라이선스

Apache 2.0
