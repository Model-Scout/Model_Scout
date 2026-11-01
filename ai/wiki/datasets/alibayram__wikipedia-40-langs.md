---
type: "dataset"
id: "alibayram/wikipedia-40-langs"
source: "huggingface"
url: "https://huggingface.co/datasets/alibayram/wikipedia-40-langs"
downloads: 165
summary: "40개 언어의 위키피디아 문서 812,000개로 다국어 NLP 연구와 언어 모델링에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
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
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# alibayram/wikipedia-40-langs

> dataset · [Hugging Face](https://huggingface.co/datasets/alibayram/wikipedia-40-langs)

40개 언어의 위키피디아 문서 812,000개로 다국어 NLP 연구와 언어 모델링에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Train multilingual classifiers with language-balanced data` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, tags, task_categories = `fill-mask` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `Build multilingual search and retrieval systems` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:language_modeling, task:retrieval = `Articles contain the full text content extracted from Wikipedia.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Articles contain the full text content extracted from Wikipedia.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `36 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `11303` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `sampled and split into train/validation/test sets with a consistent 10:3:1 ratio per language.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `sampled and split into train/validation/test sets with a consistent 10:3:1 ratio per language.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 45213자 ≈ 11303 토큰 (viewer statistics, default/validation)

## 같은 데이터의 사본·중복 등록

- `magibu/wikipedia-40-langs`
