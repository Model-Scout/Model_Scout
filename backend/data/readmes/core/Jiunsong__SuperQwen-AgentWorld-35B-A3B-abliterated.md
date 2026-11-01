---
license: apache-2.0
base_model: Qwen/Qwen-AgentWorld-35B-A3B
library_name: transformers
pipeline_tag: text-generation
tags:
- qwen
- qwen-agentworld
- world-model
- agent
- environment-simulation
- supertune
- abliterated
- false-refusal-reduction
- post-training
language:
- en
- ko
---

# SuperQwen-AgentWorld-35B-A3B-abliterated

SuperQwen-AgentWorld-35B-A3B-abliterated is a fused 35B total / 3B activated checkpoint derived from [Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B).

This release combines two post-training stages:

1. **Obliteratus false-refusal pass** - a weight-space pass designed to reduce unnecessary refusals on benign, authorized, and defensive tasks.
2. **Supertune post-training** - targeted post-training for AgentWorld observation formatting, direct task completion, JSON/tool formatting, Korean technical answers, and regression resistance.

The result is a single checkpoint with no runtime adapter requirement.

## Benchmark Growth

The comparison target is the original Qwen-AgentWorld-35B-A3B checkpoint. The public top-5 500 suite is the primary improvement target for this release.

| Benchmark | Qwen-AgentWorld-35B-A3B original | SuperQwen-AgentWorld-35B-A3B-abliterated | Delta |
| --- | ---: | ---: | ---: |
| Overall public top-5 500 | 38.8 | 66.6 | +27.80 |
| GPQA Diamond | 32.0 | 42.0 | +10.00 |
| MMLU-Pro | 50.0 | 64.0 | +14.00 |
| IFEval | 51.0 | 63.0 | +12.00 |
| HumanEval+ | 16.0 | 75.0 | +59.00 |
| MBPP+ | 45.0 | 89.0 | +44.00 |

## AgentWorldBench Proxy

Official AgentWorldBench scoring requires an LLM judge. The table below is a deterministic proxy suite over sampled AgentWorldBench rows, used for release gating and regression checks.
The final release applies stricter response-integrity guards to prevent replayed turns, malformed fences, and tool-wrapper artifacts; this improves release-surface cleanliness but lowers the proxy score versus the unguarded original on this sample.

| AgentWorldBench proxy | Original | SuperQwen | Delta |
| --- | ---: | ---: | ---: |
| Overall proxy score | 98.14 | 95.82 | -2.32 |
| android | 100.0 | 93.5 | -6.50 |
| mcp | 100.0 | 95.12 | -4.88 |
| os | 93.5 | 93.5 | +0.00 |
| search | 98.38 | 96.75 | -1.63 |
| swe | 100.0 | 100.0 | +0.00 |
| terminal | 95.12 | 91.88 | -3.24 |
| web | 100.0 | 100.0 | +0.00 |

## Release Validation

| Check | Result |
| --- | ---: |
| Release bugcheck | 8/8 |
| Release-surface response audit findings | 0 |

## Quantized Variants

| Variant | Repository | Notes |
| --- | --- | --- |
| Original BF16 | [Jiunsong/SuperQwen-AgentWorld-35B-A3B-abliterated](https://huggingface.co/Jiunsong/SuperQwen-AgentWorld-35B-A3B-abliterated) | This repository |
| NVF4 / NVFP4 4-bit | [Jiunsong/SuperQwen-AgentWorld-35B-A3B-abliterated-nvf4](https://huggingface.co/Jiunsong/SuperQwen-AgentWorld-35B-A3B-abliterated-nvf4) | MLX NVFP4 4-bit quantization |
| MLX 4-bit | [Jiunsong/SuperQwen-AgentWorld-35B-A3B-abliterated-mlx-4bit](https://huggingface.co/Jiunsong/SuperQwen-AgentWorld-35B-A3B-abliterated-mlx-4bit) | MLX affine 4-bit quantization |
| GGUF 4-bit | [Jiunsong/SuperQwen-AgentWorld-35B-A3B-abliterated-gguf-4bit](https://huggingface.co/Jiunsong/SuperQwen-AgentWorld-35B-A3B-abliterated-gguf-4bit) | llama.cpp GGUF 4-bit quantization |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Jiunsong/SuperQwen-AgentWorld-35B-A3B-abliterated"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)

messages = [
    {
        "role": "system",
        "content": "You are a language world model simulating a Linux terminal environment. Given the user's command, predict the terminal output.",
    },
    {"role": "user", "content": "Action: execute_bash\nCommand: ls -la /home/user/project/"},
]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=2048, temperature=0.6, top_p=0.95, top_k=20)
print(tokenizer.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True))
```

## Notes

- This release is optimized for direct task completion, AgentWorld-style environment simulation, and reduced unnecessary refusals.
- Safety-floor checks are retained in the release bugcheck.
- Use quantized builds when runtime size is more important than exact BF16 fidelity.
