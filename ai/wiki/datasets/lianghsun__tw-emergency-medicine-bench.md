---
type: "dataset"
id: "lianghsun/tw-emergency-medicine-bench"
source: "huggingface"
url: "https://huggingface.co/datasets/lianghsun/tw-emergency-medicine-bench"
downloads: 69
summary: "台灣衛生福利部急診醫學科專科醫師甄審筆試題庫 기반의繁體中文醫學多選題評測資料集입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lianghsun/tw-emergency-medicine-bench

> dataset · [Hugging Face](https://huggingface.co/datasets/lianghsun/tw-emergency-medicine-bench)

台灣衛生福利部急診醫學科專科醫師甄審筆試題庫 기반의繁體中文醫學多選題評測資料集입니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `multiple-choice` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `資料採 Formosa-bench 評測集之欄位格式（question / A / B / C / D / E / answer）` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `資料採 Formosa-bench 評測集之欄位格式（question / A / B / C / D / E / answer）` · 신뢰도 medium
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `38` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `可直接用於語言模型之 zero-shot 或 few-shot 多選題評測。` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 151자 ≈ 38 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[QuantFactory__Llama-3.2-Taiwan-3B-Instruct-GGUF|QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF]]
