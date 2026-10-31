---
type: "dataset"
id: "DataDrivenConstruction/cwicr-vector-db-bgem3-v3"
source: "huggingface"
url: "https://huggingface.co/datasets/DataDrivenConstruction/cwicr-vector-db-bgem3-v3"
downloads: 296
summary: "30개국 건설 공사 항목, 비용, 자원 다국어 카탈로그의 임베딩 벡터 DB로 건설비용 검색에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
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
  - "[[서비스 데이터]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# DataDrivenConstruction/cwicr-vector-db-bgem3-v3

> dataset · [Hugging Face](https://huggingface.co/datasets/DataDrivenConstruction/cwicr-vector-db-bgem3-v3)

30개국 건설 공사 항목, 비용, 자원 다국어 카탈로그의 임베딩 벡터 DB로 건설비용 검색에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Each snapshot encodes one country's rate book using the BAAI/bge-m3 embedder` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `ready to restore directly into a Qdrant server for hybrid semantic search` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `Each snapshot encodes one country's rate book using the BAAI/bge-m3 embedder` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `ready to restore directly into a Qdrant server for hybrid semantic search` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a multilingual catalogue of construction rate databases covering 30 countries / language locales` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `ready to restore directly into a Qdrant server for hybrid semantic search` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
