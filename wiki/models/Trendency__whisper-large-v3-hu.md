---
type: "model"
id: "Trendency/whisper-large-v3-hu"
source: "huggingface"
url: "https://huggingface.co/Trendency/whisper-large-v3-hu"
downloads: 2412
parameters_b: 1.543
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[소형 모델]]"
---
# Trendency/whisper-large-v3-hu

> model · [Hugging Face](https://huggingface.co/Trendency/whisper-large-v3-hu)

## 분류

- **작업**: [[음성 인식]] — metadata · task.matched = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `99 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `1.543` · 신뢰도 high

## 학습 데이터

- [[FBK-MT__Speech-MASSIVE|FBK-MT/Speech-MASSIVE]]
- [[KTH__hungarian-single-speaker-tts|KTH/hungarian-single-speaker-tts]]
- [[facebook__voxpopuli|facebook/voxpopuli]]
- [[mozilla-foundation__common_voice_17_0|mozilla-foundation/common_voice_17_0]]
