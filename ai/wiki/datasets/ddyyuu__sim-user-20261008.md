---
type: "dataset"
id: "ddyyuu/sim-user-20261008"
source: "huggingface"
url: "https://huggingface.co/datasets/ddyyuu/sim-user-20261008"
downloads: 244
summary: "MuJoCo 조이스틱 시뮬레이션 시연 데이터로 팀 공동 학습용입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ddyyuu/sim-user-20261008

> dataset · [Hugging Face](https://huggingface.co/datasets/ddyyuu/sim-user-20261008)

MuJoCo 조이스틱 시뮬레이션 시연 데이터로 팀 공동 학습용입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `팀 공동 학습을 위한 MuJoCo 조이스틱 시연 데이터의 2026-10-08 스냅샷입니다.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `observation.images.wrist: RGB 320×240, PNG 바이트가 Parquet에 포함됩니다.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · modality, readme = `시연: 259개 / 프레임: 331,753개 / 저장 속도: 30fps` · 신뢰도 high
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme = `action: dx/dy/dz(m), 월드 기준 회전벡터 증분 drx/dry/drz(rad), 신호 0/1, 총 7차원` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MuJoCo 조이스틱 시연 데이터` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `팀 공동 학습을 위한 MuJoCo 조이스틱 시연 데이터의 2026-10-08 스냅샷입니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
