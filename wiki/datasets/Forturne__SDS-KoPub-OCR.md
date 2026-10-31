---
type: "dataset"
id: "Forturne/SDS-KoPub-OCR"
source: "huggingface"
url: "https://huggingface.co/datasets/Forturne/SDS-KoPub-OCR"
downloads: 269
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
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
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Forturne/SDS-KoPub-OCR

> dataset · [Hugging Face](https://huggingface.co/datasets/Forturne/SDS-KoPub-OCR)

## 분류

- **작업**: [[임베딩]] — tag_match · tags = `embeddings` · 신뢰도 medium
- **작업**: [[문서 인식(OCR)]] — metadata · tags, task_categories = `document-question-answering` · 신뢰도 high
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:ocr, task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
