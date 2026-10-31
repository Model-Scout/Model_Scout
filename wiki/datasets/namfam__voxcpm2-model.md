---
type: "dataset"
id: "namfam/voxcpm2-model"
source: "huggingface"
url: "https://huggingface.co/datasets/namfam/voxcpm2-model"
downloads: 106
summary: "VoxCPM2는 30개 언어를 지원하는 2B 파라미터 텍스트-투-스피치 모델입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[음성 합성]]"
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
dataset_role:
  - "[[학습용]]"
---
# namfam/voxcpm2-model

> dataset · [Hugging Face](https://huggingface.co/datasets/namfam/voxcpm2-model)

VoxCPM2는 30개 언어를 지원하는 2B 파라미터 텍스트-투-스피치 모델입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Generate a novel voice from a natural-language description alone (gender, age, tone, emotion, pace…)` · 신뢰도 low
- **작업**: [[음성 합성]] — tag_match · readme, tags = `text-to-speech` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = `Clone any voice from a short clip` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:text_to_speech = `input text in any supported language directly` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `48kHz audio output` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `30 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `trained on over 2 million hours of multilingual speech data` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `trained on over 2 million hours of multilingual speech data` · 신뢰도 medium
