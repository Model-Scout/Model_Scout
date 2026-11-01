---
type: "dataset"
id: "min9805/skb"
source: "huggingface"
url: "https://huggingface.co/datasets/min9805/skb"
downloads: 56
summary: "KLUE는 한국어 자연어처리 다양한 작업을 위한 전문가 생성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
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
# min9805/skb

> dataset · [Hugging Face](https://huggingface.co/datasets/min9805/skb)

KLUE는 한국어 자연어처리 다양한 작업을 위한 전문가 생성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories, task_ids = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_ids = `semantic-similarity-scoring` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · task_categories, task_ids = `token-classification` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories = `fill-mask` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:information_extraction, task:language_modeling, task:question_answering = `language:
- ko` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:question_answering = `task_categories:
- fill-mask
- question-answering
- text-classification
- text-generation
- token-classification` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `15` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `language:
- ko` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `annotations_creators:
- expert-generated` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `title` 열 p90 23자 ≈ 15 토큰 (viewer statistics, default/test)
