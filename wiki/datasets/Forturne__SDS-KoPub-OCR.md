---
type: "dataset"
id: "Forturne/SDS-KoPub-OCR"
source: "huggingface"
url: "https://huggingface.co/datasets/Forturne/SDS-KoPub-OCR"
downloads: 269
summary: "40,781페이지 한국 공공문서의 OCR 레이아웃 파싱 결과와 멀티모달 임베딩 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 인식(OCR)]]"
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Forturne/SDS-KoPub-OCR

> dataset · [Hugging Face](https://huggingface.co/datasets/Forturne/SDS-KoPub-OCR)

40,781페이지 한국 공공문서의 OCR 레이아웃 파싱 결과와 멀티모달 임베딩 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — tag_match · readme, tags = `embeddings` · 신뢰도 medium
- **작업**: [[문서 인식(OCR)]] — metadata · readme, tags, task_categories = `document-question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `Query embeddings` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr, task:visual_qa = `Region multimodal embeddings (image+caption)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval, task:visual_qa = `Extracted text per page (embedding input)` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `Region multimodal embeddings (image+caption)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `OCR text embeddings` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `40,781 Korean public document pages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `OCR layout parsing results and VL embeddings for the SDS-KoPub-VDR-Benchmark corpus` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
