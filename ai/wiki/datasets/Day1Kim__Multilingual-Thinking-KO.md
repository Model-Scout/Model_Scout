---
type: "dataset"
id: "Day1Kim/Multilingual-Thinking-KO"
source: "huggingface"
url: "https://huggingface.co/datasets/Day1Kim/Multilingual-Thinking-KO"
downloads: 11
summary: "영어에서 한국어로 번역된 추론 체인 데이터를 포함한 reasoning 데이터셋으로 GPT5 API로 제작됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
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
# Day1Kim/Multilingual-Thinking-KO

> dataset · [Hugging Face](https://huggingface.co/datasets/Day1Kim/Multilingual-Thinking-KO)

영어에서 한국어로 번역된 추론 체인 데이터를 포함한 reasoning 데이터셋으로 GPT5 API로 제작됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `The user message is used to provide the input to the model` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Output by the model which can either be a tool call or a message output.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1433` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual-Thinking is a reasoning dataset where the chain-of-thought has been translated from English into Korean.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset was used in the OpenAI Cookbook to fine-tune the OpenAI gpt-oss models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `final` 열 p90 2150자 ≈ 1433 토큰 (viewer statistics, default/train)
