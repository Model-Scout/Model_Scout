---
type: "dataset"
id: "fdemelo/ud-conll2017-aligned"
source: "huggingface"
url: "https://huggingface.co/datasets/fdemelo/ud-conll2017-aligned"
downloads: 119
summary: "UD CoNLL Shared Task 2017 기반 다국어 품사 태깅 및 형태소 주석 정렬 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[언어 모델링]]"
input_modality:
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# fdemelo/ud-conll2017-aligned

> dataset · [Hugging Face](https://huggingface.co/datasets/fdemelo/ud-conll2017-aligned)

UD CoNLL Shared Task 2017 기반 다국어 품사 태깅 및 형태소 주석 정렬 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `The processing aligns words and tokens along with their morphological annotations using the universal part-of-speech set for sequence-to-sequence task training.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `Text sentence` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `Sequence of universal POS tags` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `50 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `51` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual Parsing from Raw Text to Universal Dependencies.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a processed version of the dataset made available for the UD CoNLL Shared Task 2017` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 204자 ≈ 51 토큰 (viewer statistics, default/test)
