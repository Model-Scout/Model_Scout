---
type: "dataset"
id: "sentence-transformers/mldr"
source: "huggingface"
url: "https://huggingface.co/datasets/sentence-transformers/mldr"
downloads: 4538
summary: "MLDR 데이터셋은 BGE-M3 모델 학습용 삼중항 문장 쌍 데이터를 제공한다."
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
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# sentence-transformers/mldr

> dataset · [Hugging Face](https://huggingface.co/datasets/sentence-transformers/mldr)

MLDR 데이터셋은 BGE-M3 모델 학습용 삼중항 문장 쌍 데이터를 제공한다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `Columns: "anchor", "positive", "negative"` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Columns: "anchor", "positive", "negative"` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3354` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This is a reformatting of the MLDR dataset used to train the BGE-M3 model.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `positive` 열 p90 13416자 ≈ 3354 토큰 (viewer statistics, ko-triplet/train)
