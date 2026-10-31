---
type: "dataset"
id: "mamahealth/mama-deid-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/mamahealth/mama-deid-dataset"
downloads: 126
summary: "22개 언어로 된 의료 문서 및 대화에서 개인정보를 익명화한 다국어 의료 비식별 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mamahealth/mama-deid-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/mamahealth/mama-deid-dataset)

22개 언어로 된 의료 문서 및 대화에서 개인정보를 익명화한 다국어 의료 비식별 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `Synthetic patient messages, short answers to app questions, documents (letters, reports, prescriptions, OCR output), longer posts and conversations` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `labelled for de-identification that keeps clinical context: identifiers are masked` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `250` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The training split includes 852 records of NVIDIA Nemotron-PII (CC BY 4.0), relabelled to this policy.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 999자 ≈ 250 토큰 (viewer statistics, default/validation)
