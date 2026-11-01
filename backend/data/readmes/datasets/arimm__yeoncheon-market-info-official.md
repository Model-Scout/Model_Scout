---
license: apache-2.0
task_categories:
- question-answering
language:
- ko
tags:
- yeoncheon
- gyeonggido
---

# 연천군 전통시장 현황 데이터셋 (Yeoncheon Market Info)

이 데이터셋은 대형 언어 모델(LLM)이 경기도 연천군과 같은 소규모 지역 정보에 대해 일으키는 환각(Hallucination) 현상을 방지하고, 정확한 정보를 제공하기 위해 제작되었습니다.

## 1. 데이터 출처
- **출처**: [경기도 공공데이터포털 - 전통시장 및 상점가 현황](https://www.gg.go.kr/opendata/openDataContent.do?gg_content_idx=10439)
- **기준일**: 2023년 12월 31일

## 2. 데이터 구성
- **instruction**: 연천군 시장 관련 질문 (대화체 및 정보 요청 포함)
- **output**: 공공데이터에 근거한 정확한 답변
- **source**: 데이터의 공식 출처

## 3. 활용 목적
- 한국 로컬 지리 및 행정 정보에 대한 AI 학습 및 검증용
- 연천군 지역 경제 및 전통시장 정보 대중화