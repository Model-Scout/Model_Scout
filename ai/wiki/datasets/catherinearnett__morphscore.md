---
type: "dataset"
id: "catherinearnett/morphscore"
source: "huggingface"
url: "https://huggingface.co/datasets/catherinearnett/morphscore"
downloads: 624
summary: "MorphScore는 형태소 경계에 따른 토크나이저 평가를 위한 86개 언어 데이터셋 모음입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
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
# catherinearnett/morphscore

> dataset · [Hugging Face](https://huggingface.co/datasets/catherinearnett/morphscore)

MorphScore는 형태소 경계에 따른 토크나이저 평가를 위한 86개 언어 데이터셋 모음입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `MorphScore is a tokenizer evaluation framework, which evaluates the extent to which a tokenizer segments words along morpheme boundaries.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `MorphScore is a tokenizer evaluation framework, which evaluates the extent to which a tokenizer segments words along morpheme boundaries.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `MorphScore is a tokenizer evaluation framework, which evaluates the extent to which a tokenizer segments words along morpheme boundaries.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `83 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `72` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `All datasets are derived from existing Universal Dependencies treebanks.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This repository contains the datasets used to calculate MorphScore.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `sentence` 열 p90 289자 ≈ 72 토큰 (viewer statistics, default/train)
