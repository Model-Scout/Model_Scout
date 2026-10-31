---
type: "dataset"
id: "ai4privacy/pii-masking-openpii-1.5m"
source: "huggingface"
url: "https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m"
downloads: 3033
summary: "OpenPII 1.5M은 아시아 태평양 확장판을 포함한 다국어 개인정보 식별자(PII) 마스킹 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ai4privacy/pii-masking-openpii-1.5m

> dataset · [Hugging Face](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m)

OpenPII 1.5M은 아시아 태평양 확장판을 포함한 다국어 개인정보 식별자(PII) 마스킹 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · tags, task_categories = `token-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction = `Each example contains the original text, a masked version with labeled placeholders, span-level annotations, and pre-computed BIO token labels` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `masked version with labeled placeholders, span-level annotations, and pre-computed BIO token labels compatible with transformer-based models` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `30 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `170` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Built to advance open research in privacy-preserving NLP` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `masked_text` 열 p90 680자 ≈ 170 토큰 (viewer statistics, default/validation)

## 같은 데이터의 사본·중복 등록

- `woojin1069/pii-masking-openpii-1.5m`
