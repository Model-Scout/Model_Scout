---
language:
- ko
- en
task_categories:
- text-generation
tags:
- agentic
- tool-use
- function-calling
- korean
- multi-turn
- synthetic
size_categories:
- 10K<n<100K
configs:
- config_name: agentic
  data_files:
  - split: train
    path: agentic/sft.jsonl
- config_name: agentic_meta
  data_files:
  - split: train
    path: agentic/meta.jsonl
- config_name: dual_control
  data_files:
  - split: train
    path: dual_control/sft.jsonl
- config_name: dual_control_meta
  data_files:
  - split: train
    path: dual_control/meta.jsonl
---

# 한국어 에이전트 도구 호출 데이터셋 (Korean Agentic Tool-Call Dataset)

한국어 중심(영어 시스템 프롬프트 혼합) **도구 호출 / 멀티턴 상담** 합성 데이터셋입니다.
도구 카탈로그를 합성하고, 그 카탈로그 안에서 궤적을 만든 뒤, **프로그램 검증기**로 걸러낸
통과분만 담았습니다. LLM 판정은 라벨로만 쓰고 채택 여부를 결정하지 않습니다.

**11,931행 중 10,642행(89.2%)이 멀티턴**입니다.

## 두 트랙

| | `agentic` | `dual_control` |
|---|---|---|
| 형태 | 단발 요청 → 도구 연쇄 (+ 후속 사용자 턴) | 고객 시뮬레이터와의 상담 |
| 행 | 7,252 | 4,679 |
| 멀티턴 | 5,968 (82.3%) | 4,674 (99.9%) |
| 사용자 턴 | 1–4 | 2–10 |
| 도구 호출/행 | 4.11 | 2.33 |
| 행당 도구 수 (중앙값) | 18 | 13 |
| 토큰 p50 / max | 3,220 / 16,283 | 2,899 / 9,882 |

`agentic`은 7개 역량으로 라벨링됩니다 — `single_call`, `chain`, `recover`, `confirm_risky`,
`clarify`, `disambiguate`, `refuse_fabricate`.

`dual_control`은 **고객만 할 수 있는 동작**이 있는 환경입니다. 에이전트는 그것을 대신 수행할 수
없고 안내만 할 수 있으며, 고객이 실제로 수행하면 공유 상태가 바뀝니다. 필요한 식별자 일부는
첫 발화에서 **의도적으로 보류**되어, 올바른 값으로 호출했다는 사실 자체가 "에이전트가 물었다"는
증거가 됩니다.

## 사용자 턴 분포

```
agentic       1턴 1,284   2턴   171   3턴 4,929   4턴   868
dual_control  2턴    56   3턴   246   4턴   525   5턴   570   6턴   584
              7턴   509   8턴   393   9턴   467  10턴 1,324
```

## 스키마

`{track}/sft.jsonl` — 학습용

```json
{"messages": [...], "tools": [...], "category": "chain", "lang": "ko", "pair_id": "..."}
```

`messages`는 OpenAI 대화 형식입니다. `assistant` 턴의 `tool_calls[].function.arguments`는
**dict**이며 JSON 문자열이 아닙니다 — 채팅 템플릿이 dict를 요구하고, 문자열이면 구조 검증은
통과한 뒤 렌더에서 `TypeError`로 죽습니다. `tool` 턴이 관측을 담습니다.

`{track}/meta.jsonl` — 같은 행 + 계보

| 필드 | 뜻 |
|---|---|
| `category` | 역량 라벨 (`dual_control`은 단일) |
| `domain` | 도구 카탈로그의 도메인 |
| `labels` | 검증기가 남긴 관측 (`goal_achieved`, `withheld_obtained`, `tool_calls` 등) |
| `risk_map` | 도구명 → `read`/`write`/`irreversible`/`outbound` |
| `prompt_axes` | 시스템 프롬프트 구성축 (역할·규칙형식·런타임형식·언어·주입된 시계) |
| `tokens` | 학생 토크나이저 기준 길이 |
| `rounds` | assistant 턴 수 |

`stats.json`에 전체 집계가 있습니다.

## 이 데이터가 실제로 강제하는 것

각 항목은 **실측으로 잡힌 결함**에 대응합니다. 통과분에는 아래가 없습니다.

* **날조 없음** — 호출 인자의 식별자는 그 호출 시점까지 사용자가 말했거나 도구가 돌려준 값
  안에 있어야 합니다. 순서에 민감하게 검사하므로, 나중에 등장한 값이 앞선 날조를 사면하지
  못합니다. 날짜·시각과 표기 차이(`010-1234-5678` vs `01012345678`)는 날조가 아닙니다.
* **자리표시자 인자 없음** — `{"complaint_id": "임시로 찾은 민원 ID"}` 같은 값은 제거됩니다.
* **내부 식별자 노출 없음** — assistant 발화에 도구명·인자명이 등장하지 않습니다.
  `계좌번호(account_id)가 필요합니다`는 제거되고 `계좌번호를 알려주시겠어요?`만 남습니다.
* **호출 대신 예고하지 않음** — `1. 주문 목록 조회 - list_user_orders로 …` 같은 계획 나열 제거.
* **근거 없는 완료 주장 없음** — 상태 변경 호출 없이 "변경이 완료되었습니다"라고 말하는 행 제거.
* **행동 목표에는 행동** — 목표가 쓰기를 요구하면 (선언된 그 도구가 아니라) 쓰기 도구를 실제로
  호출해야 합니다. 조회만 하고 "다시 문의해 주세요"로 끝나는 대화는 제거됩니다.
* **정체 반복 없음** — 같은 인사가 되풀이되는 꼬리는 잘라냈습니다. 턴 수만 채운 대화를 막습니다.
* **연속 assistant 턴 없음** — 사용자 입력 없이 비서가 두 번 답하는 행이 없습니다.
* **템플릿 렌더 통과** — 전 행이 실제 채팅 템플릿으로 렌더됩니다 (실패 0).

경로는 강제하지 않습니다. 선언된 도구 목록을 그대로 요구하면 73%가 버려지고 가장 흔한 원인이
"다른 경로로 같은 목표 달성"이었습니다. 결함만 기각하고 나머지는 통과시킵니다.

## 다양성

시스템 프롬프트는 행마다 다릅니다 — 역할 6종 × 규칙 형식 4종(bullet/numbered/prose/xml) ×
런타임 형식 5종(bullet/xml/markdown/yaml/inline) × 선택적 메타 필드, 그리고 **주입된 시계**가
2023-01~2026-12에 걸쳐 흩어져 있습니다. 시계를 고정하면 모델이 그 날짜를 암기하고, 아예 없으면
도구 결과에 무관한 날짜가 쏟아집니다.

시스템 프롬프트 언어는 한국어 65% / 영어 35%입니다. 많은 실제 환경이 사용자 언어와 무관하게
영어 시스템 프롬프트를 씁니다 — 한국어 프롬프트만으로 학습하면 "한국어 대화면 한국어 지시"를
세계에 대한 사실로 배웁니다.

## 호출된 도구의 위험도

```
agentic       read 27,397   write 1,448   outbound   484   irreversible 412
dual_control  read  5,264   outbound 3,129   write 1,229   irreversible 671
```

## 한계 — 알고 쓰십시오

* **위험 호출의 사전 확인이 일관되지 않습니다.** 되돌릴 수 없거나 외부로 나가는 호출이 있는
  행 중 **호출 전에 사용자 확인을 구한 것은 약 20%**입니다. `risk_map`으로 직접 필터링해서
  쓰시는 것을 권합니다.
* **길이가 짧습니다.** p50이 3,220토큰입니다. 32k 컨텍스트 학습에는 긴 카탈로그·긴 대화가
  더 필요합니다.
* **`agentic`의 후속 턴은 지시어를 강제합니다** (`방금 그거`, `그 중에서`). 턴 경계를 넘는 문맥
  유지를 겨냥한 설계이며, 자기완결적인 두 번째 요청은 배제됩니다.
* **도구 결과는 시뮬레이션입니다.** 누적 원장에 대해 순차적으로 생성되어 일관되지만, 실제
  시스템의 응답이 아닙니다. 실패는 첫 호출에 의도적으로 주입된 경우가 있습니다.
* **합성 데이터입니다.** 인물·계좌·주문번호는 전부 가상이며 실제 개인정보가 아닙니다.
* 라이선스는 아직 지정하지 않았습니다. 상업적 사용을 검토 중이라면 소유자에게 문의하십시오.

## 로드

```python
from datasets import load_dataset

ds = load_dataset("jungsanghyun/ko-agentic-toolcall", "agentic", split="train")
dc = load_dataset("jungsanghyun/ko-agentic-toolcall", "dual_control", split="train")

# 위험 호출에 사전 확인이 있는 행만
meta = load_dataset("jungsanghyun/ko-agentic-toolcall", "agentic_meta", split="train")
```
