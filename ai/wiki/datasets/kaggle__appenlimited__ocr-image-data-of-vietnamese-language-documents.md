---
type: "dataset"
id: "kaggle/appenlimited/ocr-image-data-of-vietnamese-language-documents"
source: "kaggle"
url: "https://www.kaggle.com/datasets/appenlimited/ocr-image-data-of-vietnamese-language-documents"
downloads: 296
summary: "베트남어 문서 OCR 이미지 데이터로 다양한 언어 문서의 문자 인식 학습에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 인식(OCR)]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/appenlimited/ocr-image-data-of-vietnamese-language-documents

> dataset · [Kaggle](https://www.kaggle.com/datasets/appenlimited/ocr-image-data-of-vietnamese-language-documents)

베트남어 문서 OCR 이미지 데이터로 다양한 언어 문서의 문자 인식 학습에 활용 가능

## 분류

- **작업**: [[문서 인식(OCR)]] — ner · readme = `This OCR database consists of image data in Korean, Vietnamese, Spanish, French, Thai, Japanese, Indonesian, Tamil, and Burmese, as well as handwritten images i` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr = `This OCR database consists of image data in Korean, Vietnamese, Spanish, French, Thai, Japanese, Indonesian, Tamil, and Burmese` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr = `The accuracy rate requirement is over 99% (both position and content are correct).` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset product can be used in many AI pilot projects and supplement production models with other data.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Usage Cases Image label recognition training` · 신뢰도 medium
