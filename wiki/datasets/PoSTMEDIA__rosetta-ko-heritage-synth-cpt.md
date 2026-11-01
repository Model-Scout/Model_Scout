---
type: "dataset"
id: "PoSTMEDIA/rosetta-ko-heritage-synth-cpt"
source: "huggingface"
url: "https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-heritage-synth-cpt"
downloads: 11
summary: "한국 공공 문화유산 기록 기반의 정제된 CPT 말뭉치 및 QA/선호/RLVR 세트 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# PoSTMEDIA/rosetta-ko-heritage-synth-cpt

> dataset · [Hugging Face](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-heritage-synth-cpt)

한국 공공 문화유산 기록 기반의 정제된 CPT 말뭉치 및 QA/선호/RLVR 세트 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `cleaned CPT corpus plus source-grounded QA/preference/RLVR sets` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `source-grounded QA/preference/RLVR sets` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:question_answering = `cleaned Korean source-unit body (continued-pretraining input)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:question_answering = `cleaned CPT corpus plus source-grounded QA/preference/RLVR sets` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — tag_match · readme, tags = `culture` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `continued-pretraining corpus (plain `text`)` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
