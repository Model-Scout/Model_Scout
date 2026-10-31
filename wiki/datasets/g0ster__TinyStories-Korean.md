---
type: "dataset"
id: "g0ster/TinyStories-Korean"
source: "huggingface"
url: "https://huggingface.co/datasets/g0ster/TinyStories-Korean"
downloads: 198
summary: "roneneldan의 TinyStories를 한국어로 번역한 텍스트 생성용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# g0ster/TinyStories-Korean

> dataset · [Hugging Face](https://huggingface.co/datasets/g0ster/TinyStories-Korean)

roneneldan의 TinyStories를 한국어로 번역한 텍스트 생성용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset is a translated version of roneneldan's TinyStories dataset.` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `I changed it back to a txt file.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `I changed it back to a txt file.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `125` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `I first downloaded roneneldan's TinyStories, and I organized it in a db file.` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 187자 ≈ 125 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[north-wind__TinyStories-Korean-800K|north-wind/TinyStories-Korean-800K]]
