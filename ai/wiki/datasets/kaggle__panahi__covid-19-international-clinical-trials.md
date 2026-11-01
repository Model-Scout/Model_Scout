---
type: "dataset"
id: "kaggle/panahi/covid-19-international-clinical-trials"
source: "kaggle"
url: "https://www.kaggle.com/datasets/panahi/covid-19-international-clinical-trials"
downloads: 3853
summary: "COVID-19 임상시험 데이터를 WHO ICTRP, ClinicalTrials.gov 등에서 수집한 국제 임상시험 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/panahi/covid-19-international-clinical-trials

> dataset · [Kaggle](https://www.kaggle.com/datasets/panahi/covid-19-international-clinical-trials)

COVID-19 임상시험 데이터를 WHO ICTRP, ClinicalTrials.gov 등에서 수집한 국제 임상시험 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `The WHO ICTRP dataset is best used to have access to all international trials.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `They release the COVID-19 data in Excel format and I converted this data to CSV` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `They release the COVID-19 data in Excel format and I converted this data to CSV` · 신뢰도 low
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `COVID-19 Clinical Trials from WHO ICTRP, ClinicalTrials.gov, etc.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This Dataset will be updated on a daily basis.` · 신뢰도 low
