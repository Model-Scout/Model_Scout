---
type: "dataset"
id: "Tribhuvand/babel-briefings"
source: "huggingface"
url: "https://huggingface.co/datasets/Tribhuvand/babel-briefings"
downloads: 173
summary: "30개 언어 뉴스 헤드라인 470만 건으로 다국어 뉴스 분석에 활용되는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[번역]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[의료·보건]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Tribhuvand/babel-briefings

> dataset · [Hugging Face](https://huggingface.co/datasets/Tribhuvand/babel-briefings)

30개 언어 뉴스 헤드라인 470만 건으로 다국어 뉴스 분석에 활용되는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `The dataset is provided in the form of 54 JSON files, one for each location containing the all the unique headlines` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `news headlines across 30 different languages collected between 8 August 2020 and 29 November 2021` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding, task:generation, task:question_answering, task:retrieval, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `30 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `53` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · tags = `health` · 신뢰도 medium
- **도메인**: [[뉴스·미디어]] — tag_match · readme, tags = `news` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is provided in the form of 54 JSON files, one for each location containing the all the unique headlines` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 214자 ≈ 53 토큰 (viewer statistics, default/train)
