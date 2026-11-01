---
type: "dataset"
id: "qanastek/MASSIVE"
source: "huggingface"
url: "https://huggingface.co/datasets/qanastek/MASSIVE"
downloads: 1305
summary: "51개 언어로 된 100만 개 이상의 발화 데이터로 의도 예측과 슬롯 주석을 위한 다국어 자연어 이해 데이터셋입니다."
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
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# qanastek/MASSIVE

> dataset · [Hugging Face](https://huggingface.co/datasets/qanastek/MASSIVE)

51개 언어로 된 100만 개 이상의 발화 데이터로 의도 예측과 슬롯 주석을 위한 다국어 자연어 이해 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **작업**: [[정보 추출]] — metadata · task_ids = `named-entity-recognition` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction = ``utt`: the raw utterance text without annotations` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `annotations for the Natural Language Understanding tasks of intent prediction and slot annotation` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `50 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MASSIVE is a parallel dataset of > 1M utterances across 51 languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = ``partition`: is either `train`, `dev`, or `test`, according to the original split in [SLURP]` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
