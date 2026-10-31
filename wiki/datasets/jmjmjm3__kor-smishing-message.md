---
type: "dataset"
id: "jmjmjm3/kor-smishing-message"
source: "huggingface"
url: "https://huggingface.co/datasets/jmjmjm3/kor-smishing-message"
downloads: 137
summary: "한국어 문자 메시지의 정상과 스미싱을 분류하는 데이터셋으로 스미싱 탐지에 활용됩니다."
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
  - "[[금융·경제]]"
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# jmjmjm3/kor-smishing-message

> dataset · [Hugging Face](https://huggingface.co/datasets/jmjmjm3/kor-smishing-message)

한국어 문자 메시지의 정상과 스미싱을 분류하는 데이터셋으로 스미싱 탐지에 활용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `한국어 문자 메시지를 대상으로 정상 메시지와 스미싱 메시지를 분류하기 위해 구축한 데이터셋입니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `단순한 이진 분류 라벨뿐만 아니라 메시지의 판단 근거와 유형 정보를 함께 포함합니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Domain: Smishing Detection, Financial Security, Cybersecurity` · 신뢰도 medium
- **도메인**: [[의료·보건]] — ner · readme = `[국민건강보험] 미납 보험료가 있습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 스미싱 탐지 모델 학습 및 평가를 목적으로 하며` · 신뢰도 medium
