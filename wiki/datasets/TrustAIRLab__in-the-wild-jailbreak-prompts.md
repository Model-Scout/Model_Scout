---
type: "dataset"
id: "TrustAIRLab/in-the-wild-jailbreak-prompts"
source: "huggingface"
url: "https://huggingface.co/datasets/TrustAIRLab/in-the-wild-jailbreak-prompts"
downloads: 4886
summary: "대규모 언어 모델의 탈옥 프롬프트를 수집·분석한 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# TrustAIRLab/in-the-wild-jailbreak-prompts

> dataset · [Hugging Face](https://huggingface.co/datasets/TrustAIRLab/in-the-wild-jailbreak-prompts)

대규모 언어 모델의 탈옥 프롬프트를 수집·분석한 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `To evaluate the effectiveness of jailbreak prompts, we construct a question set comprising 390 questions across 13 forbidden scenarios` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `15,140 prompts collected from December 2022 to December 2023` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `To evaluate the effectiveness of jailbreak prompts, we construct a question set comprising 390 questions across 13 forbidden scenarios` · 신뢰도 medium
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1068` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `In-The-Wild Jailbreak Prompts on LLMs` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `To evaluate the effectiveness of jailbreak prompts, we construct a question set comprising 390 questions across 13 forbidden scenarios` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `If you plan to use this dataset to train models, preprocessing the `prompt` field to remove duplicates is recommended.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 4272자 ≈ 1068 토큰 (viewer statistics, jailbreak_2023_05_07/train)

## 이 데이터로 학습한 모델

- [[Horizon-Labs__prompt-injection-guard-base|Horizon-Labs/prompt-injection-guard-base]]
- [[Horizon-Labs__prompt-injection-guard-large|Horizon-Labs/prompt-injection-guard-large]]
- [[Horizon-Labs__prompt-injection-guard-small|Horizon-Labs/prompt-injection-guard-small]]
