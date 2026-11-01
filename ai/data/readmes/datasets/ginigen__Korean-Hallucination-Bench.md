---
license: apache-2.0
language:
- ko
task_categories:
- question-answering
tags:
- hallucination
- korean
- benchmark
- llm-evaluation
- legal
- medical
- finance
size_categories:
- 10K<n<100K
---

# Korean Hallucination Benchmark (한국어 환각 진단 벤치마크)

한국어 LLM의 **환각(hallucination) 저항성**을 평가하는 4지선다 벤치마크입니다. 법령·특허·행정·의료·금융 5개 전문 도메인에서, 한국어 특화 환각 유형 10종을 다룹니다. 각 문항은 사실 정답 1개와 **전문가도 속을 만큼 그럴듯한 환각 오답 3개**로 구성됩니다.

## 통계
- **총 10,167문항** (4지선다)
- **도메인(5)**: 법령 1,901 · 특허 2,190 · 행정 1,864 · 의료 2,113 · 금융 2,099
- **환각 유형(10)**: 수치·날짜 오류, 조항 왜곡, 근거 없는 추론, 한자어·신조어 혼재, 과잉 일반화, 멀티턴 맥락 붕괴, 존댓말·반말 역전, 출처 날조, 용어 왜곡, 사실 날조

## 구축 방법
- **문항 생성**: Darwin-398B-JGOS (문제·선택지)
- **정답 검수·교정**: Claude (Anthropic) — 각 문항의 정답을 한국 법령/제도/사실 기준으로 재검증·교정하여 정답 신뢰성을 확보하고 생성 모델의 편향을 제거
- **자동 폐기**: 정답이 불명확하거나 복수인 문항은 제외

## 데이터 형식
```json
{
  "domain": "법령",
  "hallucination_type": "수치날짜오류",
  "question": "질문",
  "options": ["A", "B", "C", "D"],
  "answer_index": 2,
  "answer": "정답 텍스트",
  "explanation": "정답 근거와 각 오답이 틀린 이유"
}
```

## 평가 방법
모델에게 `질문 + A~D`를 제시하고 정답을 고르게 하여, **환각 선택지에 속지 않고 정답을 고르는 비율(환각 저항 정확도)**을 측정합니다 (greedy decoding).

## 용도
지니젠AI **LLM X-RAY**의 Hallucination 진단 모듈 평가셋. 한국어 LLM의 도메인별 환각 취약점을 진단합니다.

## 라이선스 & 출처
Apache 2.0 · 지니젠AI (NIPA 첨단 GPU 활용 지원사업)
