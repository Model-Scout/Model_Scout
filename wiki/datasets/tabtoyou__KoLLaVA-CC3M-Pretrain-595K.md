---
type: "dataset"
id: "tabtoyou/KoLLaVA-CC3M-Pretrain-595K"
source: "huggingface"
url: "https://huggingface.co/datasets/tabtoyou/KoLLaVA-CC3M-Pretrain-595K"
downloads: 63
summary: "LLaVA에서 공개한 CC3M 595K 시각 지시문 데이터셋을 한국어로 번역한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# tabtoyou/KoLLaVA-CC3M-Pretrain-595K

> dataset · [Hugging Face](https://huggingface.co/datasets/tabtoyou/KoLLaVA-CC3M-Pretrain-595K)

LLaVA에서 공개한 CC3M 595K 시각 지시문 데이터셋을 한국어로 번역한 데이터셋입니다.

## 분류

- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `CC3M의 595K개 Visual Instruction dataset` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `한국어 caption을 가져와 데이터셋을 구축했습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `기존 Ko-conceptual-captions에 공개된 한국어 caption을 가져와 데이터셋을 구축했습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `LLaVA에서 공개한 CC3M의 595K개 Visual Instruction dataset을 한국어로 번역한 데이터셋입니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
