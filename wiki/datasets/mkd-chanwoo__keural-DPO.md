---
type: "dataset"
id: "mkd-chanwoo/keural-DPO"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-chanwoo/keural-DPO"
downloads: 27
summary: "한국어와 영어 DPO 학습용 통합 데이터셋으로, 6개 소스에서 44만여 샘플을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
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
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mkd-chanwoo/keural-DPO

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-chanwoo/keural-DPO)

한국어와 영어 DPO 학습용 통합 데이터셋으로, 6개 소스에서 44만여 샘플을 포함합니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `한국어/영어 DPO(Direct Preference Optimization) 학습용 통합 데이터셋.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = ``prompt` 필드는 두 경로의 공통 시작점인 첫 번째 user 질문(Q1)만 저장합니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2675` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `한국어/영어 DPO(Direct Preference Optimization) 학습용 통합 데이터셋.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `chosen_chatml` 열 p90 4013자 ≈ 2675 토큰 (viewer statistics, default/train)
