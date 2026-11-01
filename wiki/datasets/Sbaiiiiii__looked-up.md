---
type: "dataset"
id: "Sbaiiiiii/looked-up"
source: "huggingface"
url: "https://huggingface.co/datasets/Sbaiiiiii/looked-up"
downloads: 52353
summary: "30개 언어별 위키피디아 시간별 페이지뷰 데이터로 관심도 분석에 활용"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[시계열 예측]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# Sbaiiiiii/looked-up

> dataset · [Hugging Face](https://huggingface.co/datasets/Sbaiiiiii/looked-up)

30개 언어별 위키피디아 시간별 페이지뷰 데이터로 관심도 분석에 활용

## 분류

- **작업**: [[시계열 예측]] — metadata · task_categories = `time-series-forecasting` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This dataset holds the hourly pageviews of every Wikipedia article in the 30 most-read language editions.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme = ``data/hourly/…/day=DD.parquet`, with rows sorted by `(lang, title, ts_hour_start)`` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = ``data/hourly/…/day=DD.parquet`, with rows sorted by `(lang, title, ts_hour_start)`` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `30 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `8` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Built and maintained by github.com/Sbaiii/looked-up, where the code, the data model and all design…` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high

샘플 길이: `title` 열 p90 34자 ≈ 8 토큰 (viewer statistics, hourly/train)
