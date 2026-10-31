---
type: "dataset"
id: "Bingsu/ko_alpaca_data"
source: "huggingface"
url: "https://huggingface.co/datasets/Bingsu/ko_alpaca_data"
downloads: 133
summary: "alpaca 데이터를 한국어로 번역하고 OpenAI API로 출력 데이터를 생성한 한국어 명령-응답 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
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
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Bingsu/ko_alpaca_data

> dataset · [Hugging Face](https://huggingface.co/datasets/Bingsu/ko_alpaca_data)

alpaca 데이터를 한국어로 번역하고 OpenAI API로 출력 데이터를 생성한 한국어 명령-응답 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Translated 'instruction' and 'input' in the dataset via the DeepL API` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `except for 'output', which we did not translate because it is the output of OpenAI's text-davinci-003 model.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `101` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean translation of alpaca data.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `| # of data | 49620 |` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 151자 ≈ 101 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[blueapple8259__TinyKo|blueapple8259/TinyKo]]
