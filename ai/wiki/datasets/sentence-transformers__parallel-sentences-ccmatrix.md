---
type: "dataset"
id: "sentence-transformers/parallel-sentences-ccmatrix"
source: "huggingface"
url: "https://huggingface.co/datasets/sentence-transformers/parallel-sentences-ccmatrix"
downloads: 2209
summary: "CCMatrix 데이터셋에서 추출한 다국어 병렬 문장 데이터로 다국어 임베딩 모델 학습에 사용됨."
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
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# sentence-transformers/parallel-sentences-ccmatrix

> dataset · [Hugging Face](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-ccmatrix)

CCMatrix 데이터셋에서 추출한 다국어 병렬 문장 데이터로 다국어 임베딩 모델 학습에 사용됨.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `Columns: "english", "non_english"` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Columns: "english", "non_english"` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `75 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `31` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 125자 ≈ 31 토큰 (viewer statistics, en-ko/train)
