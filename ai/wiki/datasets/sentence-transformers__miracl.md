---
type: "dataset"
id: "sentence-transformers/miracl"
source: "huggingface"
url: "https://huggingface.co/datasets/sentence-transformers/miracl"
downloads: 3443
summary: "MIRACL 데이터셋은 BGE-M3 모델 학습용으로 문장 임베딩 학습에 사용됩니다."
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
  - "[[대규모 데이터]]"
---
# sentence-transformers/miracl

> dataset · [Hugging Face](https://huggingface.co/datasets/sentence-transformers/miracl)

MIRACL 데이터셋은 BGE-M3 모델 학습용으로 문장 임베딩 학습에 사용됩니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `Columns: "anchor", "positive", "negative" Column types: str, str, str` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Columns: "anchor", "positive", "negative" Column types: str, str, str` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `135` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a reformatting of the MIRACL dataset used to train the BGE-M3 model.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This is a reformatting of the MIRACL dataset used to train the BGE-M3 model.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `negative` 열 p90 539자 ≈ 135 토큰 (viewer statistics, ko-triplet/train)

## 이 데이터로 학습한 모델

- [[Msobhi__Persian_Sentence_Embedding_v3|Msobhi/Persian_Sentence_Embedding_v3]]
