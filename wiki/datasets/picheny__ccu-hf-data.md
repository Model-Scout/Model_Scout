---
type: "dataset"
id: "picheny/ccu-hf-data"
source: "huggingface"
url: "https://huggingface.co/datasets/picheny/ccu-hf-data"
downloads: 578
summary: "한국어, 중국어, 히브리어, 터키어 음성 및 전사 데이터로 다국어 음성 인식 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[he]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[tr]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# picheny/ccu-hf-data

> dataset · [Hugging Face](https://huggingface.co/datasets/picheny/ccu-hf-data)

한국어, 중국어, 히브리어, 터키어 음성 및 전사 데이터로 다국어 음성 인식 연구용 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `This dataset contains segmented speech audio and transcripts for multiple languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `TSV columns are: - audio path (relative path to wav file) - transcript / text` · 신뢰도 medium
- **언어**: [[he]] — metadata · languages = `he` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[tr]] — metadata · languages = `tr` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains segmented speech audio and transcripts for multiple languages: Korean (ko), Chinese (zh), Hebrew (he), and Turkish (tr).` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `- ASR evaluation across languages` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `- ASR model training` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
