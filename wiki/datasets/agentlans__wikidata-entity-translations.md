---
type: "dataset"
id: "agentlans/wikidata-entity-translations"
source: "huggingface"
url: "https://huggingface.co/datasets/agentlans/wikidata-entity-translations"
downloads: 31
summary: "위키데이터 엔티티 번역 데이터셋으로 다국어 번역 학습에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
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
  - "[[대규모 데이터]]"
---
# agentlans/wikidata-entity-translations

> dataset · [Hugging Face](https://huggingface.co/datasets/agentlans/wikidata-entity-translations)

위키데이터 엔티티 번역 데이터셋으로 다국어 번역 학습에 활용됨

## 분류

- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `language:
- en
- ar
- de
- es
- fr
- hi
- it
- ja
- ko
- nl
- pt
- ru
- tr
- zh` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `language:
- en
- ar
- de
- es
- fr
- hi
- it
- ja
- ko
- nl
- pt
- ru
- tr
- zh` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `12` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `split: train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `en` 열 p90 48자 ≈ 12 토큰 (viewer statistics, en-ko/train)
