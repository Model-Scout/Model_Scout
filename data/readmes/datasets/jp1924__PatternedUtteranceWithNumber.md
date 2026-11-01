---
dataset_info:
- config_name: ASR
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: sentence
    dtype: string
  - name: metadata
    struct:
    - name: audio
      struct:
      - name: recordedID
        dtype: string
      - name: recordedDate
        dtype: string
      - name: recordedStart
        dtype: string
      - name: fileName
        dtype: string
      - name: filePath
        dtype: string
      - name: recordedTime
        dtype: float32
      - name: recordedQuality
        dtype: string
      - name: recordedDevice
        dtype: string
      - name: recordedDeviceName
        dtype: string
      - name: recordedEnv
        dtype: string
    - name: recordPerson
      struct:
      - name: collectedID
        dtype: string
      - name: recorderID
        dtype: string
      - name: sex
        dtype: string
      - name: generation
        dtype: string
      - name: residence
        dtype: string
      - name: dialect
        dtype: string
      - name: dialectRegion
        dtype: string
      - name: areaInfomation
        struct:
        - name: fatherHometown
          dtype: string
        - name: motherHometown
          dtype: string
  splits:
  - name: train
    num_examples: 3621732
  - name: validation
    num_examples: 429055
configs:
- config_name: ASR
  data_files:
  - split: train
    path: "hf://datasets/jp1924-audio-1/PatternedUtteranceWithNumber-part1/data/train-*"
  - split: validation
    path: "hf://datasets/jp1924-audio-1/PatternedUtteranceWithNumber-part1/data/validation-*"
task_categories:
- automatic-speech-recognition
language:
- ko
size_categories:
- n>1T
---

jp1924/TNT0.5B-Dual 모델을 활용해서 이중 전사문으로 변환한 데이터

오디오는 FLAC으로 무손실 압축되어 `jp1924-audio-1/PatternedUtteranceWithNumber-part1`에 저장되어 있습니다.
이 repo는 YAML `hf://` 참조를 통해 해당 데이터를 가리킵니다.
