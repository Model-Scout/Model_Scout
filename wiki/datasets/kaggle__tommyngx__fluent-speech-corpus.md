---
type: "dataset"
id: "kaggle/tommyngx/fluent-speech-corpus"
source: "kaggle"
url: "https://www.kaggle.com/datasets/tommyngx/fluent-speech-corpus"
downloads: 3521
summary: "Fluent Speech Commands 음성 데이터셋으로 음성 인식 및 명령 분류에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/tommyngx/fluent-speech-corpus

> dataset · [Kaggle](https://www.kaggle.com/datasets/tommyngx/fluent-speech-corpus)

Fluent Speech Commands 음성 데이터셋으로 음성 인식 및 명령 분류에 사용됨

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `classification` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `16kHz single-channel .wav files containing the speech audio recorded by that speaker.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `transcript - The prompt that the speaker was asked to read` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Fluent Speech Commands Voice Dataset for Speaking Recognition` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `data/traindata.csv, /data/validdata.csv, /data/test_data.csv` · 신뢰도 medium
