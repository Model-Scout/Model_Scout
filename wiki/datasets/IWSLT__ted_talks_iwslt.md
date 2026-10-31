---
type: "dataset"
id: "IWSLT/ted_talks_iwslt"
source: "huggingface"
url: "https://huggingface.co/datasets/IWSLT/ted_talks_iwslt"
downloads: 618
summary: "TED 강연의 원문과 109개 이상의 언어 번역을 포함한 기계 번역 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[번역]]"
input_modality:
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
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# IWSLT/ted_talks_iwslt

> dataset · [Hugging Face](https://huggingface.co/datasets/IWSLT/ted_talks_iwslt)

TED 강연의 원문과 109개 이상의 언어 번역을 포함한 기계 번역 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This effort repurposes the original content in a way which is more convenient for machine translation researchers` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `the original content published by the TED Conference website` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:retrieval, task:translation = `talk subtitles split in captions` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `104 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `TED Talks corpus, that basically redistributes the original content published by the TED Conference website` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset provides a useful resource for the MT research community` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
