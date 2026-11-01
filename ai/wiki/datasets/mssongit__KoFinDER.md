---
type: "dataset"
id: "mssongit/KoFinDER"
source: "huggingface"
url: "https://huggingface.co/datasets/mssongit/KoFinDER"
downloads: 9
summary: "KoFinDER는 한국어와 영어 질문 및 응답 쌍을 포함한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mssongit/KoFinDER

> dataset · [Hugging Face](https://huggingface.co/datasets/mssongit/KoFinDER)

KoFinDER는 한국어와 영어 질문 및 응답 쌍을 포함한 데이터셋입니다.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2342` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train
num_bytes: 171287792
num_examples: 13867` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `response_eng_kor` 열 p90 3513자 ≈ 2342 토큰 (viewer statistics, default/train)
