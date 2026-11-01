---
type: "dataset"
id: "kaggle/josemreyess/korean-demographics-2000-2022"
source: "kaggle"
url: "https://www.kaggle.com/datasets/josemreyess/korean-demographics-2000-2022"
downloads: 13
summary: "한국의 혼인, 이혼, 출생 및 연도별 인구 통계를 포함한 인구 통계 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/josemreyess/korean-demographics-2000-2022

> dataset · [Kaggle](https://www.kaggle.com/datasets/josemreyess/korean-demographics-2000-2022)

한국의 혼인, 이혼, 출생 및 연도별 인구 통계를 포함한 인구 통계 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `time series analysis` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The dataset includes vital statistics such as marriages, divorces, and births, along with South Korea's annual population by province.` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The dataset includes vital statistics such as marriages, divorces, and births, along with South Korea's annual population by province.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Vital Statistics and Population` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `I collected it using the government's statistical analysis database, KOSIS` · 신뢰도 low
