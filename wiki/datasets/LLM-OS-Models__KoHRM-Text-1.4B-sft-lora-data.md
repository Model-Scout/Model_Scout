---
type: "dataset"
id: "LLM-OS-Models/KoHRM-Text-1.4B-sft-lora-data"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/KoHRM-Text-1.4B-sft-lora-data"
downloads: 915
summary: "KoHRM-Text-1.4B SFT 및 LoRA 준비 데이터로, KoHRM 사전학습 후 행동 정렬 실험용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
---
# LLM-OS-Models/KoHRM-Text-1.4B-sft-lora-data

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/KoHRM-Text-1.4B-sft-lora-data)

KoHRM-Text-1.4B SFT 및 LoRA 준비 데이터로, KoHRM 사전학습 후 행동 정렬 실험용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · tags = `tool-use` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `The token layout follows the KoHRM/HRM-Text PrefixLM convention` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Response tokens are trained with causal response-only cross entropy.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset repo is a prepared training artifact with mixed upstream sources.` · 신뢰도 medium
