---
type: "dataset"
id: "neural-bridge/rag-dataset-12000"
source: "huggingface"
url: "https://huggingface.co/datasets/neural-bridge/rag-dataset-12000"
downloads: 1233
summary: "Retrieval-Augmented Generation(RAG) 최적화 모델 학습용 영어 질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[중문]]"
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
# neural-bridge/rag-dataset-12000

> dataset · [Hugging Face](https://huggingface.co/datasets/neural-bridge/rag-dataset-12000)

Retrieval-Augmented Generation(RAG) 최적화 모델 학습용 영어 질의응답 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `RAG offers a cost-effective method to leverage the vast data processing power of LLMs, equipped with billions of parameters, for tasks such as question-answerin` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by allowing them to consult an external authoritative knowledge base before generatin` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:retrieval = `A typical data point comprises a context, a question about the context, and an answer for the question.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `A typical data point comprises a context, a question about the context, and an answer for the question.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1412` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Retrieval-Augmented Generation (RAG) Dataset 12000 is an English dataset designed for RAG-optimized models` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 5647자 ≈ 1412 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[QuantFactory__Llama-3.2-Taiwan-3B-Instruct-GGUF|QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF]]
