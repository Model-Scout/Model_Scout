---
type: "dataset"
id: "willwade/AACConversations"
source: "huggingface"
url: "https://huggingface.co/datasets/willwade/AACConversations"
downloads: 45
summary: "AAC 사용자들의 다국어 대화와 타이핑 오류 시뮬레이션 데이터로 보조기술 개발에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# willwade/AACConversations

> dataset · [Hugging Face](https://huggingface.co/datasets/willwade/AACConversations)

AAC 사용자들의 다국어 대화와 타이핑 오류 시뮬레이션 데이터로 보조기술 개발에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `The dataset supports multiple languages, making it valuable for developing multilingual assistive technologies` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — metadata · task_ids = `language-modeling` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:language_modeling = `Each instance in the dataset represents a single utterance from an AAC user, along with context from the conversation and various augmented versions of the utte` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Each instance in the dataset represents a single utterance from an AAC user, along with context from the conversation and various augmented versions of the utte` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `30 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `The AAC Conversations Dataset is a collection of simulated conversations involving Augmentative and Alternative Communication (AAC) users` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The dataset contains: - Over 86,000 examples across train and test splits` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset contains: - Over 86,000 examples across train and test splits` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
