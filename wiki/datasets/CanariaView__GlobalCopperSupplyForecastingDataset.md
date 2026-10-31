---
type: "dataset"
id: "CanariaView/GlobalCopperSupplyForecastingDataset"
source: "huggingface"
url: "https://huggingface.co/datasets/CanariaView/GlobalCopperSupplyForecastingDataset"
downloads: 11
summary: "구리 공급 예측 모델 구축을 위한 경제 및 산업 지표의 월별 시계열 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# CanariaView/GlobalCopperSupplyForecastingDataset

> dataset · [Hugging Face](https://huggingface.co/datasets/CanariaView/GlobalCopperSupplyForecastingDataset)

구리 공급 예측 모델 구축을 위한 경제 및 산업 지표의 월별 시계열 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — metadata · readme, task_categories = `time-series-forecasting` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `Coverage Period: Monthly data from January 2000 to March 2023, encompassing a total of 279 months.` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `Coverage Period: Monthly data from January 2000 to March 2023, encompassing a total of 279 months.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `7` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `This dataset encompasses economic and industrial indicators vital for constructing a copper supply forecasting model.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset encompasses economic and industrial indicators vital for constructing a copper supply forecasting model.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `Date` 열 p90 10자 ≈ 7 토큰 (viewer statistics, default/train)
