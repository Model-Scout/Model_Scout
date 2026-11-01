---
type: "dataset"
id: "PeepDaSlan9/DIDI"
source: "huggingface"
url: "https://huggingface.co/datasets/PeepDaSlan9/DIDI"
downloads: 30
summary: "다국어(한국어 포함) 대화, 분류, 질의응답, 번역, 요약, 음성 인식 등 다양한 작업용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[음성 인식]]"
  - "[[요약]]"
  - "[[표 질의응답]]"
  - "[[음성 합성]]"
  - "[[번역]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[표 (출력 형식)|표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[am]]"
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[ig]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# PeepDaSlan9/DIDI

> dataset · [Hugging Face](https://huggingface.co/datasets/PeepDaSlan9/DIDI)

다국어(한국어 포함) 대화, 분류, 질의응답, 번역, 요약, 음성 인식 등 다양한 작업용 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `voice-activity-detection` · 신뢰도 low
- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **작업**: [[표 질의응답]] — metadata · readme, task_categories = `table-question-answering` · 신뢰도 high
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-audio` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:audio_classification, task:speech_recognition = `- automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:table_qa = `- table-question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:question_answering, task:summarization, task:table_qa, task:text_to_speech, task:translation = `- conversational` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `- table-question-answering` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:speech_recognition, task:summarization, task:table_qa, task:translation = `- conversational` · 신뢰도 medium
- **언어**: [[am]] — metadata · languages = `am` · 신뢰도 high
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[ig]] — metadata · languages = `ig` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high
