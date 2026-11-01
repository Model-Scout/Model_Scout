---
type: "dataset"
id: "sinabis-group/sinabis-1m-synthetic-pdf"
source: "huggingface"
url: "https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-pdf"
downloads: 253
summary: "Sinabis Green Energy의 100만 개 이상의 가상 비즈니스 PDF 문서 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[문서 인식(OCR)]]"
  - "[[요약]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# sinabis-group/sinabis-1m-synthetic-pdf

> dataset · [Hugging Face](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-pdf)

Sinabis Green Energy의 100만 개 이상의 가상 비즈니스 PDF 문서 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 medium
- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · modality, readme, task:ocr = `More than 1,006,000 business documents (PDF)` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr = `The scanned/photocopied documents (`scanned == True`) are images without a text layer` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding, task:generation, task:information_extraction, task:summarization = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:ocr, task:summarization = `The `text` column holds the text layer of the PDF, page by page` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `24 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `590` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `More than 1,006,000 business documents (PDF) from the everyday operations of a fictional renewable-energy group (Sinabis Green Energy) and its worldwide ecosyst` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The Parquet files under `data/` hold one row per document: all manifest fields plus the extracted text, so the dataset can be browsed in the Dataset Viewer abov` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2360자 ≈ 590 토큰 (viewer statistics, default/train)
