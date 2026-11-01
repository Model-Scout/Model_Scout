---
type: "dataset"
id: "philschmid/finanical-rag-embedding-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/philschmid/finanical-rag-embedding-dataset"
downloads: 116
summary: "NVIDIA 2023 SEC 보고서에서 추출한 질문-문맥 쌍으로 임베딩 모델 미세조정용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# philschmid/finanical-rag-embedding-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/philschmid/finanical-rag-embedding-dataset)

NVIDIA 2023 SEC 보고서에서 추출한 질문-문맥 쌍으로 임베딩 모델 미세조정용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `fine-tuning embedding models using positive text pairs (question, context)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `positive text pairs (question, context)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `positive text pairs (question, context)` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `130` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `NVIDIAs 2023 SEC Filling Report` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `for fine-tuning embedding models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 520자 ≈ 130 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[PeterAM4__Qwen3-Embedding-0.6B-GGUF|PeterAM4/Qwen3-Embedding-0.6B-GGUF]]
- [[zhiqian99__Qwen3-Embedding-0.6B-GGUF|zhiqian99/Qwen3-Embedding-0.6B-GGUF]]
