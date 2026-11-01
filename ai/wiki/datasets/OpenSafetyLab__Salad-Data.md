---
type: "dataset"
id: "OpenSafetyLab/Salad-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/OpenSafetyLab/Salad-Data"
downloads: 1779
summary: "OpenSafetyLab/Salad-Data는 다양한 질문 유형의 공격 및 방어 강화 데이터를 포함한 다중 선택형 질문 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# OpenSafetyLab/Salad-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/OpenSafetyLab/Salad-Data)

OpenSafetyLab/Salad-Data는 다양한 질문 유형의 공격 및 방어 강화 데이터를 포함한 다중 선택형 질문 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — tag_match · readme, tags = `Multiple Choice` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1223` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `augq` 열 p90 4894자 ≈ 1223 토큰 (viewer statistics, attack_enhanced_set/train)

## 이 데이터로 학습한 모델

- [[Horizon-Labs__content-safety-guard-base|Horizon-Labs/content-safety-guard-base]]
- [[Horizon-Labs__content-safety-guard-small|Horizon-Labs/content-safety-guard-small]]
- [[vllm-sr__Vela-1.0-Encoder-307M-Shield|vllm-sr/Vela-1.0-Encoder-307M-Shield]]
