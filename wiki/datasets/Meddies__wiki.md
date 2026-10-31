---
type: "dataset"
id: "Meddies/wiki"
source: "huggingface"
url: "https://huggingface.co/datasets/Meddies/wiki"
downloads: 20
summary: "위키피디아 다국어 문서 데이터로 검색 및 텍스트 처리에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Meddies/wiki

> dataset · [Hugging Face](https://huggingface.co/datasets/Meddies/wiki)

위키피디아 다국어 문서 데이터로 검색 및 텍스트 처리에 활용 가능

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = ``text`: Cirrus plain text for retrieval and chunking` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = ``text`: Cirrus plain text for retrieval and chunking` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Wikipedia namespace-0 articles from the official Wikimedia CirrusSearch content index dump` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Downstream training releases must preserve attribution/share-alike obligations` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
