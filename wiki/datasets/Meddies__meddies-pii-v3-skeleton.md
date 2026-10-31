---
type: "dataset"
id: "Meddies/meddies-pii-v3-skeleton"
source: "huggingface"
url: "https://huggingface.co/datasets/Meddies/meddies-pii-v3-skeleton"
downloads: 1370
summary: "다국어 합성 PII/PHI 학습용 타이핑 플레이스홀더 문서 스켈레톤 데이터셋입니다."
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
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Meddies/meddies-pii-v3-skeleton

> dataset · [Hugging Face](https://huggingface.co/datasets/Meddies/meddies-pii-v3-skeleton)

다국어 합성 PII/PHI 학습용 타이핑 플레이스홀더 문서 스켈레톤 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `Typed-placeholder document skeletons for multilingual synthetic PII/PHI training data.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction = `Typed-placeholder document skeletons` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Every PII-shaped slot is a `⟦label.subtype#id⟧` placeholder` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `20 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `Typed-placeholder document skeletons for multilingual synthetic PII/PHI training data.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `training data.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
