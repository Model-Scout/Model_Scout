---
type: "dataset"
id: "refine-ai/subscene"
source: "huggingface"
url: "https://huggingface.co/datasets/refine-ai/subscene"
downloads: 2171
summary: "영화, 시리즈, 애니메이션 자막 65개 언어 410GB 규모 다국어 NLP 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# refine-ai/subscene

> dataset · [Hugging Face](https://huggingface.co/datasets/refine-ai/subscene)

영화, 시리즈, 애니메이션 자막 65개 언어 410GB 규모 다국어 NLP 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `It provides a rich resource for studying language variations and building multilingual NLP models.` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:language_modeling, task:translation = `This dataset includes subtitles for movies, series, and animations gathered from the Subscene dump.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:translation = `The actual text content displayed for that specific subtitle segment.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `67 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Subscene is a vast collection of multilingual subtitles, encompassing 65 different languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `It provides a rich resource for studying language variations and building multilingual NLP models.` · 신뢰도 low
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high
