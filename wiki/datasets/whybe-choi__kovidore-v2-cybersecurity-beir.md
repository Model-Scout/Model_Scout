---
type: "dataset"
id: "whybe-choi/kovidore-v2-cybersecurity-beir"
source: "huggingface"
url: "https://huggingface.co/datasets/whybe-choi/kovidore-v2-cybersecurity-beir"
downloads: 242
summary: "한국의 사이버 위협 동향과 보안 사고 대응에 관한 기술 보고서 코퍼스 데이터셋입니다."
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# whybe-choi/kovidore-v2-cybersecurity-beir

> dataset · [Hugging Face](https://huggingface.co/datasets/whybe-choi/kovidore-v2-cybersecurity-beir)

한국의 사이버 위협 동향과 보안 사고 대응에 관한 기술 보고서 코퍼스 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — metadata · task_categories = `document-question-answering` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Contains set of questions or search queries.` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `visual-document-retrieval` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · modality, readme, task:ocr = `Document Types: Reports` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:ocr = `image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `5302` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset, Cybersecurity, is a corpus of technical reports on cyber threat trends and security incident responses in Korea` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `All annotations, query-document relevance judgments (qrels), and related metadata generated for this corpus are distributed under the Creative Commons Attributi` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `elements` 열 p90 7953자 ≈ 5302 토큰 (viewer statistics, corpus/test)
