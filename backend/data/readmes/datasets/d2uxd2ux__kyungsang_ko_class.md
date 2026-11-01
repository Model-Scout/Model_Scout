---
language:
- ko
pretty_name: standard-question-gyeongsang-answer
tags:
- korean
- dialect
- instruction
- qa
- text-generation
task_categories:
- text-generation
- question-answering
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
---

# Dataset Card for kyungsang_ko_class

## 개요

이 데이터셋은 표준어 질문과 경상도 사투리 답변으로 구성된 한국어 질의응답 데이터셋입니다.

- 입력 형식: `question`
- 출력 형식: `answer`
- 주요 특징: 표준어 질문, 경상도 사투리 답변
- 사투리 강도: strong

## 데이터 구조

각 샘플은 아래와 같은 구조를 가집니다.

```json
{
  "question": "한국의 수도는 어디인가?",
  "answer": "서울 아이가. 그건 뭐 다 아는 거라 안카나."
}
```

## 스플릿

- train: 398
- validation: 45

## 소스 파일

- 원본 업로드 파일: `data.jsonl`

## 활용 예시

- 한국어 LLM instruction tuning
- 표준어 → 경상도 사투리 스타일 변환
- 방언 생성 및 스타일 제어 실험

## 주의사항

- 본 데이터셋은 생성형 방식으로 구축되었으므로, 실제 지역 화자의 자연 발화와 차이가 있을 수 있습니다.
- 사투리 표현은 지역, 세대, 맥락에 따라 달라질 수 있습니다.
