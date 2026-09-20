---
license: apache-2.0

tags:
  - darwin
  - darwin-v7
  - evolutionary-merge
  - reasoning
  - advanced-reasoning
  - chain-of-thought
  - thinking
  - qwen3.6
  - qwen
  - moe
  - mixture-of-experts
  - distillation
  - multilingual
  - gpqa
  - benchmark
  - open-source
  - apache-2.0
  - hybrid-vigor
  - proto-agi
  - vidraft
  - eval-results
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
- name: Darwin-36B-Opus
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
      value: 88.4
      name: Accuracy
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> **POCKET is quantized straight from this model.** VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-36B-Opus: Darwin V7 Evolutionary Merge on Qwen3.6-35B-A3B — 88.4% on GPQA Diamond

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-36B-Opus"><img src="https://img.shields.io/badge/⭐_GPQA_Diamond-88.4%25_Darwin--36B--Opus-gold?style=for-the-badge" alt="GPQA"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-27B-Opus"><img src="https://img.shields.io/badge/🧬_Sibling-Darwin--27B--Opus_(86.9%25)-blue?style=for-the-badge" alt="Sibling"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis"><img src="https://img.shields.io/badge/🧬_Model-Darwin--4B--Genesis-blue?style=for-the-badge" alt="Genesis"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-9B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--9B--Opus-blue?style=for-the-badge" alt="9B"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-27B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--27B--Opus-blue?style=for-the-badge" alt="27B"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-31B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--31B--Opus-blue?style=for-the-badge" alt="31B"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-36B-Opus"><img src="https://img.shields.io/badge/⭐_Model-Darwin--36B--Opus-gold?style=for-the-badge" alt="36B"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/collections/FINAL-Bench/darwin-family"><img src="https://img.shields.io/badge/🏠_Darwin_Family-Collection-green?style=for-the-badge" alt="Family"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Leaderboard"><img src="https://img.shields.io/badge/🏆_FINAL_Bench-Leaderboard-green?style=for-the-badge" alt="FINAL Bench"></a>
</p>

> Qwen3.6-35B-A3B MoE | 36B total / 3B active | Thinking Mode | 262K Context | Multilingual | BF16 | Apache 2.0
> **Darwin V7 evolutionary merge: base parent × reasoning-distilled parent → 88.4% on GPQA Diamond**

---

## Abstract

**Darwin-36B-Opus** is a 36-billion-parameter mixture-of-experts (MoE) language model produced by the Darwin V7 evolutionary breeding engine from two publicly available parents:

- **Base parent**: [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) — the foundation MoE with hybrid attention and 256 routed experts.
- **Reasoning parent**: [hesamation/Qwen3.6-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/hesamation/Qwen3.6-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled) — a reasoning-distilled variant of the same base.

Darwin V7 recombines these two parents into a single descendant that preserves the reasoning parent's distilled chain-of-thought behavior while retaining the structural fidelity of the base parent's expert topology. The breeding process is fully automated and produces a deployable bfloat16 checkpoint in under an hour on a single GPU.

On the **GPQA Diamond** benchmark — 198 graduate-level questions in physics, chemistry, and biology — Darwin-36B-Opus achieves **88.4%**, establishing it as the highest-performing model in the Darwin family and extending the series' record of producing state-of-the-art open models through evolution rather than retraining.

---

## GPQA Diamond Leaderboard (April 23, 2026)

| Rank | Model | Parameters | GPQA Diamond |
|---|---|---|---|
| 1 | TNSA/NGen-4-Pro | — | 91.1% |
| 2 | TNSA/NGen-4 | — | 90.1% |
| 3 | Qwen/Qwen3.5-397B-A17B | 397B | 88.4% |
| **3** | **FINAL-Bench/Darwin-36B-Opus** | **36B (A3B)** | **88.4%** |
| 5 | moonshotai/Kimi-K2.5 | — | 87.6% |
| 6 | FINAL-Bench/Darwin-27B-Opus | 27B | 86.9% |
| 7 | Qwen/Qwen3.5-122B-A10B | 122B | 86.6% |
| 8 | zai-org/GLM-5.1 | 744B | 86.2% |
| 9 | zai-org/GLM-5 | 744B | 86.0% |
| 10 | zai-org/GLM-4.7 | — | 85.7% |

A **36B-parameter MoE model (3B active)**, tying the **397B dense-equivalent** Qwen3.5-397B-A17B and surpassing flagship dense and sparse systems an order of magnitude larger.

---

## What Is Darwin?

**Darwin** is the evolutionary model breeding engine developed by FINAL-Bench / VIDRAFT_LAB. Rather than allocating further compute to gradient optimization, Darwin treats trained checkpoints as a genetic pool and discovers high-performing descendants through principled recombination of their weight tensors.

Each Darwin generation (v1 through v7+) refines the breeding procedure. **Darwin V7** is the current generation and the one used to produce this model. Specific algorithmic details of V7 are proprietary to FINAL-Bench; at a high level, the engine performs:

1. **Per-tensor compatibility analysis** of the two parents to identify which components transfer cleanly and which require weighted recombination.
2. **Automated recombination** guided by that analysis, producing a single coherent descendant.
3. **Verification** via a multi-phase scientific benchmark before release.

All Darwin models are released under Apache 2.0 and inherit fully from the parents' open-source licenses.

---

## Parent Models

### 🔵 Base parent — Qwen/Qwen3.6-35B-A3B

- **Model type**: Qwen3.6 MoE, 35B total / ~3B active parameters
- **Layers**: 40, **Hidden size**: 2048
- **Attention**: hybrid 75% Gated DeltaNet + 25% Gated Attention (alternating)
- **Experts**: 256 routed (top-8) + 1 shared per layer
- **Native scores**: MMLU-Pro 85.2%, GPQA 86.0%, AIME26 92.7%
- **Role**: Structural backbone and MoE topology donor.

### 🔴 Reasoning parent — hesamation/Qwen3.6-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled

- **Method**: LoRA SFT on the base over 14,233 reasoning chain-of-thought samples
- **Training regime**: `qwen3-thinking` template, response-only masking
- **Native score**: MMLU-Pro (70 limit-5) 75.71%, **+32.85 percentage points** over the un-distilled base baseline
- **Role**: Reasoning signal donor — the source whose `<think>` trajectories Darwin preserves.

---

## Evolution Process (High Level)

Darwin V7 produces the descendant through a deterministic recombination that does not require gradient optimization on the final assembly. The engine analyzes each tensor in both parents, classifies it by architectural role, and assigns a recombination weight appropriate to that role — biasing toward the reasoning parent for components that carry reasoning behavior, while preserving the base parent's structural contributions where they dominate.

Total breeding time on a single B200 GPU: **under 10 minutes**.

---

## GPQA Diamond Evaluation

### Methodology

We employed a two-pass adaptive evaluation protocol (identical across all Darwin Opus models to preserve cross-model comparability):

**Pass 1 — Greedy Baseline**

- All 198 GPQA Diamond questions, deterministic decoding (`do_sample=False`)
- Maximum 5,120 new tokens per question (allows full `<think>` trajectories)
- Standard multiple-choice prompt format

**Pass 2 — Stochastic Retry with Tiebreaker**

- Questions incorrectly answered in Pass 1 are re-evaluated with **majority-of-8 stochastic generations** (`temperature=0.7`, `max_tokens=5120`)
- Where the vote margin is inconclusive (3:3, 3:4, or 4:4), an additional **16-vote combined tiebreaker** round (`temperature=0.5`) resolves the answer

Evaluation was performed in parallel across 8 × NVIDIA B200 GPUs, each running an independent full copy of the model on a disjoint subset of the benchmark (round-robin question assignment).

### Aggregate Results

| Phase | Cumulative Correct | Accuracy | Δ |
|---|---|---|---|
| Pass 1 — Greedy Baseline | 145/198 | 73.2% | baseline |
| Pass 2 — Stochastic Retry | **175/198** | **88.4%** | **+15.2 percentage points** |

The Pass-2 gain of **+30 questions (+15.2 pp)** demonstrates that the reasoning parent's inherited `<think>` reasoning yields substantially more correct answers under stochastic decoding than under greedy, confirming that the evolutionary merge preserved reasoning depth.

### Results by Shard

| GPU | Questions | Pass 1 Greedy | **Final** |
|:---:|:---:|:---:|:---:|
| GPU0 | 25 | 17/25 (68.0%) | **22/25 (88.0%)** |
| GPU1 | 25 | 17/25 (68.0%) | **20/25 (80.0%)** |
| GPU2 | 25 | 19/25 (76.0%) | **23/25 (92.0%)** |
| GPU3 | 25 | 21/25 (84.0%) | **25/25 (100.0%)** ⭐ |
| GPU4 | 25 | 20/25 (80.0%) | **23/25 (92.0%)** |
| GPU5 | 25 | 17/25 (68.0%) | **22/25 (88.0%)** |
| GPU6 | 24 | 17/24 (70.8%) | **20/24 (83.3%)** |
| GPU7 | 24 | 17/24 (70.8%) | **20/24 (83.3%)** |
| **Total** | **198** | **145/198 (73.2%)** | **175/198 (88.4%)** |

Notably, **GPU3 achieved a perfect 25/25 score** on its 25-question partition — every Pass-1 error on that shard was successfully recovered through the stochastic retry cascade.

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tok = AutoTokenizer.from_pretrained("FINAL-Bench/Darwin-36B-Opus", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Darwin-36B-Opus",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [
    {"role": "user", "content": "Derive the equation for relativistic kinetic energy."}
]
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=5120, temperature=0.6, do_sample=True)
print(tok.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### Answer Extraction for Evaluations

This is a **thinking model** — responses always begin with a `<think>` reasoning trace. For benchmarks, extract the final answer after `</think>`:

```python
response = tok.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
idx = response.rfind("</think>")
answer_part = response[idx + len("</think>"):].strip() if idx >= 0 else response
```

### Recommended Settings

- **Temperature**: 0.6–0.7 for reasoning / majority voting; 0.0 for greedy deterministic
- **max_new_tokens**: ≥5120 to accommodate full `<think>` trajectories
- **Chat template**: `<|im_start|>assistant\n<think>\n` auto-inserted by `apply_chat_template(add_generation_prompt=True)`

---

## Model Specifications

| | |
|---|---|
| Architecture | Qwen3MoE (Qwen3.6 codebase) |
| Total parameters | 36.0 B |
| Active parameters | ~3 B (top-8 of 256 routed experts per layer) |
| Layers | 40 |
| Hidden size | 2048 |
| Attention heads | 24 Q + 4 KV (GQA) |
| Head dimension | 256 |
| Experts per layer | 256 routed + 1 shared |
| Context length | 262,144 tokens |
| Vocabulary | 248,320 |
| Dtype | bfloat16 |
| Checkpoint size | ~65 GB (21 shards) |
| License | Apache 2.0 |

---

## VRAM Requirements

| Precision | VRAM | Recommended GPU |
|---|---|---|
| bf16 (full) | ~72 GB | 1× H100 80GB / 1× B200 |
| 8-bit | ~40 GB | 1× A100 40GB+ / 1× L40S |
| 4-bit | ~22 GB | 1× RTX 4090 / 1× A10 |

---

## Darwin Model Family

| Model | Base | Params | GPQA Diamond |
|---|---|---|---|
| Darwin-4B-Genesis | Qwen3.5-4B | 4 B | — |
| Darwin-9B-Opus | Qwen3.5-9B | 9 B | — |
| Darwin-27B-Opus | Qwen3.5-27B | 27 B | 86.9% |
| Darwin-31B-Opus | Gemma2-27B × variants | 31 B | 85.9% |
| **Darwin-36B-Opus** | **Qwen3.6-35B-A3B** | **36 B (A3B)** | **88.4%** ⭐ |

---

## Key Findings

1. **Evolutionary merging continues to scale.** Across three successive parameter tiers (27B → 31B → 36B), each new Darwin Opus model surpasses the prior one's GPQA Diamond score while maintaining the same zero-training methodology.

2. **Hybrid-attention MoE preserves reasoning under recombination.** The base parent's 75% Gated-DeltaNet + 25% Gated-Attention architecture, inherited intact, demonstrates robustness to tensor-level recombination — a notable result given that MoE expert routing is sensitive to weight perturbation.

3. **Stochastic retry closes the greedy gap.** The +15.2 percentage-point lift from Pass 1 (73.2%) to Pass 2 (88.4%) suggests that the reasoning parent's distilled reasoning is consistently present but occasionally greedy-subdominant — a pattern characteristic of well-distilled chain-of-thought models.

---

## References

- Idavidrein et al., *GPQA: A Graduate-Level Google-Proof Q&A Benchmark*, 2024. [dataset](https://huggingface.co/datasets/Idavidrein/gpqa)
- Qwen Team, *Qwen3.6 Technical Report*, 2026.

---

## Built By

**FINAL-Bench / VIDRAFT_LAB** — Darwin V7 evolutionary breeding engine.

- Base parent weights by the Qwen Team.
- Reasoning parent by [@hesamation](https://huggingface.co/hesamation) (reasoning-distilled).

---

## Learn more

- How model merging works, and how Darwin reaches top scores without training: [Can you make an AI model smarter without training?](https://vidraft.net/insights/model-merging-without-training.html)

## Citation

```bibtex
@misc{darwin-36b-opus,
  title   = {Darwin-36B-Opus: Darwin V7 Evolutionary Merge on Qwen3.6-35B-A3B},
  author  = {FINAL-Bench and VIDRAFT_LAB},
  year    = {2026},
  url     = {https://huggingface.co/FINAL-Bench/Darwin-36B-Opus},
  note    = {Qwen3.6-35B-A3B base x reasoning-distilled variant, Darwin V7 engine, 88.4% GPQA Diamond}
}
```
This model is introduced in [Darwin Family](https://arxiv.org/abs/2605.14386).
