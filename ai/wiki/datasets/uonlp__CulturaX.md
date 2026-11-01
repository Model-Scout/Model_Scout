---
type: "dataset"
id: "uonlp/CulturaX"
source: "huggingface"
url: "https://huggingface.co/datasets/uonlp/CulturaX"
downloads: 26438
summary: "167개 언어 6.3조 토큰 규모의 다국어 대형 언어 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# uonlp/CulturaX

> dataset · [Hugging Face](https://huggingface.co/datasets/uonlp/CulturaX)

167개 언어 6.3조 토큰 규모의 다국어 대형 언어 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `to significantly boost the data size and enhance the feasibility of training models in multilingual scenarios` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:language_modeling = `6.3 trillion tokens in 167 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `tailored for large language model (LLM) development` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `167 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a substantial multilingual dataset with 6.3 trillion tokens in 167 languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `to accomplish the best quality for model training` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[GuminiResearch__Gumini-1B-Base|GuminiResearch/Gumini-1B-Base]]
- [[dynamofl__dynamo-8B-v0.1|dynamofl/dynamo-8B-v0.1]]
- [[jjhsnail0822__danube-ko-1.8b-base|jjhsnail0822/danube-ko-1.8b-base]]
- [[mradermacher__Gumini-1B-Base-inherit-GGUF|mradermacher/Gumini-1B-Base-inherit-GGUF]]
- [[mradermacher__Gumini-1B-Base-inherit-i1-GGUF|mradermacher/Gumini-1B-Base-inherit-i1-GGUF]]
