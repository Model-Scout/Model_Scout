---
type: "dataset"
id: "lianghsun/reasoning-base-20k-chat"
source: "huggingface"
url: "https://huggingface.co/datasets/lianghsun/reasoning-base-20k-chat"
downloads: 12
summary: "reasoning-base-20k-chat은 수학, 논리 추론 중심의 번체중문 추론 QA 데이터셋으로 언어모델 미세조정에 적합하다."
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
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lianghsun/reasoning-base-20k-chat

> dataset · [Hugging Face](https://huggingface.co/datasets/lianghsun/reasoning-base-20k-chat)

reasoning-base-20k-chat은 수학, 논리 추론 중심의 번체중문 추론 QA 데이터셋으로 언어모델 미세조정에 적합하다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `繁體中文推理問答資料集，包含 1,881 筆單輪問答對` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `將推理任務轉化為繁體中文問答格式` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `每筆回答均以逐步推理（step-by-step reasoning）方式呈現` · 신뢰도 medium
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `其他 STEM 主題： 物理、統計、演算法` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[QuantFactory__Llama-3.2-Taiwan-3B-Instruct-GGUF|QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF]]
