---
base_model: Jackrong/Qwopus3.6-35B-A3B-v1
base_model_relation: quantized
language:
  - en
  - zh
  - ja
  - ko
  - de
license: apache-2.0
tags:
  - gguf
  - quantized
  - llama.cpp
  - qwen3_5_moe
  - mixture-of-experts
  - reasoning
  - multimodal
  - vision
  - tool-use
  - function-calling
pipeline_tag: text-generation
---

# Qwopus3.6-35B-A3B-v1 — GGUF Quantizations

GGUF quantizations of [Jackrong/Qwopus3.6-35B-A3B-v1](https://huggingface.co/Jackrong/Qwopus3.6-35B-A3B-v1) for use with [llama.cpp](https://github.com/ggml-org/llama.cpp) and compatible runtimes.

> 📎 **Vision support:** Place `mmproj.gguf` in the same directory as the main `.gguf` file to enable visual capabilities.

---

## Available Files

| Filename | Quant | Bits | Size | Description |
|---|---|---|---|---|
| `Qwopus3.6-35B-A3B-v1-BF16.gguf` | BF16 | 16 | ~70 GB | Full precision — reference quality |
| `Qwopus3.6-35B-A3B-v1-Q8_0.gguf` | Q8\_0 | 8 | ~37 GB | Near-lossless, recommended if VRAM allows |
| `Qwopus3.6-35B-A3B-v1-Q6_K.gguf` | Q6\_K | 6 | ~28 GB | Excellent quality, minimal loss |
| `Qwopus3.6-35B-A3B-v1-Q5_K_M.gguf` | Q5\_K\_M | 5 | ~24 GB | Great quality, good balance |
| `Qwopus3.6-35B-A3B-v1-Q5_K_S.gguf` | Q5\_K\_S | 5 | ~23 GB | Slightly smaller Q5 variant |
| `Qwopus3.6-35B-A3B-v1-Q4_K_M.gguf` | Q4\_K\_M | 4 | ~21 GB | **Recommended** — best size/quality tradeoff |
| `Qwopus3.6-35B-A3B-v1-Q4_K_S.gguf` | Q4\_K\_S | 4 | ~20 GB | Smaller Q4 variant |
| `Qwopus3.6-35B-A3B-v1-Q3_K_L.gguf` | Q3\_K\_L | 3 | ~17 GB | Good quality for 3-bit |
| `Qwopus3.6-35B-A3B-v1-Q3_K_M.gguf` | Q3\_K\_M | 3 | ~16 GB | Balanced 3-bit |
| `Qwopus3.6-35B-A3B-v1-Q3_K_S.gguf` | Q3\_K\_S | 3 | ~15 GB | Smallest Q3 variant |
| `Qwopus3.6-35B-A3B-v1-IQ3_XXS.gguf` | IQ3\_XXS | 3 | ~14 GB | Importance-quantized, very small |
| `Qwopus3.6-35B-A3B-v1-IQ3_S.gguf` | IQ3\_S | 3 | ~15 GB | Importance-quantized, better quality than Q3_K_S |
| `Qwopus3.6-35B-A3B-v1-Q2_K.gguf` | Q2\_K | 2 | ~12 GB | Smallest — expect quality degradation |
| `mmproj.gguf` | BF16 | 16 | — | Vision encoder — required for image input |

---

## About Qwopus3.6-35B-A3B-v1

**Qwopus3.6-35B-A3B-v1** is a reasoning-enhanced MoE model fine-tuned on top of [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) by [Jackrong](https://huggingface.co/Jackrong). It inherits the base model's hybrid sparse MoE architecture — combining Gated DeltaNet linear attention with standard gated attention layers — while sharpening reasoning depth through a structured three-stage supervised fine-tuning process.

**Key specs:**
- **Total parameters:** 35B
- **Active parameters per token:** 3B
- **Experts:** 256 routed experts, top-K routing
- **Context window:** 262k tokens
- **Multimodal:** Vision + tool calling support

> ⚠️ **Community release notice:** This model has not undergone complete performance evaluation or safety testing. Released as an experimental community version for research and exploration.

---

## Training Overview

Fine-tuning used **LoRA** with ~9% of model parameters participating in updates. Training followed a three-stage curriculum:

**Stage 1 — Format Establishment:** Short-to-medium length, format-stable reasoning samples to establish structured output.

**Stage 2 — Complexity Scaling & Multi-Teacher Distillation:** Gradually increasing proportion of complex reasoning samples distilled from a 27B teacher model.

**Stage 3 — Long-Context Reinforcement & Anti-Drift:** Long-context reasoning with 10% short sample replay to prevent catastrophic forgetting.

---

## Known Issues

- 9% trainable parameter ratio is a risky configuration for this MoE architecture
- Known incompatibilities between PEFT/LoRA, Transformers 5.x fused expert pattern, and Unsloth patches
- LoRA weight merging may fail with `ModuleNotFoundError: Could not import module 'Qwen3_5MoeForConditionalGeneration'`

These are upstream issues in the source model — the GGUF files in this repo are converted from the merged weights and are unaffected.

---

## Usage with llama.cpp

### Download

```bash
# Recommended — Q4_K_M
huggingface-cli download barozp/Qwopus3.6-35B-A3B-v1-GGUF \
    Qwopus3.6-35B-A3B-v1-Q4_K_M.gguf --local-dir ./

# With vision support
huggingface-cli download barozp/Qwopus3.6-35B-A3B-v1-GGUF \
    Qwopus3.6-35B-A3B-v1-Q4_K_M.gguf mmproj.gguf --local-dir ./
```

### CLI

```bash
# Text only
llama-cli -m Qwopus3.6-35B-A3B-v1-Q4_K_M.gguf --jinja -ngl 99 -c 32768

# With vision
llama-cli -m Qwopus3.6-35B-A3B-v1-Q4_K_M.gguf --mmproj mmproj.gguf --jinja -ngl 99 -c 32768

# Server
llama-server -m Qwopus3.6-35B-A3B-v1-Q4_K_M.gguf --mmproj mmproj.gguf --jinja -ngl 99 -c 32768 --port 8080
```

### Python

```python
from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="barozp/Qwopus3.6-35B-A3B-v1-GGUF",
    filename="Qwopus3.6-35B-A3B-v1-Q4_K_M.gguf",
    n_gpu_layers=-1,
    n_ctx=32768,
)

response = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the traveling salesman problem."},
    ]
)
print(response["choices"][0]["message"]["content"])
```

---

## VRAM Requirements

| Quant | Size | Min VRAM |
|---|---|---|
| Q2\_K | ~12 GB | 14 GB |
| IQ3\_XXS | ~14 GB | 16 GB |
| Q3\_K\_M | ~16 GB | 18 GB |
| Q4\_K\_M | ~21 GB | 24 GB |
| Q5\_K\_M | ~24 GB | 27 GB |
| Q6\_K | ~28 GB | 32 GB |
| Q8\_0 | ~37 GB | 40 GB |

For partial GPU offloading use `-ngl <layers>` to fit within available VRAM.

---

## Quantization Details

- **Source:** [Jackrong/Qwopus3.6-35B-A3B-v1](https://huggingface.co/Jackrong/Qwopus3.6-35B-A3B-v1) (BF16 safetensors)
- **Converted with:** [llama.cpp](https://github.com/ggml-org/llama.cpp) `convert_hf_to_gguf.py`
- **Quantized with:** `llama-quantize`
- **IQ quants:** `llama-quantize --imatrix` with WikiText-2 calibration data
- **Quantized by:** [barozp](https://huggingface.co/barozp)

---

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) — inherited from [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B).
