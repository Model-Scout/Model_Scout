---
license: apache-2.0
base_model: Qwen/Qwen3.5-35B-A3B
tags:
  - mlx
  - quantized
  - qwen3_5_moe
  - apple-silicon
  - 16gb
  - dynamic-quantization
  - mixture-of-experts
  - conversational
  - text-only
language:
  - ko
  - en
  - zh
  - ja
  - multilingual
pipeline_tag: text-generation
library_name: mlx
quantized_by: avlp12
---

# Qwen3.5-35B-A3B — Dynamic 2/3-bit MLX (10 GB, Optimized for M4 Mini 16GB)

> Part of the [Qwen3.5-35B-A3B · Alis builds](https://huggingface.co/collections/avlp12/qwen35-35b-a3b-alis-builds-6a565b3f238e840b8530558a) collection.

> **⚠️ This is a Text-Only model. Vision encoder is NOT included.**
> For image/video understanding, use the VLM version: [avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw-VLM](https://huggingface.co/avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw-VLM)

> **Extreme dynamic quantization to run a 35B MoE model on 16GB Apple Silicon.**
> Expert 2-bit + Attention/GDN 3-bit + Router bf16 strategy preserves quality while compressing to 10GB.
> Converted with `mlx_lm`, which excludes the vision encoder (text-only).

---

## 🚨 CRITICAL: 16GB Mac Users — Read This First

**If you're running on a 16GB Mac (M4 Mini, MacBook Air, etc.), follow ALL of these steps or the model WILL crash with OOM:**

### 1. Thinking Mode MUST be OFF
The model defaults to Thinking ON, which generates thousands of internal reasoning tokens and exhausts the 1.2 GB KV cache headroom.

```bash
# Server mode — ALWAYS add this flag
python -m mlx_lm server \
    --model avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw \
    --port 8888 \
    --chat-template-args '{"enable_thinking": false}'

# Generate mode — ALWAYS limit max-tokens
python -m mlx_lm generate \
    --model avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw \
    --prompt 'Your prompt here' \
    --max-tokens 500
```

### 2. Close ALL Other Apps
```
16.0 GB total
- 3.5 GB  macOS + background services
- 11.3 GB model (peak)
= 1.2 GB  remaining for KV cache

Safari (1 tab) = -0.5 GB  → only 0.7 GB left
+ Slack/Discord = -0.3 GB → only 0.4 GB left → CRASH
```
**Close Safari, Chrome, Slack, Discord, KakaoTalk, and any other apps before running.**

### 3. Set Sampling Parameters
| Parameter | Value | Why |
|---|---|---|
| `presence_penalty` | **≥ 1.5** | Prevents infinite repetition loops → OOM |
| `max_tokens` | **≤ 2048** | Prevents KV cache overflow |
| `temperature` | **> 0 (use 0.7)** | Greedy decoding causes loops in quantized models |

### 4. Recommended: Headless + SSH
The most stable setup is running headless (no monitor) with SSH access. This frees ~0.5 GB from WindowServer/display rendering.

```bash
# From another machine
ssh your-mac "python -m mlx_lm server \
    --model ~/models/qwen35-dynamic-v3 \
    --port 8888 \
    --chat-template-args '{\"enable_thinking\": false}'"
```

### Quick Checklist for 16GB

| Step | Required | |
|---|---|---|
| `enable_thinking: false` | ✅ MANDATORY | Prevents 2000+ token internal reasoning |
| Close all apps | ✅ MANDATORY | Frees 0.5-1.0 GB for KV cache |
| `presence_penalty ≥ 1.5` | ✅ MANDATORY | Prevents infinite repetition loops |
| `max_tokens ≤ 2048` | ✅ MANDATORY | Prevents KV cache overflow |
| `temperature > 0` | ✅ MANDATORY | Greedy decoding causes loops |
| Headless + SSH | 💡 Recommended | Frees ~0.5 GB from display |

> **💡 24GB+ users**: These restrictions are much more relaxed. Thinking ON works fine with 24GB+.

---

## Key Specs

| Item | Value |
|---|---|
| Base Model | [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B) |
| Total Parameters | 35B (Active: 3B per token) |
| Architecture | MoE 256 experts, top-8 routed + 1 shared |
| Quantization | Dynamic mixed-precision (2/3/4-bit) |
| Average BPW | **2.579** |
| Disk Size | **10 GB** |
| Peak Memory | **11.3 GB** |
| Target Hardware | **M4 Mac Mini 16GB** |
| Inference Speed | 61 tok/s (M4 Mini) · 113 tok/s (M3 Ultra) |
| Korean Quality | **100% (20/20, no QLoRA needed)** |
| Thinking Mode | ON/OFF switchable |
| Framework | MLX 0.31.1, mlx-lm 0.31.2 |

---

## Purpose

This model was built to run a **35B-class MoE language model on an Apple M4 Mac Mini with only 16GB unified memory**.

Limitations of existing quantized models:
- **Uniform 4-bit** (~21GB): Doesn't fit in 16GB
- **Uniform 3-bit** (~14GB, peak 15.3GB): Barely fits but no room for KV cache
- **Uniform 2-bit** (~11GB): Complete quality collapse (gibberish output)

This model solves the problem through **role-based dynamic quantization**:
- Core pathways active every token (Attention, GatedDeltaNet) → protected at 3-bit
- Experts where only 8 of 256 are active per token → aggressively compressed to 2-bit
- Router and Norms → kept at bf16, never quantized

Result: **10GB model with 100% Korean quality, functional English/coding/reasoning.**

---

## Quantization Strategy

### Per-Layer Bit Allocation

| Component | Bits | Rationale |
|---|---|---|
| **MoE Router** (`mlp.gate`) | **bf16** | Quantizing causes expert selection errors → hallucination. Never quantize. |
| **Shared Expert Gate** (`shared_expert_gate`) | **bf16** | Controls shared expert activation. Never quantize. |
| **Norms** (RMSNorm etc.) | **bf16** | Small tensors, quantization unnecessary |
| **GDN Parameters** (`dt_bias`, `A_log`, `conv1d`) | **bf16** | Core GatedDeltaNet parameters |
| **Embedding** (`embed_tokens`) | **3-bit** | Token mapping |
| **LM Head** (`lm_head`) | **3-bit** | Output projection |
| **Full Attention** (`self_attn`, 10 layers) | **3-bit** | Active every token → quality-critical |
| **Linear Attention / GDN** (`linear_attn`, 30 layers) | **3-bit** | Active every token → verified: 2-bit causes repetition loops |
| **Shared Expert** (40 layers) | **3-bit** | Always active |
| **Routed Experts** (`switch_mlp`, 40 × 256) | **2-bit** | Only 8 of 256 active → 2-bit impact is distributed |

### Why 2-bit Works for Experts Only

This exploits a key property of MoE architecture:
- Only **8 of 256 experts activate** per token (3.1% activation rate)
- Quantization error affects only 3.1% of pathways
- As long as the Router (bf16) correctly selects experts, slight errors in selected experts are tolerable
- In dense models, all parameters are active every token → 2-bit errors accumulate → collapse

### Failed Approaches (Lessons Learned)

| Attempt | BPW | Size | Result | Lesson |
|---|---|---|---|---|
| Uniform 2-bit | 2.50 | 10.9GB | ❌ gibberish | No Router/Attn protection → total failure |
| `mixed_2_6` | 3.18 | 13GB | ⚠️ English switching, loops | Sensitive layers at 6-bit → too large |
| `mixed_3_4` | 3.67 | ~15GB | ❌ Too large | Doesn't fit 16GB |
| Tight (linear_attn 2-bit) | 2.64 | 11GB | ⚠️ Repetition loops | GatedDeltaNet requires 3-bit minimum |
| APEX v4 (edge protection) | 2.82 | 11GB | ✅ Quality OK | Peak 12.3GB → insufficient KV headroom |
| **Dynamic v3 (this model)** | **2.58** | **10GB** | **✅ Perfect** | **Optimal balance** |

---

## Usage

### Installation

```bash
pip install mlx-lm
```

### Text Generation

```bash
python -m mlx_lm generate \
    --model avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw \
    --prompt 'What is the capital of South Korea?' \
    --max-tokens 200
```

### Python API

```python
from mlx_lm import load, generate

model, tokenizer = load("avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw")

# Thinking OFF (for agents/API — answer only)
messages = [{"role": "user", "content": "Explain 5 traditional Korean foods."}]
formatted = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True,
    enable_thinking=False, tokenize=False
)
response = generate(model, tokenizer, prompt=formatted, max_tokens=500)
print(response)

# Thinking ON (for complex reasoning)
formatted = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True,
    enable_thinking=True, tokenize=False
)
response = generate(model, tokenizer, prompt=formatted, max_tokens=1000)
print(response)
```

### API Server (OpenAI-Compatible)

```bash
python -m mlx_lm server \
    --model avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw \
    --port 8888 \
    --chat-template-args '{"enable_thinking": false}'
```

```bash
curl http://localhost:8888/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw",
        "messages": [{"role": "user", "content": "Hello!"}],
        "max_tokens": 200
    }'
```

---

## Recommended Settings (Based on Qwen Official)

### Thinking OFF (Agents, General Chat, API Serving)

| Parameter | General Text | Reasoning Tasks |
|---|---|---|
| `temperature` | **0.7** | 1.0 |
| `top_p` | **0.8** | 0.95 |
| `top_k` | 20 | 20 |
| `min_p` | 0.0 | 0.0 |
| `presence_penalty` | **1.5** | **2.0** |
| `repetition_penalty` | 1.0 | 1.0 |
| `max_tokens` | 16,384 | 32,768 |
| `enable_thinking` | **false** | **false** |

### Thinking ON (Math, Coding, Complex Reasoning)

| Parameter | General Reasoning | Precise Coding (WebDev etc.) |
|---|---|---|
| `temperature` | **1.0** | **0.6** |
| `top_p` | **0.95** | **0.95** |
| `top_k` | 20 | 20 |
| `min_p` | 0.0 | 0.0 |
| `presence_penalty` | **1.5** | **0.0** |
| `repetition_penalty` | 1.0 | 1.0 |
| `max_tokens` | 32,768 | 32,768 |
| `enable_thinking` | **true** | **true** |

### Special Notes for This 2.58 BPW Quantized Model

> ⚠️ This model uses extreme 2.58 BPW quantization. Repetition loops are slightly more likely than the original. Follow these recommendations:

- **Always set `presence_penalty` to 1.5 or higher.** Setting it to 0 may cause repetition loops.
- **Never set `temperature` to 0.** Greedy decoding causes quality degradation and repetitions in quantized models.
- For long outputs, set `max_tokens` sufficiently high (default 200 is too short).

### Server Launch Example

```bash
python -m mlx_lm server \
    --model avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw \
    --port 8888 \
    --chat-template-args '{"enable_thinking": false}' \
    --temp 0.7 --top-p 0.8 --top-k 20
```

### API Call Examples

```bash
# Thinking OFF (Agent/General Chat)
curl http://localhost:8888/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw",
        "messages": [{"role": "user", "content": "Tell me about Korean traditional foods."}],
        "max_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.8,
        "presence_penalty": 1.5,
        "extra_body": {"top_k": 20},
        "chat_template_kwargs": {"enable_thinking": false}
    }'

# Thinking ON (Math/Reasoning)
curl http://localhost:8888/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw",
        "messages": [{"role": "user", "content": "Calculate 12345 × 6789."}],
        "max_tokens": 32768,
        "temperature": 1.0,
        "top_p": 0.95,
        "presence_penalty": 1.5,
        "extra_body": {"top_k": 20},
        "chat_template_kwargs": {"enable_thinking": true}
    }'
```

---

## ⚠️ Important Notes

### Memory Budget (M4 Mini 16GB)

```
Total Memory:        16.0 GB
- macOS Overhead:    -3.5 GB
- Model (peak):      -11.3 GB
= KV Cache Headroom:  1.2 GB
```

### KV Cache and Context Length

Qwen3.5-35B-A3B's hybrid architecture makes KV cache extremely efficient:

- **Full attention**: Only **10 of 40** layers (remaining 30 are GatedDeltaNet)
- **GQA KV heads**: Only **2** (extremely low)
- **4-bit KV per token**: ~5 KB
- **GatedDeltaNet state**: ~33 MB (fixed, independent of context length)

| KV Bits | 64K | 128K | 245K |
|---|---|---|---|
| 4-bit | 0.31 GB ✅ | 0.62 GB ✅ | 1.2 GB ✅ |
| 2-bit | 0.16 GB ✅ | 0.31 GB ✅ | 0.62 GB ✅ |

**For 128K+ context, use `--kv-bits 4` or `--kv-bits 2` with `mlx_lm generate`.**
Note: `mlx_lm server` does not currently support KV cache quantization.

### Thinking Mode

- **Default**: Thinking ON (outputs internal reasoning process)
- **For agents/API**: Must set `enable_thinking=False`
- No quality degradation with Thinking OFF (Korean quality remains 100%)
- Thinking ON improves accuracy on complex math/reasoning problems

### When NOT to Use This Model

- **Image/Video understanding**: ⚠️ No vision encoder (`mlx_lm` conversion excludes it). Use the VLM version.
- **24GB+ Macs**: Uniform 3-bit or 4-bit models provide better quality
- **GPU servers**: GPTQ/AWQ quantization is more suitable

### Text-Only vs VLM Version Comparison

| | Text-Only (This Model) | VLM Version |
|---|---|---|
| Model ID | `avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw` | `avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw-VLM` |
| Size | **10 GB** | ~10.8 GB |
| Peak Memory | **11.3 GB** | ~12.1 GB |
| KV Headroom (16GB) | **1.2 GB (~245K ctx)** | ~0.4 GB (~80K ctx) |
| Image Understanding | ❌ | ✅ |
| Library | `mlx_lm` | `mlx_vlm` |
| Recommended For | Agents, coding, chat | Image analysis, multimodal |

---

## Benchmarks

### Korean Quality Test (M4 Mac Mini 16GB)

20 Korean prompts × Thinking OFF, `max_tokens=200`:

| Metric | Result |
|---|---|
| OK (correct Korean) | **20/20 (100%)** |
| Foreign characters (JP/AR mixing) | 0/20 (0%) |
| Garbage output | 0/20 (0%) |

Test prompts covered: capital city, traditional foods, kimchi recipe, Korean history, Seoul tourism, Hangul origins, seasonal weather, bulgogi recipe, economic industries, traditional medicine, education system, Jeju Island, IT industry, traditional music, holidays, bibimbap, healthcare system, Korean grammar, traditional architecture, K-pop global success.

### Inference Speed

| Hardware | Prompt (tok/s) | Generation (tok/s) | Peak Memory |
|---|---|---|---|
| M4 Mac Mini 16GB (10 GPU cores) | 114 | **61** | 11.3 GB |
| M3 Ultra 512GB (80 GPU cores) | 158 | **113** | 11.3 GB |

### Quantization Profile Comparison (Same Hardware)

| Profile | BPW | Size | Peak | Korean | Notes |
|---|---|---|---|---|---|
| Uniform 2-bit | 2.50 | 10.9GB | 11.0GB | ❌ gibberish | Unusable |
| **Dynamic v3 (this model)** | **2.58** | **10GB** | **11.3GB** | **✅ 100%** | **Optimal** |
| Tight (GDN 2-bit) | 2.64 | 11GB | 11.6GB | ⚠️ Repetition loops | GDN needs 3-bit |
| Dynamic (L0-7 boost) | 2.81 | 11GB | 12.3GB | ✅ 100% | Insufficient KV headroom |
| Uniform 3-bit | 3.50 | 14GB | 15.3GB | ✅ Perfect | Exceeds 16GB |

### lm-eval Benchmarks (0-shot)

| Benchmark | 3-bit (3.50bpw) | **v3 (2.58bpw)** | Loss |
|---|---|---|---|
| ARC-Challenge | 56.40% | **54.86%** | -1.54pp |
| ARC-Easy | 83.33% | **82.58%** | -0.75pp |
| HellaSwag | 58.54% | **54.19%** | -4.35pp |
| TruthfulQA MC2 | 50.98% | **49.27%** | -1.71pp |
| Winogrande | 71.98% | **65.82%** | -6.16pp |
| **Average** | **64.25%** | **61.34%** | **-2.90pp** |

**2.9pp average loss for 29% size reduction (14→10GB).** 3-bit doesn't fit 16GB — v3 is the only working option.

### Sensitivity Analysis

Per-layer relative error at 2-bit, measured on 8-domain calibration (Korean, English, code, reasoning):

| Component | 2-bit Error | v3 Bits | Verdict |
|---|---|---|---|
| Router | 0.5059 | bf16 | ✅ Most sensitive |
| GDN in_proj | 0.4616-0.4770 | 3-bit | ✅ High sensitivity |
| Attention q/k/v/o | 0.4156-0.4369 | 3-bit | ✅ Medium sensitivity |
| **Expert gate_up** | **0.4015** | **2-bit** | ✅ **Most robust** |
| **Expert down** | **0.3971** | **2-bit** | ✅ **Most robust** |

Expert layers are **6.5% more robust** than attention layers (MoQE, Kim 2023). Edge vs middle layers: ratio = 1.00x → APEX edge protection unnecessary.

---

## Reproducing the Quantization

Uses `mlx-lm`'s custom `quant_predicate` API:

```python
from mlx_lm.convert import convert
import re

def qwen35_v3(layer_path, layer):
    # Router: bf16 (never quantize)
    if layer_path.endswith("mlp.gate"):
        return False
    if "shared_expert_gate" in layer_path:
        return False
    # Norms: bf16
    if "norm" in layer_path and "proj" not in layer_path:
        return False
    # GDN parameters: bf16
    if any(x in layer_path for x in ["dt_bias", "A_log", "conv1d"]):
        return False
    # Embed/lm_head: 3-bit
    if "embed_tokens" in layer_path or "lm_head" in layer_path:
        return {"bits": 3, "group_size": 64}
    # Shared expert: 3-bit
    if "shared_expert" in layer_path:
        return {"bits": 3, "group_size": 64}
    # Full attention: 3-bit
    if "self_attn" in layer_path:
        return {"bits": 3, "group_size": 64}
    # Linear attention (GatedDeltaNet): 3-bit
    if "linear_attn" in layer_path:
        return {"bits": 3, "group_size": 64}
    # Routed experts: 2-bit (primary compression target)
    if "switch_mlp" in layer_path:
        return {"bits": 2, "group_size": 64}
    # Everything else: 2-bit
    if hasattr(layer, "to_quantized"):
        return {"bits": 2, "group_size": 64}
    return False

convert(
    hf_path="Qwen/Qwen3.5-35B-A3B",
    mlx_path="./qwen35-dynamic-v3",
    quantize=True,
    quant_predicate=qwen35_v3,
)
# [INFO] Quantized model with 2.579 bits per weight.
```

---

## Project Background

This model is the successor to the [Gemma 4 26B MoE extreme quantization project](https://huggingface.co/avlp12).

The Gemma4 project achieved 11GB at 92% Korean quality with OptiQ B++++ strategy, but **failed to deploy on M4 Mac Mini** due to an MLX bug where the 128-expert `gather_mm` Metal kernel malfunctions on M4 base (10 GPU cores).

Reasons for switching to Qwen3.5:
1. **M4 Compatibility**: 256 experts but different MLX implementation — works on M4 base
2. **KV Cache Efficiency**: GQA 2 heads + GatedDeltaNet hybrid → **24x** more efficient than Gemma4
3. **Korean Quality**: 201 language support, 100% OK without QLoRA

### Gemma4 vs Qwen3.5 Comparison

| | Gemma4 26B OptiQ | **Qwen3.5 35B Dynamic v3** |
|---|---|---|
| M4 Mini 16GB | ❌ MLX bug | **✅ Working** |
| Model Size | 11.0 GB | **10 GB** |
| Parameters | 26B (3.8B active) | **35B (3B active)** |
| Korean | 92% (after LoRA) | **100% (no LoRA)** |
| Context | 74K (4-bit KV) | **245K (4-bit KV)** |
| KV Efficiency | 122 KB/token | **5 KB/token (24x)** |
| Vision | ✅ | ❌ (excluded by mlx_lm) |

---

## Build Environment

- **Quantization**: M3 Ultra Mac Studio 512GB
- **Deployment/Validation**: M4 Mac Mini 16GB (macOS 26.3.1)
- **Framework**: MLX 0.31.1, mlx-lm 0.31.2
- **Date**: April 11, 2026
- **Author**: [@avlp12](https://huggingface.co/avlp12) + Claude Opus

## License

This model inherits the **Apache License 2.0** from the original [Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B).

## Citation

```bibtex
@misc{qwen35-dynamic-v3-2026,
  title   = {Qwen3.5-35B-A3B Dynamic v3: 2.58 BPW Mixed-Precision for 16GB Apple Silicon},
  author  = {avlp12},
  year    = {2026},
  url     = {https://huggingface.co/avlp12/Qwen3.5-35B-A3B-Alis-MLX-Dynamic-2.6bpw},
  note    = {Expert 2-bit + Attention/GDN 3-bit + Router bf16 dynamic quantization}
}
```

## Acknowledgments

- [Qwen Team](https://qwen.ai) — Qwen3.5 model and Apache 2.0 license
- [Apple MLX Team](https://github.com/ml-explore/mlx) — MLX framework and `quant_predicate` API
- [APEX-Quant](https://github.com/mudler/apex-quant) — Inspiration for layer-wise precision gradient strategy
- [Unsloth](https://unsloth.ai) — Dynamic 2.0 quantization benchmarks and GGUF reference data
