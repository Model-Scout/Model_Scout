---
type: "dataset"
id: "podongchip/kospi-daily-stock-features-2021-2026"
source: "huggingface"
url: "https://huggingface.co/datasets/podongchip/kospi-daily-stock-features-2021-2026"
downloads: 474
summary: "2021~2026년 KOSPI 948개 종목 일별 시세와 기술·거시지표 결합 주식 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[시계열 예측]]"
  - "[[언어 모델링]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# podongchip/kospi-daily-stock-features-2021-2026

> dataset · [Hugging Face](https://huggingface.co/datasets/podongchip/kospi-daily-stock-features-2021-2026)

2021~2026년 KOSPI 948개 종목 일별 시세와 기술·거시지표 결합 주식 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `퀀트 전략·팩터 리서치` · 신뢰도 low
- **작업**: [[시계열 예측]] — metadata · readme, task_categories = `time-series-forecasting` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `시계열·금융 ML 학습` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-regression` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme, task:tabular_prediction = `60개 컬럼` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:language_modeling = `종목코드는 앞자리 0이 있고` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `60개 컬럼` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:language_modeling = `text` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `머신러닝 학습용 한국 주식 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `kaggle/podongchip/korean-stock-daily-prices-indicators-20212026`
