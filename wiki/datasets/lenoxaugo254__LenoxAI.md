---
type: "dataset"
id: "lenoxaugo254/LenoxAI"
source: "huggingface"
url: "https://huggingface.co/datasets/lenoxaugo254/LenoxAI"
downloads: 29
summary: "Lenox Augo는 다양한 언어와 태스크를 지원하는 다목적 AI 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[이미지 생성]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
  - "[[음성 인식]]"
  - "[[요약]]"
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
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[환경·기상]]"
  - "[[금융·경제]]"
  - "[[의료·보건]]"
  - "[[법률]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# lenoxaugo254/LenoxAI

> dataset · [Hugging Face](https://huggingface.co/datasets/lenoxaugo254/LenoxAI)

Lenox Augo는 다양한 언어와 태스크를 지원하는 다목적 AI 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · readme, task_categories = `audio-classification` · 신뢰도 high
- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[이미지 생성]] — metadata · readme, task_categories = `text-to-image` · 신뢰도 high
- **작업**: [[언어 모델링]] — metadata · readme, task_categories = `fill-mask` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **작업**: [[표 질의응답]] — metadata · readme, task_categories = `table-question-answering` · 신뢰도 high
- **작업**: [[음성 합성]] — metadata · readme, task_categories = `text-to-audio` · 신뢰도 high
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **작업**: [[이미지 인식]] — metadata · readme, task_categories = `image-classification` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:audio_classification, task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:image_generation, task:vision = `image` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:generation, task:image_generation, task:language_modeling, task:question_answering, task:summarization, task:table_qa, task:text_to_speech, task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:language_modeling, task:question_answering, task:speech_recognition, task:summarization, task:table_qa, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `106 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · tags = `climate` · 신뢰도 medium
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **도메인**: [[의료·보건]] — tag_match · tags = `medical` · 신뢰도 medium
- **도메인**: [[법률]] — tag_match · tags = `legal` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
