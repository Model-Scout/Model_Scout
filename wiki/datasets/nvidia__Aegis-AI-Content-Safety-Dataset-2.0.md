---
type: "dataset"
id: "nvidia/Aegis-AI-Content-Safety-Dataset-2.0"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0"
downloads: 16014
summary: "인간과 LLM 간 상호작용의 안전성 평가를 위한 AI 콘텐츠 안전 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
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
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nvidia/Aegis-AI-Content-Safety-Dataset-2.0

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0)

인간과 LLM 간 상호작용의 안전성 평가를 위한 AI 콘텐츠 안전 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `Response safety labels generated using ensemble of 3 LLMs` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding = `user prompts, user prompts and LLM response single turn, user prompts and LLM response muliple turns` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Overall content safety labels for the conversation` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `224` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `1,964 test samples` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `30,007 training samples` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 896자 ≈ 224 토큰 (viewer statistics, default/validation)
