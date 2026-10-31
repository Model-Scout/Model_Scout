---
type: "dataset"
id: "FredZhang7/stable-diffusion-prompts-2.47M"
source: "huggingface"
url: "https://huggingface.co/datasets/FredZhang7/stable-diffusion-prompts-2.47M"
downloads: 282
summary: "Stable Diffusion 이미지 생성용 2.47M 텍스트 프롬프트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# FredZhang7/stable-diffusion-prompts-2.47M

> dataset · [Hugging Face](https://huggingface.co/datasets/FredZhang7/stable-diffusion-prompts-2.47M)

Stable Diffusion 이미지 생성용 2.47M 텍스트 프롬프트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Combined text-only dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `prompts = train["text"]` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `86` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `creativeml-openrail-m` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Combined text-only dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `train = dataset["train"]` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 346자 ≈ 86 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[llm-semantic-router__mmbert32k-modality-router-merged|llm-semantic-router/mmbert32k-modality-router-merged]]
- [[vllm-sr__mmbert32k-modality-router-merged|vllm-sr/mmbert32k-modality-router-merged]]
