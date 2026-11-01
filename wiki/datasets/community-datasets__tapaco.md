---
type: "dataset"
id: "community-datasets/tapaco"
source: "huggingface"
url: "https://huggingface.co/datasets/community-datasets/tapaco"
downloads: 1057
summary: "73개 언어의 문장 유의어 코퍼스로 언어 학습용 예문과 번역 제공 데이터입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
  - "[[번역]]"
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
  - "[[대규모 데이터]]"
---
# community-datasets/tapaco

> dataset · [Hugging Face](https://huggingface.co/datasets/community-datasets/tapaco)

73개 언어의 문장 유의어 코퍼스로 언어 학습용 예문과 번역 제공 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories, task_ids = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links between sentences “meaning the same thing”.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database.` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:retrieval, task:translation = `A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `The paraphrase corpus is created by populating a graph with Tatoeba sentences and equivalence links between sentences “meaning the same thing”.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `73 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `6` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Tatoeba is a crowdsourcing project mainly geared towards language learners.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `paraphrase` 열 p90 23자 ≈ 6 토큰 (viewer statistics, ko/train)
