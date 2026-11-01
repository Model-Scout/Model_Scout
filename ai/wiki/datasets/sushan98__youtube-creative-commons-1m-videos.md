---
type: "dataset"
id: "sushan98/youtube-creative-commons-1m-videos"
source: "huggingface"
url: "https://huggingface.co/datasets/sushan98/youtube-creative-commons-1m-videos"
downloads: 178
summary: "1,000,000개의 크리에이티브 커먼즈 라이선스 유튜브 영상 링크와 메타데이터 모음집입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
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
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# sushan98/youtube-creative-commons-1m-videos

> dataset · [Hugging Face](https://huggingface.co/datasets/sushan98/youtube-creative-commons-1m-videos)

1,000,000개의 크리에이티브 커먼즈 라이선스 유튜브 영상 링크와 메타데이터 모음집입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `Benchmarking retrieval, recommendation, or channel-level analysis` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `This dataset contains links and metadata only. It does not include any video, audio, or transcript files.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `This dataset contains links and metadata only.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset is intended for research, benchmarking, and building multilingual video corpora` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The first 1,000,000 rows of [`Pclanglais/youtube-commons-metadata`]` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
