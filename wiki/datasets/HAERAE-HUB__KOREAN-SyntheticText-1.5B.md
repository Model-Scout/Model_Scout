---
type: "dataset"
id: "HAERAE-HUB/KOREAN-SyntheticText-1.5B"
source: "huggingface"
url: "https://huggingface.co/datasets/HAERAE-HUB/KOREAN-SyntheticText-1.5B"
downloads: 93
summary: "KOREAN-SyntheticText는 1.4B 토큰의 한국어 합성 텍스트 데이터셋으로 텍스트 생성에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# HAERAE-HUB/KOREAN-SyntheticText-1.5B

> dataset · [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/KOREAN-SyntheticText-1.5B)

KOREAN-SyntheticText는 1.4B 토큰의 한국어 합성 텍스트 데이터셋으로 텍스트 생성에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `fine-tuned on text generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `fine-tuned on text generation` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `fine-tuned on text generation` · 신뢰도 medium
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `799` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `generated using a 100B + open-source LLM fine-tuned on text generation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 3196자 ≈ 799 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[FINAL-Bench__Aether-7B-5Attn|FINAL-Bench/Aether-7B-5Attn]]
- [[FINAL-Bench__Aether-7B-5Attn-it|FINAL-Bench/Aether-7B-5Attn-it]]
