---
type: "dataset"
id: "maxidl/FineNews-unfiltered"
source: "huggingface"
url: "https://huggingface.co/datasets/maxidl/FineNews-unfiltered"
downloads: 1502
summary: "Common Crawl News에서 수집한 2024년 3~5월 뉴스 문서 3500만 건의 비필터링 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# maxidl/FineNews-unfiltered

> dataset · [Hugging Face](https://huggingface.co/datasets/maxidl/FineNews-unfiltered)

Common Crawl News에서 수집한 2024년 3~5월 뉴스 문서 3500만 건의 비필터링 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Like FineWeb, but built from Common Crawl News instead of main web.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval = `Total number of documents: 35M` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Total number of documents: 35M` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `18 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `11246` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `Like FineWeb, but built from Common Crawl News instead of main web.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This is the unfiltered version, with only URL filtering applied.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 44983자 ≈ 11246 토큰 (viewer statistics, CC-NEWS-2024-03/en)
