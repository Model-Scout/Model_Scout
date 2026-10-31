---
type: "dataset"
id: "anas775/DETECT-AI-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/anas775/DETECT-AI-Dataset"
downloads: 44
summary: "텍스트, 이미지, 영상, 음성의 AI 생성 여부를 탐지하는 멀티모달 AI 탐지 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# anas775/DETECT-AI-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/anas775/DETECT-AI-Dataset)

텍스트, 이미지, 영상, 음성의 AI 생성 여부를 탐지하는 멀티모달 AI 탐지 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[이미지 인식]] — metadata · task_categories = `image-classification` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:audio_classification = `text, image, video, and audio` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `text, image, video, and audio` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `text, image, video, and audio` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `text, image, video, and audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `labeled by a weighted ensemble of 8 specialized AI-detection models.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `25 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `scraped from 19 global sources across text, image, video, and audio` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `1B+ verified samples/month scraped from 19 global sources` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
