---
type: "dataset"
id: "pacscilab/VoxCommunis"
source: "huggingface"
url: "https://huggingface.co/datasets/pacscilab/VoxCommunis"
downloads: 1460
summary: "Mozilla Common Voice에서 파생된 음성 및 음성 정렬 데이터로 음성 인식 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# pacscilab/VoxCommunis

> dataset · [Hugging Face](https://huggingface.co/datasets/pacscilab/VoxCommunis)

Mozilla Common Voice에서 파생된 음성 및 음성 정렬 데이터로 음성 인식 연구에 활용됨.

## 분류

- **작업**: [[음성 인식]] — ner · readme = `The VoxCommunis Corpus is a phonetic corpus derived from the Mozilla Common Voice Corpus.` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `Corresponding audio files and corpus metadata can be downloaded from Mozilla Common Voice` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `The TextGrids contain phone- and word-level alignments of the validated set of the Common Voice data.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `56 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The VoxCommunis Corpus is a phonetic corpus derived from the Mozilla Common Voice Corpus.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The acoustic models have been trained using the Montreal Forced Aligner` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
