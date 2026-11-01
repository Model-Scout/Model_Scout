---
type: "dataset"
id: "Dasool/huggingface-cjk-metadata"
source: "huggingface"
url: "https://huggingface.co/datasets/Dasool/huggingface-cjk-metadata"
downloads: 24
summary: "중국어, 일본어, 한국어, 영어 데이터셋 메타데이터와 문서 정보를 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[서비스 데이터]]"
---
# Dasool/huggingface-cjk-metadata

> dataset · [Hugging Face](https://huggingface.co/datasets/Dasool/huggingface-cjk-metadata)

중국어, 일본어, 한국어, 영어 데이터셋 메타데이터와 문서 정보를 제공하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Meta-evaluation of documentation quality` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Dataset ecosystem analysis` · 신뢰도 low
- **작업**: [[이미지 이해]] — ner · readme = `Visualization and benchmarking of dataset trends` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:visual_qa = `structured metadata and documentation extracted from the top 700 most downloaded datasets per language` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `structured metadata and documentation extracted from the top 700 most downloaded datasets per language` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `large-scale, cross-linguistic analysis of data curation, documentation quality, and cultural development patterns in East Asian NLP communities` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `All scraping code and analysis notebooks can be found at` · 신뢰도 low
