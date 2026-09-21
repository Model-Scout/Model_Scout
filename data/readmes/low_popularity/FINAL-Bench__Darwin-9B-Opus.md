---
license: apache-2.0

tags:
  - merge
  - evolutionary-merge
  - darwin
  - darwin-v5
  - model-mri
  - reasoning
  - advanced-reasoning
  - chain-of-thought
  - thinking
  - qwen3.5
  - qwen
  - claude-opus
  - distillation
  - multilingual
  - benchmark
  - open-source
  - apache-2.0
  - layer-wise-merge
  - coding-agent
  - tool-calling
  - long-context
language:
  - en
  - zh
  - ko
  - ja
  - de
  - fr
  - es
  - ru
  - ar
  - multilingual
pipeline_tag: text-generation
library_name: transformers
model-index:
- name: Darwin-9B-Opus
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: GPQA Diamond
      type: Idavidrein/gpqa
      config: gpqa_diamond
    metrics:
    - type: accuracy
      value: 82.5
      name: Accuracy
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-9B-Opus

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Opus"><img src="https://img.shields.io/badge/🧬_Gen1-Darwin--4B--Opus-blue?style=for-the-badge" alt="Gen1"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-David"><img src="https://img.shields.io/badge/🧬_Gen2-Darwin--4B--David-blue?style=for-the-badge" alt="Gen2"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis"><img src="https://img.shields.io/badge/⭐_Gen3-Darwin--4B--Genesis-gold?style=for-the-badge" alt="Gen3"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-9B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--9B--Opus-blue?style=for-the-badge" alt="9B"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Darwin-9B-Opus"><img src="https://img.shields.io/badge/🚀_Space-9B_Demo-purple?style=for-the-badge" alt="9B Space"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-31B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--31B--Opus-blue?style=for-the-badge" alt="31B"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Darwin-31B-Opus"><img src="https://img.shields.io/badge/🚀_Space-31B_Demo-purple?style=for-the-badge" alt="31B Space"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--35B--A3B--Opus-blue?style=for-the-badge" alt="35B"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Darwin-35B-A3B-Opus"><img src="https://img.shields.io/badge/🚀_Space-35B_Demo-purple?style=for-the-badge" alt="35B Space"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus-Q8-GGUF"><img src="https://img.shields.io/badge/📦_GGUF-Q8--Official-yellow?style=for-the-badge" alt="Q8 GGUF"></a>
  <a href="https://huggingface.co/bartowski/FINAL-Bench_Darwin-35B-A3B-Opus-GGUF"><img src="https://img.shields.io/badge/📦_GGUF-bartowski-yellow?style=for-the-badge" alt="bartowski GGUF"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/spaces/FINAL-Bench/Leaderboard"><img src="https://img.shields.io/badge/🏆_FINAL_Bench-Leaderboard-green?style=for-the-badge" alt="FINAL Bench"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/all-bench-leaderboard"><img src="https://img.shields.io/badge/📊_ALL_Bench-Leaderboard-orange?style=for-the-badge" alt="ALL Bench"></a>
</p>

> Qwen3.5 Dense 9B | Reasoning | Chain-of-Thought | 131K Context | 201 Languages | BF16 | Apache 2.0

---

## Technical Definitions

| Term | Definition | Measurement |
|---|---|---|
| Model MRI | Layer-level profiling of tensor health indicators | L2 norm, Shannon entropy, std per tensor across all layers |
| LayerMRI.compare_layers | Per-tensor A vs B quality comparison yielding optimal ratio_b | score = entropy * 0.5 + std * 0.3 + clamp(norm, 100) * 0.002 per model; ratio_b = score_b / (score_a + score_b) |
| MRI-Guided Merge | Per-tensor merge ratios derived from parent diagnostics (70% MRI + 30% genome) | final_ratio = mri_ratio * 0.7 + genome_ratio * 0.3 |
| DARE-TIES | Merge algorithm: random binary mask on delta, then weighted addition | merged = A + (B - A) * random_mask(density) * ratio |
| Transplant A / B | When MRI ratio falls below 0.05 or above 0.95, one parent is used entirely | No interpolation — direct tensor copy |
| Evolutionary Search | CMA-ES population evolution over genome space (ratio, attn, ffn, embed, density_a, density_b) | Phase 1: 200 steps heuristic proxy, Phase 2: 10 steps real benchmark |

---

## Overview

Darwin-9B-Opus is a 9B dense parameter reasoning model created using Darwin V5. Both parent models share the identical Qwen3.5-9B architecture — the Mother is a LoRA SFT on the same base, not a different architecture.

| Role | Model | Training |
|---|---|---|
| Father | [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) | Original pre-training + RLHF |
| Mother | [Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled) | LoRA SFT with text-only Claude 4.6 Opus reasoning chains |

---

## How Darwin V5 Works

Darwin V5 does not use mergekit or any external merge library. It implements DARE-TIES merge directly via PyTorch tensor operations, with MRI-guided per-layer ratios. The algorithm is inspired by the DARE-TIES method but re-implemented from scratch to support per-tensor diagnostic-guided ratios.

### Merge Implementation (actual code logic)

```python
# For each tensor pair (A, B) across all safetensor shards:
ta = model_a[key]       # Father tensor
tb = model_b[key]       # Mother tensor

# 1. MRI diagnoses both tensors
diag_a = LayerMRI.diagnose_tensor(ta)  # {norm, entropy, std}
diag_b = LayerMRI.diagnose_tensor(tb)  # {norm, entropy, std}

# 2. Quality score comparison determines ratio_b
score_a = diag_a["entropy"] * 0.5 + diag_a["std"] * 0.3 + min(diag_a["norm"], 100) * 0.002
score_b = diag_b["entropy"] * 0.5 + diag_b["std"] * 0.3 + min(diag_b["norm"], 100) * 0.002
mri_ratio = score_b / (score_a + score_b)  # Higher = Mother is better

# 3. Final ratio = MRI 70% + evolutionary genome 30%
final_ratio = mri_ratio * 0.7 + genome_type_ratio * 0.3

# 4. DARE-TIES merge with per-tensor ratio
mask = torch.rand_like(tb) < density_b
delta = (tb - ta) * mask
merged = (ta + delta * final_ratio).bfloat16()
```

### Pipeline

```
Phase 0: Model MRI
  For every tensor in both parents, measure:
    - L2 norm (layer energy)
    - Shannon entropy (weight distribution uniformity)
    - Standard deviation (activation spread)
  Compare A vs B quality scores -> per-tensor ratio prescription

Phase 1: Evolutionary Search (200 steps, heuristic proxy)
  Population of 20 genomes (ratio, attn, ffn, embed, density_a, density_b)
  Fitness: heuristic score based on genome balance + differentiation
  Selection -> SLERP crossover -> Gaussian mutation

Phase 2: Real Merge + Benchmark (10 steps)
  Top genomes from Phase 1 undergo actual tensor merge
  Each merge: MRI prescription (70%) + genome ratio (30%)
  Fitness: real benchmark score (ARC-Challenge)
  Best model selected and auto-uploaded

Phase 3: Health Check
  Layer-by-layer importance comparison: child vs both parents
  Detect interference (child >> parents) or function loss (parents >> child)
```

### What Makes This Different from Standard Merging

| Capability | Standard DARE-TIES | Darwin V5 |
|---|---|---|
| Implementation | mergekit library call | Direct PyTorch tensor operations |
| Ratio selection | Uniform ratio across all tensors | Per-tensor ratio from MRI diagnosis |
| Pre-merge analysis | None | Tensor-level norm/entropy/std profiling |
| Ratio determination | Human-set or grid search | MRI 70% + evolutionary genome 30% |
| Post-merge validation | Benchmark score only | Layer-by-layer child vs parents comparison |
| Transplant support | No | ratio < 0.05 -> use A entirely, ratio > 0.95 -> use B entirely |
| Failure diagnosis | "Score went down" | Per-tensor quality delta identifies problematic layers |

---

## Model Specifications

| | |
|---|---|
| Architecture | Qwen3.5 Dense (Gated DeltaNet hybrid) |
| Total Parameters | 9B |
| Precision | BF16 |
| Context Length | 131,072 native |
| Languages | 201 |
| Thinking | `<think>` tag chain-of-thought reasoning |
| License | Apache 2.0 |

---

## Hardware Requirements

| Setup | VRAM | Status |
|---|---|---|
| BF16 Full Precision | ~20 GB | |
| NVIDIA RTX 4090 24GB | 24 GB | Comfortable |
| NVIDIA A100 40GB | 40 GB | Very comfortable |
| NVIDIA T4 16GB | 16 GB | Requires quantization |

---

## Usage

### Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained(
    "FINAL-Bench/Darwin-9B-Opus",
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Darwin-9B-Opus",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [{"role": "user", "content": "Prove that sqrt(2) is irrational."}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=4096)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### SGLang

```bash
python -m sglang.launch_server \
  --model-path FINAL-Bench/Darwin-9B-Opus \
  --tp 1 \
  --mem-fraction-static 0.90 \
  --context-length 32768 \
  --trust-remote-code
```

### vLLM

```bash
vllm serve FINAL-Bench/Darwin-9B-Opus \
  --trust-remote-code \
  --enforce-eager
```

---

## Evolution Details

| | |
|---|---|
| Engine | Darwin V5 (Evolutionary Merge + Layer-Level Diagnostics) |
| Merge Method | DARE-TIES (direct PyTorch implementation, no external library) |
| MRI Integration | Per-tensor diagnosis: norm, entropy, std -> ratio prescription |
| Ratio Formula | final_ratio = mri_ratio * 0.7 + genome_ratio * 0.3 |
| Evolution | Phase 1: 200 steps proxy + Phase 2: 10 steps real benchmark |
| Best Score | 0.8508 (ARC-Challenge) |
| Infrastructure | 4 x NVIDIA H100 NVL (100GB each) |

---

## Acknowledgements

- Korean Government — GPU Support Program research grant
- [Qwen Team](https://huggingface.co/Qwen) — Qwen3.5 base architecture
- [Jackrong](https://huggingface.co/Jackrong) — Claude 4.6 Opus Reasoning Distilled model
- DARE-TIES algorithm — [Yadav et al., 2023](https://arxiv.org/abs/2311.03099) (re-implemented, not library-dependent)

---

## Built By

| | |
|---|---|
| Developer | VIDRAFT |
| Engine | Darwin V5 |
| Base Architecture | Qwen3.5-9B |

---

## Citation

```bibtex
@misc{vidraft_darwin_9b_opus,
  title        = {Darwin-9B-Opus: Diagnostic-Guided Evolutionary Merge},
  author       = {VIDRAFT},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-9B-Opus}}
}
```
This model is introduced in [Darwin Family](https://arxiv.org/abs/2605.14386).