---
type: "dataset"
id: "wicho/kor_3i4k"
source: "huggingface"
url: "https://huggingface.co/datasets/wicho/kor_3i4k"
downloads: 326
summary: "3i4K는 한국어 음성 발화의 화자 의도를 분류하기 위한 데이터셋입니다."
readme_status: "ok"
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
# wicho/kor_3i4k

> dataset · [Hugging Face](https://huggingface.co/datasets/wicho/kor_3i4k)

3i4K는 한국어 음성 발화의 화자 의도를 분류하기 위한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `based on its transcript` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The classification system decides whether the utterance is a fragment, statement, question, command, rhetorical question, rhetorical command, or an intonation-d` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `20` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The text in the dataset is in Korean` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `a test set of 6121 examples` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The data is split into a training set comrpised of 55134 examples` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 30자 ≈ 20 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[bespin-global__klue-roberta-small-3i4k-intent-classification|bespin-global/klue-roberta-small-3i4k-intent-classification]]
