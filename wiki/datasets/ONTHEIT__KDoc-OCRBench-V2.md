---
type: "dataset"
id: "ONTHEIT/KDoc-OCRBench-V2"
source: "huggingface"
url: "https://huggingface.co/datasets/ONTHEIT/KDoc-OCRBench-V2"
downloads: 474
summary: "한국 공공기관 문서 849건의 단일 페이지 PDF를 대상으로 한 OCR 성능 평가 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[문서 인식(OCR)]]"
  - "[[이미지 이해]]"
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
  - "[[행정·민원]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ONTHEIT/KDoc-OCRBench-V2

> dataset · [Hugging Face](https://huggingface.co/datasets/ONTHEIT/KDoc-OCRBench-V2)

한국 공공기관 문서 849건의 단일 페이지 PDF를 대상으로 한 OCR 성능 평가 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Each PDF is labelled with one of four broad categories` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · modality, readme, task:ocr = `849 single-page PDFs` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:ocr, task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `56,197 manually-reviewed unit tests across three categories` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `849 single-page documents from Korean public-sector portals` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `A Korean document OCR benchmark` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
