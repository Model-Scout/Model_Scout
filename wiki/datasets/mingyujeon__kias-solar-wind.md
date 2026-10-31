---
type: "dataset"
id: "mingyujeon/kias-solar-wind"
source: "huggingface"
url: "https://huggingface.co/datasets/mingyujeon/kias-solar-wind"
downloads: 218
summary: "SDO/AIA 193Å 이미지와 코로날 홀 시각화 포함 태양풍 예측 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mingyujeon/kias-solar-wind

> dataset · [Hugging Face](https://huggingface.co/datasets/mingyujeon/kias-solar-wind)

SDO/AIA 193Å 이미지와 코로날 홀 시각화 포함 태양풍 예측 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — metadata · readme, task_categories = `time-series-forecasting` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `SDO/AIA 193Å FITS 이미지와 시각화 PNG를 포함한 태양풍 예측 데이터셋입니다.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme = `CSV 데이터(solar_wind-public.csv, solar_wind-private.csv, solar_wind_data.csv)는 GitHub 저장소에 포함되어 있습니다.` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `태양풍 예측 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `CSV 데이터(solar_wind-public.csv, solar_wind-private.csv, solar_wind_data.csv)는 GitHub 저장소에 포함되어 있습니다.` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
