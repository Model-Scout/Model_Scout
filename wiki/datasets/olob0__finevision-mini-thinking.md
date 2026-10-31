---
type: "dataset"
id: "olob0/finevision-mini-thinking"
source: "huggingface"
url: "https://huggingface.co/datasets/olob0/finevision-mini-thinking"
downloads: 496
summary: "FineVision-mini Thinking은 FineVision 데이터셋의 일부를 번역 및 추론 정보와 함께 제공하는 이미지-대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# olob0/finevision-mini-thinking

> dataset · [Hugging Face](https://huggingface.co/datasets/olob0/finevision-mini-thinking)

FineVision-mini Thinking은 FineVision 데이터셋의 일부를 번역 및 추론 정보와 함께 제공하는 이미지-대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `every assistant turn gets a **reasoning trace** in the same language, explaining how the answer follows from the image and the question.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `The images are the only thing that stays as is.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `every assistant turn gets a **reasoning trace** in the same language` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `21 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `FineVision-mini is a slice I made of HuggingFaceM4/FineVision` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The reasoning is written so that `image + question -> reasoning -> response`` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
