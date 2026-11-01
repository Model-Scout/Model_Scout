---
type: "dataset"
id: "fdnai/foundation_v0.1"
source: "huggingface"
url: "https://huggingface.co/datasets/fdnai/foundation_v0.1"
downloads: 566
summary: "101개 언어로 된 LLM 사전학습 전용 파운데이션 레이어 학습 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# fdnai/foundation_v0.1

> dataset · [Hugging Face](https://huggingface.co/datasets/fdnai/foundation_v0.1)

101개 언어로 된 LLM 사전학습 전용 파운데이션 레이어 학습 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `We offer foundation layer training data in 101 languages* to be used BEFORE pretraining.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `We offer foundation layer training data in 101 languages* to be used BEFORE pretraining.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `We offer foundation layer training data in 101 languages* to be used BEFORE pretraining.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `90 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1508` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `We offer foundation layer training data in 101 languages* to be used BEFORE pretraining.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `We offer foundation layer training data in 101 languages* to be used BEFORE pretraining.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 6032자 ≈ 1508 토큰 (viewer statistics, default/train)
