---
type: "dataset"
id: "TeichAI/claude-haiku-4.5-high-reasoning-1700x"
source: "huggingface"
url: "https://huggingface.co/datasets/TeichAI/claude-haiku-4.5-high-reasoning-1700x"
downloads: 67
summary: "Claude Haiku 4.5 기반 고난도 추론 데이터셋으로 LLM 미세조정용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# TeichAI/claude-haiku-4.5-high-reasoning-1700x

> dataset · [Hugging Face](https://huggingface.co/datasets/TeichAI/claude-haiku-4.5-high-reasoning-1700x)

Claude Haiku 4.5 기반 고난도 추론 데이터셋으로 LLM 미세조정용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `The dataset is meant for creating distilled versions of Claude Haiku 4.5 by fine-tuning already existing open-source LLMs.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Total tokens (input + output): 6.79 M` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Total tokens (input + output): 6.79 M` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset is meant for creating distilled versions of Claude Haiku 4.5 by fine-tuning already existing open-source LLMs.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[DavidAU__Llama-3.3-8B-Instruct-Thinking-Claude-Haiku-4.5-High-Reasoning-1700x|DavidAU/Llama-3.3-8B-Instruct-Thinking-Claude-Haiku-4.5-High-Reasoning-1700x]]
