---
type: "dataset"
id: "eduagarcia/multilingual_tokenizer_benchmark"
source: "huggingface"
url: "https://huggingface.co/datasets/eduagarcia/multilingual_tokenizer_benchmark"
downloads: 399
summary: "다국어 토크나이저 벤치마크 데이터셋으로 다양한 언어와 도메인의 텍스트 토큰화 성능 평가용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
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
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[상거래·상품]]"
  - "[[일반]]"
  - "[[법률]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# eduagarcia/multilingual_tokenizer_benchmark

> dataset · [Hugging Face](https://huggingface.co/datasets/eduagarcia/multilingual_tokenizer_benchmark)

다국어 토크나이저 벤치마크 데이터셋으로 다양한 언어와 도메인의 텍스트 토큰화 성능 평가용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Num. of Domains | Num. of Docs | Num. of Characters | Num. of Words` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `More details of each subset like word count, character count, original sources, etc` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Multilingual Tokenizer Benchmark` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding, task:generation, task:language_modeling = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Multilingual Tokenizer Benchmark` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `475` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Finance` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `Multilingual Tokenizer Benchmark` · 신뢰도 low
- **도메인**: [[법률]] — ner · readme = `Legal` · 신뢰도 medium
- **도메인**: [[뉴스·미디어]] — ner · readme = `News` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Multilingual Tokenizer Benchmark` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `More details of each subset like word count, character count, original sources, etc, can be found in the dataset_meta.yaml file` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1899자 ≈ 475 토큰 (viewer statistics, ko/train)
