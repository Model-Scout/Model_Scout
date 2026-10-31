---
type: "dataset"
id: "Archangel-system/oasst2-openai-native"
source: "huggingface"
url: "https://huggingface.co/datasets/Archangel-system/oasst2-openai-native"
downloads: 71
summary: "26개 언어로 된 인간 대화 기반 다국어 SFT 및 DPO 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
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
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Archangel-system/oasst2-openai-native

> dataset · [Hugging Face](https://huggingface.co/datasets/Archangel-system/oasst2-openai-native)

26개 언어로 된 인간 대화 기반 다국어 SFT 및 DPO 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `preference optimisation (DPO, IPO, KTO, ORPO, reward modelling) on pairs that come from real human rankings` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:reranking = `JSONL is canonical. It retains native lists and objects` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `SFT row ends with `assistant`` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `57` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `human conversations from 2023` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `included `test` split is a reproducible held-out sample` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `SFT train contains 26 languages` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `meta` 열 p90 229자 ≈ 57 토큰 (viewer statistics, dpo/test)
