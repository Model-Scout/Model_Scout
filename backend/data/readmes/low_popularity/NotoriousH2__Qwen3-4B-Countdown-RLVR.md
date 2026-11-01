---
license: apache-2.0
language:
- ko
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen3-4B
datasets:
- NotoriousH2/countdown-rlvr
tags:
- qwen3
- rlvr
- reasoning
- countdown
---

# Qwen3-4B Countdown RLVR

이 모델은 Countdown 문제의 명시적인 수식 검증 보상으로 Qwen3-4B를 GRPO 학습한 병합 모델입니다.
숫자 4개를 각각 한 번 사용하고, 사칙연산으로 목표값을 만드는 수식을 생성합니다.
학습 데이터는 `NotoriousH2/countdown-rlvr` revision `257a0edd9e5ec3fed345c80d21d9c73d09995ecb`를 사용했습니다.
학습은 1~480 step 전체에서 최대 completion 길이 3,072토큰을 사용했습니다. step 120의 학습 상태를 복원해 이어서 진행했습니다.

## 1. 사용

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "NotoriousH2/Qwen3-4B-Countdown-RLVR"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
```

LoRA 파일과 토크나이저는 `adapter/`에 있습니다.
학습 설정은 `training_config.json`, 전체 학습 기록은 `history.json`에서 확인할 수 있습니다.
구간별 completion 길이와 체크포인트 재개 지점은 `training_provenance.json`에 있습니다.

검증 분할의 후보별 지표와 공개 체크포인트 선택 결과는 `checkpoint_selection.json`에 있습니다.
공개 병합 모델은 `checkpoint-360`을 사용합니다.
검증 평가는 서버 시드 42와 `VLLM_BATCH_INVARIANT=1`을 사용합니다.
test 평가는 서버 시드 42와 `VLLM_BATCH_INVARIANT=1`을 사용합니다.


## 2. 평가

Base와 RLVR 모델을 같은 test 분할과 생성 설정으로 평가했습니다.

| 모델 | pass@1 | pass@8 | 유효 수식 비율 | 평균 응답 토큰 |
|---|---:|---:|---:|---:|
| Base | 15.2% | 52.7% | 14.1% | 1775.1 |
| RLVR | 57.4% | 88.7% | 56.8% | 1737.6 |

문제별 응답과 점수는 `evaluation.json`에 있습니다.

## 3. 제한

평가 범위는 숫자 4개와 사칙연산으로 제한됩니다.
자유 형식 증명이나 수학적 추론 전반의 성능을 나타내지 않습니다.

## 4. 실제 출력 사례

학습 전후의 실제 응답을 선별한 사례는 [learning_examples.json](./learning_examples.json)에 있습니다. Reasoning 응답은 모델이 생성한 `think`와 `answer` 태그를 포함한 원문을 보존합니다.
