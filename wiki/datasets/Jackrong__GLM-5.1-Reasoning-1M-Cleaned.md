---
type: "dataset"
id: "Jackrong/GLM-5.1-Reasoning-1M-Cleaned"
source: "huggingface"
url: "https://huggingface.co/datasets/Jackrong/GLM-5.1-Reasoning-1M-Cleaned"
downloads: 946
summary: "GLM-5.1-Reasoning-1M-Cleaned는 GLM-5.1 모델 기반의 추론 및 지식 추론용 정제 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
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
domain:
  - "[[학술·논문]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Jackrong/GLM-5.1-Reasoning-1M-Cleaned

> dataset · [Hugging Face](https://huggingface.co/datasets/Jackrong/GLM-5.1-Reasoning-1M-Cleaned)

GLM-5.1-Reasoning-1M-Cleaned는 GLM-5.1 모델 기반의 추론 및 지식 추론용 정제 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `multilingual STEM reasoning data, including Chinese, English, and other languages` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `10935` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `graduate-level physics, chemistry, and biology reasoning traces` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `general reasoning and instruction-following data` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `converting every example into a unified SFT-ready schema with explicit conversations, input, output, domain, and meta fields` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 43741자 ≈ 10935 토큰 (viewer statistics, main/train)

## 이 데이터로 학습한 모델

- [[Jackrong__Qwopus3.6-27B-v1-preview-GGUF|Jackrong/Qwopus3.6-27B-v1-preview-GGUF]]
- [[luckiness__Qwopus3.6-27B-v1-preview-GGUF|luckiness/Qwopus3.6-27B-v1-preview-GGUF]]
- [[mradermacher__Qwopus3.6-27B-v1-preview-GGUF|mradermacher/Qwopus3.6-27B-v1-preview-GGUF]]
- [[mradermacher__Qwopus3.6-27B-v1-preview-i1-GGUF|mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF]]
- [[rico03__Qwopus-GLM-9B-DualReason-Distilled-GGUF|rico03/Qwopus-GLM-9B-DualReason-Distilled-GGUF]]
