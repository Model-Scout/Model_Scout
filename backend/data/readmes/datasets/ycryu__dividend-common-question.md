---
language: ko
datasets:
- dividend-common-question
task_categories:
- text-generation
tags:
- finance
- dividend
- q&a
size_categories:
- 10-100
source: custom
license: apache-2.0
---
# Dividend Common Question Dataset

## 📖 개요
이 데이터셋은 **배당주 투자 관련 자주 묻는 질문과 답변**을 Alpaca 포맷(`instruction`, `input`, `output`)으로 구성한 학습용 자료입니다.  
총 10여 개의 샘플이 포함되어 있으며, 파인튜닝 실습이나 자연어 처리 모델 학습에 활용할 수 있습니다.

## 📂 데이터 구조
데이터는 CSV 파일(`dividend-common-question.csv`)로 제공되며, 다음과 같은 열을 포함합니다:

- **instruction**: 모델에게 주는 지시문 (예: "배당성향이 높아야 좋은 건가요?")  
- **input**: 지시문을 수행하는 데 필요한 추가 입력 (없으면 빈칸)  
- **output**: 모델이 생성해야 하는 답변 (예: "꼭 그렇다고 할 수는 없습니다...")

### 예시
```csv
instruction,input,output
"시가배당수익률이 높으면 좋은 배당주인가요?","","꼭 그렇다고 할 수는 없습니다. 배당재원과 배당성향, 배당성장률 등을 함께 고려해야 합니다."
"배당성향이 높아야 좋은 건가요?","","꼭 그렇다고 할 수는 없습니다. 너무 낮으면 주주환원 의지가 부족한 것일 수 있고 너무 높으면 배당금을 무리하게 지급하느라 회사 재정이 어려워질 수 있습니다."
"유보율은 왜 중요한가요?","","유보율은 기업이 이익을 얼마나 내부에 남겨두는지를 나타내며, 미래 투자와 배당 지속 가능성을 판단하는 데 중요합니다."
```

## 🎯 활용 예시
- LLM 파인튜닝 실습용 데이터셋
- 금융/투자 관련 Q&A 챗봇 학습
- Instruction-following 모델 학습 예제

## 📌 주의사항
- 본 데이터셋은 **학습 및 실습 목적**으로 제작된 예시 데이터입니다.
- 실제 투자 판단에 활용해서는 안 되며, 교육 및 연구용으로만 사용해야 합니다.