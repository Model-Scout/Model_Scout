---
type: "dataset"
id: "occiglot/tokenizer-wiki-bench"
source: "huggingface"
url: "https://huggingface.co/datasets/occiglot/tokenizer-wiki-bench"
downloads: 20027
summary: "45개 언어 위키피디아 데이터를 활용한 다국어 토크나이저 평가 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# occiglot/tokenizer-wiki-bench

> dataset · [Hugging Face](https://huggingface.co/datasets/occiglot/tokenizer-wiki-bench)

45개 언어 위키피디아 데이터를 활용한 다국어 토크나이저 평가 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The dataset allows us to easily calculate tokenizer fertility and the proportion of continued words on any of the supported languages.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `This dataset includes pre-processed wikipedia data for tokenizer evaluation in 45 languages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The dataset allows us to easily calculate tokenizer fertility and the proportion of continued words on any of the supported languages.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `45 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3913` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset includes pre-processed wikipedia data for tokenizer evaluation in 45 languages.` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 15653자 ≈ 3913 토큰 (viewer statistics, ko/train)
