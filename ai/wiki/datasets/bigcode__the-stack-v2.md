---
type: "dataset"
id: "bigcode/the-stack-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/bigcode/the-stack-v2"
downloads: 10822
summary: "The Stack v2는 600개 이상의 프로그래밍 언어로 구성된 대규모 코드 데이터셋으로, 코드 생성 AI 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[code]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# bigcode/the-stack-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/bigcode/the-stack-v2)

The Stack v2는 600개 이상의 프로그래밍 언어로 구성된 대규모 코드 데이터셋으로, 코드 생성 AI 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `The Stack serves as a pre-training dataset for Code LLMs, i.e., code-generating AI systems` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `The Stack v2 contains over 3B files in 600+ programming and markup languages.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `The Stack serves as a pre-training dataset for Code LLMs, i.e., code-generating AI systems which enable the synthesis of programs from natural language descript` · 신뢰도 medium
- **언어**: [[code]] — metadata · languages = `code` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Stack v2 contains over 3B files in 600+ programming and markup languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset has no splits and all data is loaded as train split by default.` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[PsycheFoundation__consilience-40b-7Y9v38s5|PsycheFoundation/consilience-40b-7Y9v38s5]]
