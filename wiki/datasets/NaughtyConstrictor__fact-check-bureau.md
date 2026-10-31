---
type: "dataset"
id: "NaughtyConstrictor/fact-check-bureau"
source: "huggingface"
url: "https://huggingface.co/datasets/NaughtyConstrictor/fact-check-bureau"
downloads: 258
summary: "영어와 프랑스어 팩트체크 기사 및 주장 데이터로 팩트체크 검색 파이프라인 개발용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
input_modality:
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
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
---
# NaughtyConstrictor/fact-check-bureau

> dataset · [Hugging Face](https://huggingface.co/datasets/NaughtyConstrictor/fact-check-bureau)

영어와 프랑스어 팩트체크 기사 및 주장 데이터로 팩트체크 검색 파이프라인 개발용 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `This dataset is designed to support the development and evaluation of fact-check retrieval pipelines.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval = `list of claims, fact-check articles, and precomputed embeddings for English and French fact-checks` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `fact-check retrieval pipelines` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `fact-check articles` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The files outside of the `full_dataset/` directory are specifically curated for conducting experiments and developing the `FactCheckBureau` application.` · 신뢰도 low
