---
type: "dataset"
id: "pankajmathur/OpenThoughts-Agent-v1-SFT-cleaned"
source: "huggingface"
url: "https://huggingface.co/datasets/pankajmathur/OpenThoughts-Agent-v1-SFT-cleaned"
downloads: 25
summary: "OpenThoughts-Agent-v1-SFT는 에이전트 학습용 SFT 데이터셋으로, 터미널 명령어 및 버그 수정 작업에 활용됩니다."
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# pankajmathur/OpenThoughts-Agent-v1-SFT-cleaned

> dataset · [Hugging Face](https://huggingface.co/datasets/pankajmathur/OpenThoughts-Agent-v1-SFT-cleaned)

OpenThoughts-Agent-v1-SFT는 에이전트 학습용 SFT 데이터셋으로, 터미널 명령어 및 버그 수정 작업에 활용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `OpenThinker-Agent-v1 is a model trained for agentic tasks such as Terminal-Bench 2.0 and SWE-Bench.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `7` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `OpenThoughts-Agent is an open-source effort to curate the best datasets for training agents.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `It is SFT-ed on the OpenThoughts-Agent-v1-SFT dataset` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `trial_name` 열 p90 27자 ≈ 7 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[pankajmathur__RenCoder-Ministral-8B-Instruct-2410-GGUF|pankajmathur/RenCoder-Ministral-8B-Instruct-2410-GGUF]]
