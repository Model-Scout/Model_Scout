---
type: "dataset"
id: "danielberanek/manifest-digital-identity-optimization"
source: "huggingface"
url: "https://huggingface.co/datasets/danielberanek/manifest-digital-identity-optimization"
downloads: 214
summary: "디지털 아이덴티티 최적화 매니페스트와 온톨로지를 다국어로 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
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
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# danielberanek/manifest-digital-identity-optimization

> dataset · [Hugging Face](https://huggingface.co/datasets/danielberanek/manifest-digital-identity-optimization)

디지털 아이덴티티 최적화 매니페스트와 온톨로지를 다국어로 제공하는 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Parquet/viewer vrstva může být i přesto užitečná pro lehký náhled, textové experimenty nebo obecný programový přístup` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:generation, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `18` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `This dataset serves as an additional discovery, access, and reuse point for developers, researchers, practitioners, and readers` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 71자 ≈ 18 토큰 (viewer statistics, default/train)
