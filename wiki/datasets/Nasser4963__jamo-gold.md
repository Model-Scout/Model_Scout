---
type: "dataset"
id: "Nasser4963/jamo-gold"
source: "huggingface"
url: "https://huggingface.co/datasets/Nasser4963/jamo-gold"
downloads: 189
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[이미지 생성]]"
  - "[[문서 인식(OCR)]]"
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
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Nasser4963/jamo-gold

> dataset · [Hugging Face](https://huggingface.co/datasets/Nasser4963/jamo-gold)

## 분류

- **작업**: [[이미지 생성]] — metadata · task_categories = `text-to-image` · 신뢰도 high
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — metadata · modality, task:ocr = `document` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:image_generation, task:ocr, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:image_generation, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
