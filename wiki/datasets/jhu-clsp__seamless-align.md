---
type: "dataset"
id: "jhu-clsp/seamless-align"
source: "huggingface"
url: "https://huggingface.co/datasets/jhu-clsp/seamless-align"
downloads: 538
summary: "Meta AI가 공개한 음성-음성, 텍스트-음성, 음성-텍스트 병렬 데이터를 기반으로 한 다국어 음성 및 텍스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
  - "[[번역]]"
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
# jhu-clsp/seamless-align

> dataset · [Hugging Face](https://huggingface.co/datasets/jhu-clsp/seamless-align)

Meta AI가 공개한 음성-음성, 텍스트-음성, 음성-텍스트 병렬 데이터를 기반으로 한 다국어 음성 및 텍스트 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Parallel sentences were identified using SONAR encoders.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This dataset was created based on metadata for mined Speech-to-Speech(S2S), Text-to-Speech(TTS) and Speech-to-Text(S2T)` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `Speech-to-Speech(S2S), Text-to-Speech(TTS) and Speech-to-Text(S2T)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval, task:translation = `Speech-to-Speech(S2S), Text-to-Speech(TTS) and Speech-to-Text(S2T)` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme = `Speech-to-Speech(S2S), Text-to-Speech(TTS) and Speech-to-Text(S2T)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Speech-to-Speech(S2S), Text-to-Speech(TTS) and Speech-to-Text(S2T)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `34 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Speech and Text was collected from the web many of which are web crawls.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset provides data for training machine learning systems for many languages.` · 신뢰도 medium
