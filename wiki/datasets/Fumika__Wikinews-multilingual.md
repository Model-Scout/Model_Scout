---
type: "dataset"
id: "Fumika/Wikinews-multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/Fumika/Wikinews-multilingual"
downloads: 195
summary: "33개 언어로 된 15,200개 위키뉴스 기사 병렬 문장 데이터셋으로 다국어 뉴스 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
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
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Fumika/Wikinews-multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/Fumika/Wikinews-multilingual)

33개 언어로 된 15,200개 위키뉴스 기사 병렬 문장 데이터셋으로 다국어 뉴스 분석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `Weakly aligned multilingual pararell sentence datasets` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:retrieval = `titles and/or contents of the WikiNews pages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `news titles` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `33 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `20` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-2.5` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual WikiNews articles in 33 languages` · 신뢰도 low
- **도메인**: [[뉴스·미디어]] — ner · readme = `WikiNews articles` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Weakly aligned multilingual pararell sentence datasets` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `title` 열 p90 79자 ≈ 20 토큰 (viewer statistics, default/train)
