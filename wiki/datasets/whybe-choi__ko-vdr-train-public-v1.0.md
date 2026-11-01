---
type: "dataset"
id: "whybe-choi/ko-vdr-train-public-v1.0"
source: "huggingface"
url: "https://huggingface.co/datasets/whybe-choi/ko-vdr-train-public-v1.0"
downloads: 657
summary: "한국 정부 및 공공기관 PDF 문서에서 생성된 시각 문서 검색용 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 인식(OCR)]]"
  - "[[문서 검색]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# whybe-choi/ko-vdr-train-public-v1.0

> dataset · [Hugging Face](https://huggingface.co/datasets/whybe-choi/ko-vdr-train-public-v1.0)

한국 정부 및 공공기관 PDF 문서에서 생성된 시각 문서 검색용 학습 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — metadata · task_categories = `document-question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `visual-document-retrieval` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme, task:ocr = `generated from 23 Korean government and public institution PDF documents` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:ocr = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr = `Queries are generated from two sources: page-level summaries (79%) and direct page context (21%)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `generated from Korean government and public institution reports` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a training dataset for Korean Visual Document Retrieval.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
