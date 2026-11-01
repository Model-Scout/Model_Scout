---
type: "dataset"
id: "Lumia101/ko-perplexity-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/Lumia101/ko-perplexity-corpus"
downloads: 26
summary: "한국어 데이터셋으로 학습된 LLM의 혼란도를 측정하기 위한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
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
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Lumia101/ko-perplexity-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/Lumia101/ko-perplexity-corpus)

한국어 데이터셋으로 학습된 LLM의 혼란도를 측정하기 위한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `This dataset was created to measure the perplexity of an LLM trained on a Korean dataset.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `This dataset was created to measure the perplexity of an LLM trained on a Korean dataset.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `This dataset was created to measure the perplexity of an LLM trained on a Korean dataset.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1748` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `This dataset was created to measure the perplexity of an LLM trained on a Korean dataset.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2622자 ≈ 1748 토큰 (viewer statistics, news/train)
