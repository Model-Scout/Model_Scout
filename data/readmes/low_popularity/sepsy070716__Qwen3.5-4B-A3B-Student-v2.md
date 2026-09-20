---
license: apache-2.0
base_model:
  - Qwen/Qwen3.5-2B
  - Qwen/Qwen3.5-4B
library_name: transformers
pipeline_tag: text-generation
tags:
  - qwen3_5_moe
  - moe
  - upcycled
  - text-generation
  - research
language: [ko, en, zh, ja, es, de]
---

# Qwen3.5-4B-A3B-Student-v2

A text-only sparse-MoE release candidate built as a practical local alternative
to Qwen3.5-4B. It has 4.0B total parameters and 3.0B active parameters per
token. The initialization preserves Qwen3.5-2B behavior, while adding
output-neutral trainable capacity for later Qwen3.5-4B distillation.

This is an independently measured research release. It is not an official Qwen
model and does not include vision.

## Architecture

| Property | Value |
|---|---:|
| Total parameters | 3,995,901,760 |
| Active parameters/token | 2,995,560,256 |
| Transformer layers / hidden size | 24 / 2,048 |
| Experts / selected per token | 2 / 1 |
| Shared / routed intermediate width | 6,912 / 6,784 |
| Vision tower | No |
| Weight dtype | BF16 |

Each MoE layer initially computes one half of the original Qwen3.5-2B dense MLP
through the shared path and one half through the selected routed expert. The
two routed experts begin functionally identical. Additional neurons have random
gate/up projections and zero down projections, making them output-neutral but
trainable. Exact conversion metadata is in `conversion_manifest.json`.

## Evaluation

All reported results were produced locally on an Apple M4 with 32GB unified
memory. Raw JSON reports are included in `evaluation/`.

### Chat and sentence generation

The fixed gate contains 60 prompts: 10 each in Korean, English, Chinese,
Japanese, Spanish, and German. It covers facts, arithmetic, translation,
instruction following, and free-form sentence generation.

| Result | Score |
|---|---:|
| Non-degenerate/correct automatic checks | 60 / 60 |
| Languages meeting the gate | 6 / 6 |

Six chemical-formula answers used the correct Unicode spelling `H₂O`; the
scorer normalizes Unicode subscripts before comparison.

### Multilingual held-out LM loss

Four held-out FineWeb/FineWeb2 documents per language, 128 tokens per document:

| Model | Mean loss | Relative to Qwen3.5-4B |
|---|---:|---:|
| Qwen3.5-4B | 2.9399 | 1.000x |
| This model | 3.2085 | 1.091x |
| Qwen3.5-2B | 3.2085 | 1.091x |

### Standard benchmark development subset

EleutherAI `lm-evaluation-harness==0.4.12`, zero-shot, BF16, first 100 examples
per task. These limited results are development indicators, **not full-task
benchmark claims**.

| Model | ARC-Easy acc_norm | HellaSwag acc_norm | Mean |
|---|---:|---:|---:|
| Qwen3.5-4B | 0.81 | 0.68 | 0.745 |
| This model | 0.73 | 0.62 | 0.675 |

The subset mean is 90.6% of the Qwen3.5-4B teacher mean.

### Local service gate

The included FastAPI service completed 20/20 consecutive non-streaming
`POST /v1/chat/completions` requests:

| Metric | Value |
|---|---:|
| Successful requests | 20 / 20 |
| Mean latency | 2.60 s |
| p95 latency | 3.57 s |
| MPS allocated memory | 7.62 GB |

Requests generated up to 16 new tokens. See `evaluation/openai_service_20.json`.

## Transformers usage

Use Transformers 5.13.0 or another version that provides
`Qwen3_5MoeForCausalLM`:

```python
import torch
from transformers import AutoTokenizer, Qwen3_5MoeForCausalLM

model_id = "sepsy070716/Qwen3.5-4B-A3B-Student-v2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = Qwen3_5MoeForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16,
    device_map="auto",
)

messages = [{"role": "user", "content": "대한민국의 수도는 어디인가요?"}]
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    enable_thinking=False,
    return_tensors="pt",
    return_dict=True,
).to(model.device)
output = model.generate(**inputs, max_new_tokens=64, do_sample=False)
print(tokenizer.decode(output[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Reproduction and service

`research_code/` contains the converter, multilingual loss comparison, 60-prompt
gate and scorer, plus the local OpenAI-compatible service and its 20-request
test. The service implements `GET /health`, `GET /v1/models`, and non-streaming
`POST /v1/chat/completions`.

## Limitations

- Current quality is inherited primarily from Qwen3.5-2B; the extra capacity has
  not yet received large-scale continued pretraining or teacher distillation.
- The 100-example ARC-Easy/HellaSwag figures are small development subsets and
  have substantial sampling uncertainty. Run the full tasks before making
  publication or production claims.
- This model is text-only and cannot replace the original model's vision path.
- The included server is a single-process local research server. It has no
  authentication, TLS, streaming, tool calling, or multi-worker support.
- Apply the same safety, bias, privacy, and factuality evaluation required for
  any deployment of the upstream Qwen models.

## License and attribution

Released under Apache-2.0, following the included upstream license. Derived from
Qwen3.5-2B weights and evaluated against Qwen3.5-4B. Qwen model names and
trademarks belong to their respective owners.
