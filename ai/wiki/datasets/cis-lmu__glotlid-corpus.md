---
type: "dataset"
id: "cis-lmu/glotlid-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/cis-lmu/glotlid-corpus"
downloads: 388
summary: "GlotLID 모델 학습용 언어 식별 데이터셋으로 약 2000개 언어 분류 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# cis-lmu/glotlid-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/cis-lmu/glotlid-corpus)

GlotLID 모델 학습용 언어 식별 데이터셋으로 약 2000개 언어 분류 가능

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `a language identification model capable of classifying ~2000 labels` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `In each language folder, you will find `.txt` files` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `a language identification model capable of classifying ~2000 labels` · 신뢰도 low
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a language identification model capable of classifying ~2000 labels` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This is the corpus used to train the open GlotLID model` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[cis-lmu__glotlid|cis-lmu/glotlid]]
