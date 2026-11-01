---
type: "dataset"
id: "hoonisone/AtomicTags"
source: "huggingface"
url: "https://huggingface.co/datasets/hoonisone/AtomicTags"
downloads: 68
summary: "장면 텍스트 인식 모델의 세밀한 진단을 위한 원자 다중 태그 분류 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
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
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# hoonisone/AtomicTags

> dataset · [Hugging Face](https://huggingface.co/datasets/hoonisone/AtomicTags)

장면 텍스트 인식 모델의 세밀한 진단을 위한 원자 다중 태그 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Atomic multi-tag annotations for K-STR-Bench and Union14M. Each text crop may contain multiple visual challenge tags, enabling fine-grained analysis of recognit` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr, task:visual_qa = `Images are stored once.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:visual_qa = `Tags are columns in the CSV.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `Tags are columns in the CSV.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `scene text recognition dataset collected from 14 public datasets` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Download this dataset, then extract each `text_images.tar`. The CSV files are already unpacked.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
