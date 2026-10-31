---
type: "dataset"
id: "bzantium/korean-jev-decision-index"
source: "huggingface"
url: "https://huggingface.co/datasets/bzantium/korean-jev-decision-index"
downloads: 189
summary: "한국어로 된 의사결정 모델 평가용 벤치마크 데이터셋으로, 다양한 영역의 질문에 대한 답변 확률, 예/아니오 판단, 평점을 예측하는 데 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# bzantium/korean-jev-decision-index

> dataset · [Hugging Face](https://huggingface.co/datasets/bzantium/korean-jev-decision-index)

한국어로 된 의사결정 모델 평가용 벤치마크 데이터셋으로, 다양한 영역의 질문에 대한 답변 확률, 예/아니오 판단, 평점을 예측하는 데 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Given a state and a question, models predict probabilities over answer choices, yes/no judgments, or ratings.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Given a state and a question` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `models predict probabilities over answer choices, yes/no judgments, or ratings.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1439` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A Korean benchmark for decision models.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `82,452 evaluation requests across five areas` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `sample` 열 p90 2158자 ≈ 1439 토큰 (viewer statistics, default/test)
