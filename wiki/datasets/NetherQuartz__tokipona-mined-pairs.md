---
type: "dataset"
id: "NetherQuartz/tokipona-mined-pairs"
source: "huggingface"
url: "https://huggingface.co/datasets/NetherQuartz/tokipona-mined-pairs"
downloads: 33
summary: "Toki Pona와 19개 언어 간 위키피디아 문장 병렬 쌍 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
  - "[[번역]]"
input_modality:
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# NetherQuartz/tokipona-mined-pairs

> dataset · [Hugging Face](https://huggingface.co/datasets/NetherQuartz/tokipona-mined-pairs)

Toki Pona와 19개 언어 간 위키피디아 문장 병렬 쌍 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `sentence-similarity` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Sentence-level parallel pairs between Toki Pona and 19 other languages, mined from Wikipedia using LaBSE-tokipona.` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval, task:translation = `Sentence-level parallel pairs between Toki Pona and 19 other languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Sentence-level parallel pairs between Toki Pona and 19 other languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `20 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `57` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Wikipedia articles and their counterparts in 19 languages.` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `validation 8,748` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train 163,583` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 227자 ≈ 57 토큰 (viewer statistics, default/validation)
