---
type: "dataset"
id: "kaggle/yashdogra/multilingual-synthetic-ocr-starter"
source: "kaggle"
url: "https://www.kaggle.com/datasets/yashdogra/multilingual-synthetic-ocr-starter"
downloads: 2
summary: "6개 언어로 된 24,000개 합성 문서 페이지의 OCR 텍스트 인식 및 판독 순서 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
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
  - "[[학습용]]"
---
# kaggle/yashdogra/multilingual-synthetic-ocr-starter

> dataset · [Kaggle](https://www.kaggle.com/datasets/yashdogra/multilingual-synthetic-ocr-starter)

6개 언어로 된 24,000개 합성 문서 페이지의 OCR 텍스트 인식 및 판독 순서 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `fine-tune a multilingual text-recognition model` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `a large synthetic document dataset for OCR text detection, recognition and reading order` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `train or benchmark a multilingual OCR model` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:information_extraction, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `OCR text detection, recognition and reading order` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `synthetic document dataset for OCR text detection` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train or benchmark a multilingual OCR model on Kaggle` · 신뢰도 medium
