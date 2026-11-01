---
type: "dataset"
id: "Nikity/Pornhub"
source: "huggingface"
url: "https://huggingface.co/datasets/Nikity/Pornhub"
downloads: 180
summary: "Pornhub.com에서 수집한 동영상 메타데이터로 연구 및 교육용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
input_modality:
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
dataset_size:
  - "[[중규모 데이터]]"
---
# Nikity/Pornhub

> dataset · [Hugging Face](https://huggingface.co/datasets/Nikity/Pornhub)

Pornhub.com에서 수집한 동영상 메타데이터로 연구 및 교육용 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `The Pornhub Dataset provides a comprehensive collection of data sourced from pornhub.com, encompassing various details from MANYYY videos available on the platf` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval = `File Format: CSV
Content:
URL: The URL of the video.
Category: The genre or category of the video.
User: The username of the uploader.
Video_title: The title of` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `File Format: CSV
Content:
URL: The URL of the video.
Category: The genre or category of the video.
User: The username of the uploader.
Video_title: The title of` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `50 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Pornhub Dataset provides a comprehensive collection of data sourced from pornhub.com` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains sensitive content and is intended solely for research and educational purposes.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
