---
type: "dataset"
id: "Jackrong/Kimi-K2.5-Reasoning-1M-Cleaned"
source: "huggingface"
url: "https://huggingface.co/datasets/Jackrong/Kimi-K2.5-Reasoning-1M-Cleaned"
downloads: 572
summary: "Kimi-K2.5-Reasoning-1M-Cleaned는 ianncity/KIMI-K2.5-1000000x를 정제해 추론 학습용으로 재구성한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[중국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Jackrong/Kimi-K2.5-Reasoning-1M-Cleaned

> dataset · [Hugging Face](https://huggingface.co/datasets/Jackrong/Kimi-K2.5-Reasoning-1M-Cleaned)

Kimi-K2.5-Reasoning-1M-Cleaned는 ianncity/KIMI-K2.5-1000000x를 정제해 추론 학습용으로 재구성한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `6041` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `training-ready schema and removes records with quality issues` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 24166자 ≈ 6041 토큰 (viewer statistics, General-Distillation/train)

## 이 데이터로 학습한 모델

- [[Jackrong__Qwopus3.6-27B-v1-preview-GGUF|Jackrong/Qwopus3.6-27B-v1-preview-GGUF]]
- [[luckiness__Qwopus3.6-27B-v1-preview-GGUF|luckiness/Qwopus3.6-27B-v1-preview-GGUF]]
- [[mradermacher__Qwopus3.6-27B-v1-preview-GGUF|mradermacher/Qwopus3.6-27B-v1-preview-GGUF]]
- [[mradermacher__Qwopus3.6-27B-v1-preview-i1-GGUF|mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF]]
