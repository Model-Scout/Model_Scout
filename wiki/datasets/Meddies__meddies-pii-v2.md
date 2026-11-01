---
type: "dataset"
id: "Meddies/meddies-pii-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/Meddies/meddies-pii-v2"
downloads: 155
summary: "17개 언어와 9개 엔티티 유형의 다국어 임상 개인정보(PII) 식별 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Meddies/meddies-pii-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/Meddies/meddies-pii-v2)

17개 언어와 9개 엔티티 유형의 다국어 임상 개인정보(PII) 식별 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The nine labels are `address`, `company_name`, `date`, `email_address`, `human_name`, `id_number`, `phone_number`, `private_url`, and `secret`.` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `Character-level PII annotations` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Training code derives BIOES tags later without changing the original text or boundaries.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `three evaluation configs` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `17 language-specific training configs` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
