---
type: "dataset"
id: "Gingiris/gingiris-aso-growth"
source: "huggingface"
url: "https://huggingface.co/datasets/Gingiris/gingiris-aso-growth"
downloads: 143
summary: "30개 이상의 앱 사례를 기반으로 한 ASO 및 앱 콜드 스타트 성장 전략 가이드북입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Gingiris/gingiris-aso-growth

> dataset · [Hugging Face](https://huggingface.co/datasets/Gingiris/gingiris-aso-growth)

30개 이상의 앱 사례를 기반으로 한 ASO 및 앱 콜드 스타트 성장 전략 가이드북입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `Rank your app without buying installs — App Store Optimization + UGC creator matrix + 90-day cold start framework used by 30+ indie apps` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:retrieval = `Rank your app without buying installs — App Store Optimization + UGC creator matrix + 90-day cold start framework used by 30+ indie apps` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Rank your app without buying installs — App Store Optimization + UGC creator matrix + 90-day cold start framework used by 30+ indie apps` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This playbook documents the exact tactics 30+ apps (Chinese indie + AI startups) used to break US Top 100 without burning Apple Search Ads budget` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
