---
type: "dataset"
id: "sinabis-group/sinabis-10m-synthetic-emails"
source: "huggingface"
url: "https://huggingface.co/datasets/sinabis-group/sinabis-10m-synthetic-emails"
downloads: 224
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# sinabis-group/sinabis-10m-synthetic-emails

> dataset · [Hugging Face](https://huggingface.co/datasets/sinabis-group/sinabis-10m-synthetic-emails)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 high
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[정보 추출]] — metadata · tags, task_categories = `token-classification` · 신뢰도 high
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:generation, task:information_extraction, task:summarization = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:summarization = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `29 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
