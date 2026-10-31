---
type: "dataset"
id: "lianghsun/tw-contract-review-chat"
source: "huggingface"
url: "https://huggingface.co/datasets/lianghsun/tw-contract-review-chat"
downloads: 11
summary: "tw-contract-review-chat는 대만 계약 심사 실무 관련 전통 중국어 단일 질문-답변 데이터셋으로, 법률 분야 언어 모델 미세조정에 적합하다."
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
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lianghsun/tw-contract-review-chat

> dataset · [Hugging Face](https://huggingface.co/datasets/lianghsun/tw-contract-review-chat)

tw-contract-review-chat는 대만 계약 심사 실무 관련 전통 중국어 단일 질문-답변 데이터셋으로, 법률 분야 언어 모델 미세조정에 적합하다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `使模型能回答契約審閱相關問題` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `適用於語言模型之法律領域指令微調` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[QuantFactory__Llama-3.2-Taiwan-3B-Instruct-GGUF|QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF]]
