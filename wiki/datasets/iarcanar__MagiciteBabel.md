---
type: "dataset"
id: "iarcanar/MagiciteBabel"
source: "huggingface"
url: "https://huggingface.co/datasets/iarcanar/MagiciteBabel"
downloads: 71
summary: "FFXIV 게임 대화 실시간 번역 도구 MagicBabel로 게임 스토리텔링 경험 향상 목적."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 인식(OCR)]]"
  - "[[번역]]"
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
  - "[[th]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# iarcanar/MagiciteBabel

> dataset · [Hugging Face](https://huggingface.co/datasets/iarcanar/MagiciteBabel)

FFXIV 게임 대화 실시간 번역 도구 MagicBabel로 게임 스토리텔링 경험 향상 목적.

## 분류

- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `OCR` · 신뢰도 medium
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr = `Real-time OCR detection` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `context-aware translation` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:translation = `translation` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `specifically designed for Final Fantasy XIV (FFXIV)` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
