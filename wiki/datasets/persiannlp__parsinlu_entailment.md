---
type: "dataset"
id: "persiannlp/parsinlu_entailment"
source: "huggingface"
url: "https://huggingface.co/datasets/persiannlp/parsinlu_entailment"
downloads: 69
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[fa]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# persiannlp/parsinlu_entailment

> dataset · [Hugging Face](https://huggingface.co/datasets/persiannlp/parsinlu_entailment)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_ids = `natural-language-inference` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **언어**: [[fa]] — metadata · languages = `fa` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `53` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `sent1` 열 p90 213자 ≈ 53 토큰 (viewer statistics, parsinlu-repo/validation)

## 이 데이터로 학습한 모델

- [[Msobhi__Persian_Sentence_Embedding_v3|Msobhi/Persian_Sentence_Embedding_v3]]
