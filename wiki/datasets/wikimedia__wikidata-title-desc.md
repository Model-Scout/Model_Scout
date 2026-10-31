---
type: "dataset"
id: "wikimedia/wikidata-title-desc"
source: "huggingface"
url: "https://huggingface.co/datasets/wikimedia/wikidata-title-desc"
downloads: 335
summary: "Wikidata QID와 324개 위키백과 언어판의 제목 및 설명을 연결한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
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
# wikimedia/wikidata-title-desc

> dataset · [Hugging Face](https://huggingface.co/datasets/wikimedia/wikidata-title-desc)

Wikidata QID와 324개 위키백과 언어판의 제목 및 설명을 연결한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Each row links a Wikidata QID to the title and description as they appear in a specific language edition of Wikipedia` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Wikidata entity titles and short descriptions for all 324 Wikipedia language editions` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `Wikidata entity titles and short descriptions for all 324 Wikipedia language editions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each row links a Wikidata QID to the title and description as they appear in a specific language edition of Wikipedia` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `323 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `5` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Wikidata entity titles and short descriptions for all 324 Wikipedia language editions` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `title` 열 p90 20자 ≈ 5 토큰 (viewer statistics, ko/train)
