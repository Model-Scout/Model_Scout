---
type: "dataset"
id: "sun09125/belly-band-edu-sample"
source: "huggingface"
url: "https://huggingface.co/datasets/sun09125/belly-band-edu-sample"
downloads: 23
summary: "한국 소설 띠지 영역 객체 탐지 및 OCR 교육용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[문서 인식(OCR)]]"
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# sun09125/belly-band-edu-sample

> dataset · [Hugging Face](https://huggingface.co/datasets/sun09125/belly-band-edu-sample)

한국 소설 띠지 영역 객체 탐지 및 OCR 교육용 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `띠지(belly band / 帯, obi) 영역을 객체 탐지(YOLOv8)로 검출하고, 그 텍스트를 OCR(Gemini)로 추출하는` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `object-detection` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr, task:vision, task:visual_qa = `표지 이미지 약 1,000장` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:information_extraction, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `그 텍스트를 OCR(Gemini)로 추출하는` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `위키독스 매뉴얼 「AI 학습을 위한 한국 소설 표지·띠지 텍스트 추출」의 교육 실습용 데이터셋입니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `YOLOv8 노트북이 내려받아 학습에 사용` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
