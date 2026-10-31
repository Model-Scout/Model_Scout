---
type: "dataset"
id: "wicho/kor_sae"
source: "huggingface"
url: "https://huggingface.co/datasets/wicho/kor_sae"
downloads: 168
summary: "한국어 비정형 지시문에서 의도 인자를 추출하는 데이터셋으로, 대화 시스템의 의도 추출에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# wicho/kor_sae

> dataset · [Hugging Face](https://huggingface.co/datasets/wicho/kor_sae)

한국어 비정형 지시문에서 의도 인자를 추출하는 데이터셋으로, 대화 시스템의 의도 추출에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories, task_ids = `text-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `The goal of this dataset is to extract the intent argument of a given utterance pair without a clear directive` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction = `The text in the dataset is in Korean` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The text in the dataset is in Korean and the associated is BCP-47 code is `ko-KR`` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
