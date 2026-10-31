---
type: "dataset"
id: "anonymous128463/KoSTA-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/anonymous128463/KoSTA-dataset"
downloads: 356
summary: "한국어 PII 장면 텍스트 편집 벤치마크로, 원본과 타깃 이미지 쌍 611개로 구성됨."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 생성]]"
  - "[[문서 인식(OCR)]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# anonymous128463/KoSTA-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/anonymous128463/KoSTA-dataset)

한국어 PII 장면 텍스트 편집 벤치마크로, 원본과 타깃 이미지 쌍 611개로 구성됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `한국어 PII(개인정보) 장면 텍스트 편집(Scene Text Editing) 벤치마크` · 신뢰도 low
- **작업**: [[이미지 생성]] — metadata · task_categories = `image-to-image` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:image_generation, task:ocr = `원본 텍스트(text_s)가 담긴 원본 이미지 crop` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:image_generation = `원본 텍스트(text_s)` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme, task:image_generation = `타깃 텍스트(text_t)로 편집된 타깃 이미지 crop` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:ocr = `타깃 텍스트(text_t)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 PII(개인정보) 장면 텍스트 편집(Scene Text Editing) 벤치마크` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `한국어 PII(개인정보) 장면 텍스트 편집(Scene Text Editing) 벤치마크` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
