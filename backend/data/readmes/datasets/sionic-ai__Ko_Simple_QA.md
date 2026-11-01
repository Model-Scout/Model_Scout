
---
language: ko
license: mit
tags:
  - korean
  - question-answering
  - translation
  - multilingual
dataset_info:
  features:
    - name: metadata
      dtype: string
    - name: problem
      dtype: string
    - name: answer
      dtype: string
    - name: korean_question
      dtype: string
    - name: korean_answer
      dtype: string
  config_name: default
  splits:
    - name: train
      num_examples: 4265
---

# 한영 질문답변 데이터셋

## 데이터셋 설명
이 데이터셋은 영어 질문답변 쌍과 그에 대응하는 한국어 번역으로 구성되어 있습니다. 
각 데이터 포인트

- 메타데이터: 주제, 답변 유형, 참고 URL 등의 정보
- 영어 질문
- 영어 답변
- 한국어 질문
- 한국어 답변

총 4,265개의 질문답변 쌍이 포함되어 있으며, CSV 형식으로 제공.

## 원천 데이터 관련 링크
https://github.com/openai/simple-evals
https://openai.com/index/introducing-simpleqa/


## 데이터 예시
```json
{
  "metadata": {
    "topic": "Science and technology",
    "answer_type": "Person",
    "urls": ["https://en.wikipedia.org/wiki/IEEE_Frank_Rosenblatt_Award"]
  },
  "problem": "Who received the IEEE Frank Rosenblatt Award in 2010?",
  "answer": "Michio Sugeno",
  "korean_question": "2010년에 누가 IEEE 프랭크 로젠블랫 어워드를 수상했나요?",
  "korean_answer": "스게노 미치오"
}