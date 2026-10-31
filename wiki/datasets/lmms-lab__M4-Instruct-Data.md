---
type: "dataset"
id: "lmms-lab/M4-Instruct-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/lmms-lab/M4-Instruct-Data"
downloads: 3152
summary: "M4-Instruct는 GPT-4V API로 생성된 다중 이미지 데이터셋으로 LMM 훈련용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lmms-lab/M4-Instruct-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/lmms-lab/M4-Instruct-Data)

M4-Instruct는 GPT-4V API로 생성된 다중 이미지 데이터셋으로 LMM 훈련용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `It is constructed for training LMMs for their interleaved multi-image capbilities` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `M4-Instruct is a set of multi-image datasets` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:visual_qa = `text` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `multi-image, multi-frame (video), and multi-view (3D) data of M4-Instruct` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:visual_qa = `The primary use of M4-Instruct Data is research on large multimodal models and chatbots.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The primary intended users of the model are researchers and hobbyists in computer vision, natural language processing, machine learning, and artificial intellig` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `It is constructed for training LMMs for their interleaved multi-image capbilities` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[nc-ai-consortium__VAETKI-VL-7B-A1B|nc-ai-consortium/VAETKI-VL-7B-A1B]]
