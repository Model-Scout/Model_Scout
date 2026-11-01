---
type: "dataset"
id: "KaLM-Embedding/KaLM-reranker-training-data"
source: "huggingface"
url: "https://huggingface.co/datasets/KaLM-Embedding/KaLM-reranker-training-data"
downloads: 2106
summary: "영어, 중국어, 다국어 검색 작업용 리랭킹 모델 미세조정 대규모 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
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
# KaLM-Embedding/KaLM-reranker-training-data

> dataset · [Hugging Face](https://huggingface.co/datasets/KaLM-Embedding/KaLM-reranker-training-data)

영어, 중국어, 다국어 검색 작업용 리랭킹 모델 미세조정 대규모 데이터셋입니다.

## 분류

- **작업**: [[리랭킹]] — metadata · readme, tags, task_categories = `text-ranking` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:reranking, task:retrieval = `Each sample includes task instructions, positive passages, at least 16 hard negatives` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — metadata · modality = `timeseries` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `teacher scores annotated by Qwen3-Reranker-8B` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `19 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `378` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `covering English, Chinese, and multilingual retrieval tasks.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `3,885,265 training samples collected from 54 datasets` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 1514자 ≈ 378 토큰 (viewer statistics, default/train)
