---
type: "dataset"
id: "whybe-choi/kovidore-office-v1.0-beir"
source: "huggingface"
url: "https://huggingface.co/datasets/whybe-choi/kovidore-office-v1.0-beir"
downloads: 14
summary: "KoViDoRe Benchmark의 한국어 오피스 문서 시각 문서 검색용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 인식(OCR)]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# whybe-choi/kovidore-office-v1.0-beir

> dataset · [Hugging Face](https://huggingface.co/datasets/whybe-choi/kovidore-office-v1.0-beir)

KoViDoRe Benchmark의 한국어 오피스 문서 시각 문서 검색용 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — metadata · task_categories = `document-question-answering` · 신뢰도 low
- **작업**: [[질의응답]] — tag_match · tags = `QA` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · task_categories = `visual-document-retrieval` · 신뢰도 low
- **작업**: [[이미지 이해]] — tag_match · tags = `Visual QA` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `Document page image (PIL Image)` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval, task:visual_qa = `text query` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `relevant document image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr, task:question_answering, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Korean business/office documents (e.g., 보고서, 보도자료 등)` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This dataset is intended for benchmarking the performance of visual document retrieval systems` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
