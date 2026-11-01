---
type: "dataset"
id: "AI-Culture-Commons/philosophy-culture-translations-html-csv"
source: "huggingface"
url: "https://huggingface.co/datasets/AI-Culture-Commons/philosophy-culture-translations-html-csv"
downloads: 76
summary: "12개 언어로 된 철학·문화·문학 텍스트 병렬 번역 데이터셋으로 AI 윤리·미학 연구에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[문서 인식(OCR)]]"
  - "[[요약]]"
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# AI-Culture-Commons/philosophy-culture-translations-html-csv

> dataset · [Hugging Face](https://huggingface.co/datasets/AI-Culture-Commons/philosophy-culture-translations-html-csv)

12개 언어로 된 철학·문화·문학 텍스트 병렬 번역 데이터셋으로 AI 윤리·미학 연구에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_categories = `fill-mask` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `document-understanding` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:ocr = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:language_modeling, task:summarization, task:translation = `The CSV file contains parallel text pairs with the following columns` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:ocr, task:summarization, task:translation = `The CSV file contains parallel text pairs with the following columns` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `The corpus contains an exceptionally diverse range of cultural, philosophical, and literary texts` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
