---
type: "dataset"
id: "agentlans/refusal-classifier-data"
source: "huggingface"
url: "https://huggingface.co/datasets/agentlans/refusal-classifier-data"
downloads: 57
summary: "agentlans/refusal-classifier-data는 거절 분류기 학습용 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# agentlans/refusal-classifier-data

> dataset · [Hugging Face](https://huggingface.co/datasets/agentlans/refusal-classifier-data)

agentlans/refusal-classifier-data는 거절 분류기 학습용 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Refusal Classifier Training Data` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `All conversations have been formatted using role tokens and ellipses` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Refusal Classifier Training Data` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `37 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `934` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The resulting files are shuffled and split 80% training, 20% testing.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `input` 열 p90 3735자 ≈ 934 토큰 (viewer statistics, english_only/test)

## 이 데이터로 학습한 모델

- [[agentlans__multilingual-e5-small-refusal-classifier|agentlans/multilingual-e5-small-refusal-classifier]]
