---
type: "dataset"
id: "Ngseo/zi-gemini"
source: "huggingface"
url: "https://huggingface.co/datasets/Ngseo/zi-gemini"
downloads: 14
summary: "미국, 코스피, 코스닥 주식 시장의 교차 섹션 주가 예측 및 포트폴리오 연구용 정량 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
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
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Ngseo/zi-gemini

> dataset · [Hugging Face](https://huggingface.co/datasets/Ngseo/zi-gemini)

미국, 코스피, 코스닥 주식 시장의 교차 섹션 주가 예측 및 포트폴리오 연구용 정량 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — metadata · readme, task_categories = `time-series-forecasting` · 신뢰도 medium
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-regression` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `Quantitative stock market dataset covering US, KOSPI (KO), and KOSDAQ (KQ) exchanges.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Designed for cross-sectional stock return prediction and portfolio construction research.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Using 8-model ensemble (LightGBM, XGBoost, Ridge, MLP, Transformer, TabNet, StockMixer, DoubleAdapt)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
