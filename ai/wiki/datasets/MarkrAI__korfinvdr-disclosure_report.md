---
type: "dataset"
id: "MarkrAI/korfinvdr-disclosure_report"
source: "huggingface"
url: "https://huggingface.co/datasets/MarkrAI/korfinvdr-disclosure_report"
downloads: 48
summary: "한국 공정거래위원회 기업집단 소유구조 보고서로 시각문서 검색과 복합질의응답에 활용"
readme_status: "ok"
readme_language: "mixed"
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
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# MarkrAI/korfinvdr-disclosure_report

> dataset · [Hugging Face](https://huggingface.co/datasets/MarkrAI/korfinvdr-disclosure_report)

한국 공정거래위원회 기업집단 소유구조 보고서로 시각문서 검색과 복합질의응답에 활용

## 분류

- **작업**: [[문서 인식(OCR)]] — metadata · task_categories = `document-question-answering` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `complex-document question answering` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `visual-document-retrieval` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:ocr = `image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `6161` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Fair Trade Commission reports on corporate-group ownership` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `All annotations, query-document relevance judgments (qrels), and related metadata generated for this corpus are distributed under the Creative Commons Attributi` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `elements` 열 p90 9242자 ≈ 6161 토큰 (viewer statistics, corpus/test)
