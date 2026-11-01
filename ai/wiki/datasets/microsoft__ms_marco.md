---
type: "dataset"
id: "microsoft/ms_marco"
source: "huggingface"
url: "https://huggingface.co/datasets/microsoft/ms_marco"
downloads: 18710
summary: "MS MARCO는 Bing 질문과 답변을 포함한 검색 딥러닝용 데이터셋 모음입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# microsoft/ms_marco

> dataset · [Hugging Face](https://huggingface.co/datasets/microsoft/ms_marco)

MS MARCO는 Bing 질문과 답변을 포함한 검색 딥러닝용 데이터셋 모음입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `a natural langauge generation dataset` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `The first dataset was a question answering dataset featuring 100,000 real Bing questions and a human generated answer.` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `a passage ranking dataset` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:reranking = `100,000 real Bing questions and a human generated answer.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `a human generated answer` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `13` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MS MARCO is a collection of datasets focused on deep learning in search.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `MS MARCO is a collection of datasets focused on deep learning in search.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 52자 ≈ 13 토큰 (viewer statistics, v1.1/validation)

## 이 데이터로 학습한 모델

- [[LinerAI__Qwen3-Embedding-0.6B-academic|LinerAI/Qwen3-Embedding-0.6B-academic]]
- [[antoinelouis__colbert-xm|antoinelouis/colbert-xm]]
- [[mradermacher__snowflake-arctic-embed-l-v2.0-academic-GGUF|mradermacher/snowflake-arctic-embed-l-v2.0-academic-GGUF]]
