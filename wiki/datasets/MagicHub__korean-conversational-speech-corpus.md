---
type: "dataset"
id: "MagicHub/korean-conversational-speech-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/MagicHub/korean-conversational-speech-corpus"
downloads: 288
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# MagicHub/korean-conversational-speech-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/MagicHub/korean-conversational-speech-corpus)

## 분류

- **작업**: [[텍스트 생성]] — tag_match · tags = `Conversational` · 신뢰도 medium
- **작업**: [[음성 인식]] — tag_match · tags = `ASR` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality, task:speech_recognition = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
