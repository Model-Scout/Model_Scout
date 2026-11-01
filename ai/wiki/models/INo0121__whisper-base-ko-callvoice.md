---
type: "model"
id: "INo0121/whisper-base-ko-callvoice"
source: "huggingface"
url: "https://huggingface.co/INo0121/whisper-base-ko-callvoice"
downloads: 120
context_length: 448
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
---
# INo0121/whisper-base-ko-callvoice

> model · [Hugging Face](https://huggingface.co/INo0121/whisper-base-ko-callvoice)

## 분류

- **작업**: [[음성 인식]] — metadata · task.matched = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — metadata · context_length = `448` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]]

## 학습 데이터

- [[INo0121__low_quality_call_voice|INo0121/low_quality_call_voice]]
