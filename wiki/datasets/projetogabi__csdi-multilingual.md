---
type: "dataset"
id: "projetogabi/csdi-multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/projetogabi/csdi-multilingual"
downloads: 82
summary: "백내장 중증도와 진단 이미지를 포함한 다국어 안저 이미지 데이터셋으로 자동 백내장 선별 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# projetogabi/csdi-multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/projetogabi/csdi-multilingual)

백내장 중증도와 진단 이미지를 포함한 다국어 안저 이미지 데이터셋으로 자동 백내장 선별 연구에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The cataract severity grading criteria are defined by the original authors as follows` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Each record translates the detailed diagnostic descriptions, which follow a fixed sentence structure evaluating` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `The 187 original fundus images (.png and .jpg) are hosted by the original authors.` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:information_extraction, task:visual_qa = `This repository contains only the translated text annotations.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `translated text annotations` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `33 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `40` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `It further replicates the split used by the original authors of 37 test images and 150 training images.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `report` 열 p90 158자 ≈ 40 토큰 (viewer statistics, Korean/test)
