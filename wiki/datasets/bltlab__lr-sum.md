---
type: "dataset"
id: "bltlab/lr-sum"
source: "huggingface"
url: "https://huggingface.co/datasets/bltlab/lr-sum"
downloads: 700
summary: "LR-Sum은 적은 자원 언어를 위한 뉴스 요약 자동화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[요약]]"
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
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# bltlab/lr-sum

> dataset · [Hugging Face](https://huggingface.co/datasets/bltlab/lr-sum)

LR-Sum은 적은 자원 언어를 위한 뉴스 요약 자동화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:summarization = `LR-Sum is a automatic summarization dataset of newswire text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `human-written summaries for 39 languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `39 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `721` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `LR-Sum is a automatic summarization dataset of newswire text` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The data can be used for training text generation models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2886자 ≈ 721 토큰 (viewer statistics, kor/validation)
