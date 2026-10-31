---
type: "dataset"
id: "akaruineko/privaset"
source: "huggingface"
url: "https://huggingface.co/datasets/akaruineko/privaset"
downloads: 78
summary: "PRIVAset는 25개 언어의 개인정보(PII) 탐지용 합성 데이터셋으로 분류, 개체명 인식, 가림 작업에 활용됩니다."
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
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# akaruineko/privaset

> dataset · [Hugging Face](https://huggingface.co/datasets/akaruineko/privaset)

PRIVAset는 25개 언어의 개인정보(PII) 탐지용 합성 데이터셋으로 분류, 개체명 인식, 가림 작업에 활용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `designed for tasks such as classification, named-entity recognition (NER), and redaction` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `designed for tasks such as classification, named-entity recognition (NER), and redaction` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `All data is generated using Faker (locale-aware) and custom synthetic logic.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `replace spans with `[REDACTED_{TYPE}]`` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `25 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `28` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `PRIVAset is a large-scale, privacy-safe, synthetic dataset for training and evaluating Personally Identifiable Information (PII) filtering systems.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `making it safe for public release, model fine-tuning, and benchmarking.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `making it safe for public release, model fine-tuning, and benchmarking.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 111자 ≈ 28 토큰 (viewer statistics, default/validation)
