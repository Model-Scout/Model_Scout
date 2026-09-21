---
license: apache-2.0
language:
  - en
  - ko
  - zh
  - ja
  - multilingual
library_name: transformers
pipeline_tag: text-generation
tags:
  - darwin
  - darwin-v9
  - darwin-jgos
  - moe
  - mixture-of-experts
  - reasoning
  - gpqa
  - mmlu-pro
  - benchmark
  - greedy
  - vidraft
  - eval-results
model-index:
  - name: Darwin-398B-JGOS
    results:
      - task:
          type: text-generation
          name: Graduate-Level Reasoning
        dataset:
          type: Idavidrein/gpqa
          name: GPQA Diamond
          config: gpqa_diamond
          split: train
        metrics:
          - type: accuracy
            value: 90.9
            name: Accuracy (greedy, single-sample, no test-time engine)
            verified: false
      - task:
          type: text-generation
          name: Reasoning & Knowledge (MMLU-Pro)
        dataset:
          type: TIGER-Lab/MMLU-Pro
          name: MMLU-Pro
        metrics:
          - type: accuracy
            value: 88.08
            name: Accuracy (5-shot CoT, greedy, single-sample)
            verified: false
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-398B-JGOS — Darwin V9 Platform · 397B MoE · GPQA 90.9 % · MMLU-Pro 88.08 % (Pure Greedy)

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-398B-JGOS"><img src="https://img.shields.io/badge/⭐_GPQA_Diamond-90.9%25_Darwin--397B--JGOS-gold?style=for-the-badge" alt="GPQA"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-398B-JGOS"><img src="https://img.shields.io/badge/📊_MMLU--Pro-88.08%25-orange?style=for-the-badge" alt="MMLU-Pro"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-28B-REASON"><img src="https://img.shields.io/badge/🧬_Darwin--28B--REASON-89.39%25_(DELPHI)-blue?style=for-the-badge" alt="REASON"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-28B-Opus"><img src="https://img.shields.io/badge/🧬_Darwin--28B--Opus-88.89%25-blue?style=for-the-badge" alt="Opus"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-36B-Opus"><img src="https://img.shields.io/badge/🧬_Darwin--36B--Opus-88.4%25-blue?style=for-the-badge" alt="36B"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/collections/FINAL-Bench/darwin-family"><img src="https://img.shields.io/badge/🏠_Darwin_Family-Collection-green?style=for-the-badge" alt="Family"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Leaderboard"><img src="https://img.shields.io/badge/🏆_FINAL_Bench-Leaderboard-green?style=for-the-badge" alt="FINAL Bench"></a>
</p>

> Largest Darwin model · Qwen 3.5 397B base + Darwin V9 FFN transplant · 397B MoE (~17B active) · BF16
> **GPQA Diamond: 90.9 % — pure greedy, single-sample, NO test-time engine**

---

## Overview

**Darwin-398B-JGOS** is the largest and highest-scoring member of the Darwin family. Built on **Qwen 3.5 397B** as the base, it transplants the FFN (expert) strengths of multiple high-performance models through the **Darwin V9 platform**, producing a 397B-parameter Mixture-of-Experts model with ~17B active parameters per token.

It reaches **90.9 % on GPQA Diamond with pure greedy decoding (single sample)** — surpassing **Darwin-28B-REASON (89.39 %, achieved *with* the Darwin-DELPHI test-time engine)** without using any test-time engine at all. This is the highest GPQA Diamond score in the Darwin family to date.

---

## 🧬 Darwin Platform & Research

**Darwin** is VIDRAFT's measuring-result-driven reasoning model family — approximately **20 official models** plus **400+ community derivatives**, ranking among the top open models on GPQA.

- **Darwin V9 platform** — evolutionary FFN/expert transplant and trust-weighted merging onto large-scale MoE backbones.
- **FINAL Bench** — VIDRAFT's evaluation framework.
- **4-layer Pre-AGI roadmap** — Darwin → AETHER → PROMETHEUS → HEPHAESTUS.

---

## 🧬 Model Lineage

| Role | Model | Contribution |
|:---:|:---|:---|
| **Base** | `Qwen 3.5 397B (A17B)` | 397B Mixture-of-Experts backbone (~17B active). |
| **FFN transplant** | **Darwin V9 platform** (proprietary) | Transplants the FFN (expert) strengths of multiple high-performance models onto the base. |
| **Result** | **`Darwin-398B-JGOS`** (this model) | 397B MoE → **90.9 %** GPQA Diamond, pure greedy. |

> The full Darwin V9 merge recipe — source models, weighting, and density — is **proprietary** and **not disclosed** (trade secret).

---

## ⚙️ Technical Specifications

| Component | Value |
|:---|:---|
| Architecture | `Qwen3_5MoeForConditionalGeneration` (Qwen 3.5 generation MoE) |
| Parameters | **~397 B total / ~17 B active** (Mixture-of-Experts) |
| Base | Qwen 3.5 397B (A17B) |
| Precision | bfloat16 |
| License | apache-2.0 |

---

## 🔬 Core Technique — Darwin V9 Platform

Darwin V9 transplants the FFN (expert) strengths of multiple high-performance models onto a Qwen 3.5 397B MoE base, then applies trust-weighted evolutionary merging.

> The source models, merge weights, and density schedule are **proprietary** and constitute a **trade secret**; they are not published.

---

## 🏆 Benchmark — GPQA Diamond (198 questions)

GPQA Diamond is a 198-question, PhD-level graduate science reasoning benchmark.

| Model | Engine | **Accuracy** |
|:---|:---|:---:|
| Darwin-28B-Opus | Standard | 88.89 % (176 / 198) |
| Darwin-28B-REASON | Darwin-DELPHI (test-time) | 89.39 % (177 / 198) |
| **Darwin-398B-JGOS** | **Greedy (single-sample, no engine)** | **🥇 90.9 % (180 / 198)** |

**Reproducible evaluation settings:**
- Greedy decoding (temperature = 0), single sample — **no voting / self-consistency / test-time engine**
- Max generation: 16,384 tokens
- Answer options shuffled (seed = 42)
- Hardware: **NVIDIA B200** (tensor-parallel 2 × pipeline-parallel 3, 6 GPUs)
- Inference engine: **vLLM**, bfloat16, `max_model_len = 18432`

> Darwin-398B-JGOS achieves the family's top GPQA Diamond score using nothing but greedy decoding — no Darwin-DELPHI, no majority voting.

---

## 📊 Benchmark — MMLU-Pro (12,032 questions)

MMLU-Pro is a substantially harder successor to MMLU — **10 answer choices** (vs 4) and **12,032 reasoning-focused questions** across **14 domains**.

**Darwin-398B-JGOS scores 88.08 % (10,598 / 12,032)** with **5-shot Chain-of-Thought and pure greedy decoding** (temperature = 0, single sample) — top-tier territory.

| Category | Accuracy | Category | Accuracy |
|:---|:---:|:---|:---:|
| Math | **95.9 %** | Computer Science | 88.5 % |
| Biology | **94.7 %** | Psychology | 87.7 % |
| Physics | **92.6 %** | Philosophy | 86.6 % |
| Chemistry | **92.3 %** | Engineering | 85.3 % |
| Business | **92.0 %** | Other | 83.4 % |
| Economics | 89.3 % | Health | 81.8 % |
| History | 80.1 % | Law | 75.3 % |
| | | **Overall** | **🥇 88.08 %** |

**Reproducible evaluation settings:**
- **5-shot Chain-of-Thought**, greedy decoding (temperature = 0), single sample — **no voting / self-consistency / test-time engine**
- Max generation: 14,000 tokens
- Hardware: **NVIDIA B200** (tensor-parallel 2 × pipeline-parallel 3, 6 GPUs)
- Inference engine: **vLLM**, bfloat16, `max_model_len = 18432`

> Strongest in STEM — Math 95.9 %, Biology 94.7 %, Physics 92.6 %, Chemistry 92.3 %.

---

## 🚀 Usage (vLLM)

```bash
vllm serve FINAL-Bench/Darwin-398B-JGOS --tensor-parallel-size 2 --pipeline-parallel-size 3 --dtype bfloat16 --trust-remote-code
```

---

## 🎯 Recommended Use-Cases

- Graduate-level STEM reasoning (GPQA / science qualifying exams)
- Mathematical problem solving
- Complex multi-step chain-of-thought
- Code generation and debugging
- Bilingual reasoning (strong English + Korean; also Chinese / Japanese)

## ⚠️ Limitations

- 397B MoE in bfloat16 requires multi-GPU serving (e.g. B200 ×6 with TP2×PP3).
- The 90.9 % figure is a single-run greedy measurement on GPQA Diamond (198 items).
- Reasoning traces can be verbose — control with max tokens.

---

## 📚 Citation

```bibtex
@misc{darwin397b_jgos_2026,
  title  = {Darwin-398B-JGOS: Darwin V9 Platform FFN Transplant on a 397B MoE Base},
  author = {FINAL-Bench / Darwin Research Team},
  year   = {2026},
  howpublished = {https://huggingface.co/FINAL-Bench/Darwin-398B-JGOS},
  note   = {Darwin V9 - 90.9 percent GPQA Diamond (greedy, single-sample)}
}
```

---

## 🔗 Related Darwin Models

- **Darwin-28B-REASON** — RTD + Darwin-DELPHI, GPQA 89.39 %
- **Darwin-28B-Opus** — base, GPQA 88.89 % (HF-official GPQA top tier)
- **Darwin-36B-Opus** — MoE 36B, GPQA 88.4 %
- **Darwin-27B-Opus** — 27B dense, GPQA 86.9 %
- **Darwin-9B-NEG** — 9B Negentropy, GPQA 84.3 %

---

*Darwin-398B-JGOS · Darwin V9 Platform · 90.9 % GPQA Diamond (pure greedy) · FINAL-Bench*

<!-- eval re-index trigger: GPQA Diamond (diamond) = 90.9% (180/198), greedy single-sample, 2026-06-13 -->

