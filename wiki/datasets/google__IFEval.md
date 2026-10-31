---
type: "dataset"
id: "google/IFEval"
source: "huggingface"
url: "https://huggingface.co/datasets/google/IFEval"
downloads: 156624
summary: "IFEval은 대형 언어 모델의 지시 수행 능력을 평가하기 위한 검증 가능한 지시문 약 500개를 포함한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# google/IFEval

> dataset · [Hugging Face](https://huggingface.co/datasets/google/IFEval)

IFEval은 대형 언어 모델의 지시 수행 능력을 평가하기 위한 검증 가능한 지시문 약 500개를 포함한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `It contains around 500 "verifiable instructions" such as "write in more than 400 words" and "mention the keyword of AI at least 3 times" which can be verified b` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `This dataset contains the prompts used in the Instruction-Following Eval (IFEval) benchmark` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `It contains around 500 "verifiable instructions" such as "write in more than 400 words" and "mention the keyword of AI at least 3 times" which can be verified b` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `91` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Instruction-Following Eval (IFEval) benchmark for large language models` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `The IFEval dataset is designed for evaluating chat or instruction fine-tuned language models` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 363자 ≈ 91 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[rico03__Qwopus-GLM-9B-DualReason-Distilled-GGUF|rico03/Qwopus-GLM-9B-DualReason-Distilled-GGUF]]
