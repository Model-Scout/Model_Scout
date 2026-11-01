---
license: other
language:
- ko
task_categories:
- text-generation
pretty_name: 20G Tone Dataset KO
size_categories:
- 100K<n<1M
tags:
- sft
- korean
- conversation
- tone
- kanana
---

# 20G-tone-dataset-ko.jsonl

`20G-tone-dataset-ko.jsonl`은 원본 `cp1`에서 불필요한 메타데이터와 컬럼을 제거하고, 자연스러운 한국어 장기대화로 정제한 SFT 데이터셋이다.

- 현재 행 수: 221,328
- 한 줄 용도: 한국어 일상 대화/공감형 응답 모델을 학습하기 위한 대화 SFT 데이터셋
- 주 용도: kanana 기반 일상 대화/공감형 응답 모델 SFT
- 형식: JSONL, 한 줄에 하나의 대화 예시
- 스키마: `{"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}, ...]}`

## 데이터 의미

각 row는 여러 턴의 `user`/`assistant` 메시지로 구성된다. 대화는 일상 고민, 관계, 일, 생활 변화, 감정 정리처럼 실제 사용자가 자연스럽게 말할 법한 상황을 중심으로 이어진다.

## 말투 방향

assistant는 과하게 공손하거나 설명적인 문체보다, 가까운 친구가 현실적으로 받아주고 되묻는 톤을 따른다. 짧은 공감, 구체적 질문, 부담을 낮추는 조언, 감정의 결을 살리는 표현을 섞는다.

## 품질 기준

- 메타데이터, id, source, category 같은 보조 컬럼 없음
- 모든 메시지는 `user` 또는 `assistant` 역할만 사용
- 대화 흐름이 끊기거나 역할이 뒤집힌 row 제거
- assistant의 웃음은 `ㅋㅋㅎㅋㅎㅋㅎㅋㅎ`, 울음은 `ㅜㅜ` 표기를 사용
- 기계적인 반복, 과한 상담문, 안전하지 않은 조언 제거
- 완전 중복과 비정상 길이 데이터 제거
