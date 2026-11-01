---
type: "dataset"
id: "Wismut/nym-pii-multilingual-data"
source: "huggingface"
url: "https://huggingface.co/datasets/Wismut/nym-pii-multilingual-data"
downloads: 480
summary: "23개 언어, 6개 문자로 구성된 합성 PII 토큰 분류 데이터로 PII 탐지 모델 학습용입니다."
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Wismut/nym-pii-multilingual-data

> dataset · [Hugging Face](https://huggingface.co/datasets/Wismut/nym-pii-multilingual-data)

23개 언어, 6개 문자로 구성된 합성 PII 토큰 분류 데이터로 PII 탐지 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `40 entity types (names, DOB, contact, addresses, government/medical/financial IDs, credentials, network identifiers, …)` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `JSONL with character-offset spans (offsets index into text as UTF-8` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `exactly-labeled PII token-classification examples` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `120` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `~23 languages and 6 scripts` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `built for training nym's PII detection models` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 480자 ≈ 120 토큰 (viewer statistics, default/validation)
