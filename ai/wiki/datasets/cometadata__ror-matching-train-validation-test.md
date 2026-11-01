---
type: "dataset"
id: "cometadata/ror-matching-train-validation-test"
source: "huggingface"
url: "https://huggingface.co/datasets/cometadata/ror-matching-train-validation-test"
downloads: 132
summary: "ROR 식별자와 매칭된 원시 저자 소속 문자열로 구성된 소속 매칭 학습 및 평가용 데이터셋입니다."
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
  - "[[학술·논문]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# cometadata/ror-matching-train-validation-test

> dataset · [Hugging Face](https://huggingface.co/datasets/cometadata/ror-matching-train-validation-test)

ROR 식별자와 매칭된 원시 저자 소속 문자열로 구성된 소속 매칭 학습 및 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `Raw author-affiliation strings paired with the ROR (Research Organization Registry) identifiers` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `ROR (Research Organization Registry) identifiers they should resolve to` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `39 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `35` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Raw author-affiliation strings paired with the ROR (Research Organization Registry) identifiers` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `prepared for training and evaluating affiliation matching and entity-linking systems` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `prepared for training and evaluating affiliation matching and entity-linking systems` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `affiliation_string` 열 p90 138자 ≈ 35 토큰 (viewer statistics, crossref/validation)
