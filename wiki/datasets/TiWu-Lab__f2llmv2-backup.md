---
type: "dataset"
id: "TiWu-Lab/f2llmv2-backup"
source: "huggingface"
url: "https://huggingface.co/datasets/TiWu-Lab/f2llmv2-backup"
downloads: 274
summary: "다국어 임베딩을 위한 포괄적이고 효율적인 F2LLM-v2 데이터셋입니다."
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# TiWu-Lab/f2llmv2-backup

> dataset · [Hugging Face](https://huggingface.co/datasets/TiWu-Lab/f2llmv2-backup)

다국어 임베딩을 위한 포괄적이고 효율적인 F2LLM-v2 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding, task:retrieval = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `87 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `200` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 798자 ≈ 200 토큰 (viewer statistics, default/train)
