---
type: "dataset"
id: "PocketDoc/Dans-MemoryCore-CoreCurriculum-Small"
source: "huggingface"
url: "https://huggingface.co/datasets/PocketDoc/Dans-MemoryCore-CoreCurriculum-Small"
downloads: 144
summary: "다양한 분야의 기초 지식을 담은 질문-답변 쌍 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[환경·기상]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# PocketDoc/Dans-MemoryCore-CoreCurriculum-Small

> dataset · [Hugging Face](https://huggingface.co/datasets/PocketDoc/Dans-MemoryCore-CoreCurriculum-Small)

다양한 분야의 기초 지식을 담은 질문-답변 쌍 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `The question answer pairs were generated using a RAG implementation and a curated selection of source material.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `The question answer pairs were generated using a RAG implementation and a curated selection of source material.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `agpl-3.0` · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · tags = `climate` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `This dataset aims to provide a foundation of knowledge common to a number of fields and areas of study.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The question answer pairs were generated using a RAG implementation and a curated selection of source material.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[King-Cane__Dans-PersonalityEngine-V1.3.0-24b-Q4_K_M-GGUF|King-Cane/Dans-PersonalityEngine-V1.3.0-24b-Q4_K_M-GGUF]]
- [[Mungert__Dans-PersonalityEngine-V1.3.0-24b-GGUF|Mungert/Dans-PersonalityEngine-V1.3.0-24b-GGUF]]
- [[PocketDoc__Dans-PersonalityEngine-V1.3.0-12b|PocketDoc/Dans-PersonalityEngine-V1.3.0-12b]]
- [[PocketDoc__Dans-PersonalityEngine-V1.3.0-24b|PocketDoc/Dans-PersonalityEngine-V1.3.0-24b]]
- [[bartowski__PocketDoc_Dans-PersonalityEngine-V1.3.0-12b-GGUF|bartowski/PocketDoc_Dans-PersonalityEngine-V1.3.0-12b-GGUF]]
- [[bartowski__PocketDoc_Dans-PersonalityEngine-V1.3.0-24b-GGUF|bartowski/PocketDoc_Dans-PersonalityEngine-V1.3.0-24b-GGUF]]
- [[tensorblock__PocketDoc_Dans-PersonalityEngine-V1.3.0-12b-GGUF|tensorblock/PocketDoc_Dans-PersonalityEngine-V1.3.0-12b-GGUF]]
