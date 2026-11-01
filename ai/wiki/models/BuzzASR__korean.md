---
type: "model"
id: "BuzzASR/korean"
source: "huggingface"
url: "https://huggingface.co/BuzzASR/korean"
downloads: 144
parameters_b: 1.543
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[소형 모델]]"
---
# BuzzASR/korean

> model · [Hugging Face](https://huggingface.co/BuzzASR/korean)

## 분류

- **작업**: [[음성 인식]] — metadata · task.matched = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `1.543` · 신뢰도 high

## 학습 데이터

- [[google__fleurs|google/fleurs]]
