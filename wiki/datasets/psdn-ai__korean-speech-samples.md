---
type: "dataset"
id: "psdn-ai/korean-speech-samples"
source: "huggingface"
url: "https://huggingface.co/datasets/psdn-ai/korean-speech-samples"
downloads: 26
summary: "한국어 단일 화자 음성 샘플과 정확한 전사 텍스트를 포함한 음성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 인식]]"
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
  - "[[서비스 데이터]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# psdn-ai/korean-speech-samples

> dataset · [Hugging Face](https://huggingface.co/datasets/psdn-ai/korean-speech-samples)

한국어 단일 화자 음성 샘플과 정확한 전사 텍스트를 포함한 음성 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Modality | Audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `Ground-truth transcripts for understanding sample content` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean speech recordings from contributor collection workflows` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `It is meant to help buyers review recording quality, language coverage, and metadata structure before scoping a larger delivery.` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
