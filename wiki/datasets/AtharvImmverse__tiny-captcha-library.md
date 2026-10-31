---
type: "dataset"
id: "AtharvImmverse/tiny-captcha-library"
source: "huggingface"
url: "https://huggingface.co/datasets/AtharvImmverse/tiny-captcha-library"
downloads: 266
summary: "44개 세계 문자 체계의 4글자 합성 CAPTCHA 이미지로 OCR 및 문자 인식 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 인식(OCR)]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# AtharvImmverse/tiny-captcha-library

> dataset · [Hugging Face](https://huggingface.co/datasets/AtharvImmverse/tiny-captcha-library)

44개 세계 문자 체계의 4글자 합성 CAPTCHA 이미지로 OCR 및 문자 인식 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Script recognition research` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Vision-language model pretraining` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — ner · readme = `designed for OCR, multilingual vision models, and script recognition research` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr = `synthetic 4-character CAPTCHA images` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr = `label file mapping image filename → correct 4-character text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A multilingual dataset of synthetic 4-character CAPTCHA images` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
