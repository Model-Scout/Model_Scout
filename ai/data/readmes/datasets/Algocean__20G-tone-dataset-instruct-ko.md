---
license: other
language:
- ko
task_categories:
- text-generation
pretty_name: 20G Tone Dataset Instruct KO
size_categories:
- 100K<n<1M
tags:
- sft
- korean
- style-transfer
- tone-conversion
- kanana
---

# 20G-tone-dataset-instruct-ko.jsonl

`20G-tone-dataset-instruct-ko.jsonl`은 정적이고 공적인 한국어 문장을 `20G-tone-dataset-ko`의 자연스러운 20~30대 여성 친구 말투로 바꾸는 말투 보정 SFT 데이터셋이다.

- 현재 행 수: 412,776
- 한 줄 용도: `20G-tone-dataset-ko`의 말투를 따르도록 문장을 변환하는 한국어 instruct 데이터셋
- 주 용도: kanana 기반 말투 보정 모델 SFT
- 형식: JSONL, 한 줄에 하나의 학습 예시
- 스키마: `{"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}]}`

## 데이터 의미

`user` 메시지는 변환 요청과 원문을 담는다. `assistant` 메시지는 같은 의미를 유지하되 더 편하고 감정이 살아 있는 친구 말투로 바꾼 결과다.

## 품질 기준

- 메타데이터, id, source, category 같은 보조 컬럼 없음
- 역할 순서 고정: `user` 다음 `assistant`
- assistant는 답변이 아니라 원문 변환문
- 의미 왜곡, 과장, 불필요한 설명, 반복 표현 제거
- 웃음은 `ㅋㅋㅎㅋㅎㅋㅎㅋㅎ`, 울음은 `ㅜㅜ` 표기를 사용
- 완전 중복과 assistant 중복 제거
