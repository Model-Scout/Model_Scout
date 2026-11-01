---
type: "dataset"
id: "agentlans/openchat_sharegpt4_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/agentlans/openchat_sharegpt4_dataset"
downloads: 35
summary: "ShareGPT4 대화 데이터를 정제 및 처리한 다국어 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# agentlans/openchat_sharegpt4_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/agentlans/openchat_sharegpt4_dataset)

ShareGPT4 대화 데이터를 정제 및 처리한 다국어 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Corrected turn order Added language field for detected language Removed duplicates Redacted URLs, e-mails, phone numbers Shuffled` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Corrected turn order Added language field for detected language Removed duplicates Redacted URLs, e-mails, phone numbers Shuffled` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `18 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This is a processed version of sharegpt_clean.json from openchat/openchat_sharegpt4_dataset.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
