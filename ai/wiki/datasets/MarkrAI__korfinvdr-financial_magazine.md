---
type: "dataset"
id: "MarkrAI/korfinvdr-financial_magazine"
source: "huggingface"
url: "https://huggingface.co/datasets/MarkrAI/korfinvdr-financial_magazine"
downloads: 128
summary: "한국예금보험공사 금융위험 리뷰 기사로 구성된 한국어 시각 문서 검색 및 복합 문서 질의응답 데이터셋입니다."
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
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# MarkrAI/korfinvdr-financial_magazine

> dataset · [Hugging Face](https://huggingface.co/datasets/MarkrAI/korfinvdr-financial_magazine)

한국예금보험공사 금융위험 리뷰 기사로 구성된 한국어 시각 문서 검색 및 복합 문서 질의응답 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — metadata · task_categories = `document-question-answering` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `complex-document question answering` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `visual-document-retrieval` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr = `The rendered page image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `Text extracted from the page using the document-processing pipeline` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:question_answering = `The answer grounded in the source documents` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `8109` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Korea Deposit Insurance Corporation financial-risk review articles` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `All annotations, query-document relevance judgments (qrels), and related metadata generated for this corpus` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `elements` 열 p90 12164자 ≈ 8109 토큰 (viewer statistics, corpus/test)
