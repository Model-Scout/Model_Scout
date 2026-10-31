---
type: "dataset"
id: "CohereLabs/fusion-synth-data-ufb"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabs/fusion-synth-data-ufb"
downloads: 185
summary: "다섯 개 교사 모델의 완성문을 포함한 10,000개 UFB 프롬프트의 합성 데이터로, 모델 학습과 평가에 활용됨."
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
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# CohereLabs/fusion-synth-data-ufb

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabs/fusion-synth-data-ufb)

다섯 개 교사 모델의 완성문을 포함한 10,000개 UFB 프롬프트의 합성 데이터로, 모델 학습과 평가에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `the 5 teachers completions are ranked with a Reward Model and then the highest-scoring completion is selected` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `This data contains completions for a 10,000 subset of the  UFB prompts` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `This data contains completions for a 10,000 subset of the  UFB prompts` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `385` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `UFB prompts (translated into 9 languages)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `You may use this data to train models, conduct analyses of model differences or evaluate other aggregation methods` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 1541자 ≈ 385 토큰 (viewer statistics, default/train)
