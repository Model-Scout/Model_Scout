---
type: "dataset"
id: "Infinity08/KAWK50M-Training-Runs"
source: "huggingface"
url: "https://huggingface.co/datasets/Infinity08/KAWK50M-Training-Runs"
downloads: 217
summary: "KAWK50M 프로젝트의 학습 이력 아카이브로 실험 재현과 진단용 데이터입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[코드 (입력 형식)|코드]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[코드 (출력 형식)|코드]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Infinity08/KAWK50M-Training-Runs

> dataset · [Hugging Face](https://huggingface.co/datasets/Infinity08/KAWK50M-Training-Runs)

KAWK50M 프로젝트의 학습 이력 아카이브로 실험 재현과 진단용 데이터입니다.

## 분류

- **작업**: [[언어 모델링]] — tag_match · readme, tags = `language-modeling` · 신뢰도 medium
- **입력 형식**: [[코드 (입력 형식)|코드]] — ner · readme = `각 체크포인트의 model/과 tokenizer/는 Transformers 형식입니다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:language_modeling = `text` · 신뢰도 high
- **출력 형식**: [[코드 (출력 형식)|코드]] — ner · readme = `각 체크포인트의 model/과 tokenizer/는 Transformers 형식입니다.` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:language_modeling = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `최종·중간·실패 실험 체크포인트를 포함한 전체 학습 이력입니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
