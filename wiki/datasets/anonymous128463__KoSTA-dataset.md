---
type: "dataset"
id: "anonymous128463/KoSTA-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/anonymous128463/KoSTA-dataset"
downloads: 356
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
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
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# anonymous128463/KoSTA-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/anonymous128463/KoSTA-dataset)

## 분류

- **작업**: [[이미지 생성]] — metadata · task_categories = `image-to-image` · 신뢰도 high
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:image_generation, task:ocr = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:image_generation = `text` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
