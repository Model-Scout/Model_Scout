---
type: "dataset"
id: "HumynLabs/Korean_User_Manuals_Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/HumynLabs/Korean_User_Manuals_Dataset"
downloads: 70
summary: "전자제품 및 가전제품 한국어 사용자 설명서 이미지와 PDF로 OCR 및 문서 이해 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[문서 인식(OCR)]]"
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
# HumynLabs/Korean_User_Manuals_Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/HumynLabs/Korean_User_Manuals_Dataset)

전자제품 및 가전제품 한국어 사용자 설명서 이미지와 PDF로 OCR 및 문서 이해 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Document Classification` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `Instruction extraction and step segmentation` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · modality, readme, task:ocr = `high-resolution images and PDFs` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr = `high-resolution images and PDFs` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr = `OCR for printed Korean user manuals` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `electronics, appliances, and consumer products` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training OCR and text extraction models for Korean manuals` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
