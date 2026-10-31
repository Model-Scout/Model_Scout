---
type: "dataset"
id: "lmms-lab/M4-Instruct-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/lmms-lab/M4-Instruct-Data"
downloads: 3152
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lmms-lab/M4-Instruct-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/lmms-lab/M4-Instruct-Data)

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 high
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:question_answering, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[nc-ai-consortium__VAETKI-VL-7B-A1B|nc-ai-consortium/VAETKI-VL-7B-A1B]]
