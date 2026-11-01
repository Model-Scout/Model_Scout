---
license: other
license_name: qwen-community-1.0
license_link: LICENSE
language: [en, ko, zh, ja, multilingual]
library_name: gguf
pipeline_tag: text-generation
base_model: FINAL-Bench/Darwin-180B-RSI-R3
base_model_relation: quantized
tags:
  - gguf
  - llama.cpp
  - pocket
  - darwin
  - darwin-rsi
  - model-level-rsi
  - dgx-spark
  - on-device
  - moe
---

# POCKET-Darwin-180B-GGUF

<p align="center">
<a href="https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF"><img src="https://img.shields.io/badge/POCKET-4--bit_GGUF_·_111_GB-0f766e?style=for-the-badge"></a>
<a href="#quality--before-vs-after-quantization"><img src="https://img.shields.io/badge/Quality-=_BF16_(87.65%25)-16a34a?style=for-the-badge"></a>
<a href="#where-it-runs"><img src="https://img.shields.io/badge/💻_Laptop-8GB_GPU_%2B_32GB_RAM_·_4.17_tok%2Fs-9333ea?style=for-the-badge"></a>
<a href="#where-it-runs"><img src="https://img.shields.io/badge/CPU_only-18--21_tok%2Fs-0369a1?style=for-the-badge"></a>
<a href="#device-classes-and-recommended-specs"><img src="https://img.shields.io/badge/🧊_Mini_PC-128GB_RAM_·_no_GPU-0d9488?style=for-the-badge"></a>
<a href="#where-it-runs"><img src="https://img.shields.io/badge/NVIDIA-DGX_Spark_·_1_machine-76b900?style=for-the-badge"></a>
<a href="#ztc-zero-token-confidence"><img src="https://img.shields.io/badge/ZTC-AUC_0.758-7c3aed?style=for-the-badge"></a>
<a href="https://github.com/ggml-org/llama.cpp"><img src="https://img.shields.io/badge/llama.cpp-b11048%2B-111827?style=for-the-badge"></a>
</p>
<p align="center">
<a href="https://huggingface.co/FINAL-Bench/Darwin-180B-RSI"><img src="https://img.shields.io/badge/🧬_Original-Darwin--180B--RSI-e11d48?style=for-the-badge"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3"><img src="https://img.shields.io/badge/🔁_RSI_Round_2-Darwin--180B--RSI--R3-be123c?style=for-the-badge"></a>
</p>
<p align="center">
<a href="https://vidraft.net"><img src="https://img.shields.io/badge/🌐_VIDRAFT-vidraft.net-111827?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/Idavidrein/gpqa"><img src="https://img.shields.io/badge/GPQA_Diamond-94.44%25_%231-gold?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro"><img src="https://img.shields.io/badge/MMLU--Pro-88.12%25_%231-2563eb?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/MMMU/MMMU_Pro"><img src="https://img.shields.io/badge/MMMU--Pro-79.48%25_%231-0891b2?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/MathArena/aime_2026"><img src="https://img.shields.io/badge/AIME_2026-100%25_%231-dc2626?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/MathArena/hmmt_feb_2026"><img src="https://img.shields.io/badge/HMMT_Feb_2026-100%25_%231-ea580c?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/LEXam-Benchmark/LEXam"><img src="https://img.shields.io/badge/LEXam_(Law)-68.94%25_%231-4f46e5?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/joelniklaus/LEXam-hard"><img src="https://img.shields.io/badge/LEXam--hard_(Law)-45.72_%231-6d28d9?style=for-the-badge"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-27B-RSI"><img src="https://img.shields.io/badge/Self--Improving-RSI-e11d48?style=for-the-badge"></a>
<a href="https://huggingface.co/collections/FINAL-Bench/ztc-models-jev-ecosystems"><img src="https://img.shields.io/badge/ZTC-Zero--Token_Confidence-7c3aed?style=for-the-badge"></a>
</p>
<p align="center">
<a href="https://arxiv.org/abs/2605.14386"><img src="https://img.shields.io/badge/arXiv-2605.14386_Darwin_Family-b31b1b?style=for-the-badge"></a>
<a href="https://huggingface.co/papers/2609.20269"><img src="https://img.shields.io/badge/Paper-2609.20269_Latin_Square-b31b1b?style=for-the-badge"></a>
<a href="https://huggingface.co/collections/FINAL-Bench/darwin-family"><img src="https://img.shields.io/badge/🧬_Collection-Darwin_Family-16a34a?style=for-the-badge"></a>
<a href="https://huggingface.co/collections/FINAL-Bench/ztc-models-jev-ecosystems"><img src="https://img.shields.io/badge/🏛️_Collection-ZTC_Models-7c3aed?style=for-the-badge"></a>
</p>


**A 180B frontier model from a laptop to DGX Spark.** A 4-bit GGUF build of [Darwin-180B-RSI-R3](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3) (111.3 GB, 4 files) for llama.cpp. It runs on a **gaming laptop with an 8 GB GPU and 32 GB RAM**, a **128 GB mini PC**, a CPU-only server, a single datacenter GPU, or **NVIDIA DGX Spark**.

- **Quality kept:** MMLU-Pro (2,000 questions, paired) **87.65% vs 87.65%** for the BF16 original, difference **+0.00 points, 95% CI [−0.95, +1.00]**.
- **Runs on a laptop:** **4.17 tokens/s** on an RTX 5060 Laptop GPU (8 GB) with 32 GB RAM.
- **Runs without a GPU:** **18–21 tokens/s** on one server CPU socket, **78.8 GB peak RAM**.
- **Runs on a mini PC:** any mini PC with **128 GB RAM** holds the whole model in memory, no GPU needed.
- **Built-in confidence:** ZTC AUC **0.758** reading its own state; the 20% of questions it is most sure about are **97.5%** correct. Probe file and script included in [`ztc/`](./ztc).
- **Shorter answers:** on the same 2,000 questions, answers average **3,694 tokens vs 4,322** for the same-format parent build (−14.5%).

## From an 8-GPU server to a laptop

| | Darwin-180B-RSI original (BF16) | **POCKET-Darwin-180B (this model)** |
|---|---|---|
| Size | 360 GB (131 files) | **111.3 GB (4 files)** |
| Hardware | **4–8× NVIDIA B200**, or **8× NVIDIA H100 (80 GB)** | **a laptop with an 8 GB GPU and 32 GB RAM** · a 128 GB mini PC · a CPU-only server · one DGX Spark |
| Hardware cost (industry estimate) | an 8× H100 server: roughly **USD 350,000+** | a gaming laptop: roughly **USD 1,500** |
| MMLU-Pro | 87.65% | **87.65% (identical)** |

At BF16 the original weighs 360 GB, more than four 80 GB H100s can hold, so in practice it is served on an 8-GPU H100 server; we ran it on 4× B200, and the original card recommends 8× B200. POCKET brings that class of model to a personal computer.

## Darwin + POCKET in one picture

- **Darwin (model-level RSI):** built on **Qwen3.8-Flash-Next** (180B MoE, 512 routed experts). The model solves verifiable problems, keeps only its own checked-correct solutions and trains on them, no human-written answers. Only attention paths and shared experts are trained; the experts, router, per-layer n-gram embeddings and MTP head stay intact.
- **POCKET (on-device):** a graft onto the widely used UD-Q4_K_XL layout, exactly the 300 R3-changed tensors re-encoded in the layout's own format, every other byte identical; about **3B active parameters** per token; experts read on demand from SSD via memory mapping.

## What this is

Darwin-180B-RSI is [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) improved by **model-level recursive self-improvement (RSI)**: the model solves verifiable problems, keeps only its own solutions that check out, and trains on them, no human-written solutions. R3 is the second round on top of R1.

Only 300 tensors changed between the parent and R3 (attention paths and shared experts; all 512 routed experts, the router, the per-layer n-gram embeddings and the MTP head are unchanged). So this build takes the widely used [Unsloth UD-Q4_K_XL](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF) layout of the parent and replaces exactly those 300 tensors with R3's weights, encoded in the same format the layout uses for them (Q8_0). Every other byte is identical to the parent build.

Verified before release:
- all 300 target tensors found, same type and size, read back equal to R3, 300/300
- conversion verified against the parent build: 570 untouched tensors byte-identical
- loads and runs in llama.cpp b11048

## Quality, before vs after quantization

MMLU-Pro, 2,000 questions stratified by subject (fixed by question-id hash, never chosen by looking at results), 0-shot CoT, temperature 1.0, top-p 0.95, top-k 20, min-p 0, seed 7, up to 131K tokens. Paired bootstrap 95% CI on the same questions.

| Build | Accuracy | Paired difference |
|---|---|---|
| Darwin-180B-RSI-R3 BF16 (vLLM) | 87.65% | - |
| **POCKET-Darwin-180B-GGUF (this, llama.cpp)** | **87.65%** | **vs R3 BF16: +0.00 [−0.95, +1.00]** |

Zero truncated answers. **4-bit quantization costs nothing measurable.**

## The RSI gain carries over

Model-level RSI lifted R3 over R1 on held-out SuperGPQA by **+1.03 points (95% CI [+0.05, +2.00], statistically significant)**: 1,000 questions never used in training or selection. Because this build keeps every R3-changed tensor at 8-bit and matches R3 BF16 exactly on MMLU-Pro, it carries that gain to a single machine. See the [R3 card](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3).

## Same budget, more answers: R0 vs R3 inside the same 4-bit build

This build is the parent's public UD-Q4_K_XL file with only the 300 RSI-changed tensors swapped in, so comparing it with the parent 4-bit build isolates the effect of RSI: everything else is byte-identical.

Held-out SuperGPQA, 1,000 questions never used in training or selection, 4 samples each, 16K generation budget, same settings for both:

| Build | Mean of 4 | Single sample | Majority of 4 |
|---|---:|---:|---:|
| Parent Qwen3.8-Flash-Next UD-Q4_K_XL (R0) | 59.10% | 58.70% | 63.40% |
| **POCKET-Darwin-180B (R3, this)** | **61.55%** | **62.20%** | **65.40%** |

Paired difference (mean of 4): **+2.45 points, 95% CI [+1.54, +3.36]**.

POCKET reasons more concisely, so more of its answers finish within the same budget (675 vs 798 of 4,000 samples reached the 16K cap) and it uses fewer tokens: **13% less per question** (geometric mean of per-question ratios) and **10% less in total** (6,716 to 6,051 tokens on average). The largest gains are on the longest questions, where the parent often runs out of budget before answering.

## Reference, the original Darwin-180B-RSI (BF16) benchmark results

POCKET carries the weights of the Darwin-180B-RSI line. For reference, these are the official results of the original BF16 model ([Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI)), **#1 on seven Hugging Face official leaderboards**.

| Benchmark | Score | Setting | Leaderboard |
|:---|:---:|:---|:---|
| **GPQA Diamond** (198) | **94.44** | majority vote over up to 16 samples · 131,072-token thinking budget | [**#1**](https://huggingface.co/datasets/Idavidrein/gpqa) |
| **MMLU-Pro** (12,032) | **88.12** | single sample · 131,072-token thinking budget | [**#1**](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) |
| **AIME 2026** (30) | **100.0** | majority vote over 16 samples (mean accuracy 98.75) · 131,072-token thinking budget | [**#1**](https://huggingface.co/datasets/MathArena/aime_2026) |
| **HMMT Feb 2026** (33) | **100.0** | majority vote over 16 samples (mean accuracy 96.59) · 131,072-token thinking budget | [**#1**](https://huggingface.co/datasets/MathArena/hmmt_feb_2026) |
| **MMMU-Pro** (vision, 1,730) | **79.48** | majority vote over 3 samples · 131,072-token thinking budget | [**#1**](https://huggingface.co/datasets/MMMU/MMMU_Pro) |
| **LEXam** (law, MCQ 4-choice, 1,655) | **68.94** | majority vote over 4 samples (single sample 60.54 · mean 61.42) · 32,768-token thinking budget | [**#1**](https://huggingface.co/datasets/LEXam-Benchmark/LEXam) |
| **LEXam-hard** (law, open-ended, 518) | **45.72** | single sample · 32,768-token thinking budget (60 truncated answers regenerated at 120K) · judged by DeepSeek-R1-0528 per the official eval.yaml | [**#1**](https://huggingface.co/datasets/joelniklaus/LEXam-hard) |

Head-to-head with frontier models (published scores):

| Model | AIME 2026 | GPQA Diamond | MMLU-Pro | MMMU-Pro | HMMT Feb 2026 | LEXam | LEXam-hard |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **🧬 Darwin-180B-RSI (ours · 🇰🇷)** | **100** 🥇 | **94.44** 🥇 | **88.12** 🥇 | **79.48** 🥇 | **100** 🥇 | **68.94** 🥇 | **45.72** 🥇 |
| Inkling (Thinking Machines) | - | - | - | - | - | - | 40.82 |
| Kimi-K3 (Moonshot AI) | - | 93.5 | - | - | - | - | 29.54 |
| Kimi-K2.6 (Moonshot AI) | 96.4 | 90.5 | - | 79.4 | 92.7 | - | 36.18 |
| DeepSeek-V4-Pro (DeepSeek) | - | 90.1 | 87.5 | - | - | - | 38.93 |
| Qwen3.5-397B-A17B (Alibaba) | 93.33 | 88.4 | 87.8 | - | 87.88 | - | - |
| MiniMax-M2.1 (MiniMax) | - | 80.81 | 88 | - | - | - | - |
| GLM-5 (Zhipu AI) | 95.83 | 86 | 86 | - | 86.36 | - | - |
| Intern-S2-Preview (Shanghai AI Lab) | - | - | 88 | 76.88 | 87.31 | - | - |
| Step-3.5-Flash (StepFun) | 96.67 | 83.5 | 84.4 | - | 86.36 | - | - |
| DeepSeek-R1 (DeepSeek) | - | - | - | - | - | 52.41 | - |
| Qwen3-235B-A22B-Thinking-2507 (Alibaba) | - | - | - | - | - | 48.19 | - |

Settings for the reference results: BF16, vLLM, temperature 1.0 · top-p 0.95 · top-k 20, up to 131,072 thinking tokens; voting as listed per benchmark (see the [original card](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI#evaluation-protocol)).

## ZTC: zero-token confidence

ZTC reads a "will this answer be right?" signal from the model's own hidden state at the last prompt token, **before it writes a single token**. One forward pass over the prompt, no answer tokens, no second model. Use it to send uncertain questions to a second pass, more samples, or a human.

**Included in this repository:** [`ztc/`](./ztc) with the probe file (32 KB), a usage script for llama.cpp, and a one-line llama.cpp patch for hidden-state output.

Self-readout on MMLU-Pro (2,000 questions; POCKET answers, ZTC reads POCKET's own state; 5-fold cross-validated):

| | |
|---|---|
| ZTC AUC | **0.758** |
| Accuracy of the 20% most confident questions | **97.5%** |
| Accuracy over all questions | 87.6% |
| Wrong answers caught by reviewing only the 20% least confident | **46% of all wrong answers** |

Cross-model readout (same 400 questions with answers written by another model, same readout procedure):

| Build | ZTC AUC |
|---|---|
| Qwen3.8-Flash-Next BF16 (parent original) | 0.715 |
| Qwen3.8-Flash-Next 4-bit (same layout) | 0.722 |
| **POCKET-Darwin-180B (this model)** | **0.742** |

## Where it runs

Per token the model activates only about **3B parameters** (10 of 512 experts). llama.cpp memory-maps the file, so the experts a token needs can be read straight from a fast SSD, the whole 111 GB does **not** have to fit in memory. More memory simply means more of the model stays resident and it runs faster.

### Measured

| Device | Specs | Speed (generation) | How it runs |
|---|---|---|---|
| **💻 Gaming laptop** | NVIDIA GeForce **RTX 5060 Laptop (8 GB VRAM)** · **32 GB RAM** · NVMe SSD | **4.17 tok/s** | llama.cpp with the model memory-mapped from the SSD, experts are read on demand |
| **🖥️ CPU-only server** | AMD EPYC 9365, **1 socket · 16 threads**, no GPU | **18.4–21.0 tok/s** (prompt 54–68 tok/s) | whole model in RAM, **peak 78.8 GB**, load 85 s |
| **🟩 NVIDIA DGX Spark** | GB10 · **128 GB unified memory** | **39.25 tok/s** (single stream, reference build of identical size and layout) | fully resident on one Spark, no swap, no throttling |
| **⚡ NVIDIA B200** | 1 GPU (183 GB) | runs 8–16 parallel sessions of 131K context | 110–140 GB VRAM |

### Device classes and recommended specs

| Class | Example devices | Memory | Disk | Mode |
|---|---|---|---|---|
| **Entry, laptop / desktop** | RTX 4060/5060 laptops, RTX 3060–5090 desktops | **32 GB RAM + 8 GB+ VRAM** | **NVMe SSD, 120 GB free** | experts streamed from SSD; speed follows SSD and RAM bandwidth |
| **🧊 Mini PC** | mini PCs with **128 GB RAM** (DDR5 SO-DIMM or LPDDR5X), e.g. AMD Ryzen AI Max+ 395 mini PCs, Intel Core Ultra / AMD Ryzen mini PCs | **128 GB RAM** | NVMe SSD, 120 GB free | whole model in RAM, CPU only, or with the integrated GPU |
| **Workstation** | desktop with 96–128 GB RAM + any NVIDIA GPU | 96–128 GB RAM | NVMe SSD | experts in RAM (`--cpu-moe`), rest on GPU |
| **Unified-memory AI PC** | NVIDIA DGX Spark · Apple M-series 128 GB+ · AMD Ryzen AI Max+ 395 (128 GB) | 128 GB | NVMe SSD | fully resident |
| **CPU server** | AMD EPYC / Intel Xeon, 96 GB+ RAM | 96 GB+ | any | whole model in RAM (`--load-mode none`) |
| **Datacenter GPU** | NVIDIA B200 / H200 (one card), 2× RTX PRO 6000 | 141 GB+ VRAM | any | fully on GPU, many parallel users |

Peak RAM in the CPU run is below the file size because llama.cpp reads the per-layer n-gram embeddings from the file on demand.

## Run

Requires llama.cpp **b11048 or newer** (architecture `qwen4exp`).

```bash
# DGX Spark / single large GPU
llama-server -m POCKET-Darwin-180B-UD-Q4_K_XL-00001-of-00004.gguf -ngl 999 -fa on -c 131072 --jinja
# Laptop / desktop with 8 GB+ VRAM and 32 GB+ RAM (experts streamed from SSD)
llama-server -m POCKET-Darwin-180B-UD-Q4_K_XL-00001-of-00004.gguf -ngl 999 --cpu-moe -fa on -c 8192 --jinja
# CPU only
llama-server -m POCKET-Darwin-180B-UD-Q4_K_XL-00001-of-00004.gguf -ngl 0 -t 16 -c 8192 --jinja --load-mode none
```

Recommended sampling: temperature 1.0, top-p 0.95, top-k 20. It is a reasoning model, give it room (≥ 2,048 output tokens); the reasoning is returned in `reasoning_content`.

Text model (the vision encoder is left out to keep the build compact).

## Coming next

- DGX Spark throughput figures for this build.

## Credits and license

- Base model: [Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) by the Qwen team, Alibaba, Qwen Community License 1.0 (see `LICENSE`).
- GGUF layout: [unsloth/Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF) (UD-Q4_K_XL).
- RSI training and this build: VIDRAFT (FINAL-Bench).
