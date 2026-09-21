---
license: apache-2.0
base_model: Qwen/Qwen3-0.6B
tags:
  - verifier
  - reward-model
  - judge
  - qwen3
  - text-generation
  - gguf
library_name: transformers
pipeline_tag: text-generation
language:
  - en
  - ko
model_type: qwen3
---

# OmniEvaluator-Verifier-0.6B-v1.0

A lightweight **reference-based verifier** (LLM-as-a-judge) fine-tuned from
[Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B). Given a question,
one or more reference answers, and a model's prediction, the verifier emits
a concise reasoning trace followed by a binary correctness rating
(`Rating: 0` or `Rating: 1`).

Designed as a drop-in judge for the
[OmniEvaluator](https://github.com/naver-ai/omni-evaluator) framework —
runs on CPU via `llama.cpp` (Q8_0 quant) with negligible latency overhead
per record, or on GPU via the standard `transformers` path.

## Overview

| | |
|---|---|
| **Base model** | [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) |
| **Role** | Reference-based verifier / LLM judge |
| **Size** | ~0.6B params (596M) |
| **Context** | 40960 tokens (base), truncation-aware |
| **Formats** | `safetensors` (bf16) + `GGUF` (Q8_0, f16) |
| **License** | Apache 2.0 (inherited from Qwen3-0.6B) |
| **Framework** | [OmniEvaluator](https://github.com/naver-ai/omni-evaluator) |

For the framework, evaluation protocols, and detailed usage in a broader
benchmark pipeline, see the
[OmniEvaluator GitHub repository](https://github.com/naver-ai/omni-evaluator).

## Input / output format

**Input** — a single user turn containing:

```
[Reference Answer]
<one or more gold answers, newline-separated>

[Model Answer]
<the prediction to be judged; n>1 samples are newline-concatenated>

[Question]
<the original query>
```

Optionally followed by an `[Options]` block for multiple-choice tasks.

**Output** — a short natural-language rationale followed by a single
line-anchored rating:

```
<free-form reasoning inside <think>…</think> when reasoning is enabled>

<one-line explanation>
Rating: 0
```

Parsed by matching the final line-anchored `Rating:\s*([01])\s*$`
(MULTILINE) — the last such match wins.

## Files

| File | Format | Size | Recommended use |
|---|---|---|---|
| `model.safetensors` | HF `safetensors` (bf16) | 2.4 GB | GPU inference (`transformers`) |
| `qwen3_06b_v7-Q8_0.gguf` | GGUF, Q8_0 quant | 640 MB | CPU inference (`llama.cpp`) |
| `qwen3_06b_v7-f16.gguf` | GGUF, f16 | 1.2 GB | GGUF at native precision |

Both formats share this single repo — pick a loader based on your target
hardware.

## Usage

### Direct `llama-cpp-python`

```python
from llama_cpp import Llama

model = Llama.from_pretrained(
    repo_id="bigshanedogg/OmniEvaluator-Verifier-0.6B-v1.0",
    filename="*Q8_0.gguf",
    n_ctx=4096,
    n_threads=8,
    n_gpu_layers=0,  # CPU-only; set to -1 to offload all layers if CUDA-built
)

prompt = (
    "[Reference Answer]\n4\n\n"
    "[Model Answer]\n2 + 2 = 4\n\n"
    "[Question]\nWhat is 2 + 2?\n\n"
    "Provide a one-line explanation on the second-to-last line, then a final "
    "line 'Rating: 0' or 'Rating: 1'."
)
out = model.create_chat_completion(
    messages=[{"role": "user", "content": prompt}],
    temperature=0.0,
    max_tokens=512,
)
print(out["choices"][0]["message"]["content"])
```

### `transformers` (GPU / CPU)

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

_repo = "bigshanedogg/OmniEvaluator-Verifier-0.6B-v1.0"
tokenizer = AutoTokenizer.from_pretrained(_repo)
model = AutoModelForCausalLM.from_pretrained(
    _repo,
    dtype=torch.bfloat16,
    device_map="auto",
)

messages = [{"role": "user", "content": prompt}]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
).to(model.device)

with torch.no_grad():
    output_ids = model.generate(
        inputs,
        max_new_tokens=512,
        do_sample=False,
    )
print(tokenizer.decode(output_ids[0][inputs.shape[1]:], skip_special_tokens=True))
```

### Inside OmniEvaluator

```python
from omni_evaluator.inference.llama_cpp import LlamaCppInferencer

inferencer = LlamaCppInferencer(
    model_name_or_path="bigshanedogg/OmniEvaluator-Verifier-0.6B-v1.0",
    gguf_filename="*Q8_0.gguf",
    num_context_tokens=4096,
    num_threads=8,
)
```

See [OmniEvaluator's verifier module](https://github.com/naver-ai/omni-evaluator)
for the batched / NUMA-parallel judge loop wiring.

## Parsing the rating

```python
import re

_RATING_RE = re.compile(r"[Rr]ating:\s*([01])\s*$", re.MULTILINE)

def parse_rating(text: str):
    matches = _RATING_RE.findall(text)
    return int(matches[-1]) if matches else None
```

The trailing line-anchored regex prevents echoed prompt-instruction lines
(e.g. `"'Rating: 0' or 'Rating: 1'"`) from being mistaken for the real
rating.

## License

Apache 2.0, inherited from the base model
[Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B). See the
`LICENSE` file for the full text.

## Links

- **Framework**: <https://github.com/naver-ai/omni-evaluator>
- **Base model**: <https://huggingface.co/Qwen/Qwen3-0.6B>
