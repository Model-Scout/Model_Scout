---
type: "dataset"
id: "werty1248/sentence-transformer-parallel-En-Ko-with-Similarity"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/sentence-transformer-parallel-En-Ko-with-Similarity"
downloads: 33
summary: "영어-한국어 병렬 문장 데이터셋으로 임베딩 유사도 기반 전처리를 위한 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
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
# werty1248/sentence-transformer-parallel-En-Ko-with-Similarity

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/sentence-transformer-parallel-En-Ko-with-Similarity)

영어-한국어 병렬 문장 데이터셋으로 임베딩 유사도 기반 전처리를 위한 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `임베딩 유사도 기반 전처리를 통해 이 문제를 해결할 수 있을 것 같아서 이 데이터 셋을 제작했습니다.` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:translation = `영어 텍스트와 한국어 텍스트를 문장 단위로 분리한 후` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `임베딩 유사도 기반 전처리를 통해 이 문제를 해결할 수 있을 것 같아서 이 데이터 셋을 제작했습니다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1048` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `해외에서 제작된 많은 대규모 번역 쌍 데이터들이 영어 텍스트와 한국어 텍스트를 문장 단위로 분리한 후 기계적으로 매핑시키고 있습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `임베딩 유사도 기반 전처리를 통해 이 문제를 해결할 수 있을 것 같아서 이 데이터 셋을 제작했습니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 1572자 ≈ 1048 토큰 (viewer statistics, default/train)
