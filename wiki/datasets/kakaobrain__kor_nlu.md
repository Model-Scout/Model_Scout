---
type: "dataset"
id: "kakaobrain/kor_nlu"
source: "huggingface"
url: "https://huggingface.co/datasets/kakaobrain/kor_nlu"
downloads: 189
readme_status: "template"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kakaobrain/kor_nlu

> dataset · [Hugging Face](https://huggingface.co/datasets/kakaobrain/kor_nlu)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories, task_ids = `text-classification` · 신뢰도 high
- **작업**: [[임베딩]] — metadata · task_ids = `semantic-similarity-scoring` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[bespin-global__klue-sentence-roberta-base-kornlu|bespin-global/klue-sentence-roberta-base-kornlu]]
- [[snumin44__simcse-ko-bert-supervised|snumin44/simcse-ko-bert-supervised]]
- [[snumin44__simcse-ko-roberta-supervised|snumin44/simcse-ko-roberta-supervised]]
- [[snumin44__simcse-ko-roberta-unsupervised|snumin44/simcse-ko-roberta-unsupervised]]
