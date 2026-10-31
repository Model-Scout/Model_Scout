---
type: "dataset"
id: "sentence-transformers/parallel-sentences-opensubtitles"
source: "huggingface"
url: "https://huggingface.co/datasets/sentence-transformers/parallel-sentences-opensubtitles"
downloads: 1227
summary: "OpenSubtitles 병렬 문장 데이터셋으로 다국어 문장 임베딩 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# sentence-transformers/parallel-sentences-opensubtitles

> dataset · [Hugging Face](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-opensubtitles)

OpenSubtitles 병렬 문장 데이터셋으로 다국어 문장 임베딩 학습에 사용됨.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `This dataset contains parallel sentences (i.e. English sentence + the same sentences in another language)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `This dataset contains parallel sentences (i.e. English sentence + the same sentences in another language)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `45 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `18` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains parallel sentences (i.e. English sentence + the same sentences in another language) for numerous other languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `These datasets can be used to train multilingual sentence embedding models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 73자 ≈ 18 토큰 (viewer statistics, en-ko/train)
