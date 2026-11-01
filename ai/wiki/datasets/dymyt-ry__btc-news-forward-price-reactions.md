---
type: "dataset"
id: "dymyt-ry/btc-news-forward-price-reactions"
source: "huggingface"
url: "https://huggingface.co/datasets/dymyt-ry/btc-news-forward-price-reactions"
downloads: 122
summary: "120,981개의 다국어 뉴스 이벤트와 비트코인 가격 반응 데이터를 포함한 시계열 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[시계열 예측]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# dymyt-ry/btc-news-forward-price-reactions

> dataset · [Hugging Face](https://huggingface.co/datasets/dymyt-ry/btc-news-forward-price-reactions)

120,981개의 다국어 뉴스 이벤트와 비트코인 가격 반응 데이터를 포함한 시계열 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `Event type, BTC relevance, and experimental direction were generated from title/RSS text by a pinned multilingual embedding model` · 신뢰도 medium
- **작업**: [[시계열 예측]] — metadata · task_categories = `time-series-forecasting` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `research on how observed news aligns with market movement` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:retrieval = `multilingual news events` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `BTC returns before and after each observation, from 1 minute to 24 hours` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `weak semantic annotations` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `BTC returns before and after each observation, from 1 minute to 24 hours` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `BTC returns before and after each observation, from 1 minute to 24 hours` · 신뢰도 low
- **도메인**: [[뉴스·미디어]] — ner · readme = `120,981 multilingual news events joined to weak semantic annotations` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `Two analyses were run on this release` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The release is designed for event studies, classifier bootstrapping, temporal evaluation` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
