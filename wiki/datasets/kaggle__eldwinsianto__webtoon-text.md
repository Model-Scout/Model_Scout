---
type: "dataset"
id: "kaggle/eldwinsianto/webtoon-text"
source: "kaggle"
url: "https://www.kaggle.com/datasets/eldwinsianto/webtoon-text"
downloads: 35
summary: "한국 웹툰 대사 및 내러티브 텍스트의 OCR 학습용 한글 이미지 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
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
---
# kaggle/eldwinsianto/webtoon-text

> dataset · [Kaggle](https://www.kaggle.com/datasets/eldwinsianto/webtoon-text)

한국 웹툰 대사 및 내러티브 텍스트의 OCR 학습용 한글 이미지 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `korean OCR dataset with manually croppped webtoon text images.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `korean OCR dataset with manually croppped webtoon text images.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `corresponding OCR annotations` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains Korean text images and corresponding OCR annotations` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `created for training and evaluating Optical Character Recognition (OCR) models.` · 신뢰도 medium
