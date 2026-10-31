---
type: "dataset"
id: "ysmeta/EVE-Train-NPL-1.0"
source: "huggingface"
url: "https://huggingface.co/datasets/ysmeta/EVE-Train-NPL-1.0"
downloads: 232
summary: "베트남어 부실채권 담보 감정 문서의 시각-언어 모델 학습용 합성 스캔 문서 이미지 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[정보 추출]]"
  - "[[문서 인식(OCR)]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[vi]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ysmeta/EVE-Train-NPL-1.0

> dataset · [Hugging Face](https://huggingface.co/datasets/ysmeta/EVE-Train-NPL-1.0)

베트남어 부실채권 담보 감정 문서의 시각-언어 모델 학습용 합성 스캔 문서 이미지 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `built to train a vision-language model on Vietnamese non-performing-loan (NPL) collateral appraisal paperwork` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Synthetic scanned-document images with gold key-information-extraction labels` · 신뢰도 medium
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `document-understanding` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `Synthetic scanned-document images` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:information_extraction, task:visual_qa = `30 schema fields per image` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `gold key-information-extraction labels` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Vietnamese non-performing-loan (NPL) collateral appraisal paperwork` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `built to train a vision-language model` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
