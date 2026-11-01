---
type: "dataset"
id: "Prompthumanizer/jain_architecture"
source: "huggingface"
url: "https://huggingface.co/datasets/Prompthumanizer/jain_architecture"
downloads: 9
summary: "jain_Architecture_origin 데이터셋은 다양한 작업에 활용 가능한 대규모 다중언어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
  - "[[음성 인식]]"
  - "[[표 질의응답]]"
  - "[[음성 합성]]"
  - "[[번역]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# Prompthumanizer/jain_architecture

> dataset · [Hugging Face](https://huggingface.co/datasets/Prompthumanizer/jain_architecture)

jain_Architecture_origin 데이터셋은 다양한 작업에 활용 가능한 대규모 다중언어 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · readme, task_categories = `audio-classification` · 신뢰도 high
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 high
- **작업**: [[언어 모델링]] — metadata · readme, task_categories = `fill-mask` · 신뢰도 high
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **작업**: [[표 질의응답]] — metadata · readme, task_categories = `table-question-answering` · 신뢰도 high
- **작업**: [[음성 합성]] — metadata · readme, task_categories = `text-to-audio` · 신뢰도 high
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **작업**: [[이미지 인식]] — ner · readme = `depth-estimation` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:audio_classification, task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:vision = `image` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:generation, task:information_extraction, task:language_modeling, task:table_qa, task:text_to_speech, task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:language_modeling, task:speech_recognition, task:table_qa, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `inf` · 신뢰도 high
