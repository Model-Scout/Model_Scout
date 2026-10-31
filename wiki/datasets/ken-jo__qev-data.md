---
type: "dataset"
id: "ken-jo/qev-data"
source: "huggingface"
url: "https://huggingface.co/datasets/ken-jo/qev-data"
downloads: 1340
summary: "QEV-2B와 QEV-0.8B 모델 학습용 2026년 10월 비전 믹스 및 역사적 스냅샷 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ken-jo/qev-data

> dataset · [Hugging Face](https://huggingface.co/datasets/ken-jo/qev-data)

QEV-2B와 QEV-0.8B 모델 학습용 2026년 10월 비전 믹스 및 역사적 스냅샷 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[이미지 인식]] — metadata · task_categories = `image-classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:vision = `image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Original observations were selected and converted into typed decision views.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Original observations were selected and converted into typed decision views.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `38` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Training data for QEV decision models: the October 2026 vision mixes for QEV-2B and QEV-0.8B` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training data for QEV decision models: the October 2026 vision mixes for QEV-2B and QEV-0.8B (the first release and v3), and historical snapshots for QEV 0.2.1.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `seed` 열 p90 57자 ≈ 38 토큰 (viewer statistics, vision-2026-10-v3-coverage-manifest/train)
