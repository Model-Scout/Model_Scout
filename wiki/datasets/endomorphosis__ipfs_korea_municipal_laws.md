---
type: "dataset"
id: "endomorphosis/ipfs_korea_municipal_laws"
source: "huggingface"
url: "https://huggingface.co/datasets/endomorphosis/ipfs_korea_municipal_laws"
downloads: 4520
summary: "한국 지방자치단체의 현행 조례, 규칙 등 자치법규 전문과 조문 데이터를 제공하는 법률 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# endomorphosis/ipfs_korea_municipal_laws

> dataset · [Hugging Face](https://huggingface.co/datasets/endomorphosis/ipfs_korea_municipal_laws)

한국 지방자치단체의 현행 조례, 규칙 등 자치법규 전문과 조문 데이터를 제공하는 법률 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = ``data/articles-0000N.parquet`: one row per article (제N조) plus one supplementary-provisions row (부칙, record_type `supplementary_provision`) per instrument` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Current (현행) local legislation of Korean local governments — ordinances (조례), rules (규칙) and other local instruments` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction, task:retrieval = `one row per instrument (full text, title, effective/promulgation dates, number, issuing government)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `one row per article (제N조) plus one supplementary-provisions row (부칙, record_type `supplementary_provision`) per instrument` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Ongoing harvest in batches (data/*-0000N.parquet); later batches add more local governments.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
