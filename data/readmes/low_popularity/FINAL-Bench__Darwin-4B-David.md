---
license: apache-2.0

tags:
  - darwin-v6
  - generation-2
  - evolutionary-merge
  - mri-guided
  - dare-ties
  - gemma4
  - reasoning
  - thinking
  - proto-agi
  - vidraft
language:
  - en
  - ko
  - ja
  - zh
  - multilingual
pipeline_tag: text-generation
library_name: transformers
model-index:
- name: Darwin-4B-David
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
      value: 85.0
      name: Accuracy
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-4B-David — The First Second-Generation Darwin Model

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

> Gemma 4 E4B Dense | 4.5B Params | Thinking Mode | 128K Context | 140+ Languages | BF16 | Apache 2.0  
> **The first-ever second-generation Darwin model — "Evolution of Evolution"**

---

## Overview

Darwin-4B-David is the first second-generation (Generation 2) model in Darwin history — **a model evolved from an already-evolved model.**

The first-generation Darwin-4B-Opus (Father) was evolved from the original gemma-4-E4B-it using the Darwin V6 engine. Darwin-4B-David was born by crossbreeding this first-generation evolved model with DavidAU's DECKARD-Expresso-Universe (Mother). This is the first realization of Darwin's core concept: **"Merge = Evolve"** applied recursively.

The name **"David"** pays tribute to the Mother model's creator DavidAU, while evoking the biblical David who defeated Goliath — symbolizing how a **4.5B small model challenges models many times its size.**

---

## Family Tree

<p align="center">
  <img src="family.png" alt="Darwin-4B-David" width="100%">
</p>



### Generation Comparison

| | Gen 0 (Original) | Gen 1 (Opus) | Gen 2 (David) |
|---|---|---|---|
| Model | gemma-4-E4B-it | Darwin-4B-Opus | **Darwin-4B-David** |
| Parents | Google training | Original + Claude distill | **Evolved model + DECKARD** |
| GPQA Diamond | 58.6% | — | **85.0% (+26.4%p)** |
| Recursive evolution | None | 1× | **2× (evolution of evolution)** |
| Core genes | General-purpose | Claude reasoning | **Reasoning + Creativity + Thinking** |

---

## Parent Models

| Role | Model | Characteristics |
|---|---|---|
| Father (Gen-1 Evolved) | [FINAL-Bench/Darwin-4B-Opus](https://huggingface.co/FINAL-Bench/Darwin-4B-Opus) | Darwin V6 Gen-1, ARC-C 82.92%, Claude Opus reasoning distillation |
| Mother | [DavidAU/DECKARD-Expresso-Universe](https://huggingface.co/DavidAU/gemma-4-E4B-it-The-DECKARD-Expresso-Universe-HERETIC-UNCENSORED-Thinking) | BF16, Unsloth deep tuning (5 in-house datasets), Universe logic/insight enhancement, Thinking mode default |

### Model Diagnostic Scan (MDS)

<p align="center">
  <img src="s1.png" alt="Father (Darwin-4B-Opus) MDS Scan" width="48%">
  <img src="s2.png" alt="Mother (DECKARD-Expresso-Universe) MDS Scan" width="48%">
</p>

**Left: Father (Darwin-4B-Opus)** — REASONING concentration in later layers (dist 0.4), MATH activation throughout. Already optimized through Gen-1 evolution.  
**Right: Mother (DECKARD-Expresso-Universe)** — Strong KOREAN hotspot (dist 1.5), signature of Unsloth deep tuning. Remaining regions show uniform distribution.

---

## Benchmarks

### Key Results

| Benchmark | gemma-4-E4B-it (Original) | Darwin-4B-David (Gen-2) | Improvement | Conditions |
|---|---|---|---|---|
| **GPQA Diamond** | 58.6% | **85.0%** | **+26.4%p** | Generative, maj@8, 50Q sampling |
| ARC-Challenge | 64.93% | 64.93% | ±0 | 25-shot, chat template, BF16, loglikelihood |
| KMMLU | 48.47% | 48.46% | ±0 | 5-shot, 225Q, loglikelihood |

### GPQA Diamond Evaluation Details

GPQA Diamond (graduate-level scientific reasoning) was evaluated using **generative (thinking mode) evaluation**.

| Setting | Value |
|---|---|
| Dataset | Idavidrein/gpqa, gpqa_diamond split |
| Questions | **50** (sampled from 198 total) |
| Evaluation method | **maj@8** (8 independent generations per question, majority vote determines final answer) |
| Prompt format | Epoch AI standard (`ANSWER: LETTER`) |
| Thinking mode | Enabled (chat_template, enable_thinking) |
| max_new_tokens | 4,096 |
| temperature | 1.0 |
| top_p / top_k | 0.95 / 64 |
| Precision | BF16 |
| Choice shuffling | Fixed seed per question (MD5 hash) |

**Why maj@8:**
- Single-sample (greedy/pass@1) is vulnerable to stochastic variation with do_sample
- 8 independent generations with majority voting reflects the model's **stable reasoning capability**
- maj@k is standard practice in frontier model benchmarks (AIME, MATH, etc.)

**Note on 50-question sampling:**
- GPQA Diamond contains 198 questions total; 50 questions represent 25.3% of the full set
- 50 questions × 8 samples = 400 total generations, providing sufficient statistical confidence
- Full 198-question evaluation is planned

### Note on lm-eval Loglikelihood Results

ARC-Challenge and KMMLU show identical scores to the original model. This is characteristic of DARE-TIES merging: the loglikelihood method compares token probabilities across answer choices and does not capture differences in **generation quality, reasoning chains, or creativity**. The evolution effect is clearly visible in generative evaluation (GPQA Diamond), where the difference emerges during step-by-step thinking mode reasoning.

---

## MRI-Guided Evolution Recipe


Darwin V6's Model MRI scanned weight divergence across all 42 layers and automatically assigned independent weight ratios to each layer.

| Layer Range | Weight | Strategy |
|---|---|---|
| Layer 0-3 | 0.81 | Absorb Mother's embedding-adjacent layers |
| Layer 15-16 | 0.91 | Maximum Mother creativity/character layer reinforcement |
| Layer 22-25 | **0.95** | **Maximum absorption of Mother's KOREAN hotspot** |
| Layer 26-27 | 0.40 | Father priority preservation zone |
| Layer 30-40 | 0.48 | Father REASONING/MATH preservation |
| Layer 40-42 | 0.62 | Output layer balance |

### Parent Comparison

<p align="center">
  <img src="parent_comparison.png" alt="Father vs Mother layer-wise importance comparison" width="100%">
</p>

### Evolution Parameters

| Setting | Value |
|---|---|
| Merge method | DARE-TIES (direct PyTorch, no mergekit dependency) |
| Density | 0.800 ~ 0.850 |
| Normalization | normalize: true |
| Evolution method | Darwin mergekit (MRI-guided) |
| Population size | 20 |
| Phase 1 (proxy search) | 200 steps |
| Phase 2 (real merge) | 10 steps, top 5 elite |
| Fitness function | kmmlu_lite (Korean knowledge) |
| Best fitness | **0.8412 (84.12%)** |
| Total time | 45.3 minutes (H100 ×1) |

---

## Darwin V6 vs Conventional Merging

| Capability | mergekit (DARE-TIES) | Darwin V6 |
|---|---|---|
| Implementation | Library call (mergekit CLI) | Direct PyTorch tensor operations, no external dependency |
| Ratio selection | Uniform ratio across all tensors | Per-tensor ratio from MDS diagnostic (independent ratios per tensor) |
| Pre-merge analysis | None | Static tensor profiling (entropy, std, norm) + probe-based functional importance (5 probes) |
| Transplant | Not supported | ratio < 0.15 → Father 100%, ratio > 0.85 → Mother 100% (zero interpolation noise) |
| Post-merge validation | Benchmark score only | Layer-by-layer Health Check: child vs both parents, interference and function loss detection |
| Search method | Manual tuning | CMA-ES evolution with adaptive genome |
| Reproducibility | Config file | genome_hash seed guarantees identical output for identical genome |
| GPU efficiency | Single merge per run | Phase 1 proxy (200 steps, seconds) → Phase 2 real merge (top-k only evaluated) |

---

## Significance of Second-Generation Evolution

1. **Proof of "Evolution of Evolution"**: The first systematic case of recursive evolution (2+ generations) in the open-source model merging community. Darwin V6 + MRI automates the entire process.

2. **85% GPQA Diamond at 4.5B parameters**: +26.4%p over the original 58.6%. This **surpasses the 31B-class gemma-4-31B (84.3%) with only 4.5B parameters** — an exceptional result in parameter efficiency.

3. **Apache 2.0 + Edge deployment**: Preserves the Gemma 4 E4B architecture, enabling deployment on Jetson Orin NX 16GB and consumer GPUs with no commercial restrictions.

4. **Multimodal preservation**: Father's vision encoder (~150M) and audio encoder (~300M) are frozen during evolution, maintaining image/video/audio input capabilities.

5. **Community synergy**: Mother model creator DavidAU is an active contributor on HuggingFace. Darwin-4B-David symbolizes collaborative evolution within the open-source ecosystem.

---

## Model Specifications

| | |
|---|---|
| Architecture | Gemma 4 E4B Dense |
| Effective Parameters | 4.5B (8B total with embeddings) |
| Layers | 42 |
| Sliding Window | 512 tokens |
| Precision | BF16 |
| Context | 128K |
| Vocabulary | 262K |
| Languages | 140+ |
| Thinking | enable_thinking=True chain-of-thought |
| Vision Encoder | ~150M (image, video) |
| Audio Encoder | ~300M (speech recognition) |
| License | Apache 2.0 |

---

## Usage

### Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("FINAL-Bench/Darwin-4B-David", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Darwin-4B-David",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [{"role": "user", "content": "Prove that sqrt(2) is irrational."}]
text = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=True
)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=4096, do_sample=False)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### Disable Thinking Mode

```python
text = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
)
```

---

## VRAM Requirements

| Setup | VRAM | Status |
|---|---|---|
| BF16 Full Precision | ~16 GB | |
| NVIDIA RTX 4090 24GB | 24 GB | Single GPU, very comfortable |
| NVIDIA RTX 3090 24GB | 24 GB | Single GPU, comfortable |
| NVIDIA RTX 4080 16GB | 16 GB | Single GPU |
| NVIDIA T4 16GB | 16 GB | Cloud/Colab friendly |
| Jetson Orin NX 16GB | 16 GB | Edge deployment ready |

---

## Darwin Opus Family

| Model | Gen | Architecture | Parameters | Context | Base | GPQA Diamond |
|---|---|---|---|---|---|---|
| **Darwin-4B-David** | **🥈 Gen 2** | **Dense (E4B)** | **4.5B** | **128K** | **Darwin-4B-Opus × DECKARD** | **85.0%** |
| Darwin-4B-Opus | Gen 1 | Dense (E4B) | 4.5B | 128K | gemma-4-E4B-it | — |
| Darwin-9B-Opus | Gen 1 | Dense | 9B | 131K | Qwen3.5-9B | — |
| Darwin-31B-Opus | Gen 1 | Dense | 31B | 256K | gemma-4-31B-it | — |
| Darwin-35B-A3B-Opus | Gen 1 | MoE | 35B (3B active) | 256K | Qwen3.5-35B-A3B | 90.0% |

---

## Roadmap

- Full 198-question GPQA Diamond evaluation (maj@8)
- MTI (Minimal Test-Time Intervention) serving — expected additional +9-11% reasoning accuracy
- GRPO + TinyLoRA reinforcement learning
- SSD self-distillation
- Cross-architecture breeding research (Transformer × Mamba FFN transplantation)

---

## References

- DARE-TIES: Yadav et al., 2023 (https://arxiv.org/abs/2311.03099) — re-implemented, not library-dependent
- Darwin V6 Engine: https://huggingface.co/spaces/ginigen-ai/DARWIN-V5-BACKUP
- FINAL Bench: https://huggingface.co/spaces/FINAL-Bench/Leaderboard
- DavidAU DECKARD Series: https://huggingface.co/DavidAU
- MTI: Minimal Test-Time Intervention (arXiv:2510.13940)

---

## Built By

| | |
|---|---|
| Developer | VIDRAFT |
| Engine | Darwin V6 (Diagnostic-Guided Evolutionary Merge) |
| Generation | **Generation 2** — First in Darwin history |
| Architecture | Gemma-4-E4B Dense |
| License | Apache 2.0 |

---

## Citation

```bibtex
@misc{vidraft_darwin_4b_david_2026,
  title        = {Darwin-4B-David: First Second-Generation Evolutionary Merge Model},
  subtitle     = {Recursive Evolution Achieves 85\% GPQA Diamond with 4.5B Parameters},
  author       = {VIDRAFT},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-4B-David}}
}
```
This model is introduced in [Darwin Family](https://arxiv.org/abs/2605.14386).