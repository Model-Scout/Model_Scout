---
type: "dataset"
id: "scailaboratory/KoALA"
source: "huggingface"
url: "https://huggingface.co/datasets/scailaboratory/KoALA"
downloads: 225
summary: "KoALa-Bench는 한국어 음성 이해를 위한 대규모 음성 언어 모델 평가 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[질의응답]]"
  - "[[음성 인식]]"
  - "[[번역]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# scailaboratory/KoALA

> dataset · [Hugging Face](https://huggingface.co/datasets/scailaboratory/KoALA)

KoALa-Bench는 한국어 음성 이해를 위한 대규모 음성 언어 모델 평가 벤치마크입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality, task:audio_classification, task:speech_recognition = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:question_answering, task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:speech_recognition, task:translation = `Transcribe Korean speech into text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KoALa-Bench is a comprehensive benchmark for evaluating Large Audio Language Models (LALMs) on Korean speech understanding.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `KoALa-Bench consists of six evaluation tasks organized into two categories.` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
