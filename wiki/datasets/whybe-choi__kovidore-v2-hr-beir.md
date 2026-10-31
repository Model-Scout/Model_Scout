---
type: "dataset"
id: "whybe-choi/kovidore-v2-hr-beir"
source: "huggingface"
url: "https://huggingface.co/datasets/whybe-choi/kovidore-v2-hr-beir"
downloads: 217
summary: "한국의 노동 전망과 고용 정책 보고서로 구성된 복합 문서 이해용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 인식(OCR)]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# whybe-choi/kovidore-v2-hr-beir

> dataset · [Hugging Face](https://huggingface.co/datasets/whybe-choi/kovidore-v2-hr-beir)

한국의 노동 전망과 고용 정책 보고서로 구성된 복합 문서 이해용 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — metadata · task_categories = `document-question-answering` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Contains set of questions or search queries.` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `visual-document-retrieval` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · modality, readme, task:ocr = `Document Types: Reports` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:ocr = `image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:question_answering = `answer extracted from the source documents` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `5677` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `reports on workforce outlook and employment policy in korea` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `It is one of the 4 corpora comprising the KoViDoRe v2 Benchmark.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `elements` 열 p90 8516자 ≈ 5677 토큰 (viewer statistics, corpus/test)
