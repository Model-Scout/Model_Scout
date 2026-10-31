---
type: "dataset"
id: "lianghsun/tw-law-article-chat"
source: "huggingface"
url: "https://huggingface.co/datasets/lianghsun/tw-law-article-chat"
downloads: 15
summary: "중화민국 대만 법규 조문을 기반으로 한 법률 질의응답 데이터셋으로 법규 조회 및 해석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[리랭킹]]"
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
dataset_size:
  - "[[소규모 데이터]]"
---
# lianghsun/tw-law-article-chat

> dataset · [Hugging Face](https://huggingface.co/datasets/lianghsun/tw-law-article-chat)

중화민국 대만 법규 조문을 기반으로 한 법률 질의응답 데이터셋으로 법규 조회 및 해석에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[리랭킹]] — ner · readme = `並附帶 DPO（Direct Preference Optimization）所需的 chosen/rejected 回答對，可同時用於 SFT 與偏好對齊訓練` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:reranking = `tw-law-article-qa 是一個以中華民國法規條文為核心的繁體中文法律問答資料集` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `提供條文內容、法規背景資料與實務解釋` · 신뢰도 medium
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `並附帶 DPO（Direct Preference Optimization）所需的 chosen/rejected 回答對，可同時用於 SFT 與偏好對齊訓練` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[QuantFactory__Llama-3.2-Taiwan-3B-Instruct-GGUF|QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF]]
