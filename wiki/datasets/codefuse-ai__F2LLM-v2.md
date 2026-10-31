---
type: "dataset"
id: "codefuse-ai/F2LLM-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/codefuse-ai/F2LLM-v2"
downloads: 1895
summary: "다국어 임베딩 성능 향상을 위한 F2LLM-v2 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# codefuse-ai/F2LLM-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/codefuse-ai/F2LLM-v2)

다국어 임베딩 성능 향상을 위한 F2LLM-v2 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:retrieval = `Inclusive, Performant, and Efficient Embeddings for a Multilingual World` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Inclusive, Performant, and Efficient Embeddings for a Multilingual World` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `87 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `200` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `We recommend removing these two datasets from the training data.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 798자 ≈ 200 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[codefuse-ai__F2LLM-v2-0.6B|codefuse-ai/F2LLM-v2-0.6B]]
- [[codefuse-ai__F2LLM-v2-0.6B-Preview|codefuse-ai/F2LLM-v2-0.6B-Preview]]
- [[codefuse-ai__F2LLM-v2-1.7B|codefuse-ai/F2LLM-v2-1.7B]]
- [[codefuse-ai__F2LLM-v2-1.7B-Preview|codefuse-ai/F2LLM-v2-1.7B-Preview]]
- [[codefuse-ai__F2LLM-v2-14B|codefuse-ai/F2LLM-v2-14B]]
- [[codefuse-ai__F2LLM-v2-14B-Preview|codefuse-ai/F2LLM-v2-14B-Preview]]
- [[codefuse-ai__F2LLM-v2-160M|codefuse-ai/F2LLM-v2-160M]]
- [[codefuse-ai__F2LLM-v2-330M|codefuse-ai/F2LLM-v2-330M]]
- [[codefuse-ai__F2LLM-v2-4B|codefuse-ai/F2LLM-v2-4B]]
- [[codefuse-ai__F2LLM-v2-4B-Preview|codefuse-ai/F2LLM-v2-4B-Preview]]
- [[codefuse-ai__F2LLM-v2-80M|codefuse-ai/F2LLM-v2-80M]]
- [[codefuse-ai__F2LLM-v2-8B|codefuse-ai/F2LLM-v2-8B]]
- [[codefuse-ai__F2LLM-v2-8B-Preview|codefuse-ai/F2LLM-v2-8B-Preview]]
- [[codefuse-ai__ML-Embed-0.6B|codefuse-ai/ML-Embed-0.6B]]
- [[onnx-community__F2LLM-v2-160M-ONNX|onnx-community/F2LLM-v2-160M-ONNX]]
- [[seamon67__F2LLM-v2-1.7B-GGUF|seamon67/F2LLM-v2-1.7B-GGUF]]
- [[seamon67__F2LLM-v2-4B-GGUF|seamon67/F2LLM-v2-4B-GGUF]]
- [[seamon67__F2LLM-v2-8B-GGUF|seamon67/F2LLM-v2-8B-GGUF]]
