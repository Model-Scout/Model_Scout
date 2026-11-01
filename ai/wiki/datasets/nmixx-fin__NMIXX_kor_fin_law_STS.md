---
type: "dataset"
id: "nmixx-fin/NMIXX_kor_fin_law_STS"
source: "huggingface"
url: "https://huggingface.co/datasets/nmixx-fin/NMIXX_kor_fin_law_STS"
downloads: 32
summary: "한국어 금융·법률 문장 유사도 점수 데이터셋으로 문장 유사도 평가에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nmixx-fin/NMIXX_kor_fin_law_STS

> dataset · [Hugging Face](https://huggingface.co/datasets/nmixx-fin/NMIXX_kor_fin_law_STS)

한국어 금융·법률 문장 유사도 점수 데이터셋으로 문장 유사도 평가에 사용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `score` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `score` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding = `- name: sentence1` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `- name: score` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
