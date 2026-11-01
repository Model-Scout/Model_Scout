---
license: apache-2.0
language:
- ko
library_name: transformers
pipeline_tag: text-generation
base_model: NotoriousH2/Qwen3-4B-Calendar-Agent-SFT
datasets:
- NotoriousH2/calendar-agent-benchmark
tags:
- qwen3
- tool-calling
- function-calling
- agents
- grpo
- rlvr
- reinforcement-learning
- calendar
- korean
---

# Qwen3-4B Calendar Agent RLVR

Qwen3-4B Calendar Agent RLVR는 한국어 일정 관리 도구를 호출하는 4B 파라미터 병합 모델입니다.
Calendar 도구의 실행 궤적과 최종 상태를 보상으로 평가하여 GRPO로 학습했습니다.

다음 행동을 학습 범위에 포함합니다.

- 일정 조회, 생성, 수정, 삭제
- 필수 정보가 없을 때 사용자에게 정보 요청
- 삭제 전 사용자 승인 확인
- 일정 충돌 확인과 빈 시간 생성
- 여러 참석자의 공통 가능 시간 탐색

## 1. 사용

저장소 루트에는 병합 모델이 있으며, `adapter/`에는 LoRA 어댑터가 있습니다.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "NotoriousH2/Qwen3-4B-Calendar-Agent-RLVR"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype="auto",
    device_map="auto",
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "search_events",
            "description": "지정한 날짜의 일정을 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {"type": "string", "description": "YYYY-MM-DD"}
                },
                "required": ["date"],
            },
        },
    }
]
messages = [
    {
        "role": "system",
        "content": "사용자 요청을 처리하는 데 필요한 일정 도구를 호출하세요.",
    },
    {"role": "user", "content": "2039-07-05 일정을 알려줘."},
]

prompt = tokenizer.apply_chat_template(
    messages,
    tools=tools,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,
)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512)
response = outputs[0, inputs.input_ids.shape[1] :]
print(tokenizer.decode(response, skip_special_tokens=False))
```

모델은 도구 호출 정보를 생성합니다.
호출 실행과 도구 결과 전달은 호스트 애플리케이션에서 처리해야 합니다.

## 2. 학습 보상

같은 요청에서 16개 응답을 생성하고, 그룹 안의 보상 차이로 Advantage를 계산했습니다.

| 보상 | 가중치 | 평가 대상 |
|---|---:|---|
| 안전 규칙 | 0.25 | 필수 정보와 사용자 승인 준수 |
| 절차 진행 | 0.35 | 조회, 확인, 성공한 도구 실행 |
| 최종 성공 | 0.40 | 최종 Calendar 상태와 사용자 요청의 일치 |

전체 행동군을 다룬 첫 학습 단계에서 96개 그룹 중 68개 그룹이 서로 다른 보상을 포함했습니다.
최종 성공 여부가 같은 응답도 절차 진행 점수로 구분하여 학습 신호를 구성했습니다.

## 3. 평가

400개 합성 시나리오에서 실제 도구 루프를 실행하고 최종 상태를 평가했습니다.

| 모델 | 유효 도구 호출 | 정책 준수 | Task Success | 평균 도구 호출 |
|---|---:|---:|---:|---:|
| Qwen3-4B Base | 100.00% | 80.00% | 20.00% | 0.80 |
| Calendar Agent SFT | 100.00% | 89.25% | 89.00% | 2.55 |
| Calendar Agent RLVR | 100.00% | 99.25% | 99.00% | 2.38 |

SFT와 사례별로 비교하면 RLVR 모델은 41개 실패를 성공으로 전환했고, 1개 성공을 실패로 전환했습니다.
순증은 40개이며 전체 Task Success 차이는 10.00%p입니다.

템플릿별 Task Success는 다음과 같습니다.

| 템플릿 | SFT | RLVR | 전체 |
|---|---:|---:|---:|
| 필수 정보 요청 | 60 | 80 | 80 |
| 삭제 승인 요청 | 59 | 80 | 80 |
| 충돌 후 생성 | 77 | 76 | 80 |
| 승인 후 삭제 | 80 | 80 | 80 |
| 다중 참석자 생성 | 80 | 80 | 80 |

집계값은 [evaluation.json](./evaluation.json)에 있습니다.

## 4. 행동 사례

필수 정보가 없는 생성 요청에서는 임의의 시각을 정해 일정을 생성하지 않고 시작 시각과 소요 시간을 요청합니다.

충돌 시 대체 시간 등록을 승인한 요청에서는 기존 일정을 조회하고 빈 시간을 찾은 뒤, 충돌하지 않는 시간에 일정을 생성합니다.

## 5. 제한

이 모델은 `Asia/Seoul` 시간대의 합성 시나리오와 메모리 Calendar 환경에서 학습하고 평가했습니다.
실제 일정 서비스의 인증, 권한, 개인정보 처리, 네트워크 장애는 평가 범위에 포함하지 않습니다.

충돌 후 생성은 SFT 77/80, RLVR 76/80으로 다른 템플릿보다 낮습니다.
외부 Calendar 시스템에 적용할 때는 충돌 복구와 도구 오류 이후의 재시도를 별도로 평가해야 합니다.
