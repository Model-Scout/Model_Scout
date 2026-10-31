---
type: "dataset"
id: "Infinity08/KAWK50M-Training-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/Infinity08/KAWK50M-Training-Data"
downloads: 373
summary: "KAWK50M 학습 데이터 아카이브로, 한국어 SFT 데이터와 원문, 정제 말뭉치를 포함합니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Infinity08/KAWK50M-Training-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/Infinity08/KAWK50M-Training-Data)

KAWK50M 학습 데이터 아카이브로, 한국어 SFT 데이터와 원문, 정제 말뭉치를 포함합니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `SFT 데이터의 전체 작업 사본입니다.` · 신뢰도 low
- **작업**: [[언어 모델링]] — tag_match · tags = `language-modeling` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `원본 데이터와 조건` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `5,120 토큰 길이로 패킹한 한국어 SFT 바이너리` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `웹 원문에는 개인정보, 유해 문구, 부정확한 정보가 남아 있을 수 있습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `KAWK50M Training Data Archive` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
