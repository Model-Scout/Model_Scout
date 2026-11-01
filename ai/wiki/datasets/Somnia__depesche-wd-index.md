---
type: "dataset"
id: "Somnia/depesche-wd-index"
source: "huggingface"
url: "https://huggingface.co/datasets/Somnia/depesche-wd-index"
downloads: 293
summary: "Wikidata 기반 엔티티 링크 및 다국어 의미 유사도 검색용 인덱스 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[리랭킹]]"
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
dataset_size:
  - "[[대규모 데이터]]"
---
# Somnia/depesche-wd-index

> dataset · [Hugging Face](https://huggingface.co/datasets/Somnia/depesche-wd-index)

Wikidata 기반 엔티티 링크 및 다국어 의미 유사도 검색용 인덱스 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `multilingual semantic similarity — no external database required` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `compositional queries` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `optimized for entity linking (resolve), facet / type checks (is_a), compositional queries, and multilingual semantic similarity` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:reranking, task:retrieval = `Wikidata JSON dump `latest-all.json.gz`` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Full query surface (resolve / get / is_a / match / inbound / instances_of / types / subclasses / neighbors / value_at / top / count_by / near / path / similar)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `33 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
