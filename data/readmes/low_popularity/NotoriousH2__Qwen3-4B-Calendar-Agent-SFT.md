---
license: apache-2.0
language:
- ko
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen3-4B
datasets:
- NotoriousH2/calendar-agent-benchmark
tags:
- qwen3
- tool-calling
- agents
- sft
---

# Qwen3-4B Calendar Agent SFT

이 모델은 Calendar 일정 관리, 다중 참석자 생성, 읽기 전용 대조군의 성공 궤적에서 assistant 생성 토큰만 학습한 LoRA SFT 병합 모델입니다.
도구 호출은 `Asia/Seoul` 시간대의 메모리 Calendar 환경을 대상으로 합니다.
학습 데이터는 `NotoriousH2/calendar-agent-benchmark` revision `0eab7124771d15af17766b67e2bf6fdf14ca8d27`를 사용했습니다.

## 1. 사용

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "NotoriousH2/Qwen3-4B-Calendar-Agent-SFT"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
```

LoRA 파일과 토크나이저는 `adapter/`에 있습니다.
학습 설정은 `training_config.json`, 전체 학습 기록은 `history.json`에서 확인할 수 있습니다.

공개 병합 모델은 정해진 SFT 학습의 종료 체크포인트를 사용합니다.
이 저장소는 `checkpoint-60`(학습 step 60)을 포함합니다.
선택 근거: 60 step으로 설정한 SFT 학습의 최종 체크포인트
데이터 해시, dev 지표, 모델 해시는 `selected_checkpoint.json`에 있습니다.
공개 dev 원시 결과와 선택 summary는 각각 `selection/dev_evaluation.json`과 `selection/dev_selection_summary.json`에 있습니다.
dev 평가는 서버 시드 42와 `VLLM_BATCH_INVARIANT=1`을 사용합니다.


## 2. 평가

모든 모델은 같은 final 시나리오에서 실제 도구 루프로 평가했습니다.

| 모델 | Valid Tool Call | Policy Compliance | Task Success | Average Tool Calls |
|---|---:|---:|---:|---:|
| Base | 100.00% | 80.00% | 20.00% | 0.80 |
| SFT | 100.00% | 89.25% | 89.00% | 2.55 |

시나리오별 궤적과 판정 근거는 `base_evaluation.json`과 `sft_evaluation.json`에 있습니다.

## 3. 제한

이 모델은 합성 시나리오와 메모리 Calendar 환경에서 학습했습니다.
실제 일정 서비스의 인증, 권한, 개인정보, 장애 복구를 처리하지 않습니다.
