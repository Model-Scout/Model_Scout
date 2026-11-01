---
type: "dataset"
id: "kaggle/shirmani/characteristics-corona-patients"
source: "kaggle"
url: "https://www.kaggle.com/datasets/shirmani/characteristics-corona-patients"
downloads: 1605
summary: "COVID-19 환자 특성에 초점을 맞춘 데이터셋으로 감염, 합병증, 사망 위험군 분석에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/shirmani/characteristics-corona-patients

> dataset · [Kaggle](https://www.kaggle.com/datasets/shirmani/characteristics-corona-patients)

COVID-19 환자 특성에 초점을 맞춘 데이터셋으로 감염, 합병증, 사망 위험군 분석에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `identify the Risk groups and characteristics human-level that impact on infection, Complication and Death as a result of the disease` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `A version that includes cleaning the data and engineering new features` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Consists only of INT and FLOAT` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `healthcare` · 신뢰도 medium
- **도메인**: [[뉴스·미디어]] — tag_match · tags = `news` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Machine-ready version of machine learning model` · 신뢰도 low
