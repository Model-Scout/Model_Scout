---
type: "dataset"
id: "llami-team/Korean-OpenThoughts-114k-Normalized"
source: "huggingface"
url: "https://huggingface.co/datasets/llami-team/Korean-OpenThoughts-114k-Normalized"
downloads: 158
summary: "OpenThoughts-114k-Normalized의 한국어 번역본으로, 한국어 추론 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# llami-team/Korean-OpenThoughts-114k-Normalized

> dataset · [Hugging Face](https://huggingface.co/datasets/llami-team/Korean-OpenThoughts-114k-Normalized)

OpenThoughts-114k-Normalized의 한국어 번역본으로, 한국어 추론 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `question: 질문` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `question: 질문` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `18670` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 reasoning 모델 distillation` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `reasoning` 열 p90 28005자 ≈ 18670 토큰 (viewer statistics, default/train)
