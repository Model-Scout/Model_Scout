---
type: "dataset"
id: "mssongit/finance-task"
source: "huggingface"
url: "https://huggingface.co/datasets/mssongit/finance-task"
downloads: 64
summary: "한국어 금융 뉴스 기사로 감성 분석, 광고성 뉴스 분류, 개체명 인식에 활용하는 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# mssongit/finance-task

> dataset · [Hugging Face](https://huggingface.co/datasets/mssongit/finance-task)

한국어 금융 뉴스 기사로 감성 분석, 광고성 뉴스 분류, 개체명 인식에 활용하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `감성 분석 (긍정/부정)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `한국어 텍스트에서 다양한 자연어 처리 태스크를 훈련 및 평가할 수 있도록 설계되었습니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `감성 분석 (긍정/부정)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `다양한 자연어 처리 태스크를 훈련 및 평가할 수 있도록 설계되었습니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `다양한 자연어 처리 태스크를 훈련 및 평가할 수 있도록 설계되었습니다.` · 신뢰도 medium
