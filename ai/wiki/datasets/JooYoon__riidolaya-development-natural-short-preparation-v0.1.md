---
type: "dataset"
id: "JooYoon/riidolaya-development-natural-short-preparation-v0.1"
source: "huggingface"
url: "https://huggingface.co/datasets/JooYoon/riidolaya-development-natural-short-preparation-v0.1"
downloads: 71
summary: "자연스러운 짧은 개발 댓글의 AI 자료 검토 실패 기록 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# JooYoon/riidolaya-development-natural-short-preparation-v0.1

> dataset · [Hugging Face](https://huggingface.co/datasets/JooYoon/riidolaya-development-natural-short-preparation-v0.1)

자연스러운 짧은 개발 댓글의 AI 자료 검토 실패 기록 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `이 준비 패키지는 세 댓글 주장(응답 요청, 현재 활동, 완료)에 관한 AI 자료 검토의 실패 집계다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `한국어와 영어가 가족당 한 행씩이다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `모델 결과를 제공하지 않는다.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `English card.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `TRAIN 1,680행, DEV/CAL/TEST 각 240행이다.` · 신뢰도 medium
