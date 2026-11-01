---
type: "dataset"
id: "HAERAE-HUB/KOREAN-WEBTEXT"
source: "huggingface"
url: "https://huggingface.co/datasets/HAERAE-HUB/KOREAN-WEBTEXT"
downloads: 407
summary: "2.2억 토큰의 고품질 한국어 웹텍스트 말뭉치로, 텍스트 필터링과 중복 제거를 거쳐 연구용으로 제공됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
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
# HAERAE-HUB/KOREAN-WEBTEXT

> dataset · [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/KOREAN-WEBTEXT)

2.2억 토큰의 고품질 한국어 웹텍스트 말뭉치로, 텍스트 필터링과 중복 제거를 거쳐 연구용으로 제공됨.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `KOREAN-WEBTEXT is a high-quality Korean language corpus consisting of 2.2 billion tokens.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `The dataset undergoes rigorous filtering at both the sentence and document levels to ensure quality of text data.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `The dataset undergoes rigorous filtering at both the sentence and document levels to ensure quality of text data.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `19999` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Additional credible internet sources collected by out team` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `While the dataset may be small for pretraining models due to its size, we expect it to be better suited for ablation studies.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 29999자 ≈ 19999 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[FINAL-Bench__Aether-7B-5Attn|FINAL-Bench/Aether-7B-5Attn]]
- [[FINAL-Bench__Aether-7B-5Attn-it|FINAL-Bench/Aether-7B-5Attn-it]]
- [[idah4__etm-korean-tiny|idah4/etm-korean-tiny]]
