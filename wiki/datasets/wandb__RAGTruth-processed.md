---
type: "dataset"
id: "wandb/RAGTruth-processed"
source: "huggingface"
url: "https://huggingface.co/datasets/wandb/RAGTruth-processed"
downloads: 2245
summary: "RAGTruth 데이터셋은 RAG 기반 텍스트 생성 모델의 환각 평가용으로 전문가 주석을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# wandb/RAGTruth-processed

> dataset · [Hugging Face](https://huggingface.co/datasets/wandb/RAGTruth-processed)

RAGTruth 데이터셋은 RAG 기반 텍스트 생성 모델의 환각 평가용으로 전문가 주석을 포함합니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `expert annotations indicating whether the outputs contain hallucinations` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `evaluating hallucinations in text generation models, particularly in retrieval-augmented generation (RAG) contexts` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `A query/question
Context passages
Model output` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1516` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `evaluating hallucinations in text generation models` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Test Split > Hallucination Label Distribution` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Total examples: 15090` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `input_str` 열 p90 6066자 ≈ 1516 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[Horizon-Labs__hallucination-guard-base|Horizon-Labs/hallucination-guard-base]]
- [[Horizon-Labs__hallucination-guard-small|Horizon-Labs/hallucination-guard-small]]
