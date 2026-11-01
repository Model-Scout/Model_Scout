---
type: "dataset"
id: "clzoro/Claude-Distills"
source: "huggingface"
url: "https://huggingface.co/datasets/clzoro/Claude-Distills"
downloads: 301
summary: "Claude 모델 증류용으로 통합 및 중복 제거된 오픈소스 데이터셋 모음입니다."
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# clzoro/Claude-Distills

> dataset · [Hugging Face](https://huggingface.co/datasets/clzoro/Claude-Distills)

Claude 모델 증류용으로 통합 및 중복 제거된 오픈소스 데이터셋 모음입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Converted all data sources to a consistent `messages` format with `source` field` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Assistant responses include thinking process using special tokens to mark the thinking section, followed by the final answer.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Claude Sonnet 4.6 general, code, math, psychology data` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset is for research and educational purposes only.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Jackrong__Qwopus3.6-27B-v1-preview-GGUF|Jackrong/Qwopus3.6-27B-v1-preview-GGUF]]
- [[luckiness__Qwopus3.6-27B-v1-preview-GGUF|luckiness/Qwopus3.6-27B-v1-preview-GGUF]]
- [[mradermacher__Qwopus3.6-27B-v1-preview-GGUF|mradermacher/Qwopus3.6-27B-v1-preview-GGUF]]
- [[mradermacher__Qwopus3.6-27B-v1-preview-i1-GGUF|mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF]]
