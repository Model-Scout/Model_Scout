---
type: "dataset"
id: "kaggle/arnab91/eavdd-violence"
source: "kaggle"
url: "https://www.kaggle.com/datasets/arnab91/eavdd-violence"
downloads: 148
summary: "EAVDD는 스포츠, 영화, 소셜미디어 영상에서 폭력과 비폭력 행동을 분류하는 비디오 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/arnab91/eavdd-violence

> dataset · [Kaggle](https://www.kaggle.com/datasets/arnab91/eavdd-violence)

EAVDD는 스포츠, 영화, 소셜미디어 영상에서 폭력과 비폭력 행동을 분류하는 비디오 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Videos representing different classes are meticulously labeled and organized into distinct directories` · 신뢰도 low
- **작업**: [[이미지 인식]] — ner · readme = `The curated and extracted videos are sourced from various Sports videos, Hollywood, Korean, and Bollywood movie action scenes, Social media platforms` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:vision = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `The curated and extracted videos are sourced from various Sports videos, Hollywood, Korean, and Bollywood movie action scenes, Social media platforms` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Videos representing different classes are meticulously labeled and organized into distinct directories, each named in alignment with the specific video type.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The curated and extracted videos are sourced from various Sports videos, Hollywood, Korean, and Bollywood movie action scenes, Social media platforms` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset will be provided quarterly in several phases throughout the year.` · 신뢰도 low
