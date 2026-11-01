---
type: "dataset"
id: "yakdoli/gwanbo-digital-render"
source: "huggingface"
url: "https://huggingface.co/datasets/yakdoli/gwanbo-digital-render"
downloads: 11
summary: "대한민국 관보 1994-2000년 스캔본을 인식+재렌더해 디지털 품질로 재조판한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# yakdoli/gwanbo-digital-render

> dataset · [Hugging Face](https://huggingface.co/datasets/yakdoli/gwanbo-digital-render)

대한민국 관보 1994-2000년 스캔본을 인식+재렌더해 디지털 품질로 재조판한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `인식된 텍스트를 깨끗한 명조 폰트로 재조판해 '디지털 본에 준하는' 완벽한 글리프를 생성한다.` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `스캔 PDF(250dpi)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:ocr, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `대한민국 관보(官報) 1994–2000 PETY 스캔본` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `파이프라인으로 디지털 본 품질로 재조판한 데이터셋.` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
