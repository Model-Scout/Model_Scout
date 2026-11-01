---
type: "dataset"
id: "NomaDamas/ko-vdr-train-public"
source: "huggingface"
url: "https://huggingface.co/datasets/NomaDamas/ko-vdr-train-public"
downloads: 499
summary: "한국 정부 및 공공기관 PDF 문서에서 생성된 한국어 시각 문서 검색 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
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
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# NomaDamas/ko-vdr-train-public

> dataset · [Hugging Face](https://huggingface.co/datasets/NomaDamas/ko-vdr-train-public)

한국 정부 및 공공기관 PDF 문서에서 생성된 한국어 시각 문서 검색 학습 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — metadata · task_categories = `document-question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `visual-document-retrieval` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:ocr = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2995` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `generated from Korean government and public institution reports` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a training dataset for Korean Visual Document Retrieval.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `markdown` 열 p90 4493자 ≈ 2995 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `whybe-choi/ko-vdr-train-public`
