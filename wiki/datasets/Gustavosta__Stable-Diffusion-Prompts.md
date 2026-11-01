---
type: "dataset"
id: "Gustavosta/Stable-Diffusion-Prompts"
source: "huggingface"
url: "https://huggingface.co/datasets/Gustavosta/Stable-Diffusion-Prompts"
downloads: 4160
summary: "Stable Diffusion 이미지 생성용 약 8만 개 프롬프트 데이터셋입니다."
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
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Gustavosta/Stable-Diffusion-Prompts

> dataset · [Hugging Face](https://huggingface.co/datasets/Gustavosta/Stable-Diffusion-Prompts)

Stable Diffusion 이미지 생성용 약 8만 개 프롬프트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Stable Diffusion Dataset` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `prompts filtered and extracted` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `prompts filtered and extracted` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `103` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This is a set of about 80,000 prompts filtered and extracted from the image finder for Stable Diffusion` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `Prompt` 열 p90 413자 ≈ 103 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[llm-semantic-router__mmbert32k-modality-router-merged|llm-semantic-router/mmbert32k-modality-router-merged]]
