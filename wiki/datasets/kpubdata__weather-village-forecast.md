---
type: "dataset"
id: "kpubdata/weather-village-forecast"
source: "huggingface"
url: "https://huggingface.co/datasets/kpubdata/weather-village-forecast"
downloads: 58
summary: "기상청 단기예보 데이터를 활용한 기상 예측용 그리드 기반 날씨 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[시계열 예측]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# kpubdata/weather-village-forecast

> dataset · [Hugging Face](https://huggingface.co/datasets/kpubdata/weather-village-forecast)

기상청 단기예보 데이터를 활용한 기상 예측용 그리드 기반 날씨 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Short-term weather forecast data from the Korea Meteorological Administration (기상청). Grid-based forecasts with multiple weather categories (temperature, precipi` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-regression` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme, task:tabular_prediction = `Features: 8` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Features: 8` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · readme, tags = `weather` · 신뢰도 medium
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Data sourced via the official data.go.kr API.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
