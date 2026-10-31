---
type: "dataset"
id: "dbarbedillo/SMS_Spam_Multilingual_Collection_Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/dbarbedillo/SMS_Spam_Multilingual_Collection_Dataset"
downloads: 301
summary: "다국어 SMS 스팸 메시지 모음으로 스팸 탐지 연구에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# dbarbedillo/SMS_Spam_Multilingual_Collection_Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/dbarbedillo/SMS_Spam_Multilingual_Collection_Dataset)

다국어 SMS 스팸 메시지 모음으로 스팸 탐지 연구에 사용됨

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Collection of Multilingual SMS messages tagged as spam or legitimate` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `ham- non-spam text
spam- spam text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `21 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `45` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `gpl` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The SMS Spam Collection is a set of SMS-tagged messages that have been collected for SMS Spam research.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The SMS Spam Collection is a set of SMS-tagged messages that have been collected for SMS Spam research.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text_jv` 열 p90 180자 ≈ 45 토큰 (viewer statistics, default/train)
