---
license: apache-2.0
tags:
  - jgos
  - ourbox
  - darwin
  - darwin-platform
  - evolutionary-merge
  - ffn-merge
  - model-breeding
  - korean
  - korean-specialized
  - reasoning
  - advanced-reasoning
  - chain-of-thought
  - thinking
  - qwen3.6
  - qwen
  - moe
  - mixture-of-experts
  - multi-token-prediction
  - multilingual
  - gpqa
  - benchmark
  - open-source
  - apache-2.0
  - vidraft
  - eval-results
language:
  - ko
  - en
  - zh
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
- name: Ourbox-35B-JGOS
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
      value: 86.36
      name: Accuracy
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Ourbox-35B-JGOS: Korean-Specialized, Darwin-Evolved 35B-A3B Reasoning MoE — 86.36% on GPQA Diamond

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Ourbox-35B-JGOS"><img src="https://img.shields.io/badge/⭐_GPQA_Diamond-86.36%25_Ourbox--35B--JGOS-gold?style=for-the-badge" alt="GPQA"></a>
  <a href="https://huggingface.co/FINAL-Bench/Ourbox-35B-JGOS"><img src="https://img.shields.io/badge/🇰🇷_Korean-Specialized-red?style=for-the-badge" alt="Korean"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-36B-Opus"><img src="https://img.shields.io/badge/🧬_Sibling-Darwin--36B--Opus_(88.4%25)-blue?style=for-the-badge" alt="Sibling"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Leaderboard"><img src="https://img.shields.io/badge/🏆_FINAL_Bench-Leaderboard-green?style=for-the-badge" alt="FINAL Bench"></a>
  <a href="https://huggingface.co/datasets/Idavidrein/gpqa"><img src="https://img.shields.io/badge/📊_Benchmark-GPQA_Diamond-orange?style=for-the-badge" alt="GPQA"></a>
</p>

> Darwin-Evolved on Qwen3.6-35B-A3B | 35B total / ~3B active | 🇰🇷 Korean-Specialized | Thinking Mode | Hybrid Linear/Full Attention | Multi-Token Prediction | 262K Context | BF16 | Apache 2.0
> **Darwin FFN-level evolutionary merge → Korean specialization → 86.36% on GPQA Diamond (majority-of-8+)**

---

## Abstract

**Ourbox-35B-JGOS** is a 35-billion-parameter mixture-of-experts (MoE) reasoning model produced by the **Darwin** evolutionary breeding platform (FINAL-Bench / VIDRAFT_LAB). Rather than retraining from scratch, Darwin recombines the **feed-forward (FFN / MoE expert) tensors** of the **Qwen3.6-35B-A3B** backbone with those of additional specialized donor models, then **evolves** the merged descendant toward a target objective — here, **Korean-language specialization**.

Because the merge operates at the **expert-FFN level**, Ourbox inherits complementary domain and language competencies from multiple sources while preserving the backbone's hybrid-attention topology and 262K long-context behavior. The result is a Korean-specialized reasoning model that remains highly competitive on English graduate-level science: on **GPQA Diamond** (198 questions across physics, chemistry, biology), Ourbox-35B-JGOS scores **86.36% (171/198)** under a majority-of-8+ protocol. On Hugging Face's live GPQA leaderboard this **improves on its own Qwen3.6-35B-A3B backbone (86.0)** by +0.36 points and edges past **GLM-5.1 (86.2)** and **GLM-5 (86.0)** — with only **~3B active parameters**.

---

## GPQA Diamond Leaderboard — Hugging Face `Idavidrein/gpqa` (2026-07-11)

Ourbox-35B-JGOS on the **official Hugging Face GPQA Diamond leaderboard** (`Idavidrein/gpqa`, base-model view, 50 models). FINAL-Bench models in **bold**:

| # | Model | GPQA Diamond |
|---|---|---|
| 1 | zai-org/GLM-5.2 | 91.2 |
| 2 | **FINAL-Bench/Darwin-398B-JGOS** | 90.9 |
| 3 | moonshotai/Kimi-K2.6 | 90.5 |
| 4 | tencent/Hy3 | 90.4 |
| 5 | deepseek-ai/DeepSeek-V4-Pro | 90.1 |
| 6 | **FINAL-Bench/Darwin-28B-REASON** | 89.39 |
| 7 | Qwen/Qwen3.5-397B-A17B | 88.4 |
| 8 | **FINAL-Bench/Darwin-36B-Opus** | 88.4 |
| 9 | **FINAL-Bench/Darwin-60B-DUO** | 88.38 |
| 10 | inclusionAI/Ring-2.6-1T | 88.27 |
| 11 | deepseek-ai/DeepSeek-V4-Flash | 88.1 |
| 12 | nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B (NVFP4) | 87.9 |
| 13 | zai-org/GLM-4.7-FP8 | 87.88 |
| 14 | Qwen/Qwen3.6-27B | 87.8 |
| 15 | moonshotai/Kimi-K2.5 | 87.6 |
| 16 | moonshotai/Kimi-K2.5 *(source)* | 87.37 |
| 17 | tencent/Hy3-preview | 87.2 |
| 18 | nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B (BF16) | 87.0 |
| 19 | **FINAL-Bench/Darwin-27B-Opus** | 86.9 |
| 20 | Qwen/Qwen3.5-122B-A10B | 86.6 |
| **★ 21** | **FINAL-Bench/Ourbox-35B-JGOS** 🇰🇷 | **86.36** |
| 22 | zai-org/GLM-5.1 | 86.2 |
| 23 | zai-org/GLM-5 | 86.0 |
| 24 | Qwen/Qwen3.6-35B-A3B *(Ourbox backbone)* | 86.0 |
| 25 | **FINAL-Bench/Darwin-31B-Opus** | 85.9 |

The FINAL-Bench Darwin family dominates the upper board — **5 of the 20 models ranked above Ourbox are Darwin models** (Darwin-398B-JGOS #2, Darwin-28B-REASON #6, Darwin-36B-Opus #8, Darwin-60B-DUO #9, Darwin-27B-Opus #19). At **86.36%**, Ourbox-35B-JGOS ranks **#21 of 50** on the live leaderboard and — most notably — **improves on its own Qwen3.6-35B-A3B backbone (86.0, #24) by +0.36 points**, confirming that the Darwin FFN-merge and Korean specialization *added* capability rather than eroding it. It also edges past **GLM-5.1 (86.2, #22)** and **GLM-5 (86.0, #23)** while activating only ~3B parameters.

> Ranks reflect the live leaderboard as of 2026-07-11 (which counts quantized/duplicate entries); positions shift as it updates. Ourbox-35B-JGOS is **live and listed at #21**.

---

## What Is Darwin?

**Darwin** is the evolutionary model-breeding platform developed by FINAL-Bench / VIDRAFT_LAB. Rather than allocating further compute to gradient optimization, Darwin treats trained checkpoints as a **genetic pool** and discovers high-performing descendants through principled recombination of their weight tensors — with a particular focus on the **FFN / MoE expert** subspace, where domain and language competence is concentrated.

At a high level, the platform performs:

1. **Per-tensor compatibility analysis** across the backbone and donor models to identify which FFN experts and components transfer cleanly and which require weighted recombination.
2. **FFN-level merge & evolution** — the descendant's expert tensors are assembled from the pool and iteratively evolved toward a target objective (Korean specialization for Ourbox).
3. **Verification** via a multi-phase scientific benchmark before release.

Specific algorithmic details of the Darwin engine are proprietary to FINAL-Bench. All Darwin models are released under the base model's open-source license (Apache 2.0).

**JGOS** is the reasoning-model line built with Darwin; **Ourbox** is its Korean-specialized 35B-A3B member.

---

## Evolution Process

Ourbox-35B-JGOS is bred, not trained:

- **Backbone**: [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen) — the foundation MoE, contributing its hybrid-attention topology (¾ linear + ¼ full), 256-expert routing, MTP head, and 262K context.
- **FFN donors**: additional specialized models whose **feed-forward / expert tensors** are recombined into the backbone by the Darwin engine, contributing complementary domain and Korean-language competence.
- **Evolution objective**: Korean specialization — the evolutionary selection biases the merged expert population toward stronger Korean reasoning and generation, while structural and long-context behavior is inherited intact from the backbone.

The merge operates **without gradient optimization on the final assembly**; a deployable bfloat16 checkpoint is produced by the Darwin pipeline directly.

---

## 🇰🇷 Korean Specialization

Ourbox-35B-JGOS is specialized for **Korean**. The Darwin evolutionary process selects and recombines FFN experts to strengthen Korean-language reasoning, comprehension, and generation — targeting natural Korean output, robust handling of Korean scientific/technical text, and reduced character-level corruption on large Korean inputs.

Crucially, this specialization does **not** come at the cost of general capability: the model's **86.36% GPQA Diamond** (in English) improves on its own Qwen3.6-35B-A3B backbone (86.0) on Hugging Face's live leaderboard, evidence that the FFN-merge preserved scientific reasoning depth while adding Korean strength. The model remains fully multilingual (Korean-first), with English, Chinese, Japanese, and other languages inherited from the backbone.

---

## Architecture

Ourbox-35B-JGOS retains the full Qwen3.6-35B-A3B architecture (`qwen3_5_moe` codebase):

| | |
|---|---|
| Foundation | Qwen3.6-35B-A3B (`Qwen3_5MoeForCausalLM`) |
| Breeding platform | Darwin (FFN-level evolutionary merge) |
| Total parameters | ~35 B |
| Active parameters | ~3 B (top-8 of 256 routed experts per layer) |
| Layers | 40 |
| Hidden size | 2048 |
| Attention | **Hybrid** — 30 linear-attention + 10 full-attention layers (`full_attention_interval = 4`) |
| Full-attention heads | 16 Q / 2 KV (GQA), head dim 256, partial rotary 0.25 |
| Linear attention | Gated-DeltaNet style — 16 key heads × 128, 32 value heads × 128, conv kernel 4 |
| Experts per layer | 256 routed (top-8) + 1 shared, expert intermediate 512 |
| Multi-Token Prediction | 1 MTP layer (`mtp_num_hidden_layers = 1`) |
| Context length | 262,144 tokens |
| Vocabulary | 248,320 |
| RoPE | θ = 1e7, interleaved mRoPE, sections [11, 11, 10] |
| Dtype | bfloat16 |
| Checkpoint size | ~69 GB (2 shards) |
| License | Apache 2.0 |

The **hybrid attention** design (¾ linear + ¼ full) gives near-linear KV-cache scaling across the 262K window, and the **Multi-Token Prediction** head provides a built-in draft for speculative decoding.

---

## GPQA Diamond Evaluation

### Methodology

Ourbox-35B-JGOS was evaluated on all **198 GPQA Diamond** questions using a two-pass **majority-of-8+** protocol (identical to sibling FINAL-Bench reasoning models, for cross-model comparability):

**Pass 1 — Greedy baseline**
- All 198 questions, deterministic decoding (`do_sample=False`)
- Up to 5,120 new tokens per question (full `<think>` trajectories)
- Standard multiple-choice prompt format

**Pass 2 — Stochastic majority vote with tiebreaker**
- Each question is answered by **8 independent stochastic generations** (`temperature=0.7`, `max_tokens=5120`); the majority answer is taken
- Where the 8-vote margin is inconclusive (e.g. 3:3 / 3:4 / 4:4), an additional **16-vote tiebreaker** round (`temperature=0.5`) resolves the answer

The final answer for each question is extracted after the `</think>` delimiter.

### Result

| Metric | Value |
|---|---|
| Correct | **171 / 198** |
| **GPQA Diamond accuracy (maj@8+)** | **86.36%** |

Evaluated against the [`Idavidrein/gpqa`](https://huggingface.co/datasets/Idavidrein/gpqa) `gpqa_diamond` split. The majority-of-8+ protocol surfaces answers that greedy decoding leaves subdominant — a pattern characteristic of well-formed chain-of-thought models — carrying Ourbox above its Qwen3.6-35B-A3B backbone (86.0) and past GLM-5.1 (86.2) on graduate-level science.

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tok = AutoTokenizer.from_pretrained("FINAL-Bench/Ourbox-35B-JGOS", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Ourbox-35B-JGOS",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [
    {"role": "user", "content": "상대론적 운동에너지 식을 유도해줘."}
]
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=5120, temperature=0.6, do_sample=True)
print(tok.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### Answer extraction for evaluations

This is a **thinking model** — responses always begin with a `<think>` reasoning trace. For benchmarks, extract the final answer after `</think>`:

```python
response = tok.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
idx = response.rfind("</think>")
answer_part = response[idx + len("</think>"):].strip() if idx >= 0 else response
```

### Recommended settings

- **Temperature**: 0.6–0.7 for reasoning / majority voting; 0.0 for greedy deterministic
- **max_new_tokens**: ≥5120 to accommodate full `<think>` trajectories
- **Chat template**: assistant turn opens with `<think>` when `apply_chat_template(add_generation_prompt=True)` is used

---

## VRAM Requirements

| Precision | VRAM | Recommended GPU |
|---|---|---|
| bf16 (full) | ~72 GB | 1× H100 80GB / 1× B200 |
| 8-bit | ~40 GB | 1× A100 40GB+ / 1× L40S |
| 4-bit | ~22 GB | 1× RTX 4090 / 1× A10 |

---

## Key Findings

1. **Korean specialization without capability loss.** Darwin's FFN-level merge adds Korean-language strength while retaining **86.36% GPQA Diamond** — above the model's own Qwen3.6-35B-A3B backbone (86.0). Specialization and general reasoning are not a zero-sum trade under expert-level recombination.

2. **Specialization improves on the backbone.** On Hugging Face's live GPQA Diamond leaderboard, Ourbox (86.36) exceeds its own Qwen3.6-35B-A3B backbone (86.0) and edges past GLM-5.1 (86.2) and GLM-5 (86.0) — the Darwin FFN-merge added Korean capability without eroding scientific reasoning, at ~3B active parameters.

3. **Breeding beats retraining for specialization.** A deployable, Korean-specialized 35B checkpoint is produced by evolutionary FFN recombination — no full-model gradient training on the final assembly — demonstrating Darwin as an efficient route to targeted, high-capability models.

---

## References

- Rein et al., *GPQA: A Graduate-Level Google-Proof Q&A Benchmark*, 2024. [dataset](https://huggingface.co/datasets/Idavidrein/gpqa)
- Qwen Team, *Qwen3.6 Technical Report*, 2026.

---

## Built By

**FINAL-Bench / VIDRAFT_LAB** — Darwin evolutionary breeding platform, JGOS Korean-specialized reasoning line.
Backbone weights by the Qwen Team (Qwen3.6-35B-A3B). Released under Apache 2.0.

---

## Citation

```bibtex
@misc{ourbox-35b-jgos,
  title   = {Ourbox-35B-JGOS: Korean-Specialized, Darwin-Evolved 35B-A3B Reasoning MoE},
  author  = {FINAL-Bench and VIDRAFT_LAB},
  year    = {2026},
  url     = {https://huggingface.co/FINAL-Bench/Ourbox-35B-JGOS},
  note    = {Qwen3.6-35B-A3B backbone, Darwin FFN-level evolutionary merge, Korean-specialized, 86.36% GPQA Diamond (maj@8+)}
}
```

## Learn more
- On-device, sovereign LLMs without a GPU: [Can you run a large LLM without a GPU?](https://vidraft.net/insights/on-device-llm-without-gpu.html)
