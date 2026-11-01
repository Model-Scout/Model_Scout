---
type: "dataset"
id: "Shelton1013/SwitchLingua_text"
source: "huggingface"
url: "https://huggingface.co/datasets/Shelton1013/SwitchLingua_text"
downloads: 271
summary: "SwitchLingua는 다국어·다문화 코드스위칭 텍스트 및 음성 데이터셋으로 음성인식과 NLP 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
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
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Shelton1013/SwitchLingua_text

> dataset · [Hugging Face](https://huggingface.co/datasets/Shelton1013/SwitchLingua_text)

SwitchLingua는 다국어·다문화 코드스위칭 텍스트 및 음성 데이터셋으로 음성인식과 NLP 연구에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — ner · readme = `designed to advance research in automatic speech recognition, natural language processing, and conversational AI` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `designed to advance research in automatic speech recognition, natural language processing, and conversational AI` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `80+ hours of recordings` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `The final dataset comprises 420K textual samples` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:speech_recognition = `The final dataset comprises 420K textual samples` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `SwitchLingua is a comprehensive multilingual and multicultural code-switching dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The final dataset comprises 420K textual samples and 80+ hours of recordings, making it the largest open-source code-switching dataset` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
