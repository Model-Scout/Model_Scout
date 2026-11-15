---
base_model: InternScience/Sage-A1.5
base_model_relation: quantized
library_name: gguf
license: apache-2.0
language:
- en
- es
- fr
- zh
- de
- pt
- ja
- ru
- ar
- ko
- it
tags:
- gguf
- imatrix
- calibration
- sage-a1.5
- qwen35moe
- moe
- val-imatrix
- 1m-tokens
pipeline_tag: text-generation
---

# Sage-A1.5 VAL 1M I-Matrix GGUF

<p align="left">
  <a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>
</p>

> [!IMPORTANT]
> **Independently computed using dedicated cloud compute clusters, funded 100% out-of-pocket.**
> If you consider these releases to be of high quality and they help you in your day-to-day workflow, consider [supporting on Ko-fi](https://ko-fi.com/isvalorum). Every contribution directly sustains future cloud compute hours and helps support my university studies.

---

<p align="left">
  <img src="https://img.shields.io/badge/Model-InternScience%2FSage--A1.5-blue?style=for-the-badge&logo=huggingface" alt="Base Model">
  <img src="https://img.shields.io/badge/Architecture-Qwen3.5--MoE-orange?style=for-the-badge" alt="Architecture">
  <img src="https://img.shields.io/badge/Topology-40%20Layers%20%7C%20256%20Experts-purple?style=for-the-badge" alt="Topology">
  <img src="https://img.shields.io/badge/Volume-1%2C001%2C472%20Tokens-red?style=for-the-badge" alt="Tokens">
  <img src="https://img.shields.io/badge/MoE%20Coverage-100%25%20(0%20Unobserved)-brightgreen?style=for-the-badge" alt="MoE Coverage">
</p>

---

## Technical Overview

Handcrafted Importance Matrix (I-Matrix) computed for **[InternScience/Sage-A1.5](https://huggingface.co/InternScience/Sage-A1.5)** to power high-fidelity downstream quantization (IQ4_XS, IQ3_M, IQ3_S, IQ2_XS, etc.).

Calculated using official **llama.cpp `b11512`** (commit `a11f57ba93797579a5d1855ee216a31f10242676`) with full layer offloading (`-ngl 99`).

| Parameter | Specification |
| :--- | :--- |
| **Model Repository** | `InternScience/Sage-A1.5` |
| **Model Revision** | `3e6b02c5e6afbc481fd4556baca8e6009f26d696` |
| **Model Architecture** | `qwen35moe` (40 layers, 256 experts per layer, top-k=8, intermediate=512) |
| **Target Tokens** | 1,000,000 tokens (489 chunks x 2048 context = 1,001,472 positions) |
| **Execution Flags** | `--process-output --no-ppl --no-escape -c 2048 -b 2048 -ub 2048 --chunks 489 -ngl 99` |

---

## Macro Component Distribution (1,001,472 Positions)

The calibration dataset was assembled with a deterministic 35/25/25/15 ratio spanning 11 natural languages and 10 programming languages, fully verified against the native tokenizer:

| Component | Target Share | Measured Share | Effective Tokens | Sub-categories / Scope |
| :--- | :--- | :--- | :--- | :--- |
| **Code** | 35.0% | 34.99% | 350,419 | 10 Programming Languages (Python, JS, TS, Java, C++, C, Go, Rust, SQL, Shell) |
| **Reasoning** | 25.0% | 24.83% | 248,641 | 11 Natural Languages (Mathematical, logical, and step-by-step reasoning) |
| **Prose / Text** | 25.0% | 25.06% | 251,005 | 11 Natural Languages (High-density prose, encyclopedic text, technical documentation) |
| **Tools / Agentic** | 15.0% | 15.12% | 151,407 | 11 Natural Languages (Multi-turn tool transcripts, function calling, API schemas) |
| **Total Positions** | **100.0%** | **100.0%** | **1,001,472** | **489 chunks of 2048 tokens** |

---

## Detailed Token Breakdown by Language & Category

### 1. Code Breakdown by Programming Language (350,419 Tokens)

| Programming Language | Effective Tokens | Category Share | Corpus Share |
| :--- | :--- | :--- | :--- |
| **Python** | 92,660 | 26.44% | 9.25% |
| **JavaScript** | 57,988 | 16.55% | 5.79% |
| **C++** | 35,351 | 10.09% | 3.53% |
| **TypeScript** | 35,216 | 10.05% | 3.52% |
| **Java** | 34,763 | 9.92% | 3.47% |
| **Rust** | 23,558 | 6.72% | 2.35% |
| **Go** | 23,556 | 6.72% | 2.35% |
| **C** | 23,319 | 6.65% | 2.33% |
| **Shell** | 12,066 | 3.44% | 1.20% |
| **SQL** | 11,942 | 3.41% | 1.19% |
| **Total Code** | **350,419** | **100.00%** | **34.99%** |

### 2. Natural Languages Breakdown (Reasoning, Prose & Tools - 651,053 Tokens)

| Language | Reasoning Tokens | Prose / Text Tokens | Tools Tokens | Total Language Tokens | Corpus Share |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **English (en)** | 51,930 | 51,907 | 31,123 | 134,960 | 13.48% |
| **Spanish (es)** | 37,052 | 37,350 | 22,744 | 97,146 | 9.70% |
| **Chinese (zh)** | 37,033 | 37,037 | 22,252 | 96,322 | 9.62% |
| **French (fr)** | 29,649 | 30,150 | 17,779 | 77,578 | 7.75% |
| **Portuguese (pt)** | 18,524 | 19,055 | 11,372 | 48,951 | 4.89% |
| **German (de)** | 18,612 | 18,733 | 11,215 | 48,560 | 4.85% |
| **Russian (ru)** | 14,903 | 15,129 | 9,270 | 39,302 | 3.92% |
| **Japanese (ja)** | 14,882 | 14,931 | 9,171 | 38,984 | 3.89% |
| **Arabic (ar)** | 11,148 | 11,224 | 6,809 | 29,181 | 2.91% |
| **Italian (it)** | 7,467 | 7,770 | 4,860 | 20,097 | 2.01% |
| **Korean (ko)** | 7,441 | 7,719 | 4,812 | 19,972 | 1.99% |
| **Subtotal** | **248,641** | **251,005** | **151,407** | **651,053** | **65.01%** |

> [!NOTE]
> All document boundaries and token allocations were verified against the official native tokenizer to guarantee strict zero-deviation quotas across all language partitions.

---

## MoE Expert Coverage & Physical Verification

In an MoE architecture with 256 experts per layer and top-k=8, token observations are distributed across 10,240 independent routing experts (30,720 distinct projection matrices):

| Metric | Measured Value | Standard Required |
| :--- | :--- | :--- |
| **Total Expert Projection Matrices** | **30,720** (40 layers x 256 experts x 3 FFN projections) | 30,720 |
| **Observed Expert Matrices** | **30,720** (100.0%) | 100.0% |
| **Unobserved Experts** | **0** | 0 |
| **Minimum Observations per Expert** | **440 rows** | Greater than 0 |
| **Maximum Observations per Expert** | **361,813 rows** | Finite F32 |
| **Average Observations per Expert** | **31,296.0 rows** | Finite F32 |
| **Validation Status** | **`VALIDATED_OBSERVATIONS`** | Validated |

---

## Artifact Verification

| File Name | File Size | SHA256 Checksum | Format |
| :--- | :--- | :--- | :--- |
| **`Sage-A1.5-VAL-1M-I-Matrix.gguf`** | 384,359,808 bytes | `634336253dedbebb63643dc6cd1b51821c2132187c45c5a044a5d43d6c8b813d` | GGUF v3 |

---

## Support & Independent Research

<p align="left">
  <a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>
</p>

All compute hours and hardware allocations are funded 100% out-of-pocket to bring high-quality open-source quantizations and calibration assets to the community.

If these builds help you in your day-to-day workflow, research, or development, consider [supporting on Ko-fi](https://ko-fi.com/isvalorum). Every contribution directly sustains future cloud compute hours and supports my university studies.
