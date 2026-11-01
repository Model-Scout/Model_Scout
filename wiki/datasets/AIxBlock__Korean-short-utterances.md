---
type: "dataset"
id: "AIxBlock/Korean-short-utterances"
source: "huggingface"
url: "https://huggingface.co/datasets/AIxBlock/Korean-short-utterances"
downloads: 35
summary: "AIxBlock에서 제공하는 약 70만 개 한국어 문장으로 음성 데이터 생성과 NLP에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
  - "[[음성 인식]]"
  - "[[음성 합성]]"
  - "[[번역]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# AIxBlock/Korean-short-utterances

> dataset · [Hugging Face](https://huggingface.co/datasets/AIxBlock/Korean-short-utterances)

AIxBlock에서 제공하는 약 70만 개 한국어 문장으로 음성 데이터 생성과 NLP에 활용 가능

## 분류

- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Natural Language Processing (NLP) tasks, such as language modeling, translation, intent detection, and more` · 신뢰도 medium
- **작업**: [[음성 인식]] — ner · readme = `Speech data generation (e.g., recording short audio clips lasting 8–30 seconds per sentence)` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-audio` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `Natural Language Processing (NLP) tasks, such as language modeling, translation, intent detection, and more` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction, task:language_modeling, task:text_to_speech, task:translation = `This dataset contains around 700k sentences in Korean` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling, task:speech_recognition, task:translation = `This dataset contains around 700k sentences in Korean` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a valuable resource for a wide range of language technology applications` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains around 700k sentences in Korean` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `kaggle/aixblock2023/korean-short-utterances`
