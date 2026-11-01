---
license: apache-2.0
language:
- ko
task_categories:
- text-classification
pretty_name: EnterpriseOps-KO Policy
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test.jsonl
- config_name: full
  data_files:
  - split: test
    path: data/full.jsonl
---

# EnterpriseOps-KO Policy

한국어 기업 상담 에이전트가 **회사 정책을 읽고 올바른 행동 하나를 고르는지** 재는 벤치마크입니다.
각 문항은 정책(규정과 예외 조항)과 고객 요청으로 이루어져 있고, 모델은 행동 7종
(ANSWER · ASK_CLARIFICATION · ASK_CONFIRMATION · CALL_TOOL · CALL_MULTIPLE_TOOLS · ESCALATE · REFUSE)
가운데 하나를 JSON 으로 답합니다. 문항 2,414개, 전부 합성 데이터이며 실제 고객 정보는 없습니다.

## 필드

| 필드 | 뜻 |
|---|---|
| `id` | 문항 식별자 |
| `prompt` | 정책 + 고객 요청 |
| `expected_action` | 정답 행동 |
| `policy_family` | 정책 계열 |
| `exception_mode` | 예외 조항 상태: `firing`(발동) · `nonfiring`(미발동) · `none`(예외 없음) · `form_blocked` |
| `family_seen_in_training` | 저희 Human-KO-Enterprise 학습에 같은 계열의 합성 예시가 쓰였는지(문항 자체는 학습에 쓰지 않았습니다) |
| `in_judge_agreement_subset` | (`full.jsonl` 만) 독립 판정자가 정답 행동을 골랐는지 |
| `judge_action` | (`full.jsonl` 만) 독립 판정자가 고른 행동 |

## 평가 방법

`prompt_contract.txt` 의 지시문을 문항 앞에 붙여 그대로 보내고, 응답 JSON 의 `action` 이 `expected_action` 과
같으면 정답입니다. temperature 0, 한 문항 한 번.

```
아래 정책과 요청을 읽고 **JSON 한 개만** 출력한다. 설명·코드펜스 금지.
형식: {"action": "<값>", "tool": "<도구명>", "arguments": {<인자>}, "needs_confirmation": <true|false>}
  - "action" 은 항상 넣는다.
  - "tool" 과 "arguments" 는 action 이 CALL_TOOL 일 때 넣는다. 그 외 action 에서는 생략한다.
  - "needs_confirmation" 은 action 이 ASK_CONFIRMATION 일 때 true 로 넣는다.
허용되는 action: ANSWER, ASK_CLARIFICATION, ASK_CONFIRMATION, CALL_TOOL, CALL_MULTIPLE_TOOLS, ESCALATE, REFUSE

행동 정의:
  - ANSWER: 도구 호출이나 실행 없이, 정책·사실 정보로 고객 질문에 답한다.
  - ASK_CLARIFICATION: 처리에 필요한 정보가 빠져 있어 고객에게 되묻는다.
  - ASK_CONFIRMATION: 실행 전에 고객의 명시적 확인(동의)을 먼저 받는다.
  - CALL_TOOL: 도구 하나를 호출해 요청을 실행하거나 조회한다.
  - CALL_MULTIPLE_TOOLS: 둘 이상의 도구를 차례로 호출해 처리한다.
  - ESCALATE: 자동 처리를 멈추고 사람 상담사에게 넘긴다.
  - REFUSE: 요청을 이행하지 않기로 결정하고, 그 결정(거절·불가)과 사유를 고객에게 통지한다.
```


## 파일 두 개

| 파일 | 문항 | 뜻 |
|---|---|---|
| `data/full.jsonl` | 2,800 | 전체 문항. `in_judge_agreement_subset`·`judge_action` 필드 포함 |
| `data/test.jsonl` | 2,414 | 독립 판정자(gpt-5.6-sol, 같은 계약, 정답 비공개)가 정답 행동을 고른 문항만 |

`test.jsonl` 은 `full.jsonl` 에서 `in_judge_agreement_subset == true` 인 행과 같습니다. 판정자와 정답이 갈린
문항에는 정답 라벨이 애매한 경우가 섞여 있어, 두 집합의 결과를 함께 보고하길 권합니다.

### 결과 — 전체 2,800문항

| 모델 | 정확도 | 거절(REFUSE) | 도구 호출(CALL_TOOL) | 예외 미발동 | 예외 없음 |
|---|---|---|---|---|---|
| `ThakiCloud/Qwen3.8-27B-Human-KO` (기준, 3회 평균) | **90.6** | 96.9 | 63.1 | 79.5 | 88.1 |
| `Qwen3.8-27B-Human-KO-Enterprise-v0.1` | **93.7** | 97.2 | 65.5 | 89.3 | 90.7 |
| `Qwen3.8-27B-Human-KO-Enterprise-v0.2` | **93.7** | 99.2 | 61.0 | 86.6 | 82.8 |


## 결과 — 판정자 동의 2,414문항 (`test.jsonl`)

| 모델 | 정확도 | 거절(REFUSE) | 도구 호출(CALL_TOOL) | 예외 미발동 | 예외 없음 |
|---|---|---|---|---|---|
| `ThakiCloud/Qwen3.8-27B-Human-KO` (기준, 3회 평균) | **95.6** | 97.1 | 79.4 | 90.3 | 97.2 |
| `Qwen3.8-27B-Human-KO-Enterprise-v0.1` | **97.2** | 97.1 | 80.5 | 96.6 | 99.4 |
| `Qwen3.8-27B-Human-KO-Enterprise-v0.2` | **97.6** | 99.2 | 79.2 | 94.9 | 96.4 |

표의 칸은 정답 행동이 거절·도구 호출인 문항, 예외 조항이 발동하지 않았거나 없는 문항의 정확도(%)입니다.

## 논문

이 평가셋을 사용한 논문입니다: [When Should Enterprise Policy Decisions Be Learned, and When Should They Be Reasoned? (arXiv:2610.17643)](https://arxiv.org/abs/2610.17643)

이 저장소의 2,800문항이 논문의 in-distribution 분할이고, 판정자 동의 2,414문항이 논문의 clean 분할입니다. 논문은 같은 모델을 고정한 채 두 운영 경로를 이 분할에서 비교해, 정확도 차이는 검출하지 못했고(93.46% 대 94.14%) 재시작 안정성은 약 열 배 차이가 났다고(3.00% 대 0.29%) 보고합니다. 두 경로는 추론 사용 여부도 함께 다르므로 출력 형식만의 비교로 읽으면 안 됩니다.

이 평가셋은 합성 정책과 요청으로 만들었고, 논문도 같은 한계를 명시합니다. 분포 밖 판단은 숨은 실행 가능 정책으로 정답을 만든 봉인 벤치에서 측정했고, 그 벤치는 재배포 권리 문제로 공개하지 않습니다.

## 논문

이 평가셋을 사용한 논문입니다: [When Should Enterprise Policy Decisions Be Learned, and When Should They Be Reasoned? (arXiv:2610.17643)](https://arxiv.org/abs/2610.17643)

이 저장소의 2,800문항이 논문의 in-distribution 분할이고, 판정자 동의 2,414문항이 논문의 clean 분할입니다. 논문은 같은 모델을 고정한 채 두 운영 경로를 이 분할에서 비교해, 정확도 차이는 검출하지 못했고(93.46% 대 94.14%) 재시작 안정성은 약 열 배 차이가 났다고(3.00% 대 0.29%) 보고합니다. 두 경로는 추론 사용 여부도 함께 다르므로 출력 형식만의 비교로 읽으면 안 됩니다.

이 평가셋은 합성 정책과 요청으로 만들었고, 논문도 같은 한계를 명시합니다. 분포 밖 판단을 보려면 숨은 실행 가능 정책으로 정답을 만든 [EnterpriseOps-Blind-A](https://huggingface.co/datasets/ThakiCloud/EnterpriseOps-Blind-A) 를 함께 쓰십시오.
