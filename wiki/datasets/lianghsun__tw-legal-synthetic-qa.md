---
type: "dataset"
id: "lianghsun/tw-legal-synthetic-qa"
source: "huggingface"
url: "https://huggingface.co/datasets/lianghsun/tw-legal-synthetic-qa"
downloads: 102
summary: "THUDM/chatglm3-6b-32k 모델과 판결문 데이터를 활용해 생성한 대만 법률 질의응답 합성 데이터셋입니다."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lianghsun/tw-legal-synthetic-qa

> dataset · [Hugging Face](https://huggingface.co/datasets/lianghsun/tw-legal-synthetic-qa)

THUDM/chatglm3-6b-32k 모델과 판결문 데이터를 활용해 생성한 대만 법률 질의응답 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `由實驗後的 prompt 去生成繁體中文法律對話合成集` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `由 user 發問了一個具有（或可能有）法律情境的問題` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `assistant 回答法律相關知識` · 신뢰도 medium
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `本資料集可以運用在 SFT，讓模型學會如何回答法律問題` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[QuantFactory__Llama-3.2-Taiwan-3B-Instruct-GGUF|QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF]]
