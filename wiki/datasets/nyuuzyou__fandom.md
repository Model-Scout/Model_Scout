---
type: "dataset"
id: "nyuuzyou/fandom"
source: "huggingface"
url: "https://huggingface.co/datasets/nyuuzyou/fandom"
downloads: 866
summary: "Fandom.com 커뮤니티 위키 덤프에서 7백만 개 이상의 최신 문서와 메타데이터를 포함한 다국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
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
  - "[[극장문]]"
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
# nyuuzyou/fandom

> dataset · [Hugging Face](https://huggingface.co/datasets/nyuuzyou/fandom)

Fandom.com 커뮤니티 위키 덤프에서 7백만 개 이상의 최신 문서와 메타데이터를 포함한 다국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories, task_ids = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `includes article text, metadata, and structural information across multiple languages` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_ids = `language-modeling` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This dataset contains 7,040,984 current pages from all available Fandom.com community wiki dumps` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:language_modeling, task:retrieval = `article text, metadata, and structural information` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `article text, metadata, and structural information` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `39 languages` · 신뢰도 high
- **입력 길이**: [[극장문]] — viewer_stats · viewer_statistics = `172977` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `includes article text, metadata, and structural information across multiple languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset was created by processing the "Current pages" database dumps from all available Fandom.com wikis` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 691909자 ≈ 172977 토큰 (viewer statistics, train/train)
