---
type: "dataset"
id: "kaggle/gomjellie/kospi-price-data"
source: "kaggle"
url: "https://www.kaggle.com/datasets/gomjellie/kospi-price-data"
downloads: 1261
summary: "한국 주식 코스피 가격 데이터를 모은 CSV 파일로 주식 가격 분석에 활용 가능"
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
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/gomjellie/kospi-price-data

> dataset · [Kaggle](https://www.kaggle.com/datasets/gomjellie/kospi-price-data)

한국 주식 코스피 가격 데이터를 모은 CSV 파일로 주식 가격 분석에 활용 가능

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `kospi.csv contains average kospi price. you can use this for checking whether if korean stock is day-off or not.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `.csv files` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `.csv files` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `I got all these .csv files using `pandas data reader` but getting every single kospi data through `pandas data reader` is annoying. so I decided to share this f` · 신뢰도 low
