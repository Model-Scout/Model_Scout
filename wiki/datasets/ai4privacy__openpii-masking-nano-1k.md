---
type: "dataset"
id: "ai4privacy/openpii-masking-nano-1k"
source: "huggingface"
url: "https://huggingface.co/datasets/ai4privacy/openpii-masking-nano-1k"
downloads: 119
summary: "OpenPII Nano는 다국어 개인 식별 정보(PII) 마스킹을 위한 1,000개 샘플 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
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
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ai4privacy/openpii-masking-nano-1k

> dataset · [Hugging Face](https://huggingface.co/datasets/ai4privacy/openpii-masking-nano-1k)

OpenPII Nano는 다국어 개인 식별 정보(PII) 마스킹을 위한 1,000개 샘플 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `19 Labels` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:information_extraction = `JSONL` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `JSONL` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `30 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `156` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `perfect for quick prototyping, smoke tests, and CI fixtures.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `masked_text` 열 p90 625자 ≈ 156 토큰 (viewer statistics, default/validation)
