---
type: "dataset"
id: "dijihax/Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/dijihax/Dataset"
downloads: 47
summary: "dijihax/Dataset는 새로운 데이터셋을 위한 기본 템플릿 데이터입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[시계열 예측]]"
  - "[[텍스트 생성]]"
  - "[[이미지 생성]]"
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[음성 인식]]"
  - "[[요약]]"
  - "[[표 질의응답]]"
  - "[[표 데이터 예측]]"
  - "[[음성 합성]]"
  - "[[번역]]"
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
  - "[[금융·경제]]"
  - "[[의료·보건]]"
  - "[[법률]]"
data_format:
  - "[[CSV]]"
  - "[[JSON]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# dijihax/Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/dijihax/Dataset)

dijihax/Dataset는 새로운 데이터셋을 위한 기본 템플릿 데이터입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[시계열 예측]] — metadata · task_categories = `time-series-forecasting` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[이미지 생성]] — metadata · task_categories = `image-to-image` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_categories = `fill-mask` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `multiple-choice` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-audio` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `image-classification` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:audio_classification, task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:image_generation, task:vision, task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa, task:tabular_prediction = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:generation, task:image_generation, task:information_extraction, task:language_modeling, task:question_answering, task:retrieval, task:summarization, task:table_qa, task:text_to_speech, task:translation, task:visual_qa = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:language_modeling, task:question_answering, task:speech_recognition, task:summarization, task:table_qa, task:translation, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `148 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · tags = `climate` · 신뢰도 medium
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **도메인**: [[의료·보건]] — tag_match · tags = `medical` · 신뢰도 medium
- **도메인**: [[법률]] — tag_match · tags = `legal` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `inf` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `CheriTangerine/Scoups_Voice_Train`
- `PariPaliwal/DeDuplication`
- `Prompthumanizer/light_weight_jain_architecture_System`
- `baiyinnamula/first-dataset`
- `global-llm-2024/ko_ifeval`
