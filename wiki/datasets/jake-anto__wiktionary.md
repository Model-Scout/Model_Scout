---
type: "dataset"
id: "jake-anto/wiktionary"
source: "huggingface"
url: "https://huggingface.co/datasets/jake-anto/wiktionary"
downloads: 443
summary: "Wiktionary 데이터를 정규화된 테이블로 변환해 다양한 언어의 어휘 정보를 조회할 수 있는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
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
# jake-anto/wiktionary

> dataset · [Hugging Face](https://huggingface.co/datasets/jake-anto/wiktionary)

Wiktionary 데이터를 정규화된 테이블로 변환해 다양한 언어의 어휘 정보를 조회할 수 있는 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `so you can pull every IPA transcription, every usage example, or every synonym pair without writing a JSON parser` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **작업**: [[번역]] — metadata · tags, task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:retrieval, task:translation = `Wiktionary parsed into normalized, queryable tables` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `this dataset flattens it into seven relational tables joined on a shared key` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4474 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `109` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Covers 4,868 languages and 10,687,358 entries from the English Wiktionary dump` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Wiktionary Structured` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `etymology_text` 열 p90 436자 ≈ 109 토큰 (viewer statistics, entries/train)
