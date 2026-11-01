---
type: "dataset"
id: "kaggle/gpreda/coronavirus-2019ncov"
source: "kaggle"
url: "https://www.kaggle.com/datasets/gpreda/coronavirus-2019ncov"
downloads: 11591
summary: "존스 홉킨스 CSSE의 2019 코로나바이러스 일일 업데이트 데이터로 확진자, 사망자 등 시계열 분석 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[의료·보건]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/gpreda/coronavirus-2019ncov

> dataset · [Kaggle](https://www.kaggle.com/datasets/gpreda/coronavirus-2019ncov)

존스 홉킨스 CSSE의 2019 코로나바이러스 일일 업데이트 데이터로 확진자, 사망자 등 시계열 분석 가능

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Try to forecast the evolution of cases.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Represent the geographical data distribution of 2019-nCoV spread.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Concatenate the daily reports files` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Represent time series with Confirmed, Recovered, Deaths cases.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `Data files © Original Authors` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `healthcare` · 신뢰도 medium
- **도메인**: [[뉴스·미디어]] — tag_match · tags = `news` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a curated version of 2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE.` · 신뢰도 low
