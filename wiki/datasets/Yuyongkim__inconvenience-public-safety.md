---
type: "dataset"
id: "Yuyongkim/inconvenience-public-safety"
source: "huggingface"
url: "https://huggingface.co/datasets/Yuyongkim/inconvenience-public-safety"
downloads: 84
summary: "한국 공공안전 관련 3개 등록부를 2017년 개정 규칙에 따라 점자로 변환한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Yuyongkim/inconvenience-public-safety

> dataset · [Hugging Face](https://huggingface.co/datasets/Yuyongkim/inconvenience-public-safety)

한국 공공안전 관련 3개 등록부를 2017년 개정 규칙에 따라 점자로 변환한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = ``text_chars`, `braille_cells` | lengths, for embosser planning` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = ``sections` is kept alongside `text` because the reading order is the part that carries judgement.` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:information_extraction, task:translation = `The registers are here because their documents are shaped differently` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = ``braille` | the whole record in Unicode braille` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2195` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `Three Korean public-safety registers converted to Korean braille under the 2017 revised rules (문화체육관광부 고시 제2017-15호).` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Every register is enumerated in full, not sampled.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `braille` 열 p90 3292자 ≈ 2195 토큰 (viewer statistics, drug_leaflet/train)
