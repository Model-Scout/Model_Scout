---
type: "dataset"
id: "kpubdata/seoul-apartment-rent"
source: "huggingface"
url: "https://huggingface.co/datasets/kpubdata/seoul-apartment-rent"
downloads: 48
summary: "서울시 25개 구 아파트 전월세 실거래가 월별 데이터로 임대 시장 분석에 활용 가능"
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
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# kpubdata/seoul-apartment-rent

> dataset · [Hugging Face](https://huggingface.co/datasets/kpubdata/seoul-apartment-rent)

서울시 25개 구 아파트 전월세 실거래가 월별 데이터로 임대 시장 분석에 활용 가능

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Real transaction data for apartment rent (jeonse and wolse) in Seoul, South Korea. Covers all 25 districts with monthly granularity.` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality, task:tabular_prediction = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `7` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `Data sourced from Korea's Ministry of Land, Infrastructure and Transport (국토교통부) via the official data.go.kr API.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Records: 1,220,346` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `contract_term` 열 p90 11자 ≈ 7 토큰 (viewer statistics, default/train)
