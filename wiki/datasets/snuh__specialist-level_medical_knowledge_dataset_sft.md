---
type: "dataset"
id: "snuh/specialist-level_medical_knowledge_dataset_sft"
source: "huggingface"
url: "https://huggingface.co/datasets/snuh/specialist-level_medical_knowledge_dataset_sft"
downloads: 339
summary: "서울대병원 HARI가 개발한 13개 의학 전문 분야 임상 추론 및 질의응답용 증강 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# snuh/specialist-level_medical_knowledge_dataset_sft

> dataset · [Hugging Face](https://huggingface.co/datasets/snuh/specialist-level_medical_knowledge_dataset_sft)

서울대병원 HARI가 개발한 13개 의학 전문 분야 임상 추론 및 질의응답용 증강 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `The dataset is provided in a **JSONL** format compatible with Chat templates. Each instance contains a conversation history where the assistant provides a hidde` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `* **Assistant Content**: Contains the **Thinking Process** (` ... `) followed by the **Final Answer**.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `cc-by-nd-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This repository contains **only the augmented data (36,343 samples)** derived from the original AI-Hub source data.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
