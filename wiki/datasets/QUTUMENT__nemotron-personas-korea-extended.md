---
type: "dataset"
id: "QUTUMENT/nemotron-personas-korea-extended"
source: "huggingface"
url: "https://huggingface.co/datasets/QUTUMENT/nemotron-personas-korea-extended"
downloads: 17
summary: "NVIDIA Nemotron-Personas-Korea 확장판으로 51개 컬럼, 100만 행의 통계 기반 합성 페르소나 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# QUTUMENT/nemotron-personas-korea-extended

> dataset · [Hugging Face](https://huggingface.co/datasets/QUTUMENT/nemotron-personas-korea-extended)

NVIDIA Nemotron-Personas-Korea 확장판으로 51개 컬럼, 100만 행의 통계 기반 합성 페르소나 데이터입니다.

## 분류

- **작업**: [[표 데이터 예측]] — ner · readme = `51컬럼 · 1,000,000행` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `51컬럼 · 1,000,000행` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `51컬럼 · 1,000,000행` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `298` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `상세/금융/헬스케어 페르소나 등` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `본 저장소는 내부 FGI 시뮬레이터( QUTUMENT/fgi_simulator )의 데이터 소스로 사용됩니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `detailed_persona` 열 p90 447자 ≈ 298 토큰 (viewer statistics, default/train)
