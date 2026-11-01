---
type: "dataset"
id: "kev-KOH/time-embed-bge-m3"
source: "huggingface"
url: "https://huggingface.co/datasets/kev-KOH/time-embed-bge-m3"
downloads: 85
summary: "한국어 시간 표현 임베딩 학습용 데이터셋으로 BGE-M3 모델의 시계열 검색 성능 향상에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kev-KOH/time-embed-bge-m3

> dataset · [Hugging Face](https://huggingface.co/datasets/kev-KOH/time-embed-bge-m3)

한국어 시간 표현 임베딩 학습용 데이터셋으로 BGE-M3 모델의 시계열 검색 성능 향상에 사용됨.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `This dataset is a FlagEmbedding/BGE-M3 fine-tuning dataset for Korean LMS temporal retrieval.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `Korean temporal expressions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `embedding space` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `27` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Temporal Query Embedding Data for BGE-M3 - v1.9 Semantic Retention` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The root files now point to the v1.9 training dataset.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 41자 ≈ 27 토큰 (viewer statistics, default/validation)
