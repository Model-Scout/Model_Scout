---
type: "dataset"
id: "olob0/fineweb-2-trimming-15-languages"
source: "huggingface"
url: "https://huggingface.co/datasets/olob0/fineweb-2-trimming-15-languages"
downloads: 314
summary: "Fineweb-2의 15개 언어 필터링 데이터셋으로 모델 트리밍에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# olob0/fineweb-2-trimming-15-languages

> dataset · [Hugging Face](https://huggingface.co/datasets/olob0/fineweb-2-trimming-15-languages)

Fineweb-2의 15개 언어 필터링 데이터셋으로 모델 트리밍에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `The original [`lbourdois/fineweb-2-trimming`](https://huggingface.co/datasets/lbourdois/fineweb-2-trimming) dataset keeps a limited number of texts from 124 lan` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `The original [`lbourdois/fineweb-2-trimming`](https://huggingface.co/datasets/lbourdois/fineweb-2-trimming) dataset keeps a limited number of texts from 124 lan` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `The original [`lbourdois/fineweb-2-trimming`](https://huggingface.co/datasets/lbourdois/fineweb-2-trimming) dataset keeps a limited number of texts from 124 lan` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `6179` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Common Crawl` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The original [`lbourdois/fineweb-2-trimming`](https://huggingface.co/datasets/lbourdois/fineweb-2-trimming) dataset keeps a limited number of texts from 124 lan` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 24717자 ≈ 6179 토큰 (viewer statistics, kor/train)
