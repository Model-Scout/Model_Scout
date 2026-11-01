---
type: "dataset"
id: "legesher/language-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/legesher/language-corpus"
downloads: 101
summary: "프로그래밍 언어 개념의 예약어 번역을 다양한 언어로 제공하는 확장 가능한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
  - "[[중규모 데이터]]"
---
# legesher/language-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/legesher/language-corpus)

프로그래밍 언어 개념의 예약어 번역을 다양한 언어로 제공하는 확장 가능한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `every endorsement a person attached to it` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `every candidate rendering ("option") of a programming-language concept in a human locale` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `A concept-centric corpus of reserved-word translations for programming languages` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:retrieval = `every candidate rendering ("option") of a programming-language concept in a human locale` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `every candidate rendering ("option") of a programming-language concept in a human locale` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `56 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `102` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A concept-centric corpus of reserved-word translations for programming languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is a growing dataset, and append-only by design` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `definition_en` 열 p90 407자 ≈ 102 토큰 (viewer statistics, concepts/train)
