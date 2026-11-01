---
license: apache-2.0
language:
- ko
task_categories:
- text-generation
tags:
- tool-calling
- agents
- rlvr
- calendar
pretty_name: Calendar Agent Training and Evaluation
---

# Calendar Agent Training and Evaluation

Tool Calling SFT와 환경 기반 RLVR을 함께 실습하는 Calendar Agent 데이터입니다.

## 1. 데이터 구성

| 파일 | 개수 | 구성 | SHA-256 |
|---|---:|---|---|
| `sft_train.jsonl` | 3,000 | 기본 시나리오, 다중 참석자 생성, 안전 대조군 | `f882fba3a6c32982d2f8cca06465fa1ec3c68562c655d2ee1bcd92decd29e637` |
| `sft_validation.jsonl` | 300 | SFT 학습 중 검증 | `b657e4162ef26bd580ad975b4f2af575a616dda17c90c7b4edab38790ad66ac5` |
| `rlvr_train.jsonl` | 256 | 충돌 복구와 다중 참석자 생성 128개, 안전 경계 128개 | `7f6f141cb608eb51a11964719d33d9897bf74a60b2da6cb47e6bf3531129d891` |
| `dev.jsonl` | 200 | 체크포인트 선택, 다섯 템플릿 각 40개 | `fc06c148ae1f39c8ee03759e24d36e70c5c5fa3b4d6bfeac23a3de5a8cf4b215` |
| `final.jsonl` | 400 | 최종 평가, 다섯 템플릿 각 80개 | `c1c95eed98342a03511d7192a7515870cf0e4ea3270c7ae46a7bb0fe266be495` |

SFT 분할은 다음 행동 범주로 구성합니다.

| 행동 범주 | train | validation |
|---|---:|---:|
| 기본 일정 관리 | 2,100 | 210 |
| 다중 참석자 일정 생성 | 600 | 60 |
| 다중 참석자 읽기 전용 대조군 | 300 | 30 |

RLVR 학습 분할은 다음 템플릿으로 구성합니다.

| 템플릿 | 개수 | 목표 행동 |
|---|---:|---|
| `conflict_then_create` | 80 | 충돌 확인 후 빈 시간에 일정 생성 |
| `multi_attendee_create` | 48 | 참석자 가용성 확인 후 일정 생성 |
| `delete_confirmation` | 64 | 삭제 대상을 조회하고 승인 요청 |
| `confirmed_delete` | 32 | 사용자 승인 후 일정 삭제 |
| `missing_time_clarification` | 32 | 누락된 시작 시각과 소요 시간 요청 |

## 2. 생성 계보

모든 파일은 결정적 시나리오 템플릿과 메모리 `CalendarEnv`에서 생성합니다.
같은 seed에는 같은 초기 상태, 사용자 요청, 목표 행동이 생성됩니다.
사용자 요청의 일정 제목은 마지막 한글 음절에 종성이 있으면 목적격 조사 `을`을, 종성이 없으면 `를`을 연결합니다.
예를 들어, `프로젝트 점검을`과 `기획 회의를`을 생성합니다.

SFT의 assistant 도구 호출, 도구 관찰, 마지막 자연어 답변은 결정적 전문가 정책이 환경을 실행해 만든 궤적입니다.
RLVR 데이터에는 정답 assistant completion을 넣지 않습니다.
학습 중 Student가 생성한 도구 궤적과 최종 답변을 검증기가 채점합니다.

공개한 다섯 분할에는 Teacher 변형을 적용하지 않았습니다.
Teacher를 사용하는 선택 경로는 사용자 발화의 표현만 바꿉니다.
모델은 `cyankiwi/Qwen3.6-35B-A3B-AWQ-4bit`, revision은 `00fcea2d3bcf5389b518d4fc082e5590e0ba4844`입니다.

## 3. 검증

전문가 궤적은 메모리 `CalendarEnv`에서 실행합니다.
분할별 검증 계약은 다음과 같습니다.

| 분할 | 검증 모드 | 저장 조건 |
|---|---|---|
| `sft_train`, `sft_validation` | `strict` | 목표 상태와의 정확한 일치, 4회 이하의 도구 turn, 도구 호출 형식, ID 근거성, Calendar 규칙과 목표 행동 통과 |
| `rlvr_train`, `dev`, `final` | `strict` 기초 검증 뒤 `semantic`, `dense=True` | 목표 상태 도달, 4회 이하의 도구 turn, 여섯 dense reward 성분이 모두 1.0 |

RLVR, dev, final의 dense reward는 `schema_reward`, `grounding_reward`, `safety_fraction`, `required_read_coverage`, `target_call_coverage`, `semantic_final_success`를 검사합니다.
SFT 학습과 검증, RLVR 학습, dev, final은 서로 겹치지 않는 날짜 범위를 사용합니다.
dev 체크포인트 선택과 final 평가는 서버 시드 42와 `VLLM_BATCH_INVARIANT=1`을 적용한 vLLM 서버에서 실행합니다.

## 4. 생성

```bash
PYTHONPATH=. python -m scripts.synthesize_calendar_sft
PYTHONPATH=. python -m scripts.synthesize_calendar_rlvr
```

## 5. 제한

시나리오는 메모리 Calendar 환경에서 실행되는 합성 데이터입니다.
실제 일정 서비스의 인증, 권한, 개인정보, 네트워크 장애를 포함하지 않습니다.
final 결과는 정의된 다섯 템플릿의 도구 사용과 안전 정책을 측정하며, 일반적인 Agent 성능을 나타내지 않습니다.
