---
type: "dataset"
id: "nvidia/Nemotron-Personas-Korea"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea"
downloads: 6298
summary: "대한민국 인구통계 기반 합성 페르소나 데이터셋으로 소버린 AI 개발에 활용됨"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# nvidia/Nemotron-Personas-Korea

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea)

대한민국 인구통계 기반 합성 페르소나 데이터셋으로 소버린 AI 개발에 활용됨

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `134` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `대한민국의 실제 인구통계학적·지리적·성격 특성 분포를 기반으로 합성된 오픈소스 페르소나 데이터셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `누구나 다양한 모델 학습에 자유롭게 활용할 수 있으며, 개발자, 연구자, 데이터 전문가들의 적극적인 활용을 기대합니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `professional_persona` 열 p90 200자 ≈ 134 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[hyunseop__bge-m3-ko|hyunseop/bge-m3-ko]]
- [[hyunseop__qwen3-embedding|hyunseop/qwen3-embedding]]
