---
type: "dataset"
id: "HumynLabs/Korean_Menus_Image_Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/HumynLabs/Korean_Menus_Image_Dataset"
downloads: 47
summary: "한국 식당 메뉴 이미지 데이터셋으로 OCR, 번역, 추천 시스템 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 인식(OCR)]]"
  - "[[번역]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# HumynLabs/Korean_Menus_Image_Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/HumynLabs/Korean_Menus_Image_Dataset)

한국 식당 메뉴 이미지 데이터셋으로 OCR, 번역, 추천 시스템 연구에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Menu item classification (main dish, side dish, beverage, dessert)` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `Visual-language model training for food-tech applications` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Dish popularity and recommendation modeling` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **작업**: [[번역]] — ner · readme = `It has been curated and anonymized to support AI research in OCR, menu understanding, multilingual translation, and food recommendation systems.` · 신뢰도 medium
- **작업**: [[이미지 인식]] — metadata · task_categories = `image-classification` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:vision = `This dataset contains high-resolution images of Korean restaurant menus` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:generation, task:translation = `Text extraction from Korean menus (dish names, prices, descriptions)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:ocr, task:translation = `Text extraction from Korean menus (dish names, prices, descriptions)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `It has been curated and anonymized to support AI research in OCR, menu understanding, multilingual translation, and food recommendation systems.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training OCR and menu text recognition systems` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
