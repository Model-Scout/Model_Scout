---
type: "dataset"
id: "vibrantlabsai/fiqa"
source: "huggingface"
url: "https://huggingface.co/datasets/vibrantlabsai/fiqa"
downloads: 3941
summary: "금융 도메인 질문과 답변, 문서 검색 데이터를 포함한 RAG 시스템 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# vibrantlabsai/fiqa

> dataset · [Hugging Face](https://huggingface.co/datasets/vibrantlabsai/fiqa)

금융 도메인 질문과 답변, 문서 검색 데이터를 포함한 RAG 시스템 평가용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `evaluating Retrieval-Augmented Generation (RAG) systems` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `retrieved contexts, making it ideal for testing RAG pipelines` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:reranking, task:retrieval = `financial question to be answered` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Ground truth answer for evaluation` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `417` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `financial domain questions` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `pre-generated RAG outputs ready for evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Training/validation/test splits with questions and ground truth answers` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `doc` 열 p90 1666자 ≈ 417 토큰 (viewer statistics, corpus/corpus)

## 이 데이터로 학습한 모델

- [[PeterAM4__Qwen3-Embedding-0.6B-GGUF|PeterAM4/Qwen3-Embedding-0.6B-GGUF]]
- [[zhiqian99__Qwen3-Embedding-0.6B-GGUF|zhiqian99/Qwen3-Embedding-0.6B-GGUF]]
