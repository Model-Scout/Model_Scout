---
type: "dataset"
id: "AnHumorist/koucp-best-articles-with-contribs"
source: "huggingface"
url: "https://huggingface.co/datasets/AnHumorist/koucp-best-articles-with-contribs"
downloads: 16
summary: "한국어 유머 감각 학습을 위한 백괴사전 특집 기사 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[음성 합성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# AnHumorist/koucp-best-articles-with-contribs

> dataset · [Hugging Face](https://huggingface.co/datasets/AnHumorist/koucp-best-articles-with-contribs)

한국어 유머 감각 학습을 위한 백괴사전 특집 기사 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `sentence-similarity` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `One of the top online dataset for training Korean sense of humo(u)r from the Korean Uncyclopedia (a.k.a. Koucp, 백괴사전, baekgwaesajeon).` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:language_modeling, task:text_to_speech = `One of the top online dataset for training Korean sense of humo(u)r from the Korean Uncyclopedia (a.k.a. Koucp, 백괴사전, baekgwaesajeon).` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `One of the top online dataset for training Korean sense of humo(u)r from the Korean Uncyclopedia (a.k.a. Koucp, 백괴사전, baekgwaesajeon).` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `One of the top online dataset for training Korean sense of humo(u)r from the Korean Uncyclopedia (a.k.a. Koucp, 백괴사전, baekgwaesajeon).` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `One of the top online dataset for training Korean sense of humo(u)r from the Korean Uncyclopedia (a.k.a. Koucp, 백괴사전, baekgwaesajeon).` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
