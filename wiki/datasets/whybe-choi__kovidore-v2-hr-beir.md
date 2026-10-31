---
type: "dataset"
id: "whybe-choi/kovidore-v2-hr-beir"
source: "huggingface"
url: "https://huggingface.co/datasets/whybe-choi/kovidore-v2-hr-beir"
downloads: 217
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 인식(OCR)]]"
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
commercial_use:
  - "[[이용 조건 미확인]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# whybe-choi/kovidore-v2-hr-beir

> dataset · [Hugging Face](https://huggingface.co/datasets/whybe-choi/kovidore-v2-hr-beir)

## 분류

- **작업**: [[문서 인식(OCR)]] — metadata · task_categories = `document-question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · task_categories = `visual-document-retrieval` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — metadata · modality, task:ocr = `document` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:ocr = `image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
