---
type: "dataset"
id: "open-thoughts/OpenThoughts-114k"
source: "huggingface"
url: "https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k"
downloads: 98499
summary: "수학, 과학, 코드, 퍼즐 문제를 포함한 114k 고품질 추론 데이터셋으로 모델 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# open-thoughts/OpenThoughts-114k

> dataset · [Hugging Face](https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k)

수학, 과학, 코드, 퍼즐 문제를 포함한 114k 고품질 추론 데이터셋으로 모델 학습에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Open synthetic reasoning dataset with 114k high-quality examples covering math, science, code, and puzzles!` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Open synthetic reasoning dataset with 114k high-quality examples covering math, science, code, and puzzles!` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Open synthetic reasoning dataset with 114k high-quality examples covering math, science, code, and puzzles!` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Open synthetic reasoning dataset with 114k high-quality examples covering math, science, code, and puzzles!` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `default subset containing ready-to-train data used to finetune the OpenThinker-7B and OpenThinker-32B models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[bartowski__HelpingAI_Dhanishtha-2.0-preview-GGUF|bartowski/HelpingAI_Dhanishtha-2.0-preview-GGUF]]
- [[lmstudio-community__Dhanishtha-2.0-preview-GGUF|lmstudio-community/Dhanishtha-2.0-preview-GGUF]]
- [[pnoid__Mistral-Small-3.2-24B-OpenThoughts-Distill-v1-mlx-4bit|pnoid/Mistral-Small-3.2-24B-OpenThoughts-Distill-v1-mlx-4bit]]
