---
type: "dataset"
id: "huawei-noah/entity_cs"
source: "huggingface"
url: "https://huggingface.co/datasets/huawei-noah/entity_cs"
downloads: 318
summary: "EntityCS는 위키피디아와 위키데이터를 활용해 엔티티 기반 코드스위칭 말뭉치를 구축한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
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
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# huawei-noah/entity_cs

> dataset · [Hugging Face](https://huggingface.co/datasets/huawei-noah/entity_cs)

EntityCS는 위키피디아와 위키데이터를 활용해 엔티티 기반 코드스위칭 말뭉치를 구축한 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `In the paper we further fine-tune models on entity-centric downstream tasks, such as NER.` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `The dataset was developped for intermediate pre-training of language models.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:information_extraction, task:language_modeling = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:language_modeling = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `93 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `71` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `We use the English Wikipedia and leverage entity information from Wikidata to construct an entity-based Code Switching corpus.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset was developped for intermediate pre-training of language models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `cs_sentence` 열 p90 284자 ≈ 71 토큰 (viewer statistics, default/train)
