---
type: "dataset"
id: "zaibihassan/Quranic-Translation-Audio-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/zaibihassan/Quranic-Translation-Audio-Data"
downloads: 12886
summary: "51개 언어의 꾸란 번역 낭독 오디오와 타이밍 데이터를 포함한 다국어 음성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# zaibihassan/Quranic-Translation-Audio-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/zaibihassan/Quranic-Translation-Audio-Data)

51개 언어의 꾸란 번역 낭독 오디오와 타이밍 데이터를 포함한 다국어 음성 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **작업**: [[음성 합성]] — metadata · readme, task_categories = `text-to-speech` · 신뢰도 high
- **작업**: [[번역]] — tag_match · tags = `translation` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `multilingual audio dataset containing the complete recitation of translation audios and commentaries` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:text_to_speech, task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `high-fidelity Opus (.opus) format at a streaming-optimized bitrate of 32kbps` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Holy Quran across 51 different translation directories` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
