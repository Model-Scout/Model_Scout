---
base_model: Qwen/Qwen3-0.6B
language:
- ko
pipeline_tag: text-generation
tags:
- trl
- sft
datasets:
- NotoriousH2/meeting-to-json-ko
---
# Qwen3-0.6B-JSON-SFT

한국어 회의록에서 meeting_metadata / action_items / decisions / blockers JSON을 추출하도록 Qwen/Qwen3-0.6B를 full fine-tuning한 모델입니다.
[sllm_practice](https://github.com/NotoriousH2/sllm_practice) `[실습] 10. Instruction Data를 이용한 파인 튜닝`의 산출물입니다 (커밋 aa9338b).

## 학습

| 항목 | 값 |
|---|---|
| 데이터 | `NotoriousH2/meeting-to-json-ko` train 1,115개 (10%는 early stopping 모니터링) |
| 프롬프트 | `json_eval.SYSTEM_PROMPT` + `회의록:\n\n{meeting}`, thinking 비활성 |
| 방식 | SFT, loss_type=chunked_nll, packing, max_length 3072 |
| 하이퍼파라미터 | 3 epoch, lr 5e-6 cosine (warmup 5%), batch 2 × grad accum 8, paged_adamw_8bit, bf16 |

## 평가 (test 273개, temperature 0)

| 지표 | Qwen3-0.6B | 이 모델 |
|---|---|---|
| parse_rate | 97.8% | 98.9% |
| schema_compliance | 96.3% | 97.8% |
| semantics_pass_rate | 84.5% | 96.4% |
| field_f1_mean | 39.3% | 56.5% |
| struct_f1_mean | 47.2% | 65.7% |
| text_f1_mean | 15.4% | 28.3% |

지표는 저장소의 `json_eval.py`가 계산합니다. `field_f1`은 리스트 항목을 같은 항목끼리 짝지어 비교하고, 서술 필드는 문자 bigram 유사도로 채점합니다.
