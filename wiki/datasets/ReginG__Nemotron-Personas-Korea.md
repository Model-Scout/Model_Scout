---
type: "dataset"
id: "ReginG/Nemotron-Personas-Korea"
source: "huggingface"
url: "https://huggingface.co/datasets/ReginG/Nemotron-Personas-Korea"
downloads: 88
summary: "대한민국 실제 인구통계 기반 합성 페르소나 데이터셋으로 AI 모델 개발에 활용됨"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ReginG/Nemotron-Personas-Korea

> dataset · [Hugging Face](https://huggingface.co/datasets/ReginG/Nemotron-Personas-Korea)

대한민국 실제 인구통계 기반 합성 페르소나 데이터셋으로 AI 모델 개발에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `이 데이터셋은 소버린 AI 모델 개발을 위한 합성 데이터의 다양성 확대, 데이터 및 모델 편향 완화, 그리고 모델 응답의 다양성 향상 등에 활용될 수 있습니다.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `134` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `대한민국의 실제 인구통계학적·지리적·성격 특성 분포를 기반으로 합성된 오픈소스 페르소나 데이터셋` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `professional_persona` 열 p90 200자 ≈ 134 토큰 (viewer statistics, default/train)
