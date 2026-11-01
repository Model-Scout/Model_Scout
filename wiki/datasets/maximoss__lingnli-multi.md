---
type: "dataset"
id: "maximoss/lingnli-multi"
source: "huggingface"
url: "https://huggingface.co/datasets/maximoss/lingnli-multi"
downloads: 238
summary: "LingNLI 데이터셋을 9개 언어로 기계 번역한 자연어 추론(NLI) 분류용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[bg]]"
  - "[[el]]"
  - "[[es]]"
  - "[[fi]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[lt]]"
  - "[[다국어]]"
  - "[[pt]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# maximoss/lingnli-multi

> dataset · [Hugging Face](https://huggingface.co/datasets/maximoss/lingnli-multi)

LingNLI 데이터셋을 9개 언어로 기계 번역한 자연어 추론(NLI) 분류용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `given two sentences` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The goal is to predict textual entailment (does sentence A imply/contradict/neither sentence B), which is a classification task` · 신뢰도 low
- **언어**: [[bg]] — metadata · languages = `bg` · 신뢰도 high
- **언어**: [[el]] — metadata · languages = `el` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fi]] — metadata · languages = `fi` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[lt]] — metadata · languages = `lt` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `57` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `bsd-2-clause` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This repository contains a collection of machine translations of LingNLI dataset into 9 different languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `validation` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `For the whole dataset (LitL and LotS subsets):` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `premise` 열 p90 228자 ≈ 57 토큰 (viewer statistics, default/validation)
