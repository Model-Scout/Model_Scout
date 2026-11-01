---
license: apache-2.0

tags:
  - darwin
  - darwin-v8
  - darwin-neg
  - native-entropy-gating
  - NEG
  - reasoning
  - self-regulated-reasoning
  - advanced-reasoning
  - thinking
  - qwen3.5
  - qwen
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
  - multilingual
pipeline_tag: text-generation
library_name: transformers
model-index:
- name: Darwin-9B-NEG
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
      value: 84.34
      name: Accuracy
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-9B-NEG — The First Native Entropy Gating Model

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-9B-NEG"><img src="https://img.shields.io/badge/⭐_GPQA_Diamond-84.34%25_Darwin--9B--NEG-gold?style=for-the-badge" alt="GPQA"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-9B-Opus"><img src="https://img.shields.io/badge/🧬_Base-Darwin--9B--Opus-blue?style=for-the-badge" alt="Base"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis"><img src="https://img.shields.io/badge/🧬_Model-Darwin--4B--Genesis-blue?style=for-the-badge" alt="Genesis"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-9B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--9B--Opus-blue?style=for-the-badge" alt="9B"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-27B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--27B--Opus-blue?style=for-the-badge" alt="27B"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-31B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--31B--Opus-blue?style=for-the-badge" alt="31B"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-36B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--36B--Opus-blue?style=for-the-badge" alt="36B"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/collections/FINAL-Bench/darwin-family"><img src="https://img.shields.io/badge/🏠_Darwin_Family-Collection-green?style=for-the-badge" alt="Family"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Leaderboard"><img src="https://img.shields.io/badge/🏆_FINAL_Bench-Leaderboard-green?style=for-the-badge" alt="FINAL Bench"></a>
</p>

> Qwen3.5-9B backbone · 8.95B parameters · BF16 · Thinking Mode · Apache 2.0
> **The first NEG-enabled model — self-regulating reasoning with no extra library.**

---

## Abstract

**Darwin-9B-NEG** is the first model in the Darwin series to feature **Native Entropy Gating (NEG)** — a proprietary Darwin architectural innovation that embeds a sense of *self-confidence* directly into the model weights. Unlike external multi-turn iteration (MTI) techniques that require 3×–8× extra inference, NEG operates *inside* the single decoding loop and activates in fewer than 5 % of generation steps, lifting reasoning accuracy **by more than 12 percentage points at 1× inference cost**.

On the **GPQA Diamond** PhD-level reasoning benchmark (198 questions), Darwin-9B-NEG scores **84.34 %** with the full 3-stage ensemble protocol — surpassing even the published Qwen3.5-9B leaderboard result (81.7 %).

---

## What Makes Darwin-9B-NEG Different

### 🧬 Darwin Series — Evolutionary Model Merging
The Darwin family is produced by **Darwin V7**, an evolutionary breeding engine that recombines two parent LLMs into a single descendant, preserving hybrid vigour across reasoning and knowledge capabilities. **Darwin-9B-Opus** — this model's base — is the Qwen3.5-family member of the Darwin series, previously published as a stand-alone reasoning model.

### ⚡ NEG — Native Entropy Gating (Darwin V8)
**NEG** is a proprietary Darwin technology that gives the language model an architecturally-internalised *self-confidence sense*. Two tiny learnable modules ride alongside the transformer:

- **NEG-Head** (≈ 4 M params, ~ 0.05 % of total weights) predicts, at each step, the entropy of the next-token distribution from the last hidden state.
- **NEG-Gate** (1 learnable threshold) decides, on a per-token basis, whether the model is "confident enough" to commit to its top choice, or whether it should restrict its choice to a narrow top-k subset.

Because NEG is carried *inside* the model weights themselves, there is nothing extra to ship or to install: standard `transformers` loading with `trust_remote_code=True` attaches the modules automatically. The model file *is* the feature.

**Why it matters**
- **1× inference cost** — no multi-sample voting, no multi-turn loops
- **< 5 % gate activation** — negligible latency overhead versus the base model
- **+12.63 %p on GPQA Diamond** vs. the NEG-free Darwin-9B-Opus baseline (same greedy decoding, same prompt, same tokens)
- **Single-file deployment** — drop in to vLLM / SGLang / TGI / `transformers`, no new engine required
- **No trade-secret leaks** — the merge recipe is kept internal; only the final model weights are released under Apache 2.0

---

## 🏗️ Architecture Overview

```
Input Text
    ↓
[Darwin-9B-Opus backbone (frozen during NEG training)]
    ↓
Transformer Layers × 32
    ↓
last hidden state ──┐
    │               │
    ▼               ▼
 LM Head         NEG-Head
    │               │
  base logits    predicted entropy
    │               │
    └──▶ NEG-Gate ◀─┘
            │
            ▼
       guided logits
            │
            ▼
        next token
```

### Key Specifications

| Component | Value |
|:---|:---|
| Architecture | Qwen3.5 decoder-only transformer (32 layers, hidden 4096) |
| Total parameters | 8.95 B (base) + ≈ 4 M (NEG modules) |
| NEG-Head | 2-layer MLP with softplus output |
| NEG-Gate | top-k masking gate with learnable entropy threshold |
| Precision | bfloat16 |
| Context length | inherited from Darwin-9B-Opus |
| License | Apache 2.0 |

---

## 🏆 Benchmark Results — GPQA Diamond (198 PhD-level questions)

Darwin-9B-NEG ships **three decoding modes** from the *same* model weights, allowing users to trade inference cost for accuracy:

| Mode | Decoding Protocol | Inference Cost | **Accuracy** |
|:---:|:---|:---:|:---:|
| **0 · Baseline** | Darwin-9B-Opus greedy (NEG disabled) | 1× | 51.01 % |
| **1 · Pure NEG** | greedy decoding **with NEG enabled** | **1×** | **63.64 %** |
| **2 · Permutation** | NEG + choice-order permutation (4 orderings, majority) | 4× | 76.26 % |
| **3 · Ensemble Refinement** | NEG + permutation + temperature-sampled ensemble | ≈ 20× | **🥇 84.34 %** |

**Improvements:**
- Pure NEG (mode 1) vs. baseline: **+12.63 %p at identical inference cost**
- Ensemble (mode 3) vs. baseline: **+33.33 %p**
- Ensemble vs. Qwen3.5-9B leaderboard score (81.7 %): **+2.64 %p**

> **Gate activation rate**: 4.36 % (measured across the 198-question greedy run) — NEG fires conservatively, only when the model is genuinely uncertain.

---

## 🚀 Usage

### Quick start — Pure NEG greedy (mode 1, sales default)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tok = AutoTokenizer.from_pretrained(
    "FINAL-Bench/Darwin-9B-NEG",
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Darwin-9B-NEG",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [
    {"role": "user", "content": "Solve: If f(x) = x³ − 3x + 2, find and classify all critical points."}
]
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=2048, do_sample=False)
print(tok.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True))
```

### Using the bundled NEG loader helper

`modeling_darwin_neg.py` is shipped inside the repo and provides a convenience loader:

```python
from modeling_darwin_neg import load_darwin_neg

model = load_darwin_neg(
    "FINAL-Bench/Darwin-9B-NEG",
    hf_token="hf_xxx",
)
```

### Mode selection

- **Mode 1 (Pure NEG)**: default `do_sample=False`, NEG is always on.
- **Mode 2 (Permutation)**: shuffle the option order 4 times, greedy each, majority-vote.
- **Mode 3 (Ensemble)**: production protocol combining permutation, temperature sampling and second-opinion re-query (internal; reproduction scripts are released separately).

---

## 🧬 Model Lineage

```
Qwen/Qwen3.5-9B   +   (Opus-distilled sibling)
         ╲                ╱
          Darwin V7 evolutionary merge
                   ▼
          Darwin-9B-Opus  ── stand-alone reasoning model (Apache 2.0)
                   ▼
          NEG-Head / NEG-Gate training (Darwin V8)
                   ▼
          Darwin-9B-NEG  ── THIS MODEL
```

- **Base**: [FINAL-Bench/Darwin-9B-Opus](https://huggingface.co/FINAL-Bench/Darwin-9B-Opus) (weights frozen during NEG training)
- **Technology generation**: Darwin V8 (Native Entropy Gating) — successor to Darwin V7 (evolutionary merging)

---

## 🎯 Recommended Use-Cases

- **Graduate-level STEM reasoning** — physics, chemistry, biology, mathematics (GPQA-style)
- **Mathematical problem solving** (MATH, AIME-style)
- **Code reasoning and debugging** (HumanEval-style)
- **Complex chain-of-thought** tasks where a small reasoning model with a big boost is desired

## ⚠️ Limitations

- Optimised for English first, with secondary support for Korean / Chinese / Japanese.
- At 8.95 B parameters, knowledge coverage is smaller than the larger Darwin models (27B / 31B / 36B) — for pure world-knowledge tasks consider Darwin-36B-Opus.
- The Ensemble mode (84.34 %) uses ≈ 20× inference; choose Pure NEG (mode 1) for cost-sensitive deployments.

---

## 📚 Citation

```bibtex
@misc{darwin9b_neg_2026,
  title  = {Darwin-9B-NEG: Native Entropy Gating for Self-Regulated Reasoning at 1x Inference Cost},
  author = {FINAL-Bench / Darwin Research Team},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-9B-NEG}},
  note   = {Darwin V8 — Native Entropy Gating technology generation}
}
```

---

## 🔗 Related Darwin Models

- **Darwin-36B-Opus** — MoE 36B, Qwen3.6-35B-A3B × Opus distilled, GPQA 88.4 %
- **Darwin-31B-Opus** — 31B multilingual-strong reasoning
- **Darwin-27B-Opus** — 27B dense, GPQA 86.9 %
- **Darwin-28B-Opus** — Qwen3.6-27B × rico03 Opus distilled (new 2026-04)
- **Darwin-9B-Opus** — this model's base, Qwen3.5-9B family
- **Darwin-4B-Genesis** — smallest member, Gemma4 family

---
This model is introduced in [Darwin Family](https://arxiv.org/abs/2605.14386).

*Darwin V8 · Sealed 2026-04-24 · FINAL-Bench*
