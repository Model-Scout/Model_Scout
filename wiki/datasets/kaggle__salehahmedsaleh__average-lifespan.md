---
type: "dataset"
id: "kaggle/salehahmedsaleh/average-lifespan"
source: "kaggle"
url: "https://www.kaggle.com/datasets/salehahmedsaleh/average-lifespan"
downloads: 107
summary: "세계 인구의 출생 시 기대수명을 국가별로 제공하는 건강 및 사회과학 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[정보 추출]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/salehahmedsaleh/average-lifespan

> dataset · [Kaggle](https://www.kaggle.com/datasets/salehahmedsaleh/average-lifespan)

세계 인구의 출생 시 기대수명을 국가별로 제공하는 건강 및 사회과학 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `It provides global, regional, and country-specific figures, with separate data for males and females.` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `Life Span of the World Population
The dataset from Worldometer ranks countries based on life expectancy at birth` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `The dataset from Worldometer ranks countries based on life expectancy at birth` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `It provides global, regional, and country-specific figures, with separate data for males and females.` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Apache 2.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `As a key indicator of public health, quality of life, and healthcare efficiency, this data offers valuable insights` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Data Analysis & Machine Learning Approaches for Life Expectancy
Data Analysis Approaches
Life expectancy data can be explored using` · 신뢰도 low
