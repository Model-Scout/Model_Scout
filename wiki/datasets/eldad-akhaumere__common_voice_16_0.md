---
type: "dataset"
id: "eldad-akhaumere/common_voice_16_0"
source: "huggingface"
url: "https://huggingface.co/datasets/eldad-akhaumere/common_voice_16_0"
downloads: 132
summary: "Common Voice Corpus 16은 120개 언어의 음성 및 텍스트 데이터를 포함한 음성 인식 학습용 데이터셋입니다."
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
# eldad-akhaumere/common_voice_16_0

> dataset · [Hugging Face](https://huggingface.co/datasets/eldad-akhaumere/common_voice_16_0)

Common Voice Corpus 16은 120개 언어의 음성 및 텍스트 데이터를 포함한 음성 인식 학습용 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — ner · readme = `Many of the 30328 recorded hours in the dataset also include demographic metadata like age, sex, and accent that can help improve the accuracy of speech recogni` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `The Common Voice dataset consists of a unique MP3 and corresponding text file.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme = `The Common Voice dataset consists of a unique MP3 and corresponding text file.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `The Common Voice dataset consists of a unique MP3 and corresponding text file.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `117 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset currently consists of 19673 validated hours in 120 languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train your own CTC or Seq2Seq Automatic Speech Recognition models on Common Voice 16 with `transformers`` · 신뢰도 medium
