---
type: "dataset"
id: "sinabis-group/sinabis-1m-synthetic-xlsx"
source: "huggingface"
url: "https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-xlsx"
downloads: 164
summary: "Sinabis 그룹의 100만 개 이상의 가상 비즈니스 엑셀 스프레드시트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[시계열 예측]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# sinabis-group/sinabis-1m-synthetic-xlsx

> dataset · [Hugging Face](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-xlsx)

Sinabis 그룹의 100만 개 이상의 가상 비즈니스 엑셀 스프레드시트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[시계열 예측]] — metadata · task_categories = `time-series-forecasting` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — tag_match · readme, tags = `information-extraction` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `the dataset can be browsed in the Dataset Viewer above and loaded directly` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `business spreadsheets (.xlsx)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality, task:tabular_prediction = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding, task:generation, task:information_extraction, task:retrieval = `text` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `extracted `text`, one row per workbook` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `24 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3317` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `business spreadsheets (.xlsx) from the everyday operations of a fictional group of Sinabis companies` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The Parquet files under `data/` hold one row per workbook: all manifest fields plus the extracted text` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 13270자 ≈ 3317 토큰 (viewer statistics, default/train)
