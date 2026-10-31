---
type: "dataset"
id: "lightblue/reasoning-multilingual-R1-Llama-70B-train"
source: "huggingface"
url: "https://huggingface.co/datasets/lightblue/reasoning-multilingual-R1-Llama-70B-train"
downloads: 253
summary: "30개 이상의 언어를 포함하는 다국어 추론 데이터셋으로 다국어 추론 모델 학습에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lightblue/reasoning-multilingual-R1-Llama-70B-train

> dataset · [Hugging Face](https://huggingface.co/datasets/lightblue/reasoning-multilingual-R1-Llama-70B-train)

30개 이상의 언어를 포함하는 다국어 추론 데이터셋으로 다국어 추론 모델 학습에 사용됨

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Generating responses to these prompts 8 times using deepseek-ai/DeepSeek-R1-Distill-Llama-70B` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Sampling prompts from English datasets and translating them to various languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Generating responses to these prompts 8 times using deepseek-ai/DeepSeek-R1-Distill-Llama-70B` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `38 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1372` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a multilingual reasoning dataset covering more than 30 languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset was then used to train a multilingual reasoning finetune of the [R1 distills]` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 5486자 ≈ 1372 토큰 (viewer statistics, default/train)
