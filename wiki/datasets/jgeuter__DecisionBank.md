---
type: "dataset"
id: "jgeuter/DecisionBank"
source: "huggingface"
url: "https://huggingface.co/datasets/jgeuter/DecisionBank"
downloads: 73
summary: "DecisionBank는 의사결정 모델 학습용 데이터셋으로, 상태, 질문, 선택지, 확률 타깃을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jgeuter/DecisionBank

> dataset · [Hugging Face](https://huggingface.co/datasets/jgeuter/DecisionBank)

DecisionBank는 의사결정 모델 학습용 데이터셋으로, 상태, 질문, 선택지, 확률 타깃을 포함합니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `multiple-choice` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `Each row has a state (text or JSON), a question, its options` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `a target, i.e. a probability for each option` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `946` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `public datasets such as CLINC, banking77, MNLI, BoolQ, ARC and MMLU's auxiliary training split` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training dataset for decision models.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `state` 열 p90 3783자 ≈ 946 토큰 (viewer statistics, DecisionBank-625k/train)
