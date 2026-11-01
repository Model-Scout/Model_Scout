---
type: "dataset"
id: "kaggle/nitirajkulkarni/seoul-kr-1835848"
source: "kaggle"
url: "https://www.kaggle.com/datasets/nitirajkulkarni/seoul-kr-1835848"
downloads: 18
summary: "서울의 2022년부터 2026년까지 대기질 지표와 오염물질 시계열 데이터로 장기 대기질 분석에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[시계열 예측]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/nitirajkulkarni/seoul-kr-1835848

> dataset · [Kaggle](https://www.kaggle.com/datasets/nitirajkulkarni/seoul-kr-1835848)

서울의 2022년부터 2026년까지 대기질 지표와 오염물질 시계열 데이터로 장기 대기질 분석에 활용 가능

## 분류

- **작업**: [[임베딩]] — ner · readme = `build models that link air quality to urban characteristics` · 신뢰도 low
- **작업**: [[시계열 예측]] — ner · readme = `historical air quality time series for Seoul covering 2022-08-01 to 2026-02-18` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `historical air quality time series for Seoul` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `historical air quality time series for Seoul` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `This dataset contains historical air quality time series for Seoul` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Use this dataset to analyze long-run air quality trends in Seoul, compare Seoul with other cities, and build models` · 신뢰도 low
