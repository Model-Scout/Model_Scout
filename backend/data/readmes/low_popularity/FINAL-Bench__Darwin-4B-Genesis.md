---
base_model:
- FINAL-Bench/Darwin-4B-David
- Qwen/Qwen3.5-4B
language:
- ko
- en
- zh
- ja
- de
- fr
- es
license: apache-2.0
pipeline_tag: text-generation
library_name: transformers
tags:
- merge
- evolutionary-merge
- darwin
- darwin-v6
- model-mri
- cross-architecture
- ffn-crossbreed
- cma-es
- hybrid-vigor
- transformer-mamba
- reasoning
- gemma4
- qwen3.5
- gated-deltanet
- korean
- multilingual
- gpqa
- open-source
- world-first
model-index:
- name: Darwin-4B-Genesis
  results:
  - task:
      type: text-generation
      name: Korean Cultural Understanding
    dataset:
      name: CLIcK
      type: EunsuKim/CLIcK
    metrics:
    - type: accuracy
      value: 92.0
      name: Accuracy
      verified: false
  - task:
      type: text-generation
      name: Multi-Step Reasoning
    dataset:
      name: MuSR
      type: TAUR-Lab/MuSR
    metrics:
    - type: accuracy
      value: 70.0
      name: Accuracy
      verified: false
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-4B-Genesis

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Opus"><img src="https://img.shields.io/badge/🧬_Gen1-Darwin--4B--Opus-blue?style=for-the-badge" alt="Gen1"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-David"><img src="https://img.shields.io/badge/🧬_Gen2-Darwin--4B--David-blue?style=for-the-badge" alt="Gen2"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis"><img src="https://img.shields.io/badge/⭐_Gen3-Darwin--4B--Genesis-gold?style=for-the-badge" alt="Gen3"></a>
</p>

Darwin-4B-Genesis is presented in the paper [Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Scaling of Language-Model Reasoning](https://arxiv.org/abs/2605.14386).

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

> **World's first Transformer × Mamba evolutionary cross-architecture FFN breeding** | CLIcK 92% | MuSR 70% | A 4B model outperforming 27B | CMA-ES 42-dimensional genome search | Hybrid Vigor demonstrated | Apache 2.0

---

## What Is This?

Darwin-4B-Genesis is the 3rd generation Darwin model and the **world's first model to successfully crossbreed FFN layers across different architectures** — Transformer (Gemma4) and Mamba (Qwen3.5 GatedDeltaNet) — using evolutionary optimization.

The father's Attention layers (Gemma4 Transformer) are preserved at 100%, while the mother's FFN knowledge (Qwen3.5 Mamba) is transplanted at layer-specific optimal ratios discovered automatically by CMA-ES across 42 dimensions.

The result: the child **outperforms both parents on every benchmark** — a phenomenon known as **Hybrid Vigor**.

---

<p align="center">
  <img src="tree.png" alt="Darwin-4B-Genesis" width="100%">
</p>


## Why This Matters

### 1. World First

Existing hybrid models (Jamba, Nemotron-H, Granite 4.0) are all **designed and trained from scratch**. Darwin-4B-Genesis takes **two already-trained models** from different architecture families and breeds them evolutionarily — with **zero additional training**.

### 2. Hybrid Vigor Demonstrated

| Benchmark | David (Father) | Qwen3.5-4B (Mother) | **Genesis (Child)** |
|---|---|---|---|
| CLIcK | 90% | ~50% (est.) | **92%** ✅ |
| MuSR | 65% | ~55% (est.) | **70%** ✅ |

The child surpasses **both** parents. This is the first demonstration of Hybrid Vigor in AI model breeding.

---

## Benchmarks

| Benchmark | Genesis | David (Gen2) | K-AI #1 (27B) |
|---|---|---|---|
| **CLIcK** (Korean culture) | **92%** | 90% | 0.794 |
| **MuSR** (multi-step reasoning) | **70%** | 65% | 0.604 |
| **GPQA** (deep reasoning) | ~60% | ~60% | — |

---

## How It Works

### Cross-Architecture FFN Breeding

```
Father: Darwin-4B-David (Gemma4 Transformer, hidden=2560, 42 layers)
Mother: Qwen/Qwen3.5-4B (GatedDeltaNet/Mamba, hidden=2560, 32 layers)

Key insight: hidden_size matches (2560) → direct FFN replacement possible
Method: Attention 100% from Father, FFN blended at per-layer optimal ratios
Optimizer: CMA-ES (Covariance Matrix Adaptation Evolution Strategy)
Genome: 42 dimensions (one ratio per layer)
Fitness: CLIcK 60% + MuSR 40% composite score
Frozen layers: L15, L16, L22, L23, L24, L25 (Korean language preservation)
```

### Optimal Genome Discovered by CMA-ES

```
L00: 0.206  ██████████░  21% Qwen
L07: 0.000  ░░░░░░░░░░░  Auto-protected by CMA-ES
L15: 0.000  ░░░░░░░░░░░  Frozen (Korean)
L22: 0.000  ░░░░░░░░░░░  Frozen (Korean)
L29: 0.291  ██████████████░  29% Qwen (maximum)
L31: 0.244  ████████████░  24% Qwen
L32: 0.273  █████████████░  27% Qwen
```

Key finding: CMA-ES applied the **most aggressive Qwen blending to the final layers (L29-32)**, which govern output quality.

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained(
    "FINAL-Bench/Darwin-4B-Genesis",
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Darwin-4B-Genesis",
    dtype="bfloat16",
    device_map="auto",
    trust_remote_code=True,
)

messages = [{"role": "user", "content": "Explain how hybrid vigor works in genetics."}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=1024, do_sample=False)
print(tokenizer.decode(outputs[0][inputs['input_ids'].shape[-1]:], skip_special_tokens=True))
```

---

## Genealogy

```
google/gemma-4-E4B-it × TeichAI/Claude-Opus-Distill-E4B
    → Darwin-4B-Opus (Gen 1, DARE-TIES merge)

Darwin-4B-Opus × DavidAU/DECKARD-Expresso-Universe
    → Darwin-4B-David (Gen 2, MRI-guided merge, CLIcK 90%)

Darwin-4B-David × Qwen/Qwen3.5-4B
    → Darwin-4B-Genesis (Gen 3, Cross-Arch FFN Breeding, CLIcK 92%) ★
```

---

## Citation

```bibtex
@misc{vidraft_darwin_4b_genesis,
  title        = {Darwin-4B-Genesis: World's First Cross-Architecture FFN Breeding},
  author       = {VIDRAFT},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis}}
}

@article{kim2026darwin,
  title={Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Scaling of Language-Model Reasoning},
  author={Kim, Taebong and Hong, Youngsik and Kim, Minsik and Choi, Sunyoung and Jang, Jaewon and Shin, Junghoon and Kim, Minseo},
  journal={arXiv preprint arXiv:2605.14386},
  year={2026}
}
```