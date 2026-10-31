---
type: "dataset"
id: "sentientfutures/animal-welfare-training-claude"
source: "huggingface"
url: "https://huggingface.co/datasets/sentientfutures/animal-welfare-training-claude"
downloads: 107
summary: "동물 복지와 감각 있는 존재의 복지에 대해 신중히 추론하도록 모델을 훈련하는 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# sentientfutures/animal-welfare-training-claude

> dataset · [Hugging Face](https://huggingface.co/datasets/sentientfutures/animal-welfare-training-claude)

동물 복지와 감각 있는 존재의 복지에 대해 신중히 추론하도록 모델을 훈련하는 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Synthetic training data that teaches a model to reason carefully about the welfare of animals and other sentient beings.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `An AI coaching users through ethical dilemmas involving disenfranchised third parties, such as animals` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3129` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Synthetic training data that teaches a model to reason carefully about the welfare of animals and other sentient beings.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Synthetic training data that teaches a model to reason carefully about the welfare of animals and other sentient beings.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 12517자 ≈ 3129 토큰 (viewer statistics, synthetic documents/train)
