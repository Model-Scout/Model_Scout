---
type: "dataset"
id: "kaggle/zldzmfoq12/korean-voice"
source: "kaggle"
url: "https://www.kaggle.com/datasets/zldzmfoq12/korean-voice"
downloads: 393
summary: "한국 남성 성우 이재범의 유튜브 음성, 텍스트, 임베딩 데이터로 음성 합성 및 인식에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 인식]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
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
# kaggle/zldzmfoq12/korean-voice

> dataset · [Kaggle](https://www.kaggle.com/datasets/zldzmfoq12/korean-voice)

한국 남성 성우 이재범의 유튜브 음성, 텍스트, 임베딩 데이터로 음성 합성 및 인식에 활용 가능

## 분류

- **작업**: [[음성 인식]] — ner · readme = `The data can be used to train artificial intelligence models such as voice synthesis and voice recognition.` · 신뢰도 low
- **작업**: [[음성 합성]] — ner · readme = `The data can be used to train artificial intelligence models such as voice synthesis and voice recognition.` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `There are short audio files segmented by subtitle.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:text_to_speech = `and a refined text file that corresponds to an audio file.` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `The data can be used to train artificial intelligence models such as voice synthesis and voice recognition.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Data files © Original Authors` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `male korean voice actor audio in youtube` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The data can be used to train artificial intelligence models such as voice synthesis and voice recognition.` · 신뢰도 medium
