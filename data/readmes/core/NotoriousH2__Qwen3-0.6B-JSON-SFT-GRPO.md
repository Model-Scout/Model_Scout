---
base_model: NotoriousH2/Qwen3-0.6B-JSON-SFT
language:
- ko
pipeline_tag: text-generation
tags:
- trl
- grpo
- unsloth
datasets:
- NotoriousH2/meeting-to-json-ko
---
# Qwen3-0.6B-JSON-SFT-GRPO

`NotoriousH2/Qwen3-0.6B-JSON-SFT`를 RLVR(GRPO)로 추가 학습하고 LoRA를 병합한 16bit 모델입니다.
[sllm_practice](https://github.com/NotoriousH2/sllm_practice) `[실습] 15. GRPO와 RLVR을 이용한 강화 학습`의 산출물입니다 (커밋 aa9338b).

## 학습

| 항목 | 값 |
|---|---|
| 데이터 | train에서 600개 표본, 학습 중 평가는 test에서 64개 표본 |
| 보상 | `json_eval.rlvr_reward`: 파싱·schema 실패 0, 그 외 field_f1 |
| 방식 | GRPO (loss_type=dapo, beta 0.04, epsilon 0.2), LoRA r16 / alpha 32 |
| 생성 | num_generations 8, max_completion_length 1024, temperature 0.6, top_p 0.95, top_k 20 |
| 하이퍼파라미터 | 1 epoch (600 step), lr 1e-5 cosine, batch 2 × grad accum 4, paged_adamw_8bit, bf16 |

## 평가 (test 273개, temperature 0)

| 지표 | SFT | 이 모델 |
|---|---|---|
| parse_rate | 98.9% | 99.6% |
| schema_compliance | 97.8% | 98.9% |
| semantics_pass_rate | 96.4% | 97.9% |
| field_f1_mean | 56.5% | 61.6% |
| struct_f1_mean | 65.7% | 70.7% |
| text_f1_mean | 28.3% | 31.4% |
