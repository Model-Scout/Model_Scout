---
type: "dataset"
id: "kaggle/aiwithcagri/20-countries-salary-minimum-teacher-and-docter"
source: "kaggle"
url: "https://www.kaggle.com/datasets/aiwithcagri/20-countries-salary-minimum-teacher-and-docter"
downloads: 21
summary: "20개국의 2000~2026년 최저임금, 교사, 의사 월급 데이터를 담은 표 형식 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[문서 검색]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/aiwithcagri/20-countries-salary-minimum-teacher-and-docter

> dataset · [Kaggle](https://www.kaggle.com/datasets/aiwithcagri/20-countries-salary-minimum-teacher-and-docter)

20개국의 2000~2026년 최저임금, 교사, 의사 월급 데이터를 담은 표 형식 데이터입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `so you can easily filter and examine the specific country, year, or profession you want` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `20 Countries Minimum Salary , Teacher and Doctor Salaray` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `The first row in the Excel file is frozen (freeze panes) and automatic filters have been added` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `20 Countries Minimum Salary , Teacher and Doctor Salaray` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Apache 2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `20 Countries Minimum Salary , Teacher and Doctor Salaray` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Full Scope: A complete 27-year period from 2000 to 2026.` · 신뢰도 low
