---
type: "dataset"
id: "kaggle/lucalullo/global-education-attainment-1950-2015"
source: "kaggle"
url: "https://www.kaggle.com/datasets/lucalullo/global-education-attainment-1950-2015"
downloads: 43
summary: "1950년부터 2015년까지 146개국의 교육 수준과 학력 연수를 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
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
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/lucalullo/global-education-attainment-1950-2015

> dataset · [Kaggle](https://www.kaggle.com/datasets/lucalullo/global-education-attainment-1950-2015)

1950년부터 2015년까지 146개국의 교육 수준과 학력 연수를 제공하는 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `making it ready for immediate analysis and high-quality visualizations.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This dataset provides a comprehensive historical series of Educational Attainment levels across the global population from 1950 to 2015` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Each row represents a specific population cohort defined by Country, Year, Gender, and Age Group.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `These columns represent the percentage of the population in that cohort that has completed a specific level of schooling` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **도메인**: [[행정·민원]] — tag_match · tags = `government` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset provides a comprehensive historical series of Educational Attainment levels across the global population from 1950 to 2015` · 신뢰도 low
