---
type: "dataset"
id: "Helsinki-NLP/open_subtitles"
source: "huggingface"
url: "https://huggingface.co/datasets/Helsinki-NLP/open_subtitles"
downloads: 474
summary: "62개 언어의 영화 자막 번역 데이터로 번역 모델 학습에 활용 가능"
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Helsinki-NLP/open_subtitles

> dataset · [Hugging Face](https://huggingface.co/datasets/Helsinki-NLP/open_subtitles)

62개 언어의 영화 자막 번역 데이터로 번역 모델 학습에 활용 가능

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:translation = `subtitle collection` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `translated movie subtitles` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `58 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `movie subtitles` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `a slightly cleaner version of the subtitle collection` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
