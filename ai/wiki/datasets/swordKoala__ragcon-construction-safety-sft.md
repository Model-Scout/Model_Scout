---
type: "dataset"
id: "swordKoala/ragcon-construction-safety-sft"
source: "huggingface"
url: "https://huggingface.co/datasets/swordKoala/ragcon-construction-safety-sft"
downloads: 23
summary: "건설현장 조건 입력 시 사고유형, 심각도, 위험 시나리오 등을 생성하는 한국어 안전 분석 SFT 데이터셋입니다."
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
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# swordKoala/ragcon-construction-safety-sft

> dataset · [Hugging Face](https://huggingface.co/datasets/swordKoala/ragcon-construction-safety-sft)

건설현장 조건 입력 시 사고유형, 심각도, 위험 시나리오 등을 생성하는 한국어 안전 분석 SFT 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `건설현장의 현장 조건(시설물·공종·작업·공정률·작업자수·기상 등) 을 입력하면` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `예상 사고유형, 심각도 등급, 위험 시나리오, 사고원인, 예방 조치를 생성하도록` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `건설현장 안전 분석` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `지도학습 미세조정(SFT)하기 위한 한국어 instruction 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
