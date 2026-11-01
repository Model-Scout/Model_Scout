---
type: "dataset"
id: "Bc-AI/codva-it-data-v5.1"
source: "huggingface"
url: "https://huggingface.co/datasets/Bc-AI/codva-it-data-v5.1"
downloads: 183
summary: "CodVa 모델을 위한 다국어 코딩, 수학, 추론, 일반 QA 지침 튜닝 데이터셋입니다."
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
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Bc-AI/codva-it-data-v5.1

> dataset · [Hugging Face](https://huggingface.co/datasets/Bc-AI/codva-it-data-v5.1)

CodVa 모델을 위한 다국어 코딩, 수학, 추론, 일반 QA 지침 튜닝 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `Task Coverage: Coding, Math, Reasoning, General QA` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Format: Pure ChatML (no domain tokens)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Training labels with -100 for non-assistant tokens` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual instruction tuning dataset for CodVa model` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training Examples: ~2.2M` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
