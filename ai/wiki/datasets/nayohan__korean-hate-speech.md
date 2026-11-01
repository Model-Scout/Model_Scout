---
type: "dataset"
id: "nayohan/korean-hate-speech"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/korean-hate-speech"
downloads: 171
summary: "온라인 뉴스 댓글에서 혐오 발언 탐지를 위한 한국어 말뭉치 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nayohan/korean-hate-speech

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/korean-hate-speech)

온라인 뉴스 댓글에서 혐오 발언 탐지를 위한 한국어 말뭉치 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `toxic speech detection` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `toxic speech detection` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `35` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `news_title` 열 p90 53자 ≈ 35 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
