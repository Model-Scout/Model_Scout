---
type: "dataset"
id: "HumynLabs/Korean_Product_Labels_Image_Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/HumynLabs/Korean_Product_Labels_Image_Dataset"
downloads: 125
summary: "한국 제품 라벨과 포장 이미지로 OCR, 제품 분류, 시각-언어 AI 연구에 활용되는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[문서 인식(OCR)]]"
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
# HumynLabs/Korean_Product_Labels_Image_Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/HumynLabs/Korean_Product_Labels_Image_Dataset)

한국 제품 라벨과 포장 이미지로 OCR, 제품 분류, 시각-언어 AI 연구에 활용되는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Product category classification (food, cosmetics, household goods, etc.)` · 신뢰도 medium
- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **작업**: [[이미지 인식]] — metadata · readme, task_categories = `image-classification` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:vision = `high-resolution images of Korean product labels and packaging` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr = `Text extraction from Korean product labels and packaging` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `designed to support OCR, product classification, and visual-language AI research.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training OCR and product recognition models` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `Hyde01/Korean_Product_Labels_Image_Dataset`
