---
base_model: Qwen/Qwen3-0.6B
language:
- ko
pipeline_tag: text-generation
tags:
- trl
- sft
---

# Qwen3-0.6B-JSON-SFT

회의록→JSON 추출 SFT (학생 0.6B 교체 실험, 시나리오 1)

2026-07-19 sllm_practice 커리큘럼 개선 실험 산출물 (fa2e1ce의 experiments/results/REPORT.md 참조).
평가 지표는 json_eval.py (parse_rate / schema_compliance / semantics_pass_rate / field_f1_mean).

Qwen/Qwen3-0.6B를 meeting_to_json_train.jsonl 1,199개로 full FT (no-think). old_eval 300개 기준 parse 98.0 / schema 96.3 / semantics 96.1 / field_F1 51.4% (base 41.6%). 학습 15.4분(A40).
