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

## 학습

| 항목 | 값 |
|---|---|
| 데이터 | `NotoriousH2/meeting-to-json-ko` train 1,115개 (10%는 early stopping 모니터링) |
| 프롬프트 | JSON 스키마를 안내하는 시스템 프롬프트 + `회의록:\n\n{meeting}`, thinking 비활성 |
| 방식 | SFT, loss_type=chunked_nll, packing, max_length 3072 |
| 하이퍼파라미터 | 3 epoch, lr 5e-5 cosine (warmup 5%), batch 2 × grad accum 8, paged_adamw_8bit, bf16 |

## 평가 (test 273개, temperature 0)

| 지표 | Qwen3-0.6B | 이 모델 |
|---|---|---|
| parse_rate | 97.8% | 99.6% |
| schema_compliance | 96.3% | 99.6% |
| semantics_pass_rate | 85.1% | 99.5% |
| field_f1_mean | 39.4% | 71.1% |
| struct_f1_mean | 47.6% | 79.2% |
| text_f1_mean | 15.0% | 46.1% |

`field_f1`은 리스트 항목을 같은 항목끼리 짝지어 비교하고, 서술 필드는 문자 bigram 유사도로 채점합니다.
