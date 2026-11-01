---
type: "dataset"
id: "Forturne/sds-kopub-ocr-test"
source: "huggingface"
url: "https://huggingface.co/datasets/Forturne/sds-kopub-ocr-test"
downloads: 35
summary: "한국어 공공 문서 64페이지의 OCR 레이아웃 파싱 결과와 비전-언어 임베딩 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
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
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Forturne/sds-kopub-ocr-test

> dataset · [Hugging Face](https://huggingface.co/datasets/Forturne/sds-kopub-ocr-test)

한국어 공공 문서 64페이지의 OCR 레이아웃 파싱 결과와 비전-언어 임베딩 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — tag_match · readme, tags = `embeddings` · 신뢰도 medium
- **작업**: [[문서 인식(OCR)]] — metadata · readme, tags, task_categories = `document-question-answering` · 신뢰도 high
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr, task:visual_qa = `Page image embeddings | (64, 2048)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:visual_qa = `Extracted text per page (embedding input)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `GLM-OCR structured layout results (regions, markdown, bbox, labels)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `64 Korean public document pages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Generated with `run_b200_pipeline.py` on NVIDIA B200 (192GB).` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
