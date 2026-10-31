---
type: "dataset"
id: "jonghwanhyeon/korean-emotion-lexicon"
source: "huggingface"
url: "https://huggingface.co/datasets/jonghwanhyeon/korean-emotion-lexicon"
downloads: 65
summary: "서울대 연구진이 개발한 한국어 감정 어휘 데이터셋으로 감정 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# jonghwanhyeon/korean-emotion-lexicon

> dataset · [Hugging Face](https://huggingface.co/datasets/jonghwanhyeon/korean-emotion-lexicon)

서울대 연구진이 개발한 한국어 감정 어휘 데이터셋으로 감정 분석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `This repository contains a comprehensive dataset of Korean emotion lexicons developed through psychological research` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `The dataset includes several key measures for each emotion lexicon` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `The dataset includes several key measures for each emotion lexicon` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The dataset includes several key measures for each emotion lexicon` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `4` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This repository contains a comprehensive dataset of Korean emotion lexicons developed through psychological research` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This repository contains a comprehensive dataset of Korean emotion lexicons developed through psychological research` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `lexicon` 열 p90 5자 ≈ 4 토큰 (viewer statistics, default/train)
