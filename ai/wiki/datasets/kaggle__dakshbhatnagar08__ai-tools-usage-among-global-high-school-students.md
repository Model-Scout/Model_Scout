---
type: "dataset"
id: "kaggle/dakshbhatnagar08/ai-tools-usage-among-global-high-school-students"
source: "kaggle"
url: "https://www.kaggle.com/datasets/dakshbhatnagar08/ai-tools-usage-among-global-high-school-students"
downloads: 2144
summary: "전 세계 고등학생들의 AI 도구 사용 패턴을 시뮬레이션한 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/dakshbhatnagar08/ai-tools-usage-among-global-high-school-students

> dataset · [Kaggle](https://www.kaggle.com/datasets/dakshbhatnagar08/ai-tools-usage-among-global-high-school-students)

전 세계 고등학생들의 AI 도구 사용 패턴을 시뮬레이션한 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Classification: Predicting AI usage patterns` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `NLP tasks with open-ended responses` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Visualization & EDA` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `tabular` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `tabular` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `MIT` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `A synthetic dataset simulating how students worldwide use AI tools for academics` · 신뢰도 low
