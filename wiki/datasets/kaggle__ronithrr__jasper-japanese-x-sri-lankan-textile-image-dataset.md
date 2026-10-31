---
type: "dataset"
id: "kaggle/ronithrr/jasper-japanese-x-sri-lankan-textile-image-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/ronithrr/jasper-japanese-x-sri-lankan-textile-image-dataset"
downloads: 276
summary: "일본과 스리랑카 전통 직물 이미지 2,000장으로 문화 간 디자인 분석 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
  - "[[일반]]"
---
# kaggle/ronithrr/jasper-japanese-x-sri-lankan-textile-image-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/ronithrr/jasper-japanese-x-sri-lankan-textile-image-dataset)

일본과 스리랑카 전통 직물 이미지 2,000장으로 문화 간 디자인 분석 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Texture classification, pattern recognition, color analysis` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — ner · readme = `Training models for textile classification, style transfer, generative design` · 신뢰도 low
- **작업**: [[이미지 인식]] — tag_match · tags = `image classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `2,000 high-resolution textile images` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `cross-cultural design patterns` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `computational analysis of cross-cultural design patterns` · 신뢰도 low
