---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: text-generation
base_model:
- LiquidAI/LFM3-1.7B
tags:
- liquid
- lfm3
- recurrent-depth
- adaptive-computation
- reasoning
- custom_code
datasets:
- angrygiraffe/claude-opus-4.6-4.7-reasoning-8.7k
- Jackrong/DeepSeek-V4-Distill-8000x
- openai/gsm8k
- nvidia/OpenMathReasoning
- nvidia/OpenCodeReasoning
- interstellarninja/hermes_reasoning_tool_use
- GhettoGhostUSN/Fable-5.1-Max-Reasoning-Filtered-5000x
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
---

<div align="center">
  <img
    src="https://huggingface.co/cybertruck32489/LFM3-1.7B-RD/resolve/main/model_preview.jpg"
    alt="LFM3-1.7B-RD"
    style="width: 100%; max-width: 100%; height: auto; display: block; margin: 0; border-radius: 8px;"
  />
</div>

<p align="center">
  <a href="https://huggingface.co/LiquidAI/LFM3-1.7B"><strong>Base Model (LFM3-1.7B)</strong></a> ·
  <a href="https://github.com/cybertruck021/lfm3-rd"><strong>GitHub Repository</strong></a> ·
  <a href="#adaptive-token-level-compute-traces"><strong>Step Traces</strong></a> ·
  <a href="#inference"><strong>Inference</strong></a>
</p>

# LFM3-1.7B-RD

**LFM3-1.7B-RD** is an adaptive recurrent-depth language model built by refactoring the 24-layer tri-hybrid architecture of [**LiquidAI/LFM3-1.7B**](https://huggingface.co/LiquidAI/LFM3-1.7B) into a **Prelude -> Shared Recurrent Core -> Coda** system.

Instead of executing a fixed forward pass on every token, LFM3-1.7B-RD executes anywhere from **1 to 32 recurrent core steps per token**—either via manual effort presets (`low`, `fast`, `medium`, `high`, `max`) or dynamically per token in `auto` mode via a learned continuous depth controller.

> [!NOTE]
> This checkpoint is an experimental architectural conversion and continual alignment of [`LiquidAI/LFM3-1.7B`](https://huggingface.co/LiquidAI/LFM3-1.7B). It focuses on dynamic per-token recurrent routing, early-exit FFN completion, and deep iterative refinement without catastrophic drift.

---

## Model Details

| Property | Specification |
| :--- | :--- |
| **Base Model** | [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) |
| **Architecture** | `Lfm3RDForCausalLM` (Prelude + Shared Recurrent Core with Phase LoRAs + Coda) |
| **Sequence Operators** | Gated Short Convolutions (`Lfm3ShortConv`), Sliding-Window GQA, Full Global GQA |
| **Layout** | 2 Prelude layers -> 5 Core Phases x 4 layers (shared bank + LoRA) -> 2 Coda layers |
| **Recurrent Depth (T)** | Configurable from T = 1 to T = 32 steps (`medium` / T = 5 matches the 24-layer baseline depth) |
| **Context Length** | 256K tokens (inherited from LFM3-1.7B; aligned on 2,048-token reasoning/tool windows) |
| **Vocabulary** | 128,000 tokens |
| **Precision** | `bfloat16` |
| **License** | [LFM Open License v1.0](LICENSE) |

---

## Architecture Overview

1. **Shared Core Bank & Phase LoRA Specialization (`Lfm3SharedCoreBank`)**
   The 20 middle layers of `LFM3-1.7B` consist of 5 repetitions of a 4-layer motif (`[FullAttention, ShortConv, SlidingWindowAttention, ShortConv]`). LFM3-1.7B-RD extracts a shared recurrent operator bank across all 5 motifs paired with phase-specific low-rank adapters (`Lfm3SharedLoRALinear` and `Lfm3SharedGroupedLoRALinear` with 3 groups for B, C, x convolution projections). SwiGLU FFN blocks remain phase-specific memory modules.

2. **Early-Exit FFN-Tail Completion (T < 5)**
   Exiting the recurrent core before completing all 5 motifs (T from 1 to 4) would normally skip the unvisited SwiGLU FFNs and corrupt the representation basis entering the Coda layers. When exiting early, `_complete_ffn_tail` skips the sequence operators (`Attention` and `ShortConv`) of remaining motifs while sweeping the hidden state through their FFN blocks and updating KV/conv caches via `update_cache_only`.

3. **Canonical KV-Cache Snapshots & Gauss-Seidel Refinement (T = 6..32)**
   - **Cache Consistency:** During multi-pass recurrence (s >= 5), `_snapshot_phase_cache` and `_restore_phase_cache` roll back phase states before re-entering a motif and restore the canonical Pass-1 (T = 5) KV/convolution states upon loop termination, preventing duplicate token entries in `DynamicCache`.
   - **Feedback Injection & Deep Adapters:** At the beginning of each cycle (m = 0, s >= 5), `inject_feedback` projects the residual difference `h_latent - prelude_out` back into the input stream. Each phase refines its stored trajectory delta (`phase_deltas[m]`) using phase-specific deep adapters (`ref_A`, `ref_B`) and a token-selective gate `alpha_tok` that dampens updates on tokens that have already converged (`unready_factor`).

4. **Direct Depth Regression Controller (`Lfm3RDController`)**
   At every recurrent step s, the controller inspects the normalized hidden state, step velocity, drift from `prelude_out`, and cosine instability to predict the required depth `s_pred` in [0, 31] and halting readiness probability `p_ready`.

---

## Adaptive Token-Level Compute Traces

The primary objective of **LFM3-1.7B-RD** is dynamic per-token compute allocation during autoregressive decoding (`reasoning_mode="auto"`). Rather than using a uniform number of layers for every token, the router exits early on predictable syntax and allocates deep recurrent passes to high-entropy branching points and mathematical deductions.

Below are actual step traces recorded from the checkpoint during autoregressive evaluation (`min_recurrent_loops=1`, `max_recurrent_loops=32`):

### Trace 1: Factual Recall & Continuation (`Easy` Prompt)
*Average recurrent depth: **3.75 steps/token** (vs. 5.0 steps for a standard full pass)*

```text
Prompt : "What is the capital of France?"
Target : "The capital of France is Paris, and it is known for"
Steps  : [3, 3, 3, 2, 3, 5, 3, 3, 2, 13, 2, 3]

```

* **Predictable factual tokens** (`"The"`, `"capital"`, `"of"`, `"France"`, `"is"`): exit in **2 to 3 recurrent steps**, bypassing 40%–60% of the core sequence operators.
* **Entity resolution** (`"Paris"`): uses **5 steps** (one full pass through all 5 core motifs).
* **Open-ended semantic pivot** (`"known"`): spikes to **13 recurrent steps** when selecting the continuation attribute, then immediately drops back to **2–3 steps** on function words (`"for"`).

### Trace 2: Non-Linear Algebraic Derivation (`Hard` Reasoning Prompt)

*Average recurrent depth: **4.15 steps/token** | Peak depth: **22 steps***

```text
Prompt : "Solve the system of non-linear equations: x^3 + y^3 = 35 and x + y = 5."
Target : "<think>\nUsing the cubic identity x^3 + y^3 = (x+y)((x+y)^2 - 3xy), substitute 35 = 5(25 - 3xy), so 3xy = 18 and xy = 6."
Steps  : [12, 17, 7, 2, 3, 7, 3, 1, 3, 2, 2, 1, 2, 3, 3, 3, 3, 5, 3, 3, ...] (max = 22)

```

* **Reasoning initialization & proof strategy selection** (`"<think>\n"`, `"Using"`, `"the"`): the router allocates **12, 17, and 7 steps** on the opening tokens to set up the algebraic identity, reaching up to **22 steps** on downstream substitution pivots.
* **Mechanical syntax & bracket expansion** (`"^3"`, `"+"`, `"="`, `"("`): throttles down to **1 to 3 steps**, keeping average compute below the 5-step baseline even on multi-step math derivations.

---

## Validation Progression Across Depths (T = 1..32)

Following architectural fixes for canonical KV-cache restoration (`save_kv_tensors`) and early-exit FFN tail completion, the checkpoint was aligned for 1,250 optimizer steps (`AdamW8bit`, `bfloat16` mixed precision on H100) across a 90/10 train/validation split of 7 reasoning, math, coding, and tool-use datasets.

Validation perplexity (`Val PPL`) is measured on the held-out validation subset across all recurrent presets simultaneously:

| Optimizer Step | T = 1 (`low`) | T = 2 (`fast`) | T = 4 | T = 5 (`medium`) | T = 8 | T = 12 (`high`) | T = 32 (`max`) | Auto Steps (Easy / Hard / Max) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Step 0** *(post-fix init)* | 5.677 | 3.483 | 1.891 | 1.787 | 1.785 | 1.785 | 1.784 | 3.92 / 4.57 (max 18) |
| **Step 200** | 5.479 | 3.505 | 1.990 | 1.889 | 1.883 | 1.882 | 1.883 | 2.92 / 3.83 (max 21) |
| **Step 400** | 5.308 | 3.426 | 1.979 | 1.887 | 1.878 | 1.878 | 1.878 | 2.58 / 4.28 (max 21) |
| **Step 600** | 5.193 | 3.364 | 1.945 | 1.856 | 1.849 | 1.848 | 1.849 | 3.75 / 4.02 (max 21) |
| **Step 800** | 5.097 | 3.324 | 1.911 | 1.824 | 1.817 | 1.817 | 1.817 | 3.67 / 4.35 (max 22) |
| **Step 1000** | 5.039 | 3.286 | 1.892 | 1.804 | 1.798 | 1.798 | 1.799 | 3.75 / 4.15 (max 22) |
| **Step 1250** *(final)* | **5.033** | **3.291** | **1.906** | **1.825** | **1.818** | **1.818** | **1.820** | **2.75 / 3.52 (max 21)** |

---

## Inference

### Requirements

```bash
pip install -U torch transformers accelerate safetensors

```

### Quick Start with `transformers`

You can run **LFM3-1.7B-RD** in either adaptive `auto` mode (per-token dynamic depth during decoding) or with a fixed `reasoning_effort` preset:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "cybertruck32489/LFM3-1.7B-RD"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [
    {"role": "user", "content": "Solve the system of non-linear equations: x^3 + y^3 = 35 and x + y = 5."}
]
prompt = tokenizer.apply_chat_template(
    messages,
    enable_thinking=True,
    add_generation_prompt=True,
    tokenize=False,
)
inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to(model.device)

# 1. Adaptive per-token depth (auto mode)
model.model.act_step_history.clear()
outputs = model.generate(
    **inputs,
    max_new_tokens=256,
    do_sample=False,
    reasoning_effort="auto",  # Options: "low" (1), "fast" (2), "medium" (5), "high" (12), "max" (32), "auto"
)

generated_ids = outputs[0][inputs["input_ids"].shape[1]:]
print(tokenizer.decode(generated_ids, skip_special_tokens=False))
print("Recurrent steps per token:", model.model.act_step_history)

```

### Manual Recurrent Depth Control

To force a specific number of recurrent iterations T in [1, 32] across all tokens:

```python
# Switch model default configuration
model.set_reasoning_mode(mode="manual", loops=12)

# Or pass directly to .generate() / .forward()
outputs_t12 = model.generate(
    **inputs,
    max_new_tokens=256,
    do_sample=False,
    reasoning_mode="manual",
    recurrent_loops=12,
)

```

| Effort Preset | Mode | Recurrent Loops (T) | Sequence Operators Executed | Intended Use Case |
| --- | --- | --- | --- | --- |
| `low` | `manual` | `1` | 8 layers (+ FFN tail) | Ultra-fast draft generation |
| `fast` | `manual` | `2` | 12 layers (+ FFN tail) | Low-latency chat & simple continuations |
| `medium` | `manual` | `5` | 24 layers | Standard 1-pass baseline (equivalent to LFM3-1.7B depth) |
| `high` | `manual` | `12` | 52 layers | Multi-step math, code, and structured tool calls |
| `max` | `manual` | `32` | 132 layers | Maximum iterative refinement depth |
| `auto` | `auto` | `1 .. 32` | Dynamic per token | Automatic per-token compute routing during decoding |

---

## Training & Alignment Data

The recurrent controller (`Lfm3RDController`), phase LoRA adapters, and backbone weights were aligned on a multi-domain mixture filtered to 2,048-token assistant-masked windows:

* **Reasoning & Chain-of-Thought:** [`angrygiraffe/claude-opus-4.6-4.7-reasoning-8.7k`](https://huggingface.co/datasets/angrygiraffe/claude-opus-4.6-4.7-reasoning-8.7k), [`Jackrong/DeepSeek-V4-Distill-8000x`](https://huggingface.co/datasets/Jackrong/DeepSeek-V4-Distill-8000x)
* **Mathematics:** [`openai/gsm8k`](https://huggingface.co/datasets/openai/gsm8k), [`nvidia/OpenMathReasoning`](https://huggingface.co/datasets/nvidia/OpenMathReasoning)
* **Code Generation:** [`nvidia/OpenCodeReasoning`](https://huggingface.co/datasets/nvidia/OpenCodeReasoning)
* **Tool Calling & Agentic Traces:** [`interstellarninja/hermes_reasoning_tool_use`](https://huggingface.co/datasets/interstellarninja/hermes_reasoning_tool_use), [`GhettoGhostUSN/Fable-5.1-Max-Reasoning-Filtered-5000x`](https://huggingface.co/datasets/GhettoGhostUSN/Fable-5.1-Max-Reasoning-Filtered-5000x)

---

## License & Acknowledgments

This model is derived from **[LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B)** and is distributed under the **[LFM Open License v1.0](https://www.google.com/search?q=LICENSE)**.

```bibtex
@misc{lfm3-rd-2026,
  author = {cybertruck32489},
  title  = {LFM3-1.7B-RD: Adaptive Recurrent-Depth Architecture for Liquid Foundation Models},
  year   = {2026},
  url    = {[https://huggingface.co/cybertruck32489/LFM3-1.7B-RD](https://huggingface.co/cybertruck32489/LFM3-1.7B-RD)}
}

@article{liquidAI2026LFM3,
  author  = {Liquid AI},
  title   = {Introducing LFM3: Every Modality for Specialized Intelligence},
  journal = {Liquid AI Blog},
  year    = {2026},
  note    = {www.liquid.ai/blog/lfm3}
}

```