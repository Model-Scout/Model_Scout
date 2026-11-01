---
type: "dataset"
id: "NewTypeCola/VOKU-Archive"
source: "huggingface"
url: "https://huggingface.co/datasets/NewTypeCola/VOKU-Archive"
downloads: 332
summary: "경기대학교 학생 방송국 VOKU의 1988~2019년 라디오 대본과 큐시트 66,010페이지를 제공하는 디지털 아카이브입니다."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[서비스 데이터]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# NewTypeCola/VOKU-Archive

> dataset · [Hugging Face](https://huggingface.co/datasets/NewTypeCola/VOKU-Archive)

경기대학교 학생 방송국 VOKU의 1988~2019년 라디오 대본과 큐시트 66,010페이지를 제공하는 디지털 아카이브입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `people can read, search, and study` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:ocr = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `VOKU (Voice of Kyonggi University) is a student-run university broadcasting station` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `VOKU On so they could access and read the materials` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A former station member made this digital archive independently` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
