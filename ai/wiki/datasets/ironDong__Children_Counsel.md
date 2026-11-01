---
type: "dataset"
id: "ironDong/Children_Counsel"
source: "huggingface"
url: "https://huggingface.co/datasets/ironDong/Children_Counsel"
downloads: 234
summary: "아동·청소년 상담 음성 및 전사 데이터로 음성 인식 및 상담 분석에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ironDong/Children_Counsel

> dataset · [Hugging Face](https://huggingface.co/datasets/ironDong/Children_Counsel)

아동·청소년 상담 음성 및 전사 데이터로 음성 인식 및 상담 분석에 활용 가능

## 분류

- **작업**: [[정보 추출]] — ner · readme = `Developing NLP models for counseling text analysis` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `audio recordings of counseling sessions in MP3 format` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction = `Contains JSON files with transcriptions and metadata for each session` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `Training speech recognition models for counseling scenarios` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `This dataset contains counseling data for children and adolescents` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset can be used for: Training speech recognition models` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
