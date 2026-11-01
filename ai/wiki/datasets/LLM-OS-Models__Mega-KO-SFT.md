---
type: "dataset"
id: "LLM-OS-Models/Mega-KO-SFT"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/Mega-KO-SFT"
downloads: 27
summary: "Fabliq-KO 학습용 한국어 SFT 증류 데이터셋으로, 다중 소스의 대화 및 추론 데이터를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# LLM-OS-Models/Mega-KO-SFT

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/Mega-KO-SFT)

Fabliq-KO 학습용 한국어 SFT 증류 데이터셋으로, 다중 소스의 대화 및 추론 데이터를 포함함.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `mathematical reasoning` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `multi-turn agent traces, tool use` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:generation, task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Combined Korean SFT distillation dataset for training Fabliq-KO` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Combined Korean SFT distillation dataset for training Fabliq-KO` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
