---
type: "dataset"
id: "lianghsun/tw-instruct"
source: "huggingface"
url: "https://huggingface.co/datasets/lianghsun/tw-instruct"
downloads: 21
summary: "臺灣語境의 대규모 합성 번체중문 지시문 대화 데이터셋으로, 다양한 작업 분류 포함."
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
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# lianghsun/tw-instruct

> dataset · [Hugging Face](https://huggingface.co/datasets/lianghsun/tw-instruct)

臺灣語境의 대규모 합성 번체중문 지시문 대화 데이터셋으로, 다양한 작업 분류 포함.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `每筆樣本含 `task` 欄位（任務類型，如「開放性問答」「摘要」「翻譯」等），方便下游做任務分流／取樣` · 신뢰도 low
- **작업**: [[텍스트 생성]] — tag_match · readme, tags = `chat` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `以 Llama-3.2-Taiwan 訓練語料中的繁中文本作為參考` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `每筆樣本含 task 類別、原始指令、對話與輸出` · 신뢰도 medium
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `繁中開源指令資料常缺乏「臺灣語境」的針對性設計，導致訓練後的模型「會講中文，但對臺灣不了解」` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `訓練具備臺灣語境之繁中對話模型。` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[QuantFactory__Llama-3.2-Taiwan-3B-Instruct-GGUF|QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF]]
