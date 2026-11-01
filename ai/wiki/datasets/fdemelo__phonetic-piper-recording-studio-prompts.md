---
type: "dataset"
id: "fdemelo/phonetic-piper-recording-studio-prompts"
source: "huggingface"
url: "https://huggingface.co/datasets/fdemelo/phonetic-piper-recording-studio-prompts"
downloads: 24
summary: "다국어 발화 데이터셋으로, Piper 녹음 스튜디오용 음성 프롬프트와 음성학적 표기를 포함함"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
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
# fdemelo/phonetic-piper-recording-studio-prompts

> dataset · [Hugging Face](https://huggingface.co/datasets/fdemelo/phonetic-piper-recording-studio-prompts)

다국어 발화 데이터셋으로, Piper 녹음 스튜디오용 음성 프롬프트와 음성학적 표기를 포함함

## 분류

- **작업**: [[음성 인식]] — ner · readme = `prompts for the Piper recording studio` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme = `original prompts` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `phonemized versions of the original sentences` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `42 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `an utterance dataset made available for various languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `a 90%/10% train/test split` · 신뢰도 medium
