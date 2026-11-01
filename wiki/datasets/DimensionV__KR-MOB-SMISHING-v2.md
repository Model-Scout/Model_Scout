---
type: "dataset"
id: "DimensionV/KR-MOB-SMISHING-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/DimensionV/KR-MOB-SMISHING-v2"
downloads: 84
summary: "한국형 모바일 스미싱 합성 데이터셋으로 SIEM 상관분석 훈련 및 보안 탐지에 활용됨"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# DimensionV/KR-MOB-SMISHING-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/DimensionV/KR-MOB-SMISHING-v2)

한국형 모바일 스미싱 합성 데이터셋으로 SIEM 상관분석 훈련 및 보안 탐지에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `Format | JSON (1 file per incident)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `SIEM 상관분석 규칙 개발, 보안 분석가 훈련, 탐지 엔지니어링 벤치마킹을 위해 설계되었습니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `한국 모바일 네트워크에서 실제로 발생하는 공격 패턴을 그대로 재현하되, 개인정보 위험은 제로, 실제 피해 가능성도 제로인 합성 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `SIEM 상관분석 규칙 개발, 보안 분석가 훈련, 탐지 엔지니어링 벤치마킹을 위해 설계되었습니다.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
