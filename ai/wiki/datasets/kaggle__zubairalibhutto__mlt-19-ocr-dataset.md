---
type: "dataset"
id: "kaggle/zubairalibhutto/mlt-19-ocr-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/zubairalibhutto/mlt-19-ocr-dataset"
downloads: 2409
summary: "ICDAR 2019 MLT OCR 데이터셋으로 다국어 장면 텍스트 인식 및 검출에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 인식(OCR)]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# kaggle/zubairalibhutto/mlt-19-ocr-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/zubairalibhutto/mlt-19-ocr-dataset)

ICDAR 2019 MLT OCR 데이터셋으로 다국어 장면 텍스트 인식 및 검출에 사용됨.

## 분류

- **작업**: [[문서 인식(OCR)]] — ner · readme = `Structured and cleaned for direct use in OCR pipelines, deep learning models, and evaluation frameworks.` · 신뢰도 medium
- **작업**: [[이미지 이해]] — tag_match · tags = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr, task:visual_qa = `Includes scene text images in 10 languages` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `MIT` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual Scene Text Dataset from ICDAR 2019.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `widely used for training and evaluating multilingual scene text recognition and detection systems.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `widely used for training and evaluating multilingual scene text recognition and detection systems.` · 신뢰도 medium
