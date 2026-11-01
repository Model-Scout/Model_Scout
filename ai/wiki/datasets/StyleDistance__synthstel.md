---
type: "dataset"
id: "StyleDistance/synthstel"
source: "huggingface"
url: "https://huggingface.co/datasets/StyleDistance/synthstel"
downloads: 211
summary: "GPT-4로 합성 생성된 40개 스타일 특징 확장 STEL 태스크 데이터로 임베딩 모델 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# StyleDistance/synthstel

> dataset · [Hugging Face](https://huggingface.co/datasets/StyleDistance/synthstel)

GPT-4로 합성 생성된 40개 스타일 특징 확장 STEL 태스크 데이터로 임베딩 모델 학습에 사용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `This data was also used to train the StyleDistance embedding model` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `The SynthSTEL dataset is a synthetically generated (with GPT-4) extension of the STEL task to 40 style features` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The SynthSTEL dataset is a synthetically generated (with GPT-4) extension of the STEL task to 40 style features` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `31` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This data was also used to train the StyleDistance embedding model` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `positive` 열 p90 125자 ≈ 31 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[Baragi-AI__Munche-768|Baragi-AI/Munche-768]]
