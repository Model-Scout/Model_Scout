---
type: "dataset"
id: "kaggle/kimhyeongminkhu/korean-expiry-date-ocr"
source: "kaggle"
url: "https://www.kaggle.com/datasets/kimhyeongminkhu/korean-expiry-date-ocr"
downloads: 139
summary: "한국 편의점 상품의 유통기한 인식용 OCR 및 객체 탐지 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 인식(OCR)]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/kimhyeongminkhu/korean-expiry-date-ocr

> dataset · [Kaggle](https://www.kaggle.com/datasets/kimhyeongminkhu/korean-expiry-date-ocr)

한국 편의점 상품의 유통기한 인식용 OCR 및 객체 탐지 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — ner · readme = `A Korean convenience store expiry date dataset for OCR and object detection` · 신뢰도 medium
- **작업**: [[이미지 인식]] — ner · readme = `A Korean convenience store expiry date dataset for OCR and object detection` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr, task:vision = `This dataset contains images of expiry dates collected from real Korean convenience store products.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `CC BY-NC-SA 4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `retail and shopping` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains images of expiry dates collected from real Korean convenience store products.` · 신뢰도 low
