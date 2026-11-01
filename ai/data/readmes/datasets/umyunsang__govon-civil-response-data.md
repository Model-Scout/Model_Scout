---
language:
- ko
license: cc-by-4.0
task_categories:
- text-generation
- question-answering
tags:
- civil-complaint
- government
- korean
- instruction-tuning
size_categories:
- 10K<n<100K
---

# GovOn Civil Response Dataset

민원답변 어댑터 학습용 instruction-tuning 데이터셋.

## 소스
- **AI Hub 71852**: 공공 민원 상담 LLM 데이터 (중앙행정기관 + 지방행정기관 + 국립아시아문화전당)
- **AI Hub 71847**: 행정법 LLM 데이터 (결정례 QA + 법령 QA)

## 통계
| Split | Records | Size |
|-------|---------|------|
| train | 66,819 | 90MB |
| val   | 7,425  | 10MB |

## 형식
```json
{
  "instruction": "다음 민원에 대한 답변을 작성해 주세요.",
  "input": "질문 텍스트",
  "output": "답변 텍스트 (평균 500-1000자)",
  "source": "71852_중앙행정기관",
  "category": "도로관리과"
}
```

## 라이선스
공공누리 제1유형(출처표시) + AI Hub 이용약관
