---
type: "dataset"
id: "esdurmus/wiki_lingua"
source: "huggingface"
url: "https://huggingface.co/datasets/esdurmus/wiki_lingua"
downloads: 825
summary: "WikiLingua는 18개 언어로 된 위키하우 가이드 문서와 요약문 쌍을 제공하는 다국어 요약 평가 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# esdurmus/wiki_lingua

> dataset · [Hugging Face](https://huggingface.co/datasets/esdurmus/wiki_lingua)

WikiLingua는 18개 언어로 된 위키하우 가이드 문서와 요약문 쌍을 제공하는 다국어 요약 평가 데이터셋입니다.

## 분류

- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:summarization = `article and summary pairs in 18 languages from WikiHow` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:summarization = `article-summary alignments across languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `18 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a diverse set of topics written by human authors` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `for the evaluation of cross-lingual abstractive summarization systems` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
