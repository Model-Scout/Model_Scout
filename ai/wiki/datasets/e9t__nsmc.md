---
type: "dataset"
id: "e9t/nsmc"
source: "huggingface"
url: "https://huggingface.co/datasets/e9t/nsmc"
downloads: 688
summary: "네이버 영화 리뷰로 구성된 한국어 영화 감성 분석 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# e9t/nsmc

> dataset · [Hugging Face](https://huggingface.co/datasets/e9t/nsmc)

네이버 영화 리뷰로 구성된 한국어 영화 감성 분석 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `This is a movie review dataset in the Korean language.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `This is a movie review dataset in the Korean language.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a movie review dataset in the Korean language.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset construction is based on the method noted in Large movie review dataset from Maas et al., 2011.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[cringepnh__koelectra-korean-sentiment|cringepnh/koelectra-korean-sentiment]]
- [[daekeun-ml__koelectra-small-v3-nsmc|daekeun-ml/koelectra-small-v3-nsmc]]
