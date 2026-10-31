---
type: "dataset"
id: "dendriteholdings/ingot_corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/dendriteholdings/ingot_corpus"
downloads: 982
summary: "366개 공개 데이터셋에서 수집한 18개 도메인, 84개 언어의 1,061만 개 작업 프롬프트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
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
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# dendriteholdings/ingot_corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/dendriteholdings/ingot_corpus)

366개 공개 데이터셋에서 수집한 18개 도메인, 84개 언어의 1,061만 개 작업 프롬프트 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `It is meant for comparing a model's output distribution with a reference model's (e.g. KL divergence between a quantized model and its teacher) across as many c` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation = `It holds prompts only, no answers` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `It holds prompts only, no answers` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `84 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `74171` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A broad prompt corpus.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `the train split is the legacy 1,812,669-row release.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `user_prompt` 열 p90 296683자 ≈ 74171 토큰 (viewer statistics, default/train)
