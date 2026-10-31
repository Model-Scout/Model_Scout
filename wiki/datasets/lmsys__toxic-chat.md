---
type: "dataset"
id: "lmsys/toxic-chat"
source: "huggingface"
url: "https://huggingface.co/datasets/lmsys/toxic-chat"
downloads: 10560
summary: "Vicuna 온라인 데모에서 수집한 10K 사용자 프롬프트의 독성 주석 데이터셋으로, 안전한 AI 상호작용 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lmsys/toxic-chat

> dataset · [Hugging Face](https://huggingface.co/datasets/lmsys/toxic-chat)

Vicuna 온라인 데모에서 수집한 10K 사용자 프롬프트의 독성 주석 데이터셋으로, 안전한 AI 상호작용 연구에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `This dataset contains toxicity annotations on 10K user prompts collected from the Vicuna online demo.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `This dataset contains toxicity annotations on 10K user prompts collected from the Vicuna online demo.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `432` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains toxicity annotations on 10K user prompts collected from the Vicuna online demo.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `We release an official T5-Large model trained on ToxicChat (toxicchat0124).` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `model_output` 열 p90 1729자 ≈ 432 토큰 (viewer statistics, toxicchat0124/test)

## 이 데이터로 학습한 모델

- [[Verm1ion__injection-sentry-xlmr|Verm1ion/injection-sentry-xlmr]]
