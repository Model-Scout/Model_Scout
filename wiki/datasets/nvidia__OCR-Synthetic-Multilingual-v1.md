---
type: "dataset"
id: "nvidia/OCR-Synthetic-Multilingual-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/OCR-Synthetic-Multilingual-v1"
downloads: 7752
summary: "다국어 텍스트 검출 및 인식을 위한 대규모 합성 OCR 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
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
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# nvidia/OCR-Synthetic-Multilingual-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/OCR-Synthetic-Multilingual-v1)

다국어 텍스트 검출 및 인식을 위한 대규모 합성 OCR 학습 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `Large-scale synthetically generated OCR training dataset for multilingual text detection and recognition.` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `object-detection` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr, task:vision, task:visual_qa = `JPEG-encoded image bytes, one entry per sample` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:information_extraction, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `Full-page text label` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset is intended for machine learning researchers, AI engineers, and developers working on information retrieval with OCR.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset was used to train Nemotron OCR v2, a state-of-the-art multilingual OCR model` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
