---
type: "dataset"
id: "MagicHub/korean-conversational-speech-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/MagicHub/korean-conversational-speech-corpus"
downloads: 288
summary: "한국어 대화 음성 5.22시간 분량의 전사 데이터로 음성 인식 연구용입니다."
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# MagicHub/korean-conversational-speech-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/MagicHub/korean-conversational-speech-corpus)

한국어 대화 음성 5.22시간 분량의 전사 데이터로 음성 인식 연구용입니다.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · tags = `Conversational` · 신뢰도 low
- **작업**: [[음성 인식]] — tag_match · readme, tags = `ASR` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Audio Parameters: 16 kHz, 16 bits` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:speech_recognition = `transcribed Korean conversational speech` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `44` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean conversational speech` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This open-source dataset consists of 5.22 hours of transcribed Korean conversational speech` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 65자 ≈ 44 토큰 (viewer statistics, default/train)
