---
type: "dataset"
id: "Cognitive-Lab/NayanaOCRBench_Synthetic"
source: "huggingface"
url: "https://huggingface.co/datasets/Cognitive-Lab/NayanaOCRBench_Synthetic"
downloads: 36
summary: "22개 언어의 OCR 평가용 합성 문서 데이터셋으로 레이아웃, OCR 정답, 번역 테이블, VQA 포함"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 인식(OCR)]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Cognitive-Lab/NayanaOCRBench_Synthetic

> dataset · [Hugging Face](https://huggingface.co/datasets/Cognitive-Lab/NayanaOCRBench_Synthetic)

22개 언어의 OCR 평가용 합성 문서 데이터셋으로 레이아웃, OCR 정답, 번역 테이블, VQA 포함

## 분류

- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `Same 14 columns as the page-level NayanaOCR corpus: `image`` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `reading-order OCR ground truth, translated tables, VQA pairs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Held-out evaluation split of the NayanaOCR 2026 pipeline, 22 languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Held-out evaluation split of the NayanaOCR 2026 pipeline` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
