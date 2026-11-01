---
type: "dataset"
id: "jhu-clsp/bernice-pretrain-data"
source: "huggingface"
url: "https://huggingface.co/datasets/jhu-clsp/bernice-pretrain-data"
downloads: 106
summary: "다국어 트윗 ID 25억 건으로 구성된 Bernice 트위터 인코더 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# jhu-clsp/bernice-pretrain-data

> dataset · [Hugging Face](https://huggingface.co/datasets/jhu-clsp/bernice-pretrain-data)

다국어 트윗 ID 25억 건으로 구성된 Bernice 트위터 인코더 학습용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `used to train Bernice, a Twitter encoder` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding = `Tweet IDs for the 2.5 billion multilingual tweets` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Tweet IDs for the 2.5 billion multilingual tweets` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `65 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual tweets` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `used to train Bernice, a Twitter encoder` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high
