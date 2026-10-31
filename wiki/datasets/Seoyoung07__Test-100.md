---
type: "dataset"
id: "Seoyoung07/Test-100"
source: "huggingface"
url: "https://huggingface.co/datasets/Seoyoung07/Test-100"
downloads: 21
summary: "한국수어 사전에서 추출한 100개 단어의 한국수어 영상 클립 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Seoyoung07/Test-100

> dataset · [Hugging Face](https://huggingface.co/datasets/Seoyoung07/Test-100)

한국수어 사전에서 추출한 100개 단어의 한국수어 영상 클립 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `evaluation of the project model Seoyoung07/korean-sign-word-classifier-mediapipe` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding = `text` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `100 Korean Sign Language isolated-word MP4 clips` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `File names are the target Korean word labels` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Sign Language Dictionary` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `used for evaluation of the project model Seoyoung07/korean-sign-word-classifier-mediapipe` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
