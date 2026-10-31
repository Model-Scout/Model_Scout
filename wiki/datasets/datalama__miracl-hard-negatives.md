---
type: "dataset"
id: "datalama/miracl-hard-negatives"
source: "huggingface"
url: "https://huggingface.co/datasets/datalama/miracl-hard-negatives"
downloads: 655
summary: "18개 언어의 검색을 위한 MIRACL 다국어 정보 검색 하드 네거티브 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
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
# datalama/miracl-hard-negatives

> dataset · [Hugging Face](https://huggingface.co/datasets/datalama/miracl-hard-negatives)

18개 언어의 검색을 위한 MIRACL 다국어 정보 검색 하드 네거티브 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `181` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MIRACL (Multilingual Information Retrieval Across a Continuum of Languages) is a multilingual retrieval dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is a Parquet-converted version of mteb/miracl-hard-negatives` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 724자 ≈ 181 토큰 (viewer statistics, corpus-ko/corpus)
