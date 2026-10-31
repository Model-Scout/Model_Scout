---
type: "dataset"
id: "recursal/SuperWikiImage-7M"
source: "huggingface"
url: "https://huggingface.co/datasets/recursal/SuperWikiImage-7M"
downloads: 605
summary: "SuperWikiImage-7M은 위키피디아에서 수집한 약 700만 장 이미지 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[이미지 생성]]"
  - "[[언어 모델링]]"
  - "[[이미지 인식]]"
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
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# recursal/SuperWikiImage-7M

> dataset · [Hugging Face](https://huggingface.co/datasets/recursal/SuperWikiImage-7M)

SuperWikiImage-7M은 위키피디아에서 수집한 약 700만 장 이미지 데이터셋입니다.

## 분류

- **작업**: [[이미지 생성]] — metadata · readme, task_categories = `image-to-image` · 신뢰도 high
- **작업**: [[언어 모델링]] — metadata · task_ids = `language-modeling` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `image-classification` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:image_generation, task:vision, task:visual_qa = `A ~15TiB (~7 Million) collection of images from wikipedia.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:image_generation, task:language_modeling, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme, task:image_generation = `Anything to deal with images such as image to text, text to image, image to image and many more are supported.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:language_modeling, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `61 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `The following dataset/models provided here, is part of that commitment.` · 신뢰도 low
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `99999999999.0` · 신뢰도 high
