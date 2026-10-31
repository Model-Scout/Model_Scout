---
type: "dataset"
id: "fluently-sets/ultraset"
source: "huggingface"
url: "https://huggingface.co/datasets/fluently-sets/ultraset"
downloads: 76
summary: "Alpaca 포맷의 SFT 학습용 다국어 텍스트 데이터셋으로 LLM 모델 훈련에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[code]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
  - "[[일반]]"
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# fluently-sets/ultraset

> dataset · [Hugging Face](https://huggingface.co/datasets/fluently-sets/ultraset)

Alpaca 포맷의 SFT 학습용 다국어 텍스트 데이터셋으로 LLM 모델 훈련에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering, task:translation = `Type of dataset: text, alpaca` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:translation = `Type of dataset: text, alpaca` · 신뢰도 medium
- **언어**: [[code]] — metadata · languages = `code` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `556` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `This dataset is designed to facilitate training and retraining of LLM models using the SFT method in the Alpaca format.` · 신뢰도 low
- **도메인**: [[의료·보건]] — tag_match · tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is designed to facilitate training and retraining of LLM models using the SFT method in the Alpaca format.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 2224자 ≈ 556 토큰 (viewer statistics, default/train)
