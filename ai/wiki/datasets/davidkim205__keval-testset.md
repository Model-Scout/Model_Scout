---
type: "dataset"
id: "davidkim205/keval-testset"
source: "huggingface"
url: "https://huggingface.co/datasets/davidkim205/keval-testset"
downloads: 10
summary: "keval 모델 학습 및 검증용 데이터셋으로, LLM 응답 평가 점수를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# davidkim205/keval-testset

> dataset · [Hugging Face](https://huggingface.co/datasets/davidkim205/keval-testset)

keval 모델 학습 및 검증용 데이터셋으로, LLM 응답 평가 점수를 포함함.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The keval model assigns scores to LLM-generated responses based on predefined evaluation criteria.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The score is an integer ranging from 0 to 10 and serves as the label for training the keval model.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The keval model follows the LLM-as-a-judge approach, which evaluates LLMs by assessing their responses to prompts from the ko-bench dataset.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The keval-testset is a dataset designed for training and validating the keval model.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
