---
type: "dataset"
id: "EllieChoi/aihub_ko_fairytale_generation_by_keyword_for_llama"
source: "huggingface"
url: "https://huggingface.co/datasets/EllieChoi/aihub_ko_fairytale_generation_by_keyword_for_llama"
downloads: 22
summary: "AIHub 동화 줄거리 생성 데이터 기반 키워드로 동화 줄거리 생성 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# EllieChoi/aihub_ko_fairytale_generation_by_keyword_for_llama

> dataset · [Hugging Face](https://huggingface.co/datasets/EllieChoi/aihub_ko_fairytale_generation_by_keyword_for_llama)

AIHub 동화 줄거리 생성 데이터 기반 키워드로 동화 줄거리 생성 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `본 데이터셋은 동화 줄거리 생성을 위한 학습 데이터로, 키워드를 기반으로 동화 줄거리를 생성하는 작업에 활용할 수 있습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `키워드를 기반으로 동화 줄거리를 생성하는 작업` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `동화 줄거리 생성을 위한 학습 데이터` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `14649` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `Test: 161 samples` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train: 1281 samples` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 21974자 ≈ 14649 토큰 (viewer statistics, default/validation)
