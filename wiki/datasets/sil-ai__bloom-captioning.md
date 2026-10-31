---
type: "dataset"
id: "sil-ai/bloom-captioning"
source: "huggingface"
url: "https://huggingface.co/datasets/sil-ai/bloom-captioning"
downloads: 39
summary: "351개 언어의 이미지-캡션 쌍으로 구성된 Bloom Library 기반 이미지 캡션 생성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[이미지 생성]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# sil-ai/bloom-captioning

> dataset · [Hugging Face](https://huggingface.co/datasets/sil-ai/bloom-captioning)

351개 언어의 이미지-캡션 쌍으로 구성된 Bloom Library 기반 이미지 캡션 생성 데이터셋입니다.

## 분류

- **작업**: [[이미지 생성]] — ner · readme = `This version of the Bloom Library data is developed specifically for the image captioning task.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_ids = `image-captioning` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:image_generation, task:visual_qa = `image-caption pairs` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:image_generation, task:visual_qa = `caption` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `caption corresponding to the image` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `406 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Bloom’s primary goal is to equip non-dominant language communities and their members to create the literature they want for their community and children.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `All languages include a train, validation, and test split.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `All languages include a train, validation, and test split.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
