---
type: "dataset"
id: "HumanLLMs/Human-Like-DPO-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/HumanLLMs/Human-Like-DPO-Dataset"
downloads: 822
summary: "대화형 대규모 언어 모델의 인간 같은 응답 생성을 위한 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# HumanLLMs/Human-Like-DPO-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/HumanLLMs/Human-Like-DPO-Dataset)

대화형 대규모 언어 모델의 인간 같은 응답 생성을 위한 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `improving conversational fluency and engagement in large language models` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `521` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `llama3` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset can be used to fine-tune LLMs` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 2085자 ≈ 521 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[mradermacher__Human-Like-Qwen2.5-1.5B-Instruct-GGUF|mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-GGUF]]
- [[mradermacher__Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF|mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF]]
