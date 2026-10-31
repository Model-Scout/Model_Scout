---
type: "dataset"
id: "Algocean/20G-tone-dataset-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/Algocean/20G-tone-dataset-ko"
downloads: 42
summary: "한국어 일상 대화 및 공감형 응답 모델 학습용 장기 대화 SFT 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Algocean/20G-tone-dataset-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/Algocean/20G-tone-dataset-ko)

한국어 일상 대화 및 공감형 응답 모델 학습용 장기 대화 SFT 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `스키마: {"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}, ...]}` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `스키마: {"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}, ...]}` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `대화는 일상 고민, 관계, 일, 생활 변화, 감정 정리처럼 실제 사용자가 자연스럽게 말할 법한 상황을 중심으로 이어진다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `kanana 기반 일상 대화/공감형 응답 모델 SFT` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
