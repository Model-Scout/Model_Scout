---
type: "dataset"
id: "judicialmind/legal-training-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/judicialmind/legal-training-dataset"
downloads: 598
summary: "법률 정보 검색 및 질의응답 시스템 학습용 다국어 쿼리-본문 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[질의응답]]"
  - "[[리랭킹]]"
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
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# judicialmind/legal-training-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/judicialmind/legal-training-dataset)

법률 정보 검색 및 질의응답 시스템 학습용 다국어 쿼리-본문 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `sentence-similarity` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, tags, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[리랭킹]] — ner · readme = `reranker cross-encoders` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:question_answering, task:reranking, task:retrieval = `query–passage corpus` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `annotated query–passage pairs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `32 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `612` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `File-level A / B / C bucket split for clean train / validation / test partitioning` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `positive` 열 p90 2447자 ≈ 612 토큰 (viewer statistics, default/train)
