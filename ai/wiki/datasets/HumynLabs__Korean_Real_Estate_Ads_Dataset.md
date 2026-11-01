---
type: "dataset"
id: "HumynLabs/Korean_Real_Estate_Ads_Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/HumynLabs/Korean_Real_Estate_Ads_Dataset"
downloads: 98
summary: "한국 부동산 광고 이미지 데이터셋으로 OCR, 시각 이해, 부동산 분석 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# HumynLabs/Korean_Real_Estate_Ads_Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/HumynLabs/Korean_Real_Estate_Ads_Dataset)

한국 부동산 광고 이미지 데이터셋으로 OCR, 시각 이해, 부동산 분석 연구에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Classification of property types (apartment, house, commercial)` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `Extraction of property information from ads (price, size, location, contact)` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **작업**: [[이미지 인식]] — metadata · readme, task_categories = `image-classification` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:vision = `This dataset contains high-resolution images of Korean real estate advertisements` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr = `Training OCR and text-extraction models for real estate ads` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `This dataset contains high-resolution images of Korean real estate advertisements` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `It is designed to support AI research in OCR, visual understanding, and property analysis.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training OCR and text-extraction models for real estate ads` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
