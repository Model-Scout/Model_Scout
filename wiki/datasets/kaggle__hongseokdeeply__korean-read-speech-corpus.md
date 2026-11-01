---
type: "dataset"
id: "kaggle/hongseokdeeply/korean-read-speech-corpus"
source: "kaggle"
url: "https://www.kaggle.com/datasets/hongseokdeeply/korean-read-speech-corpus"
downloads: 179
summary: "한국어 스크립트를 읽는 화자의 음성 녹음 데이터로 음성 인식 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/hongseokdeeply/korean-read-speech-corpus

> dataset · [Kaggle](https://www.kaggle.com/datasets/hongseokdeeply/korean-read-speech-corpus)

한국어 스크립트를 읽는 화자의 음성 녹음 데이터로 음성 인식 연구에 활용됨.

## 분류

- **작업**: [[음성 인식]] — ner · readme = `Pairs of Korean speakers reading a script with , with , are recorded.` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `_Text_: the content of the script` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Pairs of Korean speakers reading a script with , with , are recorded.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is a subset(approximately 1%) of a much bigger dataset which were recorded under the same circumstances as these open source datasets.` · 신뢰도 low
