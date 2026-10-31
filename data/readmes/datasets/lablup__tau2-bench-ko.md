---
pretty_name: "τ²-bench Korean Translation"
license: mit
language:
  - ko
  - en
task_categories:
  - text-generation
  - question-answering
tags:
  - llm-routing
  - benchmark
  - translation
  - korean
  - agents
  - tool-use
  - tau2-bench
size_categories:
  - n<1K
configs:
  - config_name: retail
    data_files:
      - split: test
        path: data/retail.jsonl
  - config_name: airline
    data_files:
      - split: test
        path: data/airline.jsonl
  - config_name: telecom
    data_files:
      - split: test
        path: data/telecom.jsonl
---
# τ²-bench 한국어 번역 공개판

τ²-bench `v0.2.0`의 retail·airline·telecom 사용자 시나리오를 한국어로 번역

* 원본: `sierra-research/tau2-bench` `v0.2.0`
* 번역 및 검수 모델: `gpt-5.6-sol`, 일부 모호한 문장은 사람이 검수
* 번역 범위: 278 task, 1,004 user-scenario field

## 파일

| 파일                   | 행 수 | 설명               |
| :------------------- | --: | :--------------- |
| `data/retail.jsonl`  | 114 | 유통 에이전트 태스크      |
| `data/airline.jsonl` |  50 | 항공 에이전트 태스크      |
| `data/telecom.jsonl` | 114 | 통신 에이전트 태스크      |
| `metadata.json`      |   - | 생성 설정·파일 SHA-256 |
| `build_dataset.py`   |   - | 원본 task에 번역 필드를 결합해 jsonl 생성하는 스크립트 |
| `LICENSE`            |   - | 원본 τ²-bench의 MIT License 사본 |

`documentation/` 구성:

| 파일 | 설명 |
| :--- | :--- |
| `TRANSLATION_GUIDELINES_KO.md` | 번역 지침 v1.0 — 보존 규칙·문체·용어 처리 |
| `glossary/common.csv` | 도메인 공통 용어집 |
| `glossary/retail.csv` · `airline.csv` · `telecom.csv` | 도메인별 용어집 |
| `pilot30_manifest.json` | 파일럿 30 task 선정 기록 — 원본 커밋 고정, 구조 특징 9종 기반 greedy maximin 선정, 번역 대상 필드 목록 |
| `pilot30_review_decisions.json` | 파일럿 30 task 검수 판정 — 승인 그룹 23건·task-field 승인 목록 |
| `PERSONA_TRANSLATION_REVIEW.md` | persona 필드 번역 검토 기록 |
| `FULL_TRANSLATION_STATUS.md` | 전체 번역 진행·검증 상태 기록 |

각 JSONL 행은 원본 `tasks.json`의 태스크 구조 유지

* `user_scenario.persona`
* `user_scenario.instructions.reason_for_call`
* `user_scenario.instructions.known_info`
* `user_scenario.instructions.unknown_info`
* `user_scenario.instructions.task_instructions`

## 번역 및 검수 설정

* model: `gpt-5.6-sol`
* reasoning effort: `none`
* 호출 단위: task 1개
* 출력: instructions 네 필드 strict JSON schema, persona 템플릿 2종
* 입력: 번역 지침 v1.0, 공통·도메인별 용어집, 영어 원문
* 생성일: 2026-08-24

## 번역 원칙

* 주문번호·예약번호·사용자 ID·숫자·enum·tool 입력값 보존
* 원문 모호성이나 오류를 보완하지 않음
* 사용자 시나리오의 `agent`는 고객 서비스 역할에 맞게 `상담원`으로 번역
* persona 본문은 번역하고 task ID의 `[PERSONA:...]` 표기는 보존

## 알려진 특이사항

* retail task `15`: `want the material`에 원하는 소재가 빠져 있어 모호성을 보존했
* retail task `43`: `check if the storage` 문장이 불완전하여 최소 문맥상 저장 용량
  확인으로 옮김

* retail task `63`: `task_instructions`가 마침표 하나(`.`)뿐이었지만 그대로 보존
* 일부 `unknown_info`는 문자열이 아닌 `null`이며 그대로 유지
* telecom ID의 `[PERSONA:None|Easy|Hard]`는 식별자이므로 원문 보존
* 통신 속도 상태 `excellent`, `good`, `fair`, `poor`는 채점 enum으로 원문 보존

## 응답 언어와 채점

`initial_state`와 `evaluation_criteria`는 영어 원본과 동일함. 이 데이터에는 한국어
시나리오로 새로 실행한 대화나 점수가 포함되지 않았음. 한국어 실행 시 tool argument의
ID와 enum을 원문대로 유지해야 하며, 자연어 judge를 번역하면 별도 실험 조건으로
기록해야 함

## 사용법

```python
from datasets import load_dataset

retail = load_dataset("lablup/tau2-bench-ko", "retail", split="test")
print(retail[0]["user_scenario"]["instructions"]["reason_for_call"])
```

## 출처와 라이선스

원본 τ²-bench의 Copyright (c) 2025 Sierra Research 및 MIT License를 보존하고 있음
사용 시 원본 τ²-bench 논문·저장소와 이 번역 데이터의 정확한 revision을 함께
기록하는 것을 권장함
