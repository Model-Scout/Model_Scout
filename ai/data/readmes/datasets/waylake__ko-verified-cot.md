---
language:
- ko
license: apache-2.0
task_categories:
- text-generation
- question-answering
tags:
- korean
- reasoning
- chain-of-thought
- verified
- rejection-sampling
- synthetic
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: train
    path: train.jsonl
---

# ko-verified-cot

**2,016 short Korean reasoning traces whose final answer was verified against a ground-truth
answer key.** Wrong reasoning was thrown away, not kept.

[![GitHub](https://img.shields.io/badge/GitHub-kogemma--e2b-181717?logo=github)](https://github.com/waylake/kogemma-e2b)
[![Model](https://img.shields.io/badge/model-KoGemma--E2B-4285F4)](https://huggingface.co/waylake/KoGemma-E2B)

## How it was built

1. Sample multiple-choice questions from the **train split** of
   [KMMLU](https://huggingface.co/datasets/HAERAE-HUB/KMMLU) (45 subjects) — test split is never
   touched, so downstream evaluation stays clean.
2. Ask the teacher (`ox-alpha-free`) for a **short** Korean chain of thought (3–4 sentences) ending
   in `정답: X`. The teacher never sees the answer key.
3. Extract the predicted letter and compare with the gold label. **Keep only matches.**
4. Strip markdown, drop truncated traces, normalise the ending to `정답: X`.

Teacher accuracy on those questions was **80–85%**; the same base model we later fine-tuned scored
53% (train) / 32% (test). So the released traces are a strictly better-than-base subset.

## Why short traces

Small models (≤3B) get **worse** when trained on long/complex reasoning chains — see
[*Small Models Struggle to Learn from Strong Reasoners*](https://arxiv.org/abs/2502.12143)
(Qwen2.5-1.5B: 27.0 with long CoT vs 34.2 with short CoT). Traces here are deliberately capped at
3–4 sentences to stay inside a small model's learnable range.

## Schema

```json
{
  "messages": [
    {"role": "system", "content": "너는 한국어로 정확하게 추론하고 답하는 AI 비서다."},
    {"role": "user", "content": "<질문>\n\nA. …\nB. …\nC. …\nD. …\n\n핵심 근거만 3~4문장으로 …"},
    {"role": "assistant", "content": "<3~4문장 추론>\n\n정답: B"}
  ],
  "source": "ox-alpha-free"
}
```

The user turn keeps a fixed instruction suffix so that training and evaluation prompts match
exactly — misaligned prompt formats were the single largest source of measurement error in this
project.

## What we learned using it (honest results)

Fine-tuning `gemma-4-E2B-it` (2.3B effective) on these traces mixed 1:1 with the model's own
verified CoT (the *Mix Distillation* recipe):

| Metric (KMMLU test, 600 questions) | base | after training |
|---|---|---|
| CoT accuracy | 0.3200 | 0.3250 |
| CoT format failures | 48 (8.0%) | **27 (4.5%)** |

Accuracy did **not** move outside sampling error; format compliance clearly improved. Verified
teacher traces fix *how* a small model answers, not *how much it knows* — the bottleneck at 2.3B
is capacity, not data.

Also worth recording: measuring on 200 questions showed a fake +3.0 pp gain that vanished at 600.

## Limitations

- Multiple-choice reasoning only (KMMLU-style), Korean only.
- Verified means "final answer matched"; individual reasoning steps are not step-verified.
- Derived from KMMLU train questions — do not train and then claim KMMLU test gains without
  checking split hygiene.

## Citation

```bibtex
@misc{ko-verified-cot-2026,
  title  = {ko-verified-cot: answer-verified short Korean reasoning traces},
  author = {waylake},
  year   = {2026},
  url    = {https://huggingface.co/datasets/waylake/ko-verified-cot}
}
```
