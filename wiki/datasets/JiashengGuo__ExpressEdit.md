---
type: "dataset"
id: "JiashengGuo/ExpressEdit"
source: "huggingface"
url: "https://huggingface.co/datasets/JiashengGuo/ExpressEdit"
downloads: 116
summary: "ExpressEdit는 스타일화된 얼굴 표정 편집을 위한 표현 태그와 예시 스토리, 이미지 데이터베이스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[이미지 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# JiashengGuo/ExpressEdit

> dataset · [Hugging Face](https://huggingface.co/datasets/JiashengGuo/ExpressEdit)

ExpressEdit는 스타일화된 얼굴 표정 편집을 위한 표현 태그와 예시 스토리, 이미지 데이터베이스입니다.

## 분류

- **작업**: [[이미지 생성]] — metadata · task_categories = `image-to-image` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `a minimalist Retrieval-Augmented Generation (RAG) demo hosted on Hugging Face Spaces` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:image_generation = `Example images were automatically generated based on 5 original character images.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:image_generation, task:retrieval = `a rich combination of text, tags, and generated images` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme, task:image_generation = `3,375 total edited images` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `mapping free-form narrative intents to structured generation tags` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Facial expressions of characters are a vital component of visual storytelling.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The example stories were generated with Gemini 3 Flash.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
