---
license: cc-by-4.0
language:
- ko
task_categories:
- question-answering
- text-generation
tags:
- legal
- korean
- instruction-tuning
- lora
size_categories:
- 100K<n<1M
---

# GovOn Legal Response Dataset

법률해석 및 근거인용 LoRA 어댑터 학습용 instruction-tuning 데이터셋.

## 데이터 소스

- **HF 판례**: 70,814건
- **71841 민사법**: 75,624건
- **71843 지식재산권**: 76,160건
- **71848 형사법**: 47,432건

## 통계

- 중복 제거: 193건
- Train: 242,854건
- Validation: 26,983건
- 총합: 269,837건

## 형식

각 레코드는 JSONL 형식이며 다음 필드를 포함합니다:

```json
{
  "instruction": "다음 법률 질문에 관련 법령 조항을 인용하여 답변하세요.",
  "input": "질문 텍스트",
  "output": "법적 근거를 포함한 답변",
  "source": "데이터 소스 식별자",
  "category": "법률 카테고리"
}
```

## 라이선스

CC-BY-4.0
