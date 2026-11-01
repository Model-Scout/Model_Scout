---
type: "dataset"
id: "danielquillanroxas/unified-etymology-graph"
source: "huggingface"
url: "https://huggingface.co/datasets/danielquillanroxas/unified-etymology-graph"
downloads: 22
summary: "5,529개 언어의 6.6백만 단어와 2,270만 관계를 포함한 통합 어원 지식 그래프 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
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
dataset_size:
  - "[[대규모 데이터]]"
---
# danielquillanroxas/unified-etymology-graph

> dataset · [Hugging Face](https://huggingface.co/datasets/danielquillanroxas/unified-etymology-graph)

5,529개 언어의 6.6백만 단어와 2,270만 관계를 포함한 통합 어원 지식 그래프 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `one you can point a graph search at without wrangling five different formats` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:retrieval = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A unified etymological knowledge graph built from five publicly available datasets` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A Python pipeline downloads the raw data from each source, parses each format (TSV, CSV, Parquet, JSON), normalizes language codes to ISO 639-3, normalizes rela` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
