---
type: "dataset"
id: "nateraw/parti-prompts"
source: "huggingface"
url: "https://huggingface.co/datasets/nateraw/parti-prompts"
downloads: 2483
summary: "PartiPrompts는 모델 능력 평가용 영어 프롬프트 1600개 이상 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
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
  - "[[소규모 데이터]]"
---
# nateraw/parti-prompts

> dataset · [Hugging Face](https://huggingface.co/datasets/nateraw/parti-prompts)

PartiPrompts는 모델 능력 평가용 영어 프롬프트 1600개 이상 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `P2 can be used to measure model capabilities across various categories and challenge aspects.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `over 1600 prompts in English` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `P2 can be used to measure model capabilities` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `25` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `PartiPrompts (P2) is a rich set of over 1600 prompts in English` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `P2 can be used to measure model capabilities` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `Prompt` 열 p90 101자 ≈ 25 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[llm-semantic-router__mmbert32k-modality-router-merged|llm-semantic-router/mmbert32k-modality-router-merged]]
- [[vllm-sr__mmbert32k-modality-router-merged|vllm-sr/mmbert32k-modality-router-merged]]
